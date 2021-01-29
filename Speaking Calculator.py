import pyttsx3
engine = pyttsx3.init('sapi5')

print ("Welcome to the calculator!")

engine.say("Welcome to the calculator!")
engine.say("Enter the 2 numbers for the calculator to work upon!")
engine.runAndWait()

def calci():
    a = float (input ("Enter the 1st number:- "))
    b = float (input ("Enter the 2nd number:- "))

    engine.say("Press 1 for Addition, 2 for Subtraction, 3 for Multiplication, and 4 for Division")
    engine.runAndWait()
    x = str (input ("-> "))

    m = str(a)
    n = str(b)

    add = a + b
    stradd = str (add)

    sub1 = a - b
    sub2 = b - a
    strsub1 = str(sub1)
    strsub2 = str(sub2)

    mul1 = a * b
    strmul1 = str(mul1)

    div1 = a / b
    div2 = b / a
    strdiv1 = str(div1)
    strdiv2 = str(div2)

    e = "The sum of"
    f = "and"
    g = "is"

    sub = "The difference between"
    mul = "The product of"
    div = "The quotient while dividing"
    qs = "from"

    if x == '1':
        engine.say(e+m+f+n+g+stradd)
        engine.runAndWait()
    elif x == '2':
        if a >= b:
            engine.say(sub+m+f+n+g+strsub1)
        else:
            engine.say(sub+n+f+m+g+strsub2)
        engine.runAndWait()
    elif x == '3':
        engine.say(mul+m+f+n+g+strmul1)
        engine.runAndWait()
    elif x == '4':
        if a >= b:
            engine.say(div+m+qs+n+g+strdiv1)
        else:
            engine.say(div+n+qs+m+g+strdiv2)
        engine.runAndWait()
    else:
        engine.say("Invalid Input")
        engine.runAndWait()
        calci()
calci()

while True:
    engine.say("Do you want to reuse the application?")
    engine.say("Press 1 for yes and 2 for no")
    engine.runAndWait()

    y = str (input ("-> "))

    if y == '1':
        print ()
        calci()
    elif y == '2':
        engine.say("Thank you for using the application!")
        engine.runAndWait()
        break
    else:
        engine.say("Invalid Input")
        engine.runAndWait()
        print ()