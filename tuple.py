#immutable
marks = (86, 64, 33, 95, 76)
print(max(marks))
print(min(marks))


movie1 = input("Enter the first movie:")
movie2 = input("Enter the second movie:")
movie3 = input("Enter the third movie:")

list_of_favourite_movies = [movie1, movie2, movie3]
print(list_of_favourite_movies)


#if elif

marks = int(input("Enter your marks:"))
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
else:
    marks < 70
    print("D")