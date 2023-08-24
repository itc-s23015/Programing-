import random

# 何回実行しても同じ結果になるように乱数の種(seed)を固定する
random.seed(1)
msgs = [
    "Hi",
    "Hello",
    "Good morning",
    "Good night",
    "See you later",
    "How are you",
    "Have a good day",
]
with open("some.py", "w") as f:
    for i in range(1000000):
        f.write("{}, {}\n".format(i, random.choice(msgs)))
