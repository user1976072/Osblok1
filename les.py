input_array = input("Введите массив строк через запятую: ").split(", ")

output_array = [string for string in input_array if len(string) <= 3]

print(output_array)