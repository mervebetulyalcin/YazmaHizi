import datetime
import time

print("Please enter your sentence after 3 second.")

count = 4
while 1 < count:
    count = count - 1
    print(count)
    time.sleep(1)

start = datetime.datetime.now()
text = input("Text: ")
finish = datetime.datetime.now()
speed = finish - start
seconds = round(speed.total_seconds(),2)
letter_per_second = round(len(text)/seconds)

print(f"You typed in {seconds} seconds.")
print(f"{letter_per_second} letters per second.")