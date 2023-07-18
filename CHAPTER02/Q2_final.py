import random

alphabet = "abcdefghijklmnopqrstuvwxyz"

while True:
    random_letter = random.choice(alphabet)
    print(random_letter)
    if random_letter == "t":
        break
