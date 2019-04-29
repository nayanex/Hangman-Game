from hangman_app.models import Player


def update_player(_username, lost_count, won_count):
    try:
        player = Player.objects.get(username=_username)
        player.won_games = player.won_games + won_count
        player.lost_games = player.lost_games + lost_count
        player.high_score = player.won_games - player.lost_games
        player.save()
    except Player.DoesNotExist:
        player = Player.objects.create(username=_username)
        player.won_games = 0 + won_count
        player.lost_games = 0 + lost_count
        player.high_score = player.won_games - player.lost_games
        player.save()
