DnDSim
by Andrew Lin

DnDSim
    DnDSim is a minimalistic tool used to simulate a DnD encounter. The tool is
    capable of holding a few stats of monsters and characters: namely health,
    AC, initiative/turn order, and name. The tool is capable of modifying all
    these stats even after a character/monster has been inserted into the table.
    After a character has been inserted, they will automatically be placed 
    into the proper spot based on turn order. 

    After all monsters and characters are added, a battle can be started, which
    will indicate which character/monster is currently taking a turn. The next
    turn can then be called. This allows for smooth tracking of the turn order,
    an easy way to see critical stats.

    In order to run this program, the python package Tabulate is required. This
    can be installed with the following command:

    pip install tabulate



Usage
    In order to run DnDSim.py use a terminal and navigate to the directory that
    DnDSim is located in. Then, run the program with the following command

    py main.py
    
Commands
    Once the program is running, use the following commands to run the program.
    Most commands will ask for a character's index.

    add:
        adds a character to the program. The stats of the character will be 
        asked for by the program.
    remove: 
        Removes a character from the program.
    damage:
        Damages a character an amount of damage. 
    heal:
        Damages a character an amount of damage.
    armora: 
        Adds armor to a character's armor stat
    armorb:
        Removes armor from a character's armor stat
    start:
        Starts a round of combat. The top character will be marked as the first
        character in the turn order by an x in the column.
    Next: 
        Moves the marker to the next row. Essentialy simulates the end of a 
        round, marking the next character's turn.
    Quit:
        Quits the program.

    The program outputs descriptions of the commands after running.