nine_digits = input("Enter the first 9 digits of an ISBN-10 as a string: ")

if len(nine_digits) != 9 or not nine_digits.isdigit():
    print("Invalid input. Please enter exactly nine digits.")
else:
    checksum = int(
        (
            int(nine_digits[0]) * 1
            + int(nine_digits[1]) * 2
            + int(nine_digits[2]) * 3
            + int(nine_digits[3]) * 4
            + int(nine_digits[4]) * 5
            + int(nine_digits[5]) * 6
            + int(nine_digits[6]) * 7
            + int(nine_digits[7]) * 8
            + int(nine_digits[8]) * 9
        ) % 11
    )
    if checksum == 10:
        print(f"Your ISBN-10 number is {nine_digits}X")
    else:
        print(f"Your ISBN-10 number is {nine_digits}{checksum}")        