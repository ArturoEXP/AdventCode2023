import os

def part1(f):
    result = 0
    for line in f:
        num = ""
        for character in line:
            if character.isdigit():
                num = str(num) + str(character)
        num = str(num[0]) + str(num[0]) if len(num) == 1 else str(num[0]) + str(num[-1])
        result += int(num)
        
    print("Part 1 result: ", result)

def part2(f):
    result = 0
    numbers = {
        'one' : 1,
        'two' : 2,
        'three' : 3,
        'four' : 4,
        'five' : 5,
        'six' : 6,
        'seven' : 7,
        'eight' : 8,
        'nine' : 9
    }
    
    for line in f:
        num = ""
        print("\nLinea: ", line)
        word = ""
        for character in line:
            if character.isdigit():
                num = str(num) + str(character)
                word = ""
            elif character.isalpha():
                word += str(character)
                for number in numbers:
                    if number in word:
                        num = str(num) + str(numbers[number])
                        word = word[-1]
        num = str(num[0]) + str(num[0]) if len(num) == 1 else str(num[0]) + str(num[-1])
        result += int(num)
        
    print("Part 2 result: ",result)


directorio_actual = os.path.dirname(os.path.realpath(__file__))
ruta_relativa = os.path.join(directorio_actual, 'data.txt')
with open(ruta_relativa, 'r') as f:
    part1(f)
    part2(f)