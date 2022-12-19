# A = rock       = 1 (X)
# B = paper      = 2 (Y)
# C = scissors   = 3 (Z)

file = open("puzzle_input.txt","r")
my_score = 0

for line in file:
    opponent = line[0]
    me = line [2]

    if me == "X":
        #I have a rock.
        my_score += 1
        if opponent == "A":
            my_score += 3
        elif opponent == "C":
            my_score += 6

    elif me == "Y":
        #I have paper.
        my_score += 2
        if opponent == "B":
            my_score += 3
        elif opponent == "A":
            my_score += 6

    elif me == "Z":
        #I have scissors.
        my_score += 3
        if opponent == "C":
            my_score += 3
        elif opponent == "B":
            my_score += 6

print("My score is: ", my_score)
