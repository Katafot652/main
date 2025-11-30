n = int(input("Введіть кількість ігор: "))

teams = {}

for _ in range(n):
    match = input() 
    team1, score1, team2, score2 = match.split(';')
    score1, score2 = int(score1), int(score2)

    if team1 not in teams:
        teams[team1] = [0, 0, 0, 0, 0] 
    if team2 not in teams:
        teams[team2] = [0, 0, 0, 0, 0]

    teams[team1][0] += 1
    teams[team2][0] += 1

    if score1 > score2:  
        teams[team1][1] += 1
        teams[team1][4] += 3
        teams[team2][3] += 1
    elif score1 < score2:  
        teams[team2][1] += 1
        teams[team2][4] += 3
        teams[team1][3] += 1
    else:  # Нічия
        teams[team1][2] += 1
        teams[team2][2] += 1
        teams[team1][4] += 1
        teams[team2][4] += 1

for team, stats in teams.items():
    print(f"{team}: {stats[0]} {stats[1]} {stats[2]} {stats[3]} {stats[4]}")
