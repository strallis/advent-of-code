from aocd import lines  # type: ignore
#lines = ['A Y','B X','C Z']
score1 = 0
score2 = 0

for game in lines:

    if game[0] == 'A':
        if game[2] == 'X':
            score1 += 4
            score2 += 3
        elif game[2] == 'Y':
            score1 += 8
            score2 += 4
        else:
            score1 += 3
            score2 += 8
    elif game[0] == 'B':
        if game[2] == 'X':
            score1 += 1
            score2 += 1
        elif game[2] == 'Y':
            score1 += 5
            score2 += 5
        else:
            score1 += 9
            score2 += 9
    else:
        if game[2] == 'X':
            score1 += 7
            score2 += 2
        elif game[2] == 'Y':
            score1 += 2
            score2 += 6
        else:
            score1 += 6
            score2 += 7
print(f'1:{score1},2:{score2}')
