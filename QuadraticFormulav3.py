print("Quadratic Formula Script V3")
print("This Version contains more complex code and Graph Analysis")

roots = False
a = float(input("What is the coefficient of x squared?"))
b = float(input("what is the coefficient of x?"))
c = float(input("whats is the constant?"))


def discriminant(a, b, c):
    return (b**2) - (4 * a * c)


discriminant = discriminant(a, b, c)
discriminantstr = str(discriminant)

if discriminant >= 0:
    roots = True
else:
    roots = False


def quadratic1(a, b, c, discriminant):  # +
    return (-b + (discriminant ** (1 / 2))) / (2 * a)


quadratic1str = str(quadratic1(a, b, c, discriminant))


def quadratic2(a, b, c, discriminant):  # -
    return (-b - (discriminant ** (1 / 2))) / (2 * a)


quadratic2str = str(quadratic2(a, b, c, discriminant))

if roots == True:
    print("Your value(s) of the roots are: " + quadratic1str + " and, " + quadratic2str)
else:
    print("The graph of your Quadratic has no roots as your discriminant is: " + discriminantstr)

# --------------------------------------------------------------------------------------------------------------------

# Extras

extra = False

extra_choice = str(input(print("Would you like some extra details?")))

if extra_choice.strip == "yes" or extra_choice.lower() == "yes":
    extra = True
elif extra_choice.strip() == "no" or extra_choice.lower() == "no":
    extra = False
else:
    while extra_choice.strip() != "yes" or extra_choice.lower() != "yes" or extra_choice.strip() != "no" or extra_choice.lower() != "no":
     # while loop
        extra_choice = str(input(print("Answer with yes or no")))
        if extra_choice.strip() == "yes" or extra_choice.lower() == "yes" or extra_choice.strip() == "no" or extra_choice.lower() == "no":
            if extra_choice.strip() == "yes" or extra_choice.lower() == "yes":
                extra = True
                break
            else:
                extra = False
                break

# a == 1

def CTSone(a, b, c):
 # ("aCTSone"x + "bCTSone")^2 - cCTSone
    aCTSone = 1
    bCTSone = b / 2
    cCTSone = (-(bCTSone ** 2)) + c

 # strings
    aCTSonestr = str(aCTSone)
    bCTSonestr = str(bCTSone)
    cCTSonestr = str(cCTSone)

 # therfore
    CTSoneres = "(x + " + bCTSonestr + ")^2 + " + cCTSonestr
    print("The Completed Sqaure of your Quadratic is: " + CTSoneres)

 # stringspec
    bCTSonecoordstr = str(-bCTSone)

 # turning points
    print("Your Turning Points are: (" + bCTSonecoordstr + "," + cCTSonestr + ")")

# a != 1

def CTSother(a, b, c):
 # outerCTSother("aCTSother"x + "bCTSother" )^2 + "cCTSother"
    outerCTSother = a
    aCTSother = 1
    bCTSother = b / a
    cCTSother = ((-(bCTSother ** 2)) * outerCTSother) + c

 # strings
    CTSouter_str = str(outerCTSother)
    aCTSother_str = str(aCTSother)
    bCTSother_str = str(bCTSother)
    cCTSother_str = str(cCTSother)

 # stringspec
    xvalueother = str(-bCTSother)

 # therefore
    CTSotherres = (CTSouter_str) + "(x + " + (bCTSother_str) + ")^2 + " + (cCTSother_str)
    print("The Completed Square of your Quadratic is: " + CTSotherres)

 # turning points
    print("The Turning Point of your Quadratic is: (" + xvalueother + "," + cCTSother_str + ")")

if extra == False:
    print("Done")
    exit()
else:
    if a == 1:
        CTSone(a, b, c)
    else:
        CTSother(a, b, c)