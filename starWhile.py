n = 1
while n<=4:
    print("*"*n)
    n = n+1
print("n=",n)


#print name 10 times but each time a no. in front of it
n = 1
while n<=5:
    print(n,"."+"Saumya Singh")
    n+=1


#Write a program to print the multiplication table of any number using a while loop.

n = int(input("Enter the number:"))
i = 1
while i<=10:
    print(f"{n}x{i} = {n*i}")
    i+=1

