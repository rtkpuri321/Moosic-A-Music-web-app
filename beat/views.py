from django.shortcuts import render, HttpResponse, redirect
from youtube_search import YoutubeSearch
# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def search(request):
    search = request.GET.get('search')
    # print(search)
    song = YoutubeSearch(search, max_results=20).to_dict()
    if len(song) == 0:
        return render(request, 'index.html')
    song_li = [song[:20:2], song[1:20:2]]
    # print(song_li)
    return render(request, 'search.html', {'CONTAINER': song_li, 'song': song_li[0][0]['id']})


def playlist(request):
    return render(request, 'playlist.html')
