import secrets

def generate_passphrase(num):
    with open("dicewarewordlist.txt", "r") as file:
        lines = file.readlines()[2:7778]
        word_list = [line.split()[1] for line in lines]

    words = [secrets.choice(word_list) for i in range(num)]
    return " ".join(words)
