import string
import random
def gen():
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation
    length=int(input("Enter the length: "))
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    passwords=("".join(s[0:length]))
    print(passwords)

    
gen()