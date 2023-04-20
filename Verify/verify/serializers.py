from rest_framework import serializers
from .models import UserPostModel


class UserLoginSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=13)

    def mobile_validation(self, phone):
        if not str(phone)[1:].isnumeric():
            raise serializers.ValidationError("please enter a Valid Number")
        elif not str(phone).startswith("09") or str(phone).startswith("+98"):
            raise serializers.ValidationError("please enter a Valid Number")
        elif len(phone) != 11 or 13:
            raise serializers.ValidationError("please enter a Valid Number")
        return phone


class UserVerifySerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=13)
    otp = serializers.CharField(required=False)

    def mobile_validation(self, phone):
        if not str(phone)[1:].isnumeric():
            raise serializers.ValidationError("please enter a Valid Number")
        elif not str(phone).startswith("09") or str(phone).startswith("+989"):
            raise serializers.ValidationError("please enter a Valid Number")
        elif len(phone) != 11 or 13:
            raise serializers.ValidationError("please enter a Valid Number")
        return phone

    def otp_validation(self, otp):
        if len(otp) != 6:
            raise serializers.ValidationError("Please enter a correct password")
        elif not str(otp).isnumeric():
            raise serializers.ValidationError("Please enter a correct password")
        return otp


class UserPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserPostModel
        fields = "__all__"
