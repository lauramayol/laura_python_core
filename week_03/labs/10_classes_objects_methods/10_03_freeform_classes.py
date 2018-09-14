'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the + operator in one of the classes
    so that it adds two attributes of that class.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...

'''


class Workout():
    """
        Exercise: Activity requiring physical effort, carried out to sustain or improve health and fitness.

        Attributes:
            workout_type (str): which kind of exercise
            equipment (str): what do you need to employ this exercise

    """

    def __init__(self, workout_type="running", equipment="running shoes"):
        self.workout_type = workout_type
        self.equipment = equipment

    def print_prepare(self):
        print(f"Get ready for your {self.workout_type} workout! You will need a {self.equipment}.")

    def __str__(self):
        return f"{self.workout_type} | {self.equipment}"


class Yoga(Workout):
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
        Workout.__init__(self, self.workout_type, self.equipment)

    def print_prepare(self):
        print(f"Get ready for your {self.practice_type} {self.workout_type} workout! You will need a {self.equipment} for your {self.teacher_format} class.")

    def __str__(self):
        return f"{self.workout_type} | {self.equipment} | {self.practice_type} | {self.teacher_format}"


class Run(Workout):
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
        Workout.__init__(self, self.workout_type, self.equipment)

    def print_prepare(self):
        print(f"Get ready for your {self.distance} km {self.workout_type}! You will need your {self.equipment}.")

    def __str__(self):
        return f"{self.workout_type} | {self.equipment} | {self.distance}"

    def __add__(self, other):
        total_distance = self.distance() + other.distance()
        return total_distance


wk1_workout = Workout("swim", "swimsuit")
wk1_workout.length_mins = 45
wk2_workout = Workout("crossfit", "weights")
wk2_workout.length_mins = 60

wk3_workout = Yoga()
wk4_workout = Yoga("hatha", "self-taught")

wk5_workout = Run()
wk6_workout = Run(10)
wk6_workout.direction = "East"

print(wk1_workout.__dict__)
print(wk6_workout)

print(wk5_workout.distance + wk6_workout.distance)

wk4_workout.practice_type = "rocket"
wk5_workout.equipment = "pair of running shoes"


wk4_workout.print_prepare()
wk5_workout.print_prepare()
