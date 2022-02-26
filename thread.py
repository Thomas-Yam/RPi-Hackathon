from threading import Thread
from time import sleep

result = None

def update_every_second():
    while result is None:
        print("update")

t = Thread(target=update_every_second)
t.start()
result = input('Type something: ')

print ("The user typed", result)