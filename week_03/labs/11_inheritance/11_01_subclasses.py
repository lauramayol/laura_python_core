'''
Build on 10_03_freeform_classes from the section on Classes, Objects and
Methods.
Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in 10_03_freeform_classes.

If you cannot think of a way to build on your previous exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''
import freeform_classes


class Yoga(freeform_classes.Workout):
    """
        A Hindu spiritual and ascetic discipline, a part of which, including breath control, simple meditation, and the adoption of specific bodily postures, is widely practised for health and relaxation.

        Attributes:
            workout_type (str): yoga, this is always the same for Yoga class.
            equipment (str): you need a yoga mat
            practice_type (str): there are different types of yoga, such as Hatha, Vinyasa, Yin, etc.
            teacher_format (str): you can take an online class, live, or self-taught.
    """

    def __init__(self, practice_type="vinyasa", teacher_format="online"):
        self.workout_type = "yoga"
        self.equipment = "yoga mat"
        self.practice_type = practice_type
        self.teacher_format = teacher_format
        freeform_classes.Workout.__init__(self, self.workout_type, self.equipment)

    def print_prepare(self):
        print(f"Get ready for your {self.practice_type} {self.workout_type} workout! You will need a {self.equipment} for your {self.teacher_format} class.")

    def __str__(self):
        return f"{self.workout_type} | {self.equipment} | {self.practice_type} | {self.teacher_format}"


class Run(freeform_classes.Workout):
    """
        Move at a speed faster than a walk, never having both or all the feet on the ground at the same time.

        Attributes:
            workout_type (str): running, this is always the same for Run class
            equipment (str): you need running shoes
            distance (float): distance to run in km
    """

    def __init__(self, distance=5):
        self.workout_type = "running"
        self.equipment = "running shoes"
        self.distance = distance
        freeform_classes.Workout.__init__(self, self.workout_type, self.equipment)

    def print_prepare(self):
        print(f"Get ready for your {self.distance} km {self.workout_type}! You will need your {self.equipment}.")

    def __str__(self):
        return f"{self.workout_type} | {self.equipment} | {self.distance}"

    def __add__(self, other):
        total_distance = self.distance() + other.distance()
        return total_distance


class Wine(freeform_classes.Beverage):
    """
        An alcoholic drink made from fermented grape juice..

        Attributes:
            category (str): category of the beverage.
            has_alcohol (bool): determines whether the beverage is alcoholic.
            has_caffeine (bool): determines whether the beverage has caffeine.
            variety (str): red, white, rose, sparkling.
    """

    def __init__(self, variety="red", has_alcohol=True):
        self.category = "wine"
        self.has_alcohol = has_alcohol
        self.has_caffeine = False
        self.variety = variety
        freeform_classes.Beverage.__init__(self, self.category, self.has_alcohol, self.has_caffeine)

    def print_instance(self):
        if self.has_alcohol == True:
            print(f"You are having {self.variety} wine today.")
        else:
            print(f"You are having non-alcoholic {self.variety} wine today.")

    def __str__(self):
        return f"{self.variety} | {self.has_alcohol}"


class Sparkling_Wine(Wine):

    def __init__(self, region="champagne", grape_mix="chardonnay", has_alcohol=True):
        self.has_alcohol = has_alcohol
        self.variety = "sparkling"
        self.region = region
        self.grape_mix = grape_mix
        Wine.__init__(self, self.variety, self.has_alcohol)

    def print_instance(self):
        if self.has_alcohol == True:
            alcoholic = ""
        else:
            alcoholic = "non-alcoholic"
        print(f"You are having {alcoholic} sparkling wine from {self.region} region made with {self.grape_mix}!")

    def __str__(self):
        return f"{self.region} | {self.grape_mix} | {self.has_alcohol}"


wk3_workout = Yoga()
wk4_workout = Yoga("hatha", "self-taught")

wk5_workout = Run()
wk6_workout = Run(10)
wk6_workout.direction = "East"


wk4_workout.print_prepare()
wk5_workout.print_prepare()

print(wk6_workout)

print(wk5_workout.distance + wk6_workout.distance)


my_wine = Wine()

my_wine.print_instance()

my_birthday_wine = Sparkling_Wine()

my_birthday_wine.print_instance()
