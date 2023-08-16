from GameEngines import *
from PATTERNS.Observer.SoundDownloader import sounds

game_starter = GameStarter()
window, player, bot, ball, p1, p2 = game_starter.start_game()
events_handler = EventsHandler(window, p1, p2, player, bot, sounds, ball)
game = GameMechanics(player, bot, ball)
game.attach(events_handler)
game.run()
