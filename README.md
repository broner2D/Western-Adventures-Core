# Western Adventures Core

This is a replit source project that contains the core code for a text-based adventure game set in the Wild West. The
game is written in Python and uses the `adventurelib` library to handle the game logic and commands.

## Features

- A dynamic and interactive world with multiple locations, items, characters, and events.
- A rich and immersive story with branching paths and multiple endings.
- A simple and intuitive command system that lets you explore, interact, and fight in the game world.
- A save and load feature that lets you resume your game from any point.
- A custom map generator that creates a unique world for each playthrough.

## How to play

To play the game, you need to run the `main.py` file in the replit workspace. You will see a welcome message and a
prompt where you can enter commands. You can type `help` to see a list of available commands, or `look` to see your
current location and surroundings.

Some of the commands you can use are:

- `go <direction>`: Move to a different location in the given direction (north, south, east, west).
- `look`: Look around your current location and see what you can interact with.
- `examine <object>`: Examine an object more closely and see if it has any hidden features or secrets.
- `take <object>`: Take an object and add it to your inventory.
- `use <object>`: Use an object in your inventory or in your surroundings. This can have different effects depending on
  the object and the situation.
- `talk <character>`: Talk to a character and learn more about them or the world. You can also ask them questions or
  give them commands.
- `fight <character>`: Fight a character if they are hostile or if you want to challenge them. You can use weapons or
  items in your inventory to improve your chances of winning.
- `inventory`: See what items you have in your inventory.
- `save`: Save your current game progress to a file.
- `load`: Load a previously saved game from a file.
- `quit`: Quit the game.

## How to modify

If you want to modify the game or create your own adventure, you can edit the files in the `src` folder. The files are
organized as follows:

- `main.py`: The main file that runs the game loop and handles user input and output.
- `world.py`: The file that defines the world class and its methods. The world class contains all the locations, items,
  characters, and events in the game world.
- `map.py`: The file that defines the map class and its methods. The map class generates a random map for each
  playthrough using Perlin noise and cellular automata algorithms.
- `location.py`: The file that defines the location class and its methods. The location class represents a single place
  in the game world with a name, description, exits, items, characters, and events.
- `item.py`: The file that defines the item class and its methods. The item class represents an object that can be
  interacted with in the game world with a name, description, type, attributes, and effects.
- `character.py`: The file that defines the character class and its methods. The character class represents a person or
  an animal that can be interacted with in the game world with a name, description, health, inventory, dialogue,
  actions, and reactions.
- `event.py`: The file that defines the event class and its methods. The event class represents a special occurrence
  that can happen in the game world with a name, description, condition, effect, and frequency.

You can modify any of these files to change or add new features to the game. For example, you can add new locations,
items, characters, or events by creating new instances of their respective classes and adding them to the world object.
You can also change how the map is generated by tweaking the parameters of the map object.

## Credits

This project was created by @broner3D using replit.com, a collaborative browser based IDE that lets you code and
collaborate from anywhere. The project was inspired by classic text-based adventure games such as Zork and Colossal Cave
Adventure.

: https://replit.com/
: https://github.com/replit
: https://docs.replit.com/hosting/sharing-your-repl