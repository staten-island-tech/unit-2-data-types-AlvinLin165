##TUTORIAL THING

""" x = 3
y = float(3)
print(x,y)

values = [1,2.23,5,7,2,30,1, 5]
print(values)
for i in values:
    print(i)

print(values[0])
print(values[7])

x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """ 
##END

##COUNT WORDS IN SENTENCE

""" sentence = input("write a sentence plspls pls do it for me")
word = len(sentence.split()) #len counts individual letters, use split to count words
print("that sentence has", word, "number of words") 
 """
##END

##MAD LIBS

"""sentence = input("enter name, number, adjective, verb in past tense, verb in past tense, celebrity (only first name), adjective, celebrity (only first name), your name, number, number, and name (DO NOT separate with comma)")
y = sentence.split()

a = y[0]
b = y[1]
c = y[2]
d = y[3]
e = y[4]
f = y[5]
g = y[6]
h = y[7]
i = y[8]
j = y[9]
k = y[10]
l = y[11]

print("On a bright rainy day", a, "decided to go outside and play", b,"video games. He was", c,"with his new gaming setup. He", d,"and", e, "and eventually beat", f, "after a", g,"game.", h,"got so mad that they decided to call", i, "to send" , j, "bomber planes, a blade of grass," , k, "nukes, and a toothbrush to", l,"'s location")
  """
##END

##CLASS NOTES

"""  def login(password):
    if password == "secret":
        print("logged in")
    else:
        print("incorrect")
x = input("what da password")
login(x)

def grade(score): 
    if score >=92:
        print("A")
    elif score >= 82:
        print("B")
    elif score >= 72:
        print("C")
    else:
        print("F")
x = int(input("what da score"))
grade(x)  """

##END

##BOOLEANS AND CONTROL FLOW

""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect")

x = "hello"
print(f"hello {x}")

temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold')   """
##END

##ODD OR EVEN

""" number = int(input("write a number"))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd") """

##END

##TIP CALCULATOR

""" bill = int(input("how much tip? (0%, 15%, 20%, 25% without the percentage symbol)"))

if bill == 15:
    print("okay")
elif bill == 20:
    print("good")
elif bill == 25:
    print("great")
elif bill == 0:
    print("your hairline was better than the food and your hairline recedes back to the Paleolithic Era")
else:
    print("I said tips are in 0%, 15%, 20%, and 25% you banana") """

##END    

##INPUT FACTORS EASY

""" def find_factors(number):
    factors = [] 
    for i in range(1, number + 1):
        if number % i == 0: 
            factors.append(i) 
    return factors 
a = int(input("Enter a number to find its factors: ")) 
print(f"Factors of {a}: {find_factors(a)}") """

##END

##GCF

def ql(number): # find factors
    q = [] #list
    for i in range(1, number + 1): #loop starts divisor at 1 and goes up then divide
        if number % i == 0:  #loops for factor if number divide add to list
            q.append(i) #add to list
    return q #repeat loop

def qv(c, d): #find gcf

    qa = ql(c) #runs the factoring code with 2 user input
    qb = ql(d) #define ql by running the factor loop
     

    qr = list(set(qa) & set(qb)) #the & operator finds common factors
    #common factors finds similar values in 2 factors and puts highest in list

    gcf = max(qr) #max finds biggest vale
    return gcf #return t o list


c = int(input("first number: ")) #ask user
d = int(input("second number: ")) #ask user again

#plugs in num 1 and num 2, then the result goes back to find gcf to be put in here 
print(f"The GCF of {c} and {d} is: {qv(c, d)}") #tells the user f string

##END