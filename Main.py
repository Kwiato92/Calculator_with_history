keep_going = True
calc_list = ['A', 'S', 'M', 'D', 'E', 'H']
history = []

while keep_going:
    print(
        'Which equation would you like to use?\n(A)ddition\n(S)ubtraction\n(M)ultiplication\nd(D)ivide\n(H)istory\n(E)nd')
    action = input()

    if action == calc_list[4]:
        keep_going = False
        continue
    elif action == calc_list[5]:
        print('History:', history)
        if not history:
            print('History is empty')
        continue

    if action not in calc_list:
        print('Invalid equation')
        continue

    print('Give first number')
    try:
        number_1 = float(input())
    except ValueError:
        print('Do not use letters')
        continue

    print('Give second number')
    try:
        number_2 = float(input())
    except ValueError:
        print('Do not use letters')
        continue

    result = None
    if action == calc_list[0]:
        result = number_1 + number_2
    elif action == calc_list[1]:
        result = number_1 - number_2
    elif action == calc_list[2]:
        result = number_1 * number_2
    elif action == calc_list[3]:
        if number_2 == 0:
            print('Division by zero is not allowed.')
            continue
        result = number_1 / number_2

    if result is not None:
        print(result)
        history.append(f'{number_1} {action} {number_2} = {result}')

print('THE END')
