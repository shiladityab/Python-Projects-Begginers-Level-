print("-----------------------------------------------------")

print("Examples of Function and Arguments")

def fahr2celsious(fahr):
    celsious = (5*(fahr-32))/9
    return celsious

print("Celsious :  ", round(fahr2celsious(100),2))
print("Kelvin :  ", round(fahr2celsious(100)+273.5 , 2))

print("-----------------------------------------------------")

def say_hello(person1, person2="the boy"):
    print("Hello " + person1 + " " + person2 + " is waiting")

say_hello("Jane")

print("-----------------------------------------------------")
