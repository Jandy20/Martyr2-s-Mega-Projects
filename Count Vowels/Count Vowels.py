user_input = input("Input:").lower()

vowels = {"a":0,"e":0,"i":0,"o":0,"u":0}
#Method 1
#for vowel in vowels:
#    vowels[vowel] += user_input.count(vowel)
#print("Vowel Report")
#for vowel in vowels:
#    print(vowel+":"+ str(vowels[vowel]))

#Method 2
#for vowel in vowels:
#    for x in user_input:
#        if x==vowel:
#            vowels[vowel]+=1
#print("Vowel Report")
#for vowel in vowels:
#    print(vowel+":"+ str(vowels[vowel]))

#Method 3

for x in user_input:
    if x in vowels:
        vowels[x]+=1
print("Vowel Report")
for vowel in vowels:
    print(vowel+":"+ str(vowels[vowel]))


