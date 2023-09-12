while True:
    get_int = int(input("Enter: "))

    if get_int == 0:
        print("It is 0")
        break
    elif get_int < 0:
        print("It is negative")
        break
    else:        
        binary_string = ''
        while get_int > 0:
            digit = get_int % 2
            binary_string += str(digit)
            get_int //= 2    
        print(f"Binary is: {binary_string[::-1]}")

        decimal = 0
        i = 0

        for digit in binary_string:
            dec = int(digit)
            decimal += dec * (2 ** i)
            i += 1
        print(f"Integer is: {decimal}")