#UPPERCASE CHARACTERS, LOWERCASE CHARACTERS, NUMBERS, SPECIAL CHARACTERS

ch = input("Enter a character : ")
if (ord(ch) >= 65 and ord(ch) <= 90):
    print(ch, " is a Uppercase character.")
elif(ord(ch) >= 97 and ord(ch) <= 122):
    printf(ch, " is a Lowercase character.")
elif (ord(ch) >= 48 and ord(ch) <= 57):
    print(ch, " is a number.")
else:
    print(ch, " is a Special character.")

'''
OUTPUT:
-------
Enter a character : @
@  is a Special character.
'''
