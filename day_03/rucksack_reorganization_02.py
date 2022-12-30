from itertools import islice

items = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
file = open("/Users/benjamingorjanc/Programing/advent_of_code_2022/day_03/puzzle_input.txt","r")
sum_of_item_values = 0

while True:
    #Read next three lines.
    try:
        next_three_lines = list(islice(file,3))
        item_a = next_three_lines[0].strip()
        item_b = next_three_lines[1].strip()
        item_c = next_three_lines[2].strip()

        common_set = set(item_a) & set(item_b) & set(item_c)
        common_item = list(common_set)[0]

        common_item_value = items.index(common_item[0]) +1 
        sum_of_item_values += common_item_value

    except:
        break

    if not next_three_lines:
        break

print(sum_of_item_values)

