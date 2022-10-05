import time
import pygame

import os

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
# pygame.mixer.init()
sound = pygame.mixer.Sound(".\\sfx\\Enya_May_it_be_lyrics.mp3")
sound.set_volume(0.3)
sound.play()
os.system("cls")

all_players = []

max_map_x = [x for x in range(1, 25)]
max_map_y = [x for x in range(1, 25)]

game_active = False


class SingleTile:
    def __init__(self, type_of_tile, x_cord, y_cord):
        self.type_of_title = type_of_tile
        self.x_cord = x_cord
        self.y_cord = y_cord


class PlayerChar:
    def __init__(self, name, mana, strength, energy, level, gold, x_cord, y_cord, health_points):
        self.name = name
        self.mana = mana
        self.strength = strength
        self.energy = energy
        self.health_points = health_points
        self.level = level
        self.gold = gold
        self.x_cord = x_cord
        self.y_cord = y_cord

    def hurt(self, amount_hurt):
        self.health_points -= amount_hurt

    def heal(self, amount_heal):
        self.health_points += amount_heal


def output_player_stats(player_to_check):
    player_data = player_to_check.__dict__
    print(player_data)


# Tile Variables
tile = "[x]"
tiles_in_x = []
tiles_in_y = []


def main_game_loop():
    global game_active
    game_active = True

    print(f"Hello Dear {player.name}.")
    time.sleep(1)
    print(f"And welcome.")
    time.sleep(1)
    for tile_x in max_map_x:
        tiles_in_x.append(tile)
        if len(tiles_in_x) <= 10:
            print(tile)
            for tile_y in max_map_y:
                tiles_in_y.append(tile)
                print(tile, end="")

        else:
            tiles_in_x.clear()
            tiles_in_y.clear()


# Create Character
usr_chosen_name = input("\nPlayer_Name: ")

player = PlayerChar(name=usr_chosen_name, mana=100, strength=10, energy=100, health_points=100, gold=10, level=0,
                    x_cord=10,
                    y_cord=10)


def main():
    # Print Current Stats Of [Player]
    output_player_stats(player)

    # Start Adventure?
    answ = input("Start adventure? (y/n - q to exit): ").lower()
    if answ.__contains__("y"):
        # Start Game.
        print("Starting...")
        main_game_loop()

    elif answ.__contains__("n"):
        # Exit out.
        print("Exiting...")

    elif answ.__contains__("q") or answ.__contains__("e"):
        exit(0)
    else:
        print("[Please input a valid answer and try again (y/n)...]")


main()