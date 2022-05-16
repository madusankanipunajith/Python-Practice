while True:
    inp = input("> ")
    if inp.lower() == "help":
        print("start : To start the car")
        print("stop : To stop the car")
        print("exit : Quit the game")
    elif inp.lower() == "start":
        print("Car started... ready to go")
    elif inp.lower() == "stop":
        print("Car is stopped")
    elif inp.lower() == "quit":
        break
    else:
        print("Can't understand the command")

print("Thank you")


