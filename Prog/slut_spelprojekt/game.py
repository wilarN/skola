# Python general modules
import json
import os
import random
import time
# Game specific modules
import src.world as world
import src.misc as misc
import src.headers as header

# Translations
import src.language.en_EN as lan_en
import src.language.se_SE as lan_se

op3x_text = ['''
 ▄▄▄       █    ██  ██▀███   ▒█████   ██▀███   ▄▄▄      
▒████▄     ██  ▓██▒▓██ ▒ ██▒▒██▒  ██▒▓██ ▒ ██▒▒████▄    
▒██  ▀█▄  ▓██  ▒██░▓██ ░▄█ ▒▒██░  ██▒▓██ ░▄█ ▒▒██  ▀█▄  
░██▄▄▄▄██ ▓▓█  ░██░▒██▀▀█▄  ▒██   ██░▒██▀▀█▄  ░██▄▄▄▄██ 
 ▓█   ▓██▒▒▒█████▓ ░██▓ ▒██▒░ ████▓▒░░██▓ ▒██▒ ▓█   ▓██▒
 ▒▒   ▓▒█░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░
  ▒   ▒▒ ░░░▒░ ░ ░   ░▒ ░ ▒░  ░ ▒ ▒░   ░▒ ░ ▒░  ▒   ▒▒ ░
  ░   ▒    ░░░ ░ ░   ░░   ░ ░ ░ ░ ▒    ░░   ░   ░   ▒   
      ░  ░   ░        ░         ░ ░     ░           ░  ░
''',
             """       
  ______   __    __   ______    ______    ______   ______  
 /      \\ /  |  /  | /      \\  /      \\  /      \\ /      \\ 
 $$$$$$  |$$ |  $$ |/$$$$$$  |/$$$$$$  |/$$$$$$  |$$$$$$  |
 /    $$ |$$ |  $$ |$$ |  $$/ $$ |  $$ |$$ |  $$/ /    $$ |
/$$$$$$$ |$$ \\__$$ |$$ |      $$ \\__$$ |$$ |     /$$$$$$$ |
$$    $$ |$$    $$/ $$ |      $$    $$/ $$ |     $$    $$ |
 $$$$$$$/  $$$$$$/  $$/        $$$$$$/  $$/       $$$$$$$/                                
""",
             '''
          _____                    _____                    _____                   _______                   _____                    _____          
         /\    \\                  /\    \\                  /\    \\                 /::\    \\                 /\    \\                  /\    \\         
        /::\    \\                /::\____\                /::\    \\               /::::\    \\               /::\    \\                /::\    \\        
       /::::\    \\              /:::/    /               /::::\    \\             /::::::\    \\             /::::\    \\              /::::\    \\       
      /::::::\    \\            /:::/    /               /::::::\    \\           /::::::::\    \\           /::::::\    \\            /::::::\    \\      
     /:::/\:::\    \\          /:::/    /               /:::/\:::\    \\         /:::/~~\:::\    \\         /:::/\:::\    \\          /:::/\:::\    \\     
    /:::/__\:::\    \\        /:::/    /               /:::/__\:::\    \\       /:::/    \\:::\    \\       /:::/__\:::\    \\        /:::/__\:::\    \\    
   /::::\   \\:::\    \\      /:::/    /               /::::\   \\:::\    \\     /:::/    / \\:::\    \\     /::::\   \\:::\    \\      /::::\   \\:::\    \\   
  /::::::\   \\:::\    \\    /:::/    /      _____    /::::::\   \\:::\    \\   /:::/____/   \\:::\____\   /::::::\   \\:::\    \\    /::::::\   \\:::\    \\  
 /:::/\:::\   \\:::\    \\  /:::/____/      /\    \\  /:::/\:::\   \\:::\____\ |:::|    |     |:::|    | /:::/\:::\   \\:::\____\  /:::/\:::\   \\:::\    \\ 
/:::/  \\:::\   \\:::\____\|:::|    /      /::\____\/:::/  \\:::\   \\:::|    ||:::|____|     |:::|    |/:::/  \\:::\   \\:::|    |/:::/  \\:::\   \\:::\____\\
\::/    \\:::\  /:::/    /|:::|____\     /:::/    /\::/   |::::\  /:::|____| \\:::\    \\   /:::/    / \\::/   |::::\  /:::|____|\::/    \\:::\  /:::/    /
 \\/____/ \\:::\/:::/    /  \\:::\    \\   /:::/    /  \\/____|:::::\/:::/    /   \\:::\    \\ /:::/    /   \\/____|:::::\/:::/    /  \\/____/ \\:::\/:::/    / 
          \\::::::/    /    \\:::\    \\ /:::/    /         |:::::::::/    /     \\:::\    /:::/    /          |:::::::::/    /            \\::::::/    /  
           \\::::/    /      \\:::\    /:::/    /          |::|\::::/    /       \\:::\__/:::/    /           |::|\::::/    /              \\::::/    /   
           /:::/    /        \\:::\__/:::/    /           |::| \\::/____/         \\::::::::/    /            |::| \\::/____/               /:::/    /    
          /:::/    /          \\::::::::/    /            |::|   |                \\::::::/    /             |::|   |                    /:::/    /     
         /:::/    /            \\::::::/    /             |::|   |                 \\::::/    /              |::|   |                   /:::/    /      
        /:::/    /              \\::::/    /              \\::|   |                  \\::/____/               \\::|   |                  /:::/    /       
        \\::/    /                \\::/____/                \\:|   |                                           \\:|   |                  \\::/    /        
         \\/____/                                           \\|___|                                            \\|___|                   \\/____/         
''']

global language


def main():
    global language
    language = header.check_json_value_settings("lang")
    # User selects translation of game.
    while language == "":
        usr_language = input("Swedish or english? - [s/S - e/E]")

        if usr_language.lower() == "e":
            header.update_json_settings("lang", "en_EN")
        elif usr_language.lower() == "s":
            header.update_json_settings("lang", "se_SE")

        else:
            print("Please select a valid language.")
        language = header.check_json_value_settings("lang")

    header.___init()
    header.update_json_settings("player_name", "test_player_name")

    # Check if used has already started a session, characted or realm.
    # If not, create a character and realm to play in.
    if header.check_json_value_settings("Has_Begun") == "False":
        header.slow_print("It looks like you haven't yet begun your adventure here in the shadow realm.\n"
                          "Please start by creating your hero.", 0.02)

        # Create Character and save playerdata to settings.json.
        player = header.create_character()
        header.update_player_save(player)
        header.clear()
        header.slow_print("Now, let's move on to creating the realm.", 0.02)
    else:
        header.slow_print(f"Welcome back {os.uname().sysname}.", 0.02)
        player = header.load_player_save()

    header.create_realm()

    while True:
        header.clear()
        header.get_lines(op3x_text, True)
        header.get_lines(op3x_menu, True)

        usr_sel = input("~$: ")

        if usr_sel.lower() == "cc":
            continue
        else:
            print("Please Input A Valid Selection!")
            time.sleep(1)


if __name__ == '__main__':
    main()
