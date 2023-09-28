# The Slot_Machine_Model is a fully operational slot machine. It is composed of 2 main classes:

import os
import csv
import random

# =================================================================================================
# This block reads the csv file and returns a list of lines of the file. Each line is a dictionary.
# The key is the column name and the value is the column contant for that specific line.

FILE_NAME = os.getcwd() + "/Slot_Machine_Config.csv"

def read_config_csv() -> list[dict]:
    config_list = []
    try:
        with open(FILE_NAME, "r") as config_file:
            reader = csv.DictReader(config_file)
            for row in reader:
                row["Chance"] = int(row["Chance"])
                row["Prize"] = int(row["Prize"])
                config_list.append(row)
            return config_list
    except FileNotFoundError:
        with open(FILE_NAME, "w",
                  newline="") as config_file:
            field_names = ('Symbol', 'Chance', 'Prize')
            writer = csv.DictWriter(config_file, fieldnames=field_names)
            writer.writeheader()
        return config_list
# =================================================================================================

class Wheel:
    """
    Class Wheel – A class that represents a single wheel. 
    Attributes:
        1 – symbol_list: The list of symbols printed on the wheel.
        2 – symbol_prize: A dictionary with a pair Symbol: Prize. In other words, what is the Prize of each Symbol.
        3 – current_symbol: Which Symbol from the symbol_list is showing now in the display of the that specific wheel.
    Methods:
        1 – spin(): This method spins the wheel, which will randomly pic another value from the symbol_list and show it in current_symbol.
    """
    def __init__(self):
        self.symbol_list: list = []
        self.symbol_prize: dict = {}
        self.current_symbol: str = ''

        # Creating the symbol_list and the symbol_prize based on the config file.
        for item in read_config_csv():
            self.symbol_prize[item["Symbol"]] = item["Prize"]
            for i in range(item["Chance"]):
                self.symbol_list.append(item["Symbol"])

    def __eq__(self, other):
        return self.current_symbol == other.current_symbol

    def spin(self):
        self.current_symbol = random.choice(self.symbol_list)


class SlotMachine:
    """
    Class SlotMachine – A class that represents a fully functional slot machine.
	Attributes:
		1 – initial_balance: How much money the user deposited in the machine.
		2 – current_balance: How much money the user has inside the machine.
		3 – wheels: A list of Wheel objects described above.
		4 – wheels_state: A list of current_symbols on each wheel.
		5 – prize: How much money the user won as a prize. It’s 0 if the user didn’t win on that round.
		6 – bet: How much money the user bet on that round.
    Methods:
		1 – play(): This method spins all the 3 wheels of the slot machine, 
          get the new current_symbol of each wheel and save them in wheels_state attribute.
    """
    def __init__(self, initial_balance: float, wheels_quantity: int):
        self.initial_balance = initial_balance
        self.current_balance = initial_balance
        self.wheels = [Wheel(), Wheel(), Wheel()]
        self.wheels_state: list = [str * wheels_quantity]
        self.prize = 0
        self.bet = 0
        self.performance = 100
	self.wheels_quantity = wheels_quantity

    @property
    def bet(self):
        return self._bet

    @bet.setter
    def bet(self, bet):
        if bet > self.current_balance:
            raise ValueError("Bet cannot be bigger than current balance!")
        self._bet = bet

    def __calculate_balance(self):
        # Internal method that calculates the current_balance, 
        # the prize and the performance depending if the user won or lost this round
        if legth(set(self.wheels_state)) == 1:
            self.prize = self.bet * self.wheels[0].symbol_prize[self.wheels[0].current_symbol]
            self.current_balance += self.bet + self.prize
        else:
            self.prize = 0
            self.current_balance -= self.bet
        self.performance = (self.current_balance - self.initial_balance) / self.initial_balance * 100

    def play_slot_machine(self) :
        # Method that spins all wheels, updates the wheels_state and calls the _calculate_balance.
        for i in range(self.wheels_quantity):
            self.wheels[i].spin()
            self.wheels_state[i] = self.wheels[i].current_symbol
        self.__calculate_balance()
