from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from sorrie.models import Category
app_name = 'sorrie'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
]

