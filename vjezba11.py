import json
import random
import datetime


current_time = datetime.datetime.now()

secret = random.randint(1, 30)
attempts = 0

wrong_guesses = []

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())

for score_dict in score_list:
    print("Attempts: " + str(score_dict.get("attempts")) + " " + "Time:" + score_dict["time"] + " Name: " + score_dict["player_name"] + " Secret number: " + score_dict["secret_number"] + " Wrong guesses: " + str(score_dict["wrong_guess"]))

name = input("Your name: ")

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        score_list.append({"attempts": attempts, "time": str(current_time), "player_name": name, "secret_number": str(secret), "wrong_guess": wrong_guesses})
        wrong_guesses.append(guess)
        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break

    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

    wrong_guesses.append(guess)
