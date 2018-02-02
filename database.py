films= {
    "Bourne": [17, 12],
    "It": [13,10],
    "Wonder Woman": [10,2],
    "Superman":[13,2],
    "Payback": [8,5]

}

while True:
    choice= input("What would you like to see?:").strip().title()

    if choice in films :
        age= int(input("How old are you?:").strip())
        if age > films[choice][0]:
            num_seats=films[choice][1]

            if num_seats > 0:

                print("Say no more, fam. Enjoy my guy:")
                films[choice][1]= films[choice][1]-1
            else:
                print("Sorry, we are sold out!")
        else:
            print ("You tried it. You know you're too young.")

    else :
        print("Nahhhh my guy. We don't have that film.")