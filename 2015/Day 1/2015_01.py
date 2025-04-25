def santa_directions():
    with open('2015_01_input.txt', 'r') as file:
        char_list = list(file.read())
    
    floor = 0
    current_char = 0
    basement_first = False

    for char in char_list:
        current_char += 1
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
            if floor == -1 and basement_first == False:
                basement_char = current_char
                basement_first = True

    print(f"First character to enter the basement: {basement_char}")        
    print(f"Final floor: {floor}")

santa_directions()
