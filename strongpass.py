
'''readme file 
1-import string module+random module
2-store all charecters in lists (upper case(30%)
,
lower case(30%) ,
numbers(digits)(20%),
punctuation(20%)
)
3-take number of characters form the user (>=6),
4-to generate a random password in a disorderly way:shuffle all lists
5-create a loop to combine the password in a list of elements 
5-join the created list to get a string and that will be the final result :)
thanks
'''
import string
import random
upper=list(string.ascii_uppercase)
lower=list(string.ascii_lowercase)
numbers=list(string.digits)
punctuation=list(string.punctuation)
nb_char=input("give number of characters for the password: ")
#verification section
while True:
    try:
        nb_char=int(nb_char)
        if nb_char >6:
            break
        else:
            print("ENTER A NUMBER >=6")
            nb_char=input("give number of characters for the password: ")
            
    except:
        print("ENTER A NUMBER!")
        nb_char=input("give number of characters for the password: ")
#verification section
random.shuffle(upper)
random.shuffle(lower)
random.shuffle(numbers)
random.shuffle(punctuation)

lettersection=round(nb_char*(30/100))
numberpunctsection=round(nb_char*(20/100))
generatedpassword=[]
for i in range(lettersection):
    generatedpassword.append(lower[i])
    generatedpassword.append(upper[i])
for i in range(numberpunctsection):
    generatedpassword.append(numbers[i])
    generatedpassword.append(punctuation[i])
generatedpassword="".join(generatedpassword[0:])
print(generatedpassword)        