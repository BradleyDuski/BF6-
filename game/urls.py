from django.urls import path
from . import views
from .views import  like_post, PostDeleteView, AddReply
urlpatterns = [
    path("operators/", views.OperatorList.as_view(), name="operator_list"),
    path("operator/detail/<int:pk>/", views.OperatorDetail.as_view(),name="operator_detail"),
    path("weapons/", views.WeaponList.as_view(), name="weapon_list"),
    path("weapons/detail/<int:pk>/", views.WeaponDetail.as_view(),name="weapon_detail"),
    path('forum/new/', views.PostCreateView.as_view(), name='post_create'),
    path('forum/', views.PostList.as_view(), name='post_list'),
    path('forum/<int:pk>/like/', like_post, name='like_post'),
    path('forum/<int:pk>/',views.PostDetail.as_view(), name='post_detail'),
    path("forum/<int:pk>/replies/", views.ReplyList.as_view(), name="reply_list"),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:post_id>/reply/', AddReply.as_view(), name='add_reply'),
    path('reply/<int:reply_id>/delete/', views.delete_reply, name='delete_reply'),
]