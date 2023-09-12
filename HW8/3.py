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