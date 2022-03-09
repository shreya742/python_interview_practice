#PROGRAM TO CHECK WHETHER CHARACTER IS AN ALPHABET OR NOT.

def alphabet(ch):
    if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
        print(ch, "is an alphabet.")
    else :
        print(ch, "is not an alphabet.")
ch = input("Enter a character : ")
print(alphabet(ch))

'''
OUTPUT:
Enter a character : S
S is an alphabet.
'''
