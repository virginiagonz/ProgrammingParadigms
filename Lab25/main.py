# This program displays how multithreading and concurrency works
# using a producer and consumer function
#
# Created by Virginia Gonzalez
# November 18, 2022

from time import sleep
from threading import Thread
from queue import Queue
import random


# this function adds a random number to a queue 1s apart
# and prints the number added to the queue
def producer(queue, num):
    for x in range(num):
        y = random.randint(1, 50)
        sleep(1)
        queue.put(y)
        print("added to queue: " + str(y))


# this function prints and removes the next number from the queue 2s apart
# then task_done() is called to notfiy joins when
def consumer(queue, num):
    for y in range(num):
        x = queue.get()
        sleep(2)
        print("popped from queue: " + str(x))
        # The Queue.join() function only works if threads retrieving items or
        # tasks from the queue via Queue.get() also call the Queue.task_done() function.
        queue.task_done()


# num variable to add items to a queue
# testq variable to hold a queue
num = 6
testq = Queue()

# create two new threads, one for consumer and another for producer
producer = Thread(target=producer, args=[testq, num])
consumer = Thread(target=consumer, args=[testq, num])

# starting the threads
producer.start()
print("starting producer")
consumer.start()
print("starting consumer")

# waiting for the threads to finish
producer.join()
print("finished producer")
consumer.join()
print("finished consumer")




