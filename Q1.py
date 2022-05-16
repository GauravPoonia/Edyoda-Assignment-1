# lets play with fibonacci

num_1 = 0
num_2 = 1
num_3 = 1

print("Fibonacci series is : ",end="")

while num_3 < 50:
    print(num_3,end=" ")
    num_3 = num_1 + num_2
    num_1 = num_2
    num_2 = num_3
    
