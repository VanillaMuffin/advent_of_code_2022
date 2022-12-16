file = open("food_list.txt","r")
current_elf_calories=0
elf_with_max_calories=0
for line in file:
    if line.strip():
        #Check if line is empty.
        current_elf_calories+=int(line)
        print("Current callories: ", current_elf_calories)
    else:
        if current_elf_calories>elf_with_max_calories:
            elf_with_max_calories=current_elf_calories
        current_elf_calories=0
print("Elf with max callories has:", elf_with_max_calories)