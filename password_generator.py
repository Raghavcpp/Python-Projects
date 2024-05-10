import string
import random
from csv import writer
# head = ['Platform', 'Password']
# with open('pass.csv','w') as f:
#     writedata = writer(f)
#     writedata.writerow(head)

def passgen():
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    platform = input("Enter the name of the platform : ")
    pass_length = int(input("Enter the length of the password : "))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    password = ("".join(s[0:pass_length]))
    print(password)
    passdata = [platform, password]
    with open('pass.csv','a') as f:
        writedata = writer(f)
        writedata.writerow(passdata)


passgen()