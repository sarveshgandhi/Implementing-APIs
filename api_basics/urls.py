from django.urls import path
from . import views
urlpatterns = [

  # path('article', views.article_list, name='article-list'),
  # path('article/<int:pk>', views.article_details, name = 'article-detail'),
  # ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
  # these urls were the ones with Json response
  # -------------------------------------------

  # path('article/', views.article_list_withAPIView, name = 'article-list'),
  # path('article/<int:pk>', views.article_details_withAPIView, name = 'article-detail'),
  # ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
  # these urls were the ones with rest_framework response
  # -------------------------------------------

  path('article/', views.ArticleAPIView.as_view(), name = 'article-list'),
  path('article/<int:id>', views.ArticleDetails.as_view(), name = 'article-detail'),
  # ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
  # these urls were the ones with class based views
  # -------------------------------------------

  path('generic/article/<int:id>', views.GenericAPIView.as_view(), name = 'article-list'),
  # ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
  # these urls were the ones with generic views(they are different here)
  # -------------------------------------------


]
