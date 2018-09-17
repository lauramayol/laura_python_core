import random
import time


class Player():
    """
        A person taking part in a sport or game. This class has method "determine_level" that can randomly determine what level the player is.

        Attributes:
            player_type (str): currently, "Opponent" or "Hero," but can be built for many different kinds of players.
            level (int): the starting level of skill for this player.

    """

    def __init__(self, player_type="Opponent", level=1):
        self.player_type = player_type
        self.level = level

    def determine_level(self, max_level=10):
        level_assign = random.randrange(1, max_level)
        self.level = level_assign
        return level_assign


class Hero(Player):
    """
        A person who is admired for their courage, outstanding achievements, or noble qualities. Inherited from the Player() class meant for the main player of the game.

        Attributes:
            name (str): the name of the player, defaulted to the "player_type"

    """
    player_type = "Hero"

    def __init__(self, level, name=player_type):
        self.name = name
        Player.__init__(self, self.player_type, level)

    def attack(self, other_player, new_dice):
        new_roll = new_dice.roll_dice()
        opp_roll = new_dice.roll_dice()
        print(f"{self.name}: level {self.level} | {other_player.name}: level {other_player.level}")
        print(f"{self.name} rolls dice: {new_roll}")
        print("Opponent rolls dice: " + str(opp_roll))

        # Allow Hero to roll again if the opponent has this skill. We subtract one from the range because the hero's roll has already been initialized above.
        if other_player.special_skill == "nice":
            for turn in range(0, other_player.n_tries - 1):
                next_roll = new_dice.roll_dice()
                if new_roll < next_roll:
                    new_roll = next_roll
            print(f"{other_player.name} allows {self.name} to roll again: {new_roll}")

        # Replace skipper's value if the opponent has this skill.
        if other_player.special_skill == "skipper" and opp_roll == other_player.skip_num:
            opp_roll = other_player.skip_to_num
            print("Skipper changes dice: " + str(opp_roll))

        # Check if you have a Killer Opponent. You can only beat a Killer if you get the max dice or if you have higher level. The catch is that the killer starts at much higher level than you. But if you Win, you will get 2 levels increased.
        if other_player.special_skill == "killer":

            if new_roll == new_dice.num_of_dice * 6 or self.level > other_player.level:
                self.level += 2
                return "Win"
            else:
                return self.you_lost(other_player)
        # For all other opponents, hero will win if (1)rolls higher number than opponent or (2)level is higher than opponent and hero does not roll lowest number and opponent does not roll highest number.
        elif new_roll > opp_roll or (self.level > other_player.level and new_roll > new_dice.num_of_dice and opp_roll < new_dice.num_of_dice * 6):
            self.level += 1
            return "Win"
        else:
            return self.you_lost(other_player)

    def you_lost(self, opponent_player):
        self.level = self.level - 1
        opponent_player.level += 1
        print("You lost, please wait...")
        time.sleep(5)
        return "Lose"

    def __str__(self):
        return f"Player Type: {self.player_type} | Name: {self.name} | Level: {self.level}"


class Opponent(Player):
    """
        A person who is admired for their courage, outstanding achievements, or noble qualities. Inherited from the Player() class meant for the opposing players of the Hero.

        Attributes:
            name (str): the name of the player, defaulted to the "player_type"
            special_skill (str): whether this opponent has a special skill or not.

    """
    player_type = "Opponent"

    def __init__(self, level, name=player_type, special_skill="basic"):
        self.special_skill = special_skill
        self.name = name
        Player.__init__(self, self.player_type, level)

    def __str__(self):
        return f"Player Type: {self.player_type} | Name: {self.name} | Level: {self.level} | Special Skill: {self.special_skill}"


class Dice():
    """
        Creates a set of numbers the user specified number of dice. Assumes one die has numbers 1-6.

        Attributes:
            num_of_dice (int): the number of dice one player can roll during their turn to get one result.

    """

    def __init__(self, num_of_dice=1):
        self.num_of_dice = num_of_dice

    def roll_dice(self):
        dice_result = random.randint(self.num_of_dice, self.num_of_dice * 6)
        return dice_result

    def __str__(self):
        return f"# of dice in play: {self.num_of_dice}"


class Game():
    """
        A form of competitive activity played according to rules. The rules of the game are:

        1. Every round is an encounter. User specifies whether to attack or quit.
        2. During an attack, the two players will roll the dice. The winner of the attack is determined if (1)rolls higher number than opponent or (2)level is higher than opponent and hero does not roll lowest number and opponent does not roll highest number.
        3. The user does not find out the level of the opponent until after the attack.
        4. After a win, the hero gets a level increase of +1 and opponent is removed from the game.
        5. After a loss, the hero gets a level decrease of -1 and opponent gains a level.
        6. By default, every game will have one of each special opponent type (ie. Killer Opponent), and the rest will be regular Opponents.

        Attributes:
            hero_list (list): the instances of heros created for a particular Game instance.
            opponent_list (list): the instances of opponents created for a particular Game instance.
            num_wins (int): tracks the number of wins for the hero.
            num_loss (int): tracks the number of losses for the hero.
            num_of_players (int): total number of players in the game.
            num_of_heros (int): Defaulted to 1, but this will allow the game to grow to have multiple heros and have hero-to-hero encounters in the future.

    """
    hero_list = []
    opponent_list = []
    num_wins = 0
    num_loss = 0
    this_dice = Dice(1)

    def __init__(self, num_of_players=6, num_of_heros=1):
        self.num_of_players = num_of_players
        self.num_of_heros = num_of_heros
        print ("Hello, Welcome to the game!")
        print("Please enter your player name: ")

    def create_heros(self, name):
        for x in range(0, self.num_of_heros):
            self.hero_list.append(Hero(1, name))
            self.hero_list[x].name += str(x + 1)
            self.hero_list[x].determine_level()
        return self.hero_list

    def create_opponents(self):
        for x in range(0, (self.num_of_players - self.num_of_heros)):
            if x == 0:
                self.opponent_list.append(Nice_Opponent())
            elif x == 1:
                create_skipper = Skipper_Opponent(self.this_dice.num_of_dice * 3, self.this_dice.num_of_dice * 6)
                self.opponent_list.append(create_skipper)
            elif x == 2:
                create_killer = Killer_Opponent(self.this_dice.num_of_dice * 6)
                self.opponent_list.append(create_killer)
            else:
                self.opponent_list.append(Opponent(1))

            # Randomly determine level
            if self.opponent_list[x].special_skill != "killer":
                self.opponent_list[x].determine_level()

            # Assign names to all opponents with their index+1 value (ie. Opponent1, Opponent2, etc.)
            self.opponent_list[x].name += str(x + 1)
        return self.opponent_list

    def create_players(self, hero_name="Hero"):
        return self.create_heros(hero_name), self.create_opponents()

    def encounter(self, hero_player):
        opp_choice = random.choice(self.opponent_list)
        result = hero_player.attack(opp_choice, self.this_dice)
        if result == "Win":
            self.opponent_list.remove(opp_choice)
            self.num_wins += 1
        elif result == "Lose":
            self.num_loss += 1
        return "Attack Result: " + result

    def print_players(self):
        for x in self.hero_list:
            print(x)
        for x in self.opponent_list:
            print(x)


class Skipper_Opponent(Opponent):
    """
        Inherited from the Opponent() class, this opponent will replace the skip_num when shows up on the dice with a skip_to_num to try to beat the opposing player.

        Attributes:
            skip_num (int): if the dice rolls this number for this player, the number will get replaced or skipped.
            skip_to_num (int): this number will replace the skip_num.

    """
    skill = "skipper"

    def __init__(self, skip_num=3, skip_to_num=6, level=2, name="Skipper Opponent"):
        self.skip_num = skip_num
        self.skip_to_num = skip_to_num
        Opponent.__init__(self, level, name, self.skill)


class Killer_Opponent(Opponent):
    """
        Inherited from the Opponent() class, this opponent will beat the Hero every time unless the Hero rolls the "beat_num".

        Attributes:
            beat_num (int): the number the opposing player (usually the Hero) has to roll to beat this Opponent.

    """
    skill = "killer"

    def __init__(self, beat_num=6, level=10, name="Killer Opponent"):
        self.beat_num = beat_num
        Opponent.__init__(self, level, name, self.skill)


class Nice_Opponent(Opponent):
    """
        Inherited from the Opponent() class, this opponent will always give the opponent "n" number of tries to roll and take the highest number.

        Attributes:
            n_tries (int): the number of times the opposing player can roll to get their best/highest number.

    """
    skill = "nice"

    def __init__(self, n_tries=2, level=2, name="Nice Opponent"):
        self.n_tries = n_tries
        Opponent.__init__(self, level, name, self.skill)
