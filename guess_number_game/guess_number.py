import random, time

no_of_tries = 0
start = time.time()
random_num = random.randint(1, 100)

while True:
    raw = input("Guess a number between 1 to 100: ")

    try:
        num = int(raw)
    except:
        print("Sorry, enter an integer number..")
        continue

    if num is random_num:
        no_of_tries += 1
        end = time.time()
        print()
        print("You guessed right!")
        print()
        print("Number of tries: %s" % no_of_tries)
        print("Run time was: %s" % int(end - start), "seconds")
        break
    elif num < random_num:
        no_of_tries += 1
        print("Try higher..")
    else:
        no_of_tries += 1
        print("Try lower..")
