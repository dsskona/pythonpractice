patients = []
patients.append("John Dalton")
patients.append("Oli London")
print("After adding:", patients)
patients.remove("John Dalton")
print("After removing:", patients)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Patient(Person):
    def __init__(self, name, age, disease, doctor):
        super().__init__(name, age)
        self.disease = disease
        self.doctor = doctor

    def display(self):
        print(self.name, self.age, self.disease, self.doctor)


p1 = Patient("John", 30, "Fever", "Dr. Smith")
p1.display() 

try:
    age = int(input("Enter patient's age: "))
    print("Age:",age)
except ValueError:
    print("Invalid input. Please enter a valid age.")

 #methods
 list = []

class Patient:
    def __init__(self, name, disease):
        self.name = name
        self.disease = disease


def add_patient(p):
    list.append(p)

def display_patients():
    for p in list:
        print(p.name, p.disease)


p1 = Patient("Alice", "Cold")
p2 = Patient("Bob", "Flu")

add_patient(p1)
add_patient(p2)

display_patients()   

    