str = input("Enter the string : ")
vovels = 0 # Initialize vowel count
conconents = 0 # Initialize conconent count

for char in str:
    if char in ("a","e","i","o","u"): # Check if it's a vowel
        vovels = vovels + 1 # Increment vovel by 1
    elif char.isalpha(): # Check if it's a conconent
        conconents = conconents + 1 # Increment conconent by 1

print("Number of vowels are : ", vovels)
print("Number of consonents are : ", conconents)

