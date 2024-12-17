name = input("Hi, type your name: ")
print("Hello", name + "! This is a choose your own adventure game.")

will_you_play = input("Do you want to play? ").lower()

if will_you_play == "yes" or will_you_play == "y":
    print("Horray, let's play!")
    device = input("Choose a device (matches/snacks): ").lower()
    
    direction = input("Do you want to go left or right? (left/right)").lower()
    if direction == "left":
        print("We went left and fell into a trap. Game over. Try again.")
    elif direction == "right":
        choice = input("Okay, you now see a hot air balloon. Do you fly it or keep walking? (fly/walk)"
        ).lower()
        if choice == "fly" and device == "snacks":
            print("We can't start the air balloon. We wait for the pilot, but he nevers comes. Game over."
        )
        elif choice == "fly" and device == "matches":
            print("Shwew, we made it. Good thing you brought those matches. I see a town! We're saved!"
        )
        if choice == "walk" and device == "snacks":
            select = input("We've been walking for a long time, should we go back? (yes/no): "
            ).lower()
            if select == "yes" and device == "snacks":
                print("We made it back to the air balloon! And the pilot is here! He takes snacks as payment. We're saved!"
            )
            else:
                print("I ate all the snacks. Game over.")
        elif choice == "walk" and device == "matches":
            print("A bear comes, but we don't have snacks. Game over.")
    else:
        print("Sorry, bad choice. You were abducted by aliens.")
else:
    print("Wah, wahhhhhh.")