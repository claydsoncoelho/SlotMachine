# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import colorama
import Slot_Machine_Model

def make_deposit() -> float:
    """
        Returns a valid valid for deposit.
    """
    value: str = ''
    while not(value.isdigit()):
        value = input(" Enter deposit: ")
    return float(value)


def make_bet(balance: float) -> float:
    """
        Returns a valid valid for deposit.
    """
    value: str = ''
    bet_value = balance + 1

    while bet_value > balance:
        while not(value.isdigit()):
            value = input(" Enter your bet: ")

        if float(value) > balance:
            print(colorama.Style.RESET_ALL, "Insufficient balance. Your balance is:", balance)

        bet_value = float(value)
        value = ''

    return float(bet_value)


def print_result(machine: Slot_Machine_Model.SlotMachine) -> None:
    """
        Returns the performance of the player.
    """
    print()
    print(" Initial deposit:", machine.initial_balance)
    print(" Final balance:", machine.current_balance)
    print(" Gain/Lost: ", end="")
    if machine.performance >= 0:
        print(colorama.Fore.BLUE, str(machine.performance) + "%")
    else:
        print(colorama.Fore.RED, str(machine.performance) + "%")
    print(colorama.Style.RESET_ALL, "\nThanks for playing!")


if __name__ == '__main__':
    NUMBER_OF_WHEELS = 3
    print("SLOT MACHINE")
    slot_machine = Slot_Machine_Model.SlotMachine(make_deposit(), NUMBER_OF_WHEELS)
    slot_machine.bet = make_bet(slot_machine.current_balance)

    while slot_machine.bet != 0 and slot_machine.current_balance > 0:
        slot_machine.play_slot_machine()
        print(f" Bet: {slot_machine.bet}")

        if slot_machine.prize > 0:
            print(colorama.Fore.BLUE, "Slot Machine Result: ", slot_machine.wheels_state)
            print(colorama.Fore.BLUE, "Gain: ", slot_machine.prize)
            print(colorama.Style.RESET_ALL, end="")
        else:
            print(colorama.Fore.RED, "Slot Machine Result: ", slot_machine.wheels_state)
            print(colorama.Style.RESET_ALL, end="")

        print(f" Current balance: {slot_machine.current_balance}")
        if slot_machine.current_balance > 0:
            print("***************************************")
            slot_machine.bet = make_bet(slot_machine.current_balance)

    print_result(slot_machine)
