from os import sep
from turtle import end_fill


print("ahoj", "pavle", "jak", "se", "mas", sep="**", end="\n\n")

#positional arguments, required parameters

#keyword arguments = kwargs 

def prumer(*args):
    print(args)
    if len(args) > 0:
        return sum(args) / len(args)
    else:
        return 0
print(prumer(6, 7, 5, 3, 12, 15, 16))


def vytiskni(prvni, *args, **kwargs):
    print(args)
    print(*args, **kwargs)
    
    
vytiskni("ahoj", "jak", "se", "mas", sep="--", end="\n\n")