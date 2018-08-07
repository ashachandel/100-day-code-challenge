number =int(input("enter a non-negative integer to take the factorial of: "))
            
fact=1
for i in range(number):
    fact=fact * (i+1)

print(fact)    
