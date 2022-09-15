import subprocess
import pywhatkit as kt
import os
import threading
import time

visual_subprocess_active = True

current_source_picture = "./img/test_goblin.png"
source_path = current_source_picture
target_path = "./img/ascii_output/temp.text"

kt.image_to_ascii_art(source_path, target_path)


def visual_thread():
    visual_subprocess = subprocess.call('start python visuals.py', shell=True)


def main_game_thread():
    print("Main Game Thread INIT")
    visual_active = visual_subprocess_active
    while visual_active:
        print("Main Game Thread")
        time.sleep(2)
    print("sub_proc not active")


def game_manager():
    pass


def main():
    vt = threading.Thread(target=visual_thread, name="vt")
    mgt = threading.Thread(target=main_game_thread, name="mgt")
    # gm = threading.Thread(target=game_manager, name="gm")
    mgt.start()
    vt.start()

    mgt.join()
    vt.join()
    # gm.start()


if __name__ == '__main__':
    main()
