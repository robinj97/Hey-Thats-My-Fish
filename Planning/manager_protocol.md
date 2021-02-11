The tournament manager;
 signs up players for tournaments, 
 allocates players to games,  
 creates referees to run games, 
 and collects tournament statistics. 
 It also informs a tournament observer of on-going actions. 
 
 Calling Sequence
================

1. __init__
    
        Always called first
        Initalizes the tournament manager, creating a tournament manager object

2. add_player


        This function will then access the available players and add them to a tournament.

3. start_tournament

        Once players have been added to the tournament, the tournament can start, this function will perform various operations


        - Runs tournament
            - For each game in the tournament:
                - Adds referee
                    - The referee sets up the game after its passed the list of players
                    - Referee can add observers as observers wish to be added to specific game
                - Once game is ended get_info is called to store the info for the tournament observer

4. get_info

        This method will be called once events occur within the tournament.
        An event may be one of:
            - Player winning a single game
            - Player getting kicked from a single game
            - Tournament concluding


 * add_observer 

        This method can be called anytime after the tournament manager is created
        add_observer adds a tournament_observer that will receive update about the tournament (when games end and when the tournament ends) which will be one of:
            -("Game Ended", winners, final game_state)
            -("Tournament Ended", winner, List of Games)
                - where winner is the Player who won and the a game is a tuple of (list of winning Players, final game_state)