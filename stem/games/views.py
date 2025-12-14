from django.shortcuts import render, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'games/index.html')


def catalog(request):
    games = Game.objects.all()  # отримуємо всі ігри
    return render(request, 'games/catalog.html', {"games": games})


def game_info(request, game_id):
    game = Game.objects.get(id=game_id)
    return render(request, 'games/info.html', {"game": game})



@login_required(login_url='login')
def buy_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    return render(request, 'games/buy.html', {"game": game})


