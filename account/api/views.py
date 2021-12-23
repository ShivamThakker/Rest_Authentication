from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.decorators import APIView, api_view
from account.api.serializers import RegisterationSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from account.models import Account
from .forms import RegisterForm


def register_view(request):
    form = RegisterForm
    context = {"forms":form}
    return render(request,'account/register_page.html',context)

# class registeration_view(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = (IsAuthenticated, )

@api_view(['POST',])
def registeration_func(request):

    if request.method == "POST":
        serializer = RegisterationSerializer(data=request.data)
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Successfull"
            # temp = Account.objects.filter(email=account.email)
            # print(len(temp))
            data['email'] = account.email
            data['username'] = account.username
            # data = {"response":"Successful","email":account.email,"username":account.username}
        else:
            data = serializer.errors
        
        return Response(data)
    # context={}
    # return render(request,'account/base.html',context={})

