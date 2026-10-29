import time
import random

while True:
    time_to_guess = random.randint(5, 15)

    print(f"Guess the time. Your time is {time_to_guess}s")
    input("press enter to start>")

    start_time = time.time()

    input("Press enter to stop time>")

    end_time = time.time()
    final_time = end_time-start_time
    off_time = final_time-time_to_guess

    print(f"\nThe time to guess was: {time_to_guess}.\nYour time was: {final_time :.2f}\nYou where off by: {off_time :.2f}\n")
