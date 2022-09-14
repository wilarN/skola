import os
import time
import random as r

# Weather variables
sun_active = False
is_raining = False
is_blowing = False
is_snowing = False
current_degrees = 22

# Polly(Parrot) variables
polly_seeds = 0

polly_max_seeds = 50

# Replies --> Songs, Stories etc.
fun_story_01 = "Once upon a time, there was a parrot walking.\n" \
               "The parrot fell and everyone thought that was really funny.\n" \
               "ha ha ha ha.\n" \
               "Funny...\n"
song_about_life_01 = "Yesterday\n" \
                     "All my troubles seemed so far away\n" \
                     "Now it looks as though they're here to stay\n" \
                     "Oh, I believe in yesterday.\n" \
                     "Yesterday, By The Beatles. \n" \

def program_output(message: str, mode: int):
    # Information output
    if mode == 1:
        print(f"[INFO] {message}")

    elif mode == 2:
        print(f"[ALERT] {message}")


def randomise_weather_variables():
    pass


def program_output_delay_effect(message: str, write_speed: float):
    for char in message:
        print(f"{char}", end="")
        time.sleep(write_speed)


def grant_seed(who_to_grant: str, amount: int, grant_var):
    program_output(f"{who_to_grant} was granted {amount} seeds!", 1)
    grant_var += amount


# Run loop until polly has got the max ammount of seeds.
while not polly_seeds >= polly_max_seeds:

    # Check if user wants to manually setup the weather parameters or want them randomly generated.
    # MANUAL WEATHER CONTROL
    if input("Do you want to manually set weather values?[y(yes)/n(o)]").lower().__contains__("y"):
        os.system("cls")
        print("[ Manual Weather Control Menu ]\n")
        if input("Should the sun be shining?").lower().__contains__("y"):
            sun_active = True
        else:
            sun_active = False
        if input("Should it be raining?").lower().__contains__("y"):
            is_raining = True
        else:
            is_raining = False
        if input("Should it be snowing?").lower().__contains__("y"):
            is_snowing = True
        else:
            is_snowing = False
        temp = input("What should the temperature be?")
        if not type(temp) == int():
            int(temp)
            current_degrees = temp
        time.sleep(1)
        print(f"Rain: {is_raining}\n"
              f"Snow: {is_snowing}\n"
              f"Wind: {is_blowing}\n"
              f"Sun: {sun_active}\n"
              f"Current Temperature: {current_degrees}\u00b0C\n")
        time.sleep(2)
        os.system("cls")

    # AUTOMATIC WEATHER CONTROL
    else:
        os.system("cls")
        print("Randomly generating weather values...")
        time.sleep(.5)
        current_degrees = r.randint(-10, 30)
        is_raining = r.choice([True, False])
        is_snowing = r.choice([True, False])
        is_blowing = r.choice([True, False])
        sun_active = r.choice([True, False])

        print(f"Rain: {is_raining}\n"
              f"Snow: {is_snowing}\n"
              f"Wind: {is_blowing}\n"
              f"Sun: {sun_active}\n"
              f"Current Temperature: {current_degrees}\u00b0C\n")

    if int(current_degrees) > 20 and sun_active:
        os.system("cls")
        print(f"It's {current_degrees} \u00b0C outside and the sun is shining! Amazing!\n")
        grant_seed("Polly", 5, polly_seeds)
        print(f"Because of the immense heat Polly feels like listening to a fun story!\n")
        program_output_delay_effect(fun_story_01, .05)
        time.sleep(1)

    elif int(current_degrees) < 20 and not is_raining:
        os.system("cls")
        print("Ohh nooo, it's less than 20 degrees outside! plus it isn't raining. A real bummer if you ask Polly.\n")
        time.sleep(3)
        print("Therefore i think we should grant Polly some extra seeds to make up for it!\n")
        time.sleep(3)
        grant_seed("Polly", 10, polly_seeds)
        time.sleep(5)
        print("\nPolly also wants to hear a song about life on the sea, but because Polly is a parrot, Polly don't get to choose what song it will be.\n")
        time.sleep(5)
        program_output_delay_effect(song_about_life_01, 0.05)

    elif int(current_degrees) == 20 or is_blowing:
        os.system("cls")
        print(f"It's either exactly 20 \u00b0C outside, Orrrrrrrr Polly just got crazy because of the wind.\n")
        time.sleep(2)
        print("Either way, Polly feels like putting on the radio.\n")
        program_output("*Polly put on the radio.*", 1)

    elif int(current_degrees) < 0 or is_snowing:
        os.system("cls")
        print(f"It's either really cold outside, Or it's snowing.\n")
        time.sleep(2)
        print("Either way, Polly wants her seeds randomised.\n")
        time.sleep(2)
        temp_seeds = r.randint(1, 20)
        print(f"Polly ended up getting {temp_seeds}! Wohoooo")

### Fixa extra sektionen


# program_output("Now polly has got enough seeds for today.", 2)
