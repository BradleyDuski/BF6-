from django.urls import path
from . import views

urlpatterns = [
    path("game/", views.OperatorList.as_view(), name="operator_list"),
    path("detail/<int:pk>/", views.OperatorDetail.as_view(),name="operator_detail"),

]