from rest_framework import serializers

from account.models import Account

class RegisterationSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['email','username','password','confirm_password']
        extra_kwargs = {
            'password': {'write_only':True}
        }

    def save(self):
        temp_email = Account.objects.filter(email=self.validated_data['email'])
        temp_username = Account.objects.filter(username=self.validated_data['username'])
        if len(temp_email) == 0 and len(temp_username) == 0:
            account = Account(
                email = self.validated_data['email'],
                username = self.validated_data['username']
            )
            password = self.validated_data['password']
            confirm_password = self.validated_data['confirm_password']

            if password != confirm_password:
                raise serializers.ValidationError({'password' : 'Passwords must match.'})
            account.password = password
            account.save()
            return account
        else:
            raise serializers.ValidationError({'email' : 'account with this email already exist.','username':'account with this username already exist'})