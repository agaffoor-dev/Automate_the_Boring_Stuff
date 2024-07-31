import time
import playsound

initial = int(input("How many seconds? "))

stop = 0

while initial > stop:
    initial -= 1
    time.sleep(1)
    print(initial, end = "\r")

