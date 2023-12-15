import os
import re
from unittest import result

def part1(f):
    result = 0
    quantity_of_cubes_by_color = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    
    for line in f:
        patron_game = r'Game (\d+)'
        game_id = re.search(patron_game, line).group(1)
        is_posible = True
        
        line = re.split(r';', re.split(r':', line).pop(-1))
        for subgroup in line:
            subgroup = subgroup.strip()
            subgroup = re.split(r',', subgroup)
            for member in subgroup:
                num = int(re.findall(r'\d+', member)[0])
                color = str(re.findall(r'[a-z]+', member)[0])
                if color in quantity_of_cubes_by_color:
                    if num > quantity_of_cubes_by_color[color]:
                        is_posible = False
                        break
            if not is_posible:
                break

        if is_posible:
            result += int(game_id)
    
    print("Part 1 result: ", result)

def part2(f):
    result = 0
    for line in f:
        line_result = 0
        max_cubes_quantity_by_color = {
                "red": 0,
                "green": 0,
                "blue": 0
            }
        
        line = re.split(r';', re.split(r':', line).pop(-1))
        for subgroup in line:
            subgroup = subgroup.strip()
            subgroup = re.split(r',', subgroup)
            
            for member in subgroup:
                num = int(re.findall(r'\d+', member)[0])
                color = str(re.findall(r'[a-z]+', member)[0])
                print(color, num)
                max_cubes_quantity_by_color[color] = max(max_cubes_quantity_by_color[color], num)
        
        line_result = max_cubes_quantity_by_color["red"] * max_cubes_quantity_by_color["green"] * max_cubes_quantity_by_color["blue"]
        print(line_result)
                
        result += line_result
    print("Part 2 result: ", result)


directorio_actual = os.path.dirname(os.path.realpath(__file__))
ruta_relativa = os.path.join(directorio_actual, 'data.txt')
with open(ruta_relativa, 'r') as f:
    #part1(f)
    part2(f)