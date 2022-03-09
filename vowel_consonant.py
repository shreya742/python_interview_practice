#TO CHECK WHETHER THE CHARACTER IS VOWEL OR CONSONANT.

def vowel_consonant(ch):
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
       print(ch, "is Vowel.")
    else :
        print(ch, "is Consonant.")
ch = input("Enter a character : ")
print(vowel_consonant(ch))
