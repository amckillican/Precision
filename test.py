names_file = open("names_file.txt", "r")
times_file = open("times_file.txt", "r")

number_list = []
for line_numbers in times_file:
    line_value = int(str(line_numbers)[:-1])
    number_list.append(line_value)

number_list.sort()

first = number_list[0]
second = number_list[1]
third = number_list[2]
fourth = number_list[3]
fifth = number_list[4]
print(first, second, third, fourth, fifth)