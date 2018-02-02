from random import choice
questions= ["Why is the sky blue?", "WHy are there so many haters?", "Why is Malcolm so fine?"]
question = choice(questions)

answer= input(" What is the meaning of life?: ").strip().title()
while answer != "Just Because":

    answer= input("Whyyyyy?").strip().title()

print("Oh...")
