# REPEAT
#   OUTPUT ‘Please enter the winners name’
#       winner = USERINPUT
#   if winner = karl
#       karls_wins += 1
#   else if winner = john
#       jons_wins += 1
# UNTIL games_played > 10
#
#
# if karls_wins > jons_wins
#   OUTPUT 'Karl is the winner'
# else if jons_wins > karls_wins
#   OUTPUT 'Jon is the winner'
# else
#   OUTPUT 'It's a draw!'

games_played = 0
#karls_wins = 0
#jons_wins = 0

while games_played <= 10:
    winner = input("Please enter the winner's name.")
    if winner == 'Karl':
        karls_wins = karls_wins + 1
    elif winner == 'Jon':
        jons_wins = jons_wins + 1
    else:
        "Please spell the name correctly"

if karls_wins > jons_wins:
    print("Karl is the winner")
