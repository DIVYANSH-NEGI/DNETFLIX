import imp
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from . models import Profile, Movie
from . forms import ProfileForm


def Home(request):
        if request.user.is_authenticated:
            return redirect('netflixapp:profile-list')
        return render(request, 'index.html')

@login_required(login_url='')
def ProfileList(request):

        profile = request.user.profile.all()

        context = {
            'profile':profile
        }
        return render(request, 'profilelist.html', context)

@login_required(login_url='')
def ProfileCreate(request):

    form = ProfileForm(request.POST or None)
    if form.is_valid():
        profile = Profile.objects.create(**form.cleaned_data)
        if profile:
            request.user.profile.add(profile)
            return redirect("netflixapp:profile-list")

    context = {
               'form':form
               }
    return render(request,'profilecreate.html',context)

def MovieList(request,profile_id):
        try:
            profile = Profile.objects.get(uuid=profile_id)
            movies = Movie.objects.filter(age_limit=profile.age_limit)
            if profile not in request.user.profile.all():
                return redirect('netflixapp:profile-list')

            context = {
            'movies':movies
            }
            return render(request, 'movielist.html', context)
        except Profile.DoesNotExist:
            return redirect('netflixapp:profile-list')
@login_required(login_url='')
def MovieDetail(request,movie_id):
        try:

            movie = Movie.objects.get(uuid=movie_id)

            context = {
            'movie':movie
            }
            return render(request, 'moviedetail.html', context)
        except Movie.DoesNotExist:
            return redirect('netflixapp:profile-list')


@login_required(login_url='')
def PlayMovie(request,movie_id):
        try:

            movie = Movie.objects.get(uuid=movie_id)
            movie = movie.video.values()
            context = {
            'movie':list(movie)
            }
            return render(request, 'playmovie.html', context)
        except Movie.DoesNotExist:
            return redirect('netflixapp:profile-list')
