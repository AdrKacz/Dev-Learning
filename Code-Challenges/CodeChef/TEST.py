has_been_found = False

while not has_been_found:
    input_number = 0
    try:
        input_number = int(input())
    except:
        has_been_found = True
    if input_number == 42:
        has_been_found = True
    else:
        print(input_number)
