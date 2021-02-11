#initializer (creates a tournament manager object)
def __init__(self)

# Player Date -> Void
# Adds a player to the tournament where the given date represents the player's birthdate
#   - birth date is used for passing players to the referee in age ascending order
def add_player(self,Player,dob)

# Adds a tournament observer to the list of observers who receieve updates about the tournament
#   - the given Observer must be an object that implements update_tournament_observer(msg) with signature (TournamentUpdate -> Void)
#       - where TournamentUpdate is one of: 
#            -("Game Ended", List of Player, game_state)
#                - where winners is a List of Player and the game_state is the final state of the game
#            -("Tournament Ended", Player, List of Games)
#                - where Player is the player who won and a game is a tuple of (List of Player, game_state) = winning player, final game state
def add_observer(self, observer)

# void --> void
# Starts a single tournament and runs it (taking care of the execution of the whole tournament)
#   - includes organizing players into games, creating referees to execute the games, advancing winning players to the next round, and ending with a single winner
def start_tournament(self)

# Void -> TournamentInfo
# Gets a tournament's statistics
#   - where TournamentInfo is one of:
#       -("Tournament Ended", Player, List of Games)
#           - where Player is the player who won and a game is a tuple of (List of Player, game_state) = winning player, final game state
#       -("In progress", List of Games)
#           - where a game is a tuple of (List of Player, game_state) = winning player, final game state
def get_tournament_stats(self)


