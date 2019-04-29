from django.shortcuts import render, redirect
from django.views.generic import ListView

from hangman_app.forms import PlayerForm
from hangman_app.hangman import HangmanGame, is_valid_guess, is_game_won,\
    is_game_over, generate_board
from hangman_app.models import Player
from hangman_app.model_manager import update_player


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
            player.won_games = 0
            player.lost_games = 0
            player.high_score = 0
            player.save()
            return redirect("home")
    else:
        return render(request, "hangman_app/player.html", {"form": form})


def new_game(request):
    return render(request, 'hangman_app/new_game_modal.html')


def game(request):
    if request.method == "POST":
        hangman_game = HangmanGame()
        request.session['player'] = request.POST['player']
        request.session['secret_word'] = hangman_game.secret_word
        request.session['hangman'] = hangman_game.hangman
        request.session['missed_characters'] = hangman_game.missed_characters
        request.session['correct_characters'] = hangman_game.correct_characters
        request.session['is_game_over'] = hangman_game.is_game_over
        request.session['is_game_won'] = hangman_game.is_game_won
        request.session['is_game_done'] = hangman_game.is_game_done
        request.session['alpha_numeric_list'] = hangman_game.alpha_numeric_list
        request.session['cells'] = hangman_game.cells
        request.session['invalid_guess_msg'] = hangman_game.invalid_guess_msg
        context = {
            'player': request.session['player'],
            'secret_word': request.session['secret_word'],
            'hangman': request.session['hangman'],
            'missed_characters': request.session['missed_characters'],
            'correct_characters': request.session['correct_characters'],
            'is_game_over': request.session['is_game_over'],
            'is_game_won': request.session['is_game_won'],
            'is_game_done': request.session['is_game_done'],
            'alpha_numeric_list': request.session['alpha_numeric_list'],
            'cells': request.session['cells'],
            'invalid_guess_msg': request.session['invalid_guess_msg']
        }
        return render(request, 'hangman_app/game.html', context)

    return render(request, 'hangman_app/home.html', context)


def add_char(request):
    if request.method == "POST":
        request.session['guess'] = request.POST['guess']

        already_guessed = request.session['missed_characters'] + \
            request.session['correct_characters']

        if is_valid_guess(already_guessed, request.session['guess'])[0]:
            if request.session['guess'].lower() in\
                    request.session['secret_word']:
                request.session['correct_characters'] =\
                    request.session['correct_characters'] + \
                    request.session['guess']
                request.session['is_game_won'] = is_game_won(
                    request.session['secret_word'],
                    request.session['correct_characters'])
            else:
                request.session['missed_characters'] += \
                    request.session['guess']
                request.session['is_game_over'] = is_game_over(
                    request.session['missed_characters'])

            request.session['cells'] = generate_board(
                request.session['secret_word'],
                request.session['correct_characters'])
            request.session['hangman'] = len(
                request.session['missed_characters'])

        request.session['invalid_guess_msg'] = is_valid_guess(
            already_guessed, request.session['guess'])[1]

        context = {
            'player': request.session['player'],
            'secret_word': request.session['secret_word'],
            'hangman': request.session['hangman'],
            'missed_characters': request.session['missed_characters'],
            'correct_characters': request.session['correct_characters'],
            'is_game_won': request.session['is_game_won'],
            'is_game_over': request.session['is_game_over'],
            'alpha_numeric_list': request.session['alpha_numeric_list'],
            'cells': request.session['cells'],
            'guess': request.session['guess'],
            'invalid_guess_msg': request.session['invalid_guess_msg'],
        }

        if request.session['is_game_won']:
            update_player(request.session['player'], 0, 1)
        elif request.session['is_game_over']:
            update_player(request.session['player'], 1, 0)

        return render(request, 'hangman_app/game.html', context)
    else:
        return render(request, "hangman_app/home.html")
