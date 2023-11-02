user_input = input("Word to be transformed:").lower()

vowels = ["a","e","i","o","u"]
consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
beginning = ""

for x in user_input:
    if x in vowels:
        break
    else:
        beginning += x

if beginning == "":
    print("Transformed Word:"+user_input+"way")
else:
    print("Transformed Word:"+user_input[len(beginning):]+beginning+"ay")
    
    
    
        
