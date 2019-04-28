from django.urls import path
from hangman_app import views
from hangman_app.models import Player

home_list_view = views.HomeListView.as_view(
    queryset=Player.objects.order_by("high_score")[:20],
    context_object_name="player_list",
    template_name="hangman_app/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("new_game/", views.new_game, name="new_game"),
    path("add_char", views.add_char, name="add_char"),
    path("user/", views.create_user, name="create_user"),
    path("game/", views.game, name="game"),
]
