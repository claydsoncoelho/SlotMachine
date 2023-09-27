import os
import csv
import random


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


class Wheel:
    def __init__(self):
        self.symbol_list: list = []
        self.symbol_prize: dict = {}
        self.current_symbol: str = ''

        for item in read_config_csv():
            self.symbol_prize[item["Symbol"]] = item["Prize"]
            for i in range(item["Chance"]):
                self.symbol_list.append(item["Symbol"])

    def __eq__(self, other):
        return self.current_symbol == other.current_symbol

    def spin(self):
        self.current_symbol = random.choice(self.symbol_list)


class SlotMachine:
    def __init__(self, initial_balance: float):
        self.initial_balance = initial_balance
        self.current_balance = initial_balance
        self.wheels = [Wheel(), Wheel(), Wheel()]
        self.wheels_state: list = [str, str, str]
        self.prize = 0
        self.bet = 0
        self.performance = 100

    @property
    def bet(self):
        return self._bet

    @bet.setter
    def bet(self, bet):
        if bet > self.current_balance:
            raise ValueError("Bet cannot be bigger than current balance!")
        self._bet = bet

    def __calculate_balance(self):
        if self.wheels[0] == self.wheels[1] and self.wheels[1] == self.wheels[2]:
            self.prize = self.bet * self.wheels[0].symbol_prize[self.wheels[0].current_symbol]
            self.current_balance += self.bet + self.prize
        else:
            self.prize = 0
            self.current_balance -= self.bet
        self.performance = (self.current_balance - self.initial_balance) / self.initial_balance * 100

    def play_slot_machine(self) :
        for i in range(3):
            self.wheels[i].spin()
            self.wheels_state[i] = self.wheels[i].current_symbol
        self.__calculate_balance()
