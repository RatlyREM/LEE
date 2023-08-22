from django.urls import path
from . import views

urlpatterns = [
    path('', views.RoutineCreateAPIView.as_view()),
    path('check/<int:pk>/', views.RoutineCheckAPIView.as_view()),
    path('modify/<int:pk>/', views.RoutinePutAPIView.as_view()),
    path('delete/<int:pk>/', views.RoutineDeleteAPIView.as_view()),

    #path('detail/', views.RoutineDetailCreateAPIView.as_view()),
    #path('detail/check/<int:pk>/', views.RoutineDetailCheckAPIView.as_view()),

]