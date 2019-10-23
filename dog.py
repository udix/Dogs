class Dog:
    species = 'caniche'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printObj(self):
        print("{} is {}.".format(self.name, self.age))

    @staticmethod
    def get_biggest_number(*args):

        biggest = 0

        for x in args:

            if not isinstance(x, int):
                print("All arguments must be integers!")
                return

            if x > biggest:
                biggest = x

        return biggest
    

bambi  = Dog("Bambi", 5)
mikey  = Dog("Rufus", 6)
copito = Dog("Copito", 10)
drako  = Dog("Drako", 2)
zeus   = Dog("Zeus", 8)

bambi.printObj()
mikey.printObj()
copito.printObj()
drako.printObj()
zeus.printObj()

print("Oldest Dog is {0} years old!".format(Dog.get_biggest_number(bambi.age, mikey.age, copito.age, drako.age, zeus.age)))

if bambi.species == "caniche":
    print("{0} is a {1}!".format(bambi.name, bambi.species))