height = int(input("Enter Height : "))
print("Inverted Pyramid :")

for i in range(height , 0 , -1):
    print(" "*(height-i)+ "*"*(2*i-1))