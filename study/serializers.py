from rest_framework import serializers
from study.models import Study
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["id", "email"]


class StudySerializer(serializers.ModelSerializer):
  creator = UserSerializer(read_only=True)

  def validate(self, data):
    validated_data = super().validate(data)
    validated_data["creator"] = self.context["request"].user
    return validated_data

  class Meta:
    model = Study
    fields = "__all__"
