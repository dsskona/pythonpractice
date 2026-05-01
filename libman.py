list = []
list.append("Ikigai")
list.append("The Psychology of Money")
list.append("Ego is the Enemy")
print("After adding:", list)

list.remove("The Psychology of Money")
print("After removing:", list)

index = list.index("Ikigai")
list[index] = "Ikigai: The Japanese Secret to a Long and Happy Life"
print("After updating:", list)

#inheritance

class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
class Librarian(Person):
    def __init__(self, name, id,):
        super().__init__(name, id)

class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
            print(self.title, self.author)


b1 = book("Ikigai", "ABC")
b1.display() 

#exception handling
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input. Please enter a valid number.")
except Exception as e:
    print("error:", e)
    
