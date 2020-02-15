from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
def article_list(request):
  if request.method == "GET":
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many = True)
    return JsonResponse(serializer.data, safe=False)
  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = ArticleSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def article_details(request, pk):
  try:
    article = Article.objects.get(pk=pk)
  except:
    return HttpResponse(status=404)
  if request.method == 'GET':
    ser = ArticleSerializer(article)
    return JsonResponse(ser.data)
  elif request.method == 'PUT':
    data = JSONParser().parse(request)
    serializer = ArticleSerializer(article, data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)
  elif request.method == 'DELETE':
    article.delete()
    return HttpResponse(status=204)




@api_view(['GET', 'POST'])
def article_list_withAPIView(request):
  if request.method == "GET":
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many = True)
    return Response(serializer.data)
  elif request.method == 'POST':
    # data = JSONParser().parse(request)
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def article_details_withAPIView(request, pk):
  try:
    article = Article.objects.get(pk=pk)
  except:
    return HttpResponse(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    ser = ArticleSerializer(article)
    return Response(ser.data)
  elif request.method == 'PUT':
    # data = JSONParser().parse(request)
    serializer = ArticleSerializer(article, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
  elif request.method == 'DELETE':
    article.delete()
    return HttpResponse(status=status.HTTP_204_NO_CONTENT)




class ArticleAPIView(APIView):

  def get(self, response):
    articles = Article.objects.all()
    ser = ArticleSerializer(articles, many=True)
    return Response(ser.data)
  
  def post(self, response):
    ser = ArticleSerializer(data=response.data)
    if ser.is_valid():
      ser.save()
      return Response(ser.data, status=status.HTTP_201_CREATED)
    return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetails(APIView):

  def get_object(self, id):
    try:
      return Article.objects.get(id=id)
    except:
      return HttpResponse(status=status.HTTP_404_NOT_FOUND)
  
  def get(self, request, id):
    article = self.get_object(id)
    ser = ArticleSerializer(article)
    return Response(ser.data)
  
  def put(self, request, id):
    article = self.get_object(id)
    ser = ArticleSerializer(article, data=request.data)
    if ser.is_valid():
      ser.save()
      return Response(ser.data)
    return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, response, id):
    article = self.get_object(id)
    article.delete()
    return Response(status=status.HTTP_404_NOT_FOUND)



class GenericAPIView(
    generics.GenericAPIView, 
    mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin
  ):
  serializer_class = ArticleSerializer
  queryset = Article.objects.all()
  lookup_field = 'id'
  authentication_classes = [SessionAuthentication, BasicAuthentication]
  # authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticated]

  def get(self, request, id=None):
    if id:
      return self.retrieve(request)
    return self.list(request)
  
  def post(self, request):
    return self.create(request)
  
  def put(self, request, id=None):
    return self.update(request, id)
  
  def delete(self, request, id=None):
    return self.destroy(request, id)

