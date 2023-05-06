#import string
#import random
#str=input("Enter the word: ")
#s=string.printable
#print(s)
import random
def get_string (text):
    random.shuffle(text)
my_string = input("word: ")
print("New modified string is : ", get_string(my_string))