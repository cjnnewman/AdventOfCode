def santa_directions():
    with open('2015_01_input.txt', 'r') as file:
        char_list = list(file.read())
    
    floor = 0
    current_char = 0
    for char in char_list:
        current_char += 1
        if char == '(':
            floor += 1
            if floor == -1:
                print(f"Entered basement on character number: {current_char}")
                break
        elif char == ')':
            floor -= 1
            if floor == -1:
                print(f"Entered basement on character number: {current_char}")
                break
            
    print(f"Final floor: {floor}")

santa_directions()
