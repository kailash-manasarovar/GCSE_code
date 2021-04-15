karls_wins = 0
johns_wins = 0

for game in range(0, 10):
    winner = input("Who is the winner?, enter 'K' or 'J'")
    if winner == "K":
        karls_wins = karls_wins + 1
    elif winner == "J":
        johns_wins = johns_wins + 1

if johns_wins > karls_wins:
    print("John is the winner")
elif karls_wins > johns_wins:
    print("Karl is the winner")
else:
    print("It's a draw!")

