known_users=["Alice", "Bob", "Shakira", "Desiree", "Aaliyah"]

while True:
    print("My name is Travis, I am a SPIRIT!")
    name= input(" What's your name?: ").strip().capitalize()
    if name in known_users:
        print("Thou Shalt Pass!")
        remove= input("Would you like to be removed from the system (y/n)?").lower()
        if remove == "y":
            print(known_users)
            known_users.remove(name)
            print(known_users)
        elif remove =="n":
            print("No problem, I didn't want you to leave!")

    else:
        print("Hmmm... I don't think that we've met yet {}".format(name))
        add_me= input("Wanna be added, though (y/n)?: ").strip().lower()
        if add_me == "y":
            known_users.append(name)