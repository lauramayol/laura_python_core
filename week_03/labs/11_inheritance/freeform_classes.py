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


class Beverage():
    """
        Any drink other than water.

        Attributes:
            is_liquid (bool): all beverages are liquid.
            category (str): category of the beverage.
            has_alcohol (bool): determines whether the beverage is alcoholic.
            has_caffeine (bool): determines whether the beverage has caffeine.

    """

    def __init__(self, category="wine", has_alcohol=True, has_caffeine=False):
        self.is_liquid = True
        self.category = category
        self.has_alcohol = has_alcohol
        self.has_caffeine = has_caffeine

    def print_details(self):
        print(f"Category: {self.category} | Liquid beverage? {self.is_liquid} | Has alcohol? {self.has_alcohol} | Has caffeine? {self.has_caffeine}")

    def __str__(self):
        return f"{self.category} | {self.is_liquid} | {self.has_alcohol} | {self.has_caffeine}"


class Sport():
    """
        An activity involving physical exertion and skill in which an individual or team competes against another or others for entertainment.

        Attributes:
            game (str): name of the type of sport
            number_of_players (int): number of players required to play this sport.
            length (int): average number of minutes of a standard game or match.

    """

    def __init__(self, game="Futbol", number_of_players=22, length=90):
        self.game = game
        self.number_of_players = number_of_players
        self.length = length

    def print_prepare(self):
        print(f"The sport of {self.game} requires {self.number_of_players} person(s) to play.")

    def __str__(self):
        return f"{self.game} | {self.number_of_players}"

    def __add__(self, other):
        total_time = self.length() + other.length()
        return total_time


# wk1_workout = Workout("swim", "swimsuit")
# wk1_workout.length_mins = 45
# wk2_workout = Workout("crossfit", "weights")
# wk2_workout.length_mins = 60

# my_evening_drink = Beverage(True, False)
# my_morning_drink = Beverage(False, True)

# baseball_match = Sport("Baseball", 18, 180)
# baseball_match.gender = "Male"
# tennis_match = Sport("Tennis", 2, 120)
# tennis_match.gender = "Female"

# print(wk1_workout.__dict__)
# print(wk2_workout)

# print(f"You will need {(baseball_match.length + tennis_match.length)/60} hours to watch both matches.")

# my_evening_drink.has_alcohol = False
# tennis_match.number_of_players = 4


# my_evening_drink.print_details()
# tennis_match.print_prepare()
