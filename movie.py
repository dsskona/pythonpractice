movies = []
movies.append("They call him OG")
movies.append("Yashoda")
movies.append("Ala Vaikunthapurramuloo")
print("After adding:", movies)

movies.remove("Yashoda")
print("After removing:", movies)

index = movies.index("They call him OG")
movies[index] = "They call him OG: Ojas Gambheera"
print("After updating:", movies)
movies.reverse()
print("After reversing:", movies)

#polymorphism
class media:
    def __init__(self, title):
        self.title = title
class movie(media):
    def __init__(self, title, rating, year):
        super().__init__(title)
        self.rating = rating
        self.year = year
    def display(self):
        print(self.title, self.rating, self.year)
m1 = movie("They call him OG", 8.5, 2025)
m2 = movie("Ala Vaikunthapurramuloo", 8.0, 2020)
m1.display()
m2.display()

try:
    rating = float(input("Enter movie rating: "))
    print("Rating:", rating)
except ValueError:
    print("Invalid input, Please enter a valid rating.")