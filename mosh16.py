command=""
while command!="quit":
    command=input(">").lower()
    if command=="start":
        print("Car started...")
    elif command=="stop":
        print("car stopped.:")
    elif command=="help":
        print("""
              start-to start the car
              stop-to stop yhe car
              quit-to quit
              """)
    else:
        print("Sorry,I don't undarstand that!")