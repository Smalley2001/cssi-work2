#
# students = {
#     "D": "Dorian",
#     "A": "Austin",
#     "S": "Saka",
#     "M": "Mofe",
#
# }
# print(students)
#
# for name in students:
#     print(" The first letter is " + name)
#     print(" First name is "+ students[name])
#
# #Modify
# print(students["D"] + "prefers to be called Smalley.")
# students['D']= "Smalley"
# print(students)
#
# #REMOVE
# print(students)
# students.pop("M")
# print(students)
#
#
# dorian_subjects = {
#     "name": "Dorian",
#     "age": 18,
#     "favorite subject": {
#         "name": "Mathematics",
#         "most hated subject": {
#             "name": "Art",
#         }
# }
# }
#
# for name in dorian_subjects:
#     print("Dorian's favorite subject is " + str(dorian_subjects["favorite subject"]["name"]))
#
# pet= {
#
# "name": "Skeemer",
# "animal": "dog",
# "breed": "bichon frise",
# "age": 16,
# }
#
# class Pet(object):
#     def __init__(self,name,age):
#         self.name =name
#         self.age = age
#     def bark(self):
#         print("Ruff ruff ruff")
#
#
# my_pet= Pet("Finn", 14)
#
#
# print("My new pet is " + my_pet.name + " and he/she is" + str(my_pet.age))
# my_pet.bark()



class Pokemon(object):
    #This is a Constructor
    def __init__(self,name,type,sex):
        self.name = name
        self.type = type
        self.sex = sex

    def attack(self,move):
        print(move)

my_Pokemon= Pokemon("Pikachu", "electric", "male")
my_Pokemon.attack("electro shock therapy")

class Charizard(Pokemon):
    #Constructor
    def __init__(self, name, type, sex, tail_flame_size):
        Pokemon.__init__(self, name, type, sex)
        self.tail_flame_size = tail_flame_size

    def burnTheGuy(self):
        print("$$$$")

charizard = Charizard("Charry", "flame-fly", "Female","large")

print(charizard.name)
charizard.burnTheGuy())
