from django.urls import path
from . import views

app_name = 'netflixapp'

urlpatterns = [
    path('', views.Home, name="Home"),
    path('profiles/', views.ProfileList, name="profile-list"),
    path('profiles/create', views.ProfileCreate, name="profile-create"),
    path('watch/<str:profile_id>/', views.MovieList, name="movie-list"),
    path('watch/detail/<str:movie_id>/', views.MovieDetail, name="movie-detail"),
    path('watch/play/<str:movie_id>/', views.PlayMovie, name="play-movie"),

]
