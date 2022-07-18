helpTxt = input("")
if helpTxt == 'help':
    print("start -> to start the engine")
    print("stop -> to turn of the engine")
    print("quit -> to stop")

while True:
    inputTxt = input("")
    if inputTxt == 'start':
        print("engine starts->ready to go")
    elif inputTxt == 'stop':
        print("turn of the engine")
    elif inputTxt == 'quit':
        print("exit from the game")
        break
    elif inputTxt != 'start' or inputTxt != 'stop' or inputTxt != 'quit':
        print("not a valid input")
        break
