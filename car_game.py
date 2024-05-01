#car game
    
command = ""
car_started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if car_started:
            print("car is already started")
        else:
            car_started = True
            print("car started.. ready to go!")
    elif command ==  "stop":
        if not car_started:
            print("car is not running")
        else:
            car_started = False
            print("car stopped")
    elif command == "help":
        print("start - to start the car\nstop - to stop the car\nquit - to exit")
    elif command == "quit":
        break
    else:
        print("i don't understand that")
