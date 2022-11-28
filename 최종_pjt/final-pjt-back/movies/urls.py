from django.urls import path
from . import views

urlpatterns = [
    # GET -> movie 리스트
    path('', views.get_movie_list),
    # GET -> movie detail
    path('<int:movie_pk>/', views.get_movie_detail),
    # POST -> 영화 찜하기/취소
    path('<int:movie_pk>/wish/', views.wish_movies_add),


    # POST -> 리뷰 좋아요/취소 
    # path('<int:movie_pk>/articles/<int:article_pk>/like/', views.article_like),
    # GET -> movie articles list / POST -> 리뷰 작성
    # path('<int:movie_pk>/articles/', views.article_list_or_create),
    # # GET -> 해당 리뷰 가져오기 / PUT -> 리뷰 수정 / DELETE -> 리뷰 삭제 
    # path('<int:movie_pk>/articles/<int:article_pk>/', views.article_update_or_delete),
    # # POST -> 댓글 작성 / 
    # path('<int:movie_pk>/articles/<int:article_pk>/comments/', views.comment_create),
    # # PUT -> 댓글 수정 / DELETE -> 댓글 삭제
    # path('<int:movie_pk>/articles/<int:article_pk>/comments/<int:comment_pk>/', views.comment_update_or_delete),
    # GET -> 점수 확인 / POST -> 점수 작성 / PUT -> 점수 수정 / DELETE -> 점수 삭제
    # path('<int:movie_pk>/score/<username>/', views.score_movie),
    
]