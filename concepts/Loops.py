input = input("Enter a string: ")
reversed_string = ""

for char in input:
    reversed_string = char + reversed_string
print("Reversed string:", reversed_string)