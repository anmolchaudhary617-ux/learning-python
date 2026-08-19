car_started = False
while True:
    start_game = input('>').lower()
    if start_game == "help":
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')
    elif start_game == "start" and car_started == False: 
        print('Car started...Ready to go!')
        car_started = True
    elif start_game == "start" and car_started == True: 
        print('Car already Started!')
    elif start_game == "stop" and car_started == True:
        print('Car stopped.')
        car_started = False
    elif start_game == "stop" and car_started == False:
        print("Car already stopped! or Car hasn't started yet!")
    elif start_game == "quit":
        break
    else:
        print("I don't understand...")
    