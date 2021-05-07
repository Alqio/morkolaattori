import RPi.GPIO as GPIO
from time import sleep
from Queue import Queue
import pygame
from datetime import datetime

light_pin = 16
limit = 300
sound_file = "morko.mp3"

GPIO.setmode(GPIO.BOARD)

pygame.mixer.init()
pygame.mixer.music.load(sound_file)
playing = False
played = False

def light_time(pin):
    count = 0

    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    sleep(0.1)

    GPIO.setup(pin, GPIO.IN)

    while GPIO.input(pin) == GPIO.LOW:
        count += 1

    return count


pygame.mixer.music.play()
pygame.mixer.music.pause()

played_at = None

try:
    q = Queue(max_length=20)
    while True:
        t = light_time(light_pin)
        q.add(t)
        print(q.average())

        if q.average() > limit:
            if not playing:
                pygame.mixer.music.unpause()
                #pygame.mixer.music.rewind()
                playing = True
                played_at = datetime.now()
        else:
            pygame.mixer.music.pause()
            playing = False
        
        if played_at:
            diff = datetime.now() - played_at
            diff_in_hours = diff.total_seconds() / 3600
            if diff_in_hours >= 4:
                pygame.mixer.music.rewind()

except KeyboardInterrupt:
    print("Stopping")

finally:
    GPIO.cleanup()
