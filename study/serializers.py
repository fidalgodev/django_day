from rest_framework import serializers
from study.models import Study
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["id", "email"]


class StudySerializer(serializers.ModelSerializer):
  creator = UserSerializer(read_only=True)
  reward_per_hour = serializers.ReadOnlyField()

  def validate(self, data):
    validated_data = super().validate(data)

    if validated_data["reward"] / validated_data["estimated_time_minutes"] * 60 < 15:
      raise serializers.ValidationError(
        {
          "reward": "The reward per hour must be at least 15",
        }
      )

    validated_data["creator"] = self.context["request"].user

    return validated_data

  class Meta:
    model = Study
    fields = "__all__"
