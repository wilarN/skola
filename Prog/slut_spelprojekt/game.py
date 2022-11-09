import json
import os
import random
import time
from datetime import datetime

game_file_dir = "./files"
global_log = f"{game_file_dir}/logs/globalLogFile.log"
global_settings_path = f"{game_file_dir}/settings.json"
now = datetime.now()
global_character_path = f"{game_file_dir}/characters"
global_game_path = f"{game_file_dir}/game"

file_keep_count = [global_log, global_settings_path]
dirs_keep_count = [game_file_dir, global_character_path, global_game_path]

for i in dirs_keep_count:
    if not os.path.exists(i):
        os.makedirs(i)

for i in file_keep_count:
    if not os.path.exists(i):
        os.makedirs(i)

character_list = []
realm_list = []


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def logOutput(msg, logType):
    # Log
    if logType == 1:
        # print("\n[ LOG ] " + msg)
        write_to_file("\n[LOG] " + msg, globalLogPath, "a+")
    # Error
    elif logType == 2:
        # print("\n[ ERROR ] " + msg)
        write_to_file("\n[ERROR] " + msg, globalLogPath, "a+")
    # Warning
    elif logType == 3:
        # print("\n[ WARNING ] " + msg)
        write_to_file("\n[WARNING] " + msg, globalLogPath, "a+")


def read_from_json(json_path: str):
    with open(json_path, "r") as json_file:
        data = json.load(json_file)
    json_file.close()
    return data


settings = {
    "_comment": "Settings JSON file, Don't Mess with the values if you don't know what you're doing thanks :D",
    "activeRealm" : ""
}


# socket_chat_settings = {
#    "_comment": "Settings Used with the socketchat client module:",
#    "USERNAME": "",
#    "IP": "cH4nG3_tH1S",
#    "PORT": "cH4nG3_tH1S",
# }

    # Json socketchat settings file
    #    if not os.path.exists(global_settings_socketchat_path):
    #        json_settings = json.dumps(socket_chat_settings)

    #        with open("settings_socketchat.json", "w") as jsonfile:
    #            jsonfile.write(json_settings)
    #        jsonfile.close()
    #
    # Master Global Latest Log File


def get_lines(text_obj, output: bool):
    logo_lines = []
    if type(text_obj) == list:
        for line in text_obj[random.randint(0, len(text_obj) - 1)].split("\n"):
            logo_lines.append(line)
    else:
        for line in text_obj.split("\n"):
            logo_lines.append(line)

    if output:
        for line in logo_lines:
            time.sleep(0.1)
            print(line)


createGlobalLogFile()


def write_to_file(text_to_write, path_to_file, typeOfWrite):
    if os.path.exists(path_to_file):
        write_file = open(path_to_file, typeOfWrite)
        write_file.write(text_to_write)
        write_file.close()


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

op3x_menu = '''
######################################################################
##                       - Create Character( cc )                   ##
##                       - List Characters( lc )                    ##
##                  ---------------------------------               ##
##                       - Create Realm( cr )                       ##
##                       - List Realms( lr )                        ##
##                  ---------------------------------               ##
##                       - Exit/Terminate(E/e/Q/q)                  ##
######################################################################
'''


def main():
    while True:
        clear()
        get_lines(op3x_text, True)
        get_lines(op3x_menu, True)

        usr_sel = input("~$: ")

        if usr_sel.lower() == "cc":
            continue
        else:
            print("Please Input A Valid Selection!")
            time.sleep(1)


if __name__ == '__main__':
    main()
