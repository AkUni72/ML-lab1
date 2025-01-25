str = input("Enter the string : ")
vovels = 0
conconents = 0

for char in str:
    if char in ("a","e","i","o","u"):
        vovels = vovels + 1
    elif char.isalpha():
        conconents = conconents + 1

print("Number of vowels are : ", vovels)
print("Number of consonents are : ", conconents)

