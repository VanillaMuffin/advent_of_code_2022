
items = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
file = open("/Users/benjamingorjanc/Programing/advent_of_code_2022/day_03/puzzle_input.txt","r")
sum_of_item_values = 0

for line in file:
    #Split rucksack into two items. 
    first_compartment = line[:len(line)//2]
    second_compartment = line[len(line)//2:]

    #We look for the item present in both lists.
    common_item = list(set(first_compartment).intersection(list(second_compartment)))

    # Common_item is intersection of two sets. +1 Because we start counting with 0.
    value_of_item = items.index(common_item[0]) +1 

    sum_of_item_values += value_of_item
print(sum_of_item_values)

