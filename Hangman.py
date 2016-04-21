from math import pi
def square():
    print "SQUARE"
    side = raw_input("Enter length of each side: ")
    if side.isdigit():
        return multiplier(int(side),int(side),int(side))
    else:
        print "Invalid Input!"
        square()
def rectangle():
    print "RECTANGLE"
    length = raw_input("Enter length: ")
    if length.isdigit():
        width = raw_input("Enter width: ")
        if width.isdigit():
            return multiplier(int(width),int(length),int(length))
        else:
            print "Invalid Input"
            rectangle()
    else:
        print "Invalid Input"
        rectangle()
def circle():
    print "CIRCLE"
    radius = raw_input("Enter radius: ")
    if radius.isdigit():
        return pi_multiplier(int(radius),int(radius),int(radius))
    else:
        print "Invalid Input!"
        circle()
def triangle():
    print "TRIANGLE"
    base = raw_input("Enter base: ")
    if base.isdigit():
        height = raw_input("Enter height: ")
        if height.isdigit():
            return half_multiplier(int(base),int(height),int(height))
        else:
            print "Invalid Input!"
            triangle()
    else:
        print "Invalid Input!"
        triangle()
def multiplier(count,parameter,parameter1):
    return parameter if count == 1 else multiplier(count-1,parameter+parameter1,parameter1)
def pi_multiplier(count,parameter,parameter1):
    return multiplier(parameter,pi,pi) if count == 1 else pi_multiplier(count-1,parameter+parameter1,parameter1)
def half_multiplier(count,parameter,parameter1):
    return multiplier(parameter,0.5,0.5) if count == 1 else half_multiplier(count-1,parameter+parameter1,parameter1)
values = {square():"square",rectangle():"rectangle",circle():"circle",triangle():"triangle"}
answer = values[max(values)]
def compare():
    print "++Guess the largest area (square,rectangle,circle,triangle)+++\nYou only have 2 tries"
    guess = raw_input("Enter guess: ")
    if guess == answer:
        print "Correct!"
    elif guess != answer:
        print "Wrong, you only have one last try"
        second = raw_input("Enter last guess: ")
        if second == answer:
            print "Correct!"
        else:
            print "Wrong! Game Over!"
compare()