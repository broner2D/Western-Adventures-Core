import GameHandlerModules

while True:
    cammand = input("> ")
    print(GameHandlerModules.commands.execute(cammand))