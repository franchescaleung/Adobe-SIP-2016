start = '''
You wake up one morning and find that you aren’t in your bed; you aren’t even in your room.
You’re in the middle of a giant maze.
A sign is hanging from the ivy: “You have one hour. Don’t touch the walls.”
There is a hallway to your right and to your left.
'''

print("start")


print("Type 'left' to go left or 'right' to go right.")
user_input = input()
while (user_input != "left" and user_input != "right"):
    print("Oops! Please choose a side!'")
    user_input = input("Type 'left' or 'right'")
    
if user_input == "left":
    print("You decide to go left and you see a giant gorilla in front of you. He looks like he's ready for some lunch.") 
    user_input = input("Type 'ahead' to go towards the gorilla or 'run back' to turn away and run.")
    while (user_input != "ahead" and user_input != "run back"):
        print("Either run 'ahead' or 'run back'")
        user_input = input("Type 'ahead' or 'run back'")
    if user_input == "ahead":
        print("The Gorilla tries to attack you. What's your fate?")
        user_input = input("Choose a color 'blue' or 'green'")
        while (user_input != "blue" and user_input != "green"):
            print("Pick a color")
            user_input = input("Type 'green' or 'blue'")
        if user_input == 'blue':
            print("You escape!! Congrats!! Now don't run into any other trouble.")
        elif user_input == 'green':
            print("The gorilla digests you slowly. Sorry, but it's hard to escape from inside a gorilla. Good luck!")	
    elif user_input == "run back":
        print("Don't look back! A gorilla one undred times your size chases after you. What will you do?")
        user_input = input("Type 'hide' or 'run' to continue running")
        while (user_input != 'hide' and user_input != 'run'):
            print("You only have two options!")
            user_input = input("Type 'hide' or 'run'")
        if user_input == 'hide':
            print("That was a close one! I think you lost the gorilla! Find a big tree to hide behind for now. ")
        elif user_input == 'run':
            print("The gorilla eats you. Should have known you couldn't run out that giant.")
	
elif user_input == "right":
    print("You choose to go right and you step into a puddle of mud.") 
    user_input = input("Type 'leave' to step away from the puddle or 'stomp' to stay")
    while (user_input != "leave" and user_input != "stomp"):
        print("Either leave or stomp on the mud")
        user_input = input("Type 'leave' or 'stomp'")
    if user_input == "leave":
        print("You continue exploring the rest of the jungle.")
        user_input = input("You reach a diverged road. Pick road 'a' or 'b'")
        while (user_input != "a" and user_input != "b"):
            print("Pick a letter")
            user_input = input("Type 'a' or 'b'")
        if user_input == 'a':
            print("You've reached a dead end.")
        elif user_input == 'b':
            print("You split open these two tall plants and discover another kingdom.")	
    elif user_input == "stomp":
        print("You get yourself all dirty.")
        user_input = input("Type 'touch' to touch the wall or 'clean' to find a shower")
        while (user_input != 'touch' and user_input != 'clean'):
            print("Do you want to touch the wall or clean yourself?")
            user_input = input("Type 'touch' or 'clean'")
        if user_input == "touch":
                print("You touch the wall and go into another dimension.")
        elif user_input == "clean":
                print("You find youself a shower in the middle of a jungle??")
