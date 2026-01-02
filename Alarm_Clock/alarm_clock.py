import time
import pygame

pygame.mixer.init()

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will ring in: {minutes_left:02d}:{seconds_left:02d}")

    pygame.mixer.music.load(r"D:\Projects\Python-Projects\Alarm_Clock\audio.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)


try:
    minutes = int(input("Enter minutes: "))
    seconds = int(input("Enter seconds: "))

    if minutes < 0 or seconds < 0:
        raise ValueError

    total_seconds = minutes * 60 + seconds
    alarm(total_seconds)

except ValueError:
    print("Please enter valid non-negative integers.")