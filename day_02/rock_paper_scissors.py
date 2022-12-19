# A = rock       = 1
# B = paper      = 2
# C = scissors   = 3

file = open("puzzle_input.txt","r")
my_score = 0

for line in file:
    first_elf = line[0]
    second_elf = line [2]


    if first_elf == "A":
        #I have a rock.
        my_score += 1
        if second_elf == "X":
            my_score += 3
        if second_elf == "Z":
            my_score += 6

    elif first_elf == "B":
        #I have paper.
        my_score += 2
        if second_elf == "Y":
            my_score += 3
        if second_elf == "X":
            my_score += 6
    elif first_elf == "C":
        #I have scissors.
        my_score =+ 3
        if second_elf == "Z":
            my_score += 3
        if second_elf == "Y":
            my_score += 6

print("My score is: ", my_score)
