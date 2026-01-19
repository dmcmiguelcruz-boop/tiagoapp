import random
import time

def greet(name):
    greetings = ["Hello", "Hey", "Hi", "Howdy", "Greetings"]
    return f"{random.choice(greetings)}, {name}!"

def roll_dice(sides=6):
    return random.randint(1, sides)

def fortune():
    fortunes = [
        "Today is your lucky day!",
        "Something exciting is coming.",
        "Take a chance on something new.",
        "Good things come to those who code.",
    ]
    return random.choice(fortunes)

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"  {i}...", end=" ", flush=True)
        time.sleep(0.3)
    print("Go!")

def magic_8ball():
    answers = ["Yes", "No", "Maybe", "Ask again later", "Definitely", "Doubtful"]
    return random.choice(answers)

if __name__ == "__main__":
    print(greet("Miguel"))
    print(f"Rolling dice:", end="")
    countdown(3)
    print(f"  You rolled: {roll_dice()}")
    print(f"Magic 8-Ball says: {magic_8ball()}")
    print(f"Fortune: {fortune()}")
