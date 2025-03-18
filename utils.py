from pygame import mixer
import math

def map_coords(x, y):
    # mapped_x = (y / 1080) * 1920
    # mapped_y = 1080 - ((x / 1920) * 1080)
    mapped_x = x
    mapped_y = y
    return mapped_x, mapped_y

def play_sound(file_path):
    mixer.music.stop()
    mixer.music.load(file_path)
    mixer.music.play()

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)