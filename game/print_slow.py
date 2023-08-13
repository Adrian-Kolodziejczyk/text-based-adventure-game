from time import sleep
from sys import stdout


def print_slow(text):
    for char in text:
        stdout.write(char)
        stdout.flush()
        sleep(0.5 / (len(text)))


def input_slow(text):
    print_slow(text)
    return input()
