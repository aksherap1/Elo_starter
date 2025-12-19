#------------------------------------------------------------------------------
# Run this script to update players' chess ratings after a game, using a
# standard Elo scheme with a single k-factor.
#------------------------------------------------------------------------------
# Define the rating system's calibration parameters here
S = 400 # an advantage of scale points predict ~75% win rate
K = 32 # the maximum number of points at stake to win/lose in a game

# Get players' current rating and game outcome from user
p1 = float(input("What is your current rating? "))
p2 = float(input("What is your opponent's rating? "))
score = float(input("How did you do (win=1, lose=0, draw=0.5)? "))

# Calculate player 1's expected score, i.e., probability of winning
expected = 1 / (1 + 10 ** ((p2 - p1) / S))

# The update scheme gives player 1 a fraction of the stake proportional to
# the difference between their actual score and expected score
difference1 = p1 + K * (score - expected)

# Player 2's update can be calculated the same way, but taking into account the
# symmetry in all the algebra you can easily see that it simplifies to just
# being the reverse of player 1's update, i.e., however many points player 1
# gained or lost, player 2 lost or gained...
difference2 = p2 + K * ((1 - score) - (1 - expected))

# The script ends by printing both player's updated ratings
print(f"Your new rating is {round(difference1)}.")
print(f"Opponent's new rating is {round(difference2)}.")
