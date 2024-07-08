height = int(input("Enter Height : "))
print("Diamond :")

for i in range(height):
    print(" "*(height-i-1) + "*"*(2*i+1))
for j in range(height-1 , 0 , -1):
    print(" "*(height-j)+ "*"*(2*j-1))