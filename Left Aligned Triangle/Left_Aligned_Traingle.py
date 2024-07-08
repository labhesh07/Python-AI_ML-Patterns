height = int(input("Enter Height : "))
print("Left Aligned Triangle :")

for i in range(height):
    print(" "*(height-i)+"*"*(i+1))