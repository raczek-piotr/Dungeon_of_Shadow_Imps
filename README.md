## Dungeons of Shadow Imps
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Errors in curses](#errors-in-curses)
* [Contact](#contact)
* [Authors](#authors)

## General info
* Roguelike game with simple interface played in console.
* The polish translation is disabled default, so you can enable it in "local_translator.py" `lang = "PL"` but it is't finished yet… -PR-
* game characters: https://github.com/raczek-piotr/Dungeon_of_Shadow_Imps/blob/main/curses/characters.md
	
## Technologies
### Project with curses is created with (curses):
* Python 3.10 or better
* Libraries: curses
* Size(x,y): 80x24
* FontSize: What do you like!
	
## Setup
* To run this project with curses, run terminal or cmd in windows, and run the file "main.py" is (in main dictionary);
* To run it, type command "python3 main.py".
* Or just run the .exe file (you will need "maps" folder)
	
## Errors in curses
### Errors:
  1. `no module called curses` or `no module called _curses`
      *  curses is not installed
      *  install windows.curses
  2. `_curses.error: setupterm: could not find terminal`
      *  you had to ran it in editor's terminal or console, but it has it be the terminal/cmd (ctrl + t, great shortcut in thonny)
  3. if any errors occur while playing, there is simple logfile with **almost** no *log* in it

## Contact
* email raczek.piotr@o2.pl

## Authors
* By: Piotr Raczek
* Comments in code: -PR-
