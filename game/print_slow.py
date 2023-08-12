from time import sleep
import sys


def print_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.05)
    sleep(0.5)


def input_slow(text):
    print_slow(text)
    return input()
