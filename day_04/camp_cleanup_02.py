file = open("/Users/benjamingorjanc/Programing/advent_of_code_2022/day_04/puzzle_input.txt","r")
overlaping_assignments = 0

for line in file:
    assigment = line.split(',')
    first_elf_sections = assigment[0].split('-')
    second_elf_sections = assigment[1].split('-')

    first_elf_sections_set = set()
    second_elf_sections_set = set()

    for section in range(int(first_elf_sections[0]), int(first_elf_sections[1])+1):
        first_elf_sections_set.add(section)
    for section in range(int(second_elf_sections[0]), int(second_elf_sections[1])+1):
        second_elf_sections_set.add(section)

    intersection = list(first_elf_sections_set & second_elf_sections_set)
    
    if len(intersection):
        overlaping_assignments+=1
          
print(overlaping_assignments)