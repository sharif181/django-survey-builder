from django.shortcuts import render

from .serializers import QuestionTypeSerializer
from django.views import generic
from rest_framework.views import APIView
from .models import QuestionType
from rest_framework.response import Response
# class HomeView(TemplateView):
#     template_name = 'index.html'


class HomeView(generic.View):
    def get(self,request):
        return render(request, 'index.html')



class QuestionTypeView(APIView):
    def get(self, request, format=None):
        types = QuestionType.objects.all()
        serializer = QuestionTypeSerializer(types, many=True)
        return Response(serializer.data)
    def post(self,request):
        print('backend')



