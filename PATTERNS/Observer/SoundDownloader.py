import pygame

hit = pygame.mixer.Sound('sounds/hit.mp3')
fail = pygame.mixer.Sound('sounds/fail.mp3')
score_sound = pygame.mixer.Sound('sounds/score.mp3')
super_hit_sound = pygame.mixer.Sound('sounds/super_hit.mp3')
victory = pygame.mixer.Sound('sounds/victory.mp3')
wall_hit = pygame.mixer.Sound('sounds/wall_hit.mp3')

sounds = {
    'score_sound': score_sound,
    'fail_sound': fail,
    'victory_sound': victory,
    'hit_sound': hit,
    'wall_hit_sound': wall_hit,
    'super_hit_sound': super_hit_sound
}