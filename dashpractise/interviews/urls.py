from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="interviews.index"),
    # path('interview/add', views.interview_Add, name="interview.add"),
]
