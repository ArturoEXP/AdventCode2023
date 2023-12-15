with open('D:\\Users\\artur\\Desktop\\LEARN\\Programación\\AdventCalendar2023\\Day01\\data.txt', 'r') as archivo:
    result = 0
    for linea in archivo:
        num = ""
        print("Linea: ", linea)
        for character in linea:
            if character.isdigit():
                num = str(num) + str(character)
        print("Num entero: ", num)
        num = str(num[0]) + str(num[0]) if len(num) == 1 else str(num[0]) + str(num[-1])
        print("Num despues de modificarlo: ", num)
        print("Result antes de suma: ",result)
        result += int(num)
        print("Result despues de suma: ",result)
        
    print(result)