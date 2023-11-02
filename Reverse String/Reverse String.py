user_input = input("String to be reversed:")

# First Method
#print("".join(reversed(user_input)))

#Second Method
#reversed_array = []
#for x in user_input:
#   reversed_array.insert(0,x)

#reversed_string = "".join(reversed_array)
#print("Reversed String: "+reversed_string)

#Third Method

#print(user_input[::-1])

#Fourth Method

reversed_string = ""
for x in user_input:
    reversed_string = x+ reversed_string
print(reversed_string)


