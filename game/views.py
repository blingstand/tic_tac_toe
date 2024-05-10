from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    if request.method == 'POST':
        room_code = request.POST.get('room_code')
        character_choice = request.POST.get('character_choice')
        return redirect(
            f'/game/{room_code}?&choice={character_choice}'
        )
    return render(request, "index.html", {})

def game(request, room_code):
    choice = request.GET.get('choice')
    if choice not in ['X', 'O']:
        raise Http404("Choice does not exist")
    context = {
        'char_choice': choice,
        'room_code': room_code,
    }
    return render(request, "game.html", context)