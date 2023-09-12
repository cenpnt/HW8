#1
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
        print("Binary is:", binary_string[::-1])

        decimal = 0
        i = 0

        for digit in binary_string:
            dec = int(digit)
            decimal += dec * (2 ** i)
            i += 1
        print("Integer is:", decimal)

#######################################################
#2
text = input("Enter some text: ")

char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

percentage_dict = {}

for char, count in char_count.items():
    percentage = (count / len(text)) * 100
    percentage_dict[char] = percentage

for char, percentage in percentage_dict.items():
    print(f"{char}    {percentage:.2f}%")

#######################################################
#3
import turtle
t = turtle.Turtle()
t2 = turtle.Turtle()
t.speed(0)
t2.speed(0)

text = input("Enter some text: ")

char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

turtle_font = "Arial"
turtle_font_size = "13"
t.pu()
t.goto(-100,-50)

def draw_bar(char, count):   
    t.pd()
    t.fd(15)
    t.left(90)
    t.fd(count*20)
    t.right(90)
    t.fd(15)
    t.right(90)
    t.fd(count*20)  
    t.right(90)
    t.fd(15)     
    t.pu()
    t.left(90)
    t.fd(30)    
    t.write(char, align='center', font=(turtle_font, turtle_font_size))    
    t.back(30)
    t.pd()
    t.right(90)
    t.right(180)
    t.fd(15)

for char, count in char_count.items():
    draw_bar(char, count)

max_percentage = max(char_count.values())
t.fd(15)
t2.pu()
t2.goto(-100,-50)
t2.pd()
t2.left(90)
t2.fd(max_percentage*20)
turtle.done()

#######################################################
#4
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