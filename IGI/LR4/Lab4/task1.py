import csv
import pickle

def task1():
    classroom = Classroom()
    classroom.add_pupil(Pupil("Smith", 10))
    classroom.add_pupil(Pupil("Johnson", 12))
    classroom.add_pupil(Pupil("Williams", 15))
    classroom.add_pupil(Pupil("Brown", 17))

    # Serialize to CSV
    serialize_to_csv(classroom, 'classroom.csv')

    # Deserialize from CSV
    classroom_from_csv = deserialize_from_csv('classroom.csv')
    print("Deserialized from CSV:")
    for age_group, pupils in classroom_from_csv.get_age_groups().items():
        print(f"{age_group}: {[str(pupil) for pupil in pupils]}")

    # Serialize to pickle
    serialize_to_pickle(classroom, 'classroom.pickle')

    # Deserialize from pickle
    classroom_from_pickle = deserialize_from_pickle('classroom.pickle')
    print("\nDeserialized from pickle:")
    for age_group, pupils in classroom_from_pickle.get_age_groups().items():
        print(f"{age_group}: {[str(pupil) for pupil in pupils]}")

    # Print pupil info
    surname_to_find = input("Enter the surname of the pupil to find: ")
    classroom_from_pickle.print_pupil_info(surname_to_find)

class Pupil:
    def __init__(self, surname, age):
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"{self.surname}, {self.age}"

class Classroom:
    def __init__(self):
        self.pupils = []

    def add_pupil(self, pupil):
        self.pupils.append(pupil)

    def get_age_groups(self):
        age_groups = {
            "Kindergarten": [],
            "Elementary School": [],
            "Middle School": [],
            "High School": []
        }

        for pupil in self.pupils:
            if pupil.age >= 6 and pupil.age <= 11:
                age_groups["Elementary School"].append(pupil)
            elif pupil.age >= 12 and pupil.age <= 14:
                age_groups["Middle School"].append(pupil)
            elif pupil.age >= 15 and pupil.age <= 18:
                age_groups["High School"].append(pupil)
            else:
                age_groups["Kindergarten"].append(pupil)

        return age_groups

    def print_pupil_info(self, surname):
        for pupil in self.pupils:
            if pupil.surname == surname:
                print(pupil)
                return
        print("Pupil not found.")

def serialize_to_csv(classroom, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Surname", "Age"])
        for pupil in classroom.pupils:
            writer.writerow([pupil.surname, pupil.age])

def deserialize_from_csv(filename):
    classroom = Classroom()
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            surname, age = row
            pupil = Pupil(surname, int(age))
            classroom.add_pupil(pupil)
    return classroom

def serialize_to_pickle(classroom, filename):
    with open(filename, 'wb') as file:
        pickle.dump(classroom, file)

def deserialize_from_pickle(filename):
    with open(filename, 'rb') as file:
        classroom = pickle.load(file)
    return classroom
