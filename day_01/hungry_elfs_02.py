file = open("food_list.txt","r")
current_elf_calories=0
list_of_elfs_with_max_calories=[]
elf_with_max_calories=0
for line in file:
    if line.strip():
        #Check if line is empty.
        current_elf_calories+=int(line)
        print("Current callories: ", current_elf_calories)
    else:
        #Line is empty.
        if len(list_of_elfs_with_max_calories) < 3:
            list_of_elfs_with_max_calories.append(current_elf_calories)

        elf_with_min_calories = min(list_of_elfs_with_max_calories)
        if current_elf_calories > elf_with_min_calories:
            list_of_elfs_with_max_calories[list_of_elfs_with_max_calories.index(elf_with_min_calories)] = current_elf_calories
        #Reset the callories counter.
        current_elf_calories=0

print("Elfs with max calories have:", (list_of_elfs_with_max_calories[0] + list_of_elfs_with_max_calories[1] + list_of_elfs_with_max_calories[2]))