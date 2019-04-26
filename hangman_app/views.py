from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

from hangman_app.forms import PlayerForm
from hangman_app.hangman import HangmanGame
from hangman_app.models import Player
from hangman_app.utils import is_valid_guess, is_game_finished, is_game_over


class HomeListView(ListView):
    """Renders the home page, with a list of all users."""
    model = Player

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context


def create_user(request):
    form = PlayerForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            player = form.save(commit=False)
            player.save()
            return redirect("home")
    else:
        return render(request, "hangman_app/player.html", {"form": form})


def new_game(request):
    hangman_game = HangmanGame()
    request.session['secret_word'] = hangman_game.secret_word
    request.session['hangman'] = hangman_game.hangman
    request.session['missed_characters'] = hangman_game.missed_characters
    request.session['correct_characters'] = hangman_game.correct_characters
    request.session['game_is_finished'] = hangman_game.game_is_finished
    request.session['alpha_numeric_list'] = hangman_game.alpha_numeric_list
    request.session['cells'] = hangman_game.cells

    context = {
        'secret_word': request.session['secret_word'],
        'hangman': request.session['hangman'],
        'missed_characters': request.session['missed_characters'],
        'correct_characters': request.session['correct__characters'],
        'game_is_finished': request.session['game_is_finished'],
        'alpha_numeric_list': request.session['alpha_numeric_list'],
        'cells': request.session['cells']
    }
    return render(request, 'hangman_app/game.html', context)


def add_char(request):
    if request.method == "POST":
        request.session['guess'] = request.POST['guess'].encode('utf8')

        context = {
            'secret_word': request.session['secret_word'],
            'hangman': request.session['hangman'],
            'missed_characters': request.session['missed_letters'],
            'correct_characters': request.session['correct_letters'],
            'game_is_finished': request.session['game_is_finished'],
            'alpha_numeric_list': request.session['alpha_numeric_list'],
            'cells': request.session['cells'],
            'guess': request.session['guess'],
        }

        already_guessed = request.session['missed_characters'] + \
            request.session['correct_characters']

        if is_valid_guess(already_guessed, request.session['guess']):
            correct_characters = request.session['correct_characters'] + \
                request.session['guess']
            if request.session['guess'].lower() in request.session['secret_word']:
                request.session['game_is_finished'] = is_game_finished(
                    request.session['secret_word'], correct_characters)
                request.session['cells'] = generate_board(
                    request.session['secret_word'], request.session['correct_characters'])
            else:
                request.session['missed_characters'] += request.session['guess']
                request.session['game_is_finished'] = is_game_over(
                    request.session['missed_characters'])
                request.session['cells'] = generate_board(
                    request.session['secret_word'], request.session['correct_characters'])

        correctCharacters = correctCharacters + guess
        else:
            return redirect("home")
    else:
        return render(request, "hangman_app/game.html")
