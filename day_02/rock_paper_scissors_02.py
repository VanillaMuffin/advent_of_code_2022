# A = rock       = 1 (X)
# B = paper      = 2 (Y)
# C = scissors   = 3 (Z)

file = open("puzzle_input.txt","r")
my_score = 0

for line in file:
    opponent = line[0]
    me = line [2]

    if me == "X":
        #I need to loose.
        my_score += 0
        if opponent == "A":
            my_score += 3
        elif opponent == "B":
            my_score += 1
        else:
            my_score += 2

    elif me == "Y":
        #Draw.
        my_score += 3
        if opponent == "A":
            my_score += 1
        elif opponent == "B":
            my_score += 2
        else:
            my_score += 3

    elif me == "Z":
        #I need to win.
        my_score += 6
        if opponent == "A":
            my_score += 2
        elif opponent == "B":
            my_score += 3
        else:
            my_score += 1

print("My score is: ", my_score)
