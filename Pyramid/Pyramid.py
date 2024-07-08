height = int(input("Enter Height : "))
print("Pyramid :")

for i in range(height):
    print(" "*(height-i-1) + "*"*(2*i+1))