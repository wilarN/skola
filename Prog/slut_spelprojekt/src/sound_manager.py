import pygame

global talk_SFX_file


def initialise():
    global talk_SFX_file
    pygame.mixer.init()
    talk_SFX_file = pygame.mixer.Sound("src/sfx/talk.mp3")
    # pygame.mixer.music.load("src/sfx/Undertale_Premonition.mp3")
    pygame.mixer.music.load("src/sfx/Undertale_Another_Medium.mp3")
    pygame.mixer.music.queue("src/sfx/Undertale_Another_Medium.mp3")
    # pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play()


# Might not be able to use this yet, but as a reference for later.
def play_sound_effect(effect):
    pygame.mixer.Sound(effect)


def talk_SFX():
    global talk_SFX_file
    talk_SFX_file.play()
