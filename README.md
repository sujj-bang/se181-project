# se181-project #

### Release Notes	### 

### Version 1.0.0 ###
#### November 30, 2020 ####
_ _ _ _

#### Description: ####
  Checkers Initial Release!


#### Requirements: ####
  * Each client (player) must download the whole source code file in order to run the game correctly.
  
  * Python3.x, the pygame module, and pip must be installed and imported in order to play this game of checkers.
  
  * Server in server.py and network.py are set to ‘localhost’ at the moment, if players want to play outside of localhost, they must change the server IP address to their IPV4 address. IPV4 address allows players to play if they are on the same wifi network as the server.
  
  * In order to run the game, ‘server.py’ must be run first *python3 server.py*, then the each client may run  ‘menu.py’ *python3 server.py* in their separate terminal (macOs)/powershell(Windows).
  
  * Only two clients may access the game of checkers at the moment of release


#### New Features: ####
  * Users can play a game of checkers on their own or with a friend!
  
  * Two users can join and connect to a game.
  
  * Users can add their player names in the menu screen.
  
  * User can select a desired color for their checker pieces (tbd).


#### Known Issues: ####
  * If a client (player) exits out of the game, and he/she/they try(s) to start the game again without restarting the server, the game will show up the way it was left. At that screen there are no movements on screen. In order to play a new game, server.py must restart.
  
  * When a client (player) clicks too fast or clicks on too many items on the screen, the game may freeze for a couple seconds, but that is refreshed on its own in a short amount of time. If the client takes a breath for one second and tries to click on the checkers piece calmly, the game will work as expected.
  
  * The name feature on the checkers menu is not actually a required input in order to start the game. 


#### Out of Scope: ####
  * Once time permits, features listed below may become part of Group 9’s deliverables for future releases:
    * Messaging feature during the game between the two players
    * Utilizing the name feature on the menu screen for the game itself
    * Display of pieces that each player has captured
    * Allowing multiple games to be run on the server for various clients (players)
