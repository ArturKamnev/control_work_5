from django.urls import path
from .views import PostsApiView, PostDetailApiView, CommentsApiView, CommentDetailApiView

urlpatterns = [
    path('', PostsApiView.as_view()),
    path('<int:post_id>/', PostDetailApiView.as_view()),
    path('<int:post_id>/comments/', CommentsApiView.as_view()),
    path('<int:post_id>/comments/<int:comment_id>/', CommentDetailApiView.as_view())

]