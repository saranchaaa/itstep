#---PASSWORD GENERATOR---#

import random #importing

num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #list of numbers
str = r"qwertyuasdfhjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,./P[]';:\'\"\-\*/+-\"" #string of other symbols
sym_list = ' '.join(str).split() #making list out of the string

x = f"{random.choice(num_list)}{random.choice(sym_list)}{random.choice(num_list)}{random.choice(sym_list)}{random.choice(num_list)}{random.choice(sym_list)}{random.choice(num_list)}{random.choice(sym_list)}" #making the password
print(x) #print