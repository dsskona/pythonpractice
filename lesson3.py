str1 = 'Hello'
str2 = "Dhanya"
str3 = '''Python course by Saumya Dii'''
print(str1)
print(str2)
print(str3) 



#strings are immutable
#concatenating strings
print(str1 + " " + str2)

#length of the string
print(len(str1))

name = input("Enter your name:")
print(name[0])
print(name[5])
print(len(name))


#slicing
#syntax:[start:end] #end index excluded
#last index = length-1
sweet = "GulabJamun"
print(sweet[0:5]) #Gulab
print(sweet[5:]) #Jamun
print(sweet[:6]) #GulabJ
print(sweet[5:10])



