from rest_framework.serializers import ModelSerializer
from .models import QuestionType


class QuestionTypeSerializer(ModelSerializer):
    class Meta:
        model = QuestionType
        fields = ['id','title','type','options']