"""
Function takes two arguments, a string player name
and an integer score, and keeps a "high score" table
in a Python shelve.
"""
import shelve

def check_player_score(name,score):
    """ If the score is higher than the player's current high score,
        or if the player has no recorded score, log the score as the
        new high score. Returns the current high score for player.
    """
    shelf = shelve.open(r'v:\workspace\PersistentStorage_Homework\src\myshelf.shlf', writeback=True)
    
    # Check if player has an existing score
    try:
        existing_score = shelf[name]
    except KeyError:
        existing_score = 0
    
    # Store the new score if higher or no score
    high_score = max(score,existing_score)
    shelf[name] = high_score
    shelf.close()
    
    # Return high score
    return high_score