from GameHandlerModules import help
from sys import exit
import random

def execute(command):
    commands = ["play", "help", "exit", ""]
    if command == commands[0]:
        random.randrange(1, 10)
    
    if command == commands[1]:
        help.display()
    if command == commands[2]:
        exit(0)
    if command == commands[3]:
        return ""
    
