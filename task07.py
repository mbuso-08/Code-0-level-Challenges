celsius = int(28)

def convert(c):
    return (9/5 * c) + 32  #your code goes here
    
fahrenheit = convert(celsius)
print(fahrenheit)

fahrenheit = 82.4

def opp(f):
    return (f - 32) * (5/9)

transmute = opp(fahrenheit)
print(transmute)