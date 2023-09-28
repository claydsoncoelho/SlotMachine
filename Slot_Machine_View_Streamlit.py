import streamlit as st
import pandas as pd
import Slot_Machine_Model
import random

controller_container = st.container()
display_container = st.container()
performance_container = st.container()


def translate_symbol():
    """
        To turn thing visually more attractive, this function will replace the original symbols in the config file by emojis. 
        A new random dictionary, symbols_dict, will be created every time this function is called.
        Symbols_dict will have a key value pair equals “Old_Key”: “New random value”.
        The random value will be chosen from new_symbols list, which is a list of emojis.
    """
    slot_machine = st.session_state['slot_machine']
    display = ''
    new_symbols = [' :four_leaf_clover: ', ' :taco: ', ' :watermelon: ', ' :hot_pepper: ', ' :corn: ', ' :maple_leaf: ', ' :grapes: ', ' :peach: ']
    key_list = list(set(slot_machine.wheels[0].symbol_list))
    key_list.sort()
    symbols_dict = {}

    for i in range(len(key_list)):
        #new_symbols.pop() is used because once an emoji is chosen, it will be removed from new_symbols list, avoiding it to be chosen again.
        #random.choicec() will choose a number between 0 and the lenght of the new_symbols list, which will be the index of the chosen emoji.
        symbols_dict[key_list[i]] = new_symbols.pop(random.choice(range(len(new_symbols))))

    for symbol in slot_machine.wheels_state:
        display += symbols_dict[symbol]
        
    return display


def print_performance():
    slot_machine = st.session_state['slot_machine']
    performance_container.write('Deposit: ' + str(slot_machine.initial_balance))

    if slot_machine.performance > 0:
        text1 = f'Performance: :green[{slot_machine.performance:.2f}] % :sunglasses:'
        performance_container.write(text1)
    else:
        text1 = f'Performance: :red[{slot_machine.performance:.2f}] % :sob:'
        performance_container.write(text1)


def make_deposit(initial):
    if 'slot_machine' not in st.session_state:
        st.session_state['slot_machine'] = Slot_Machine_Model.SlotMachine(initial, 3)
    else:
        st.session_state['slot_machine'].initial_balance += initial
        st.session_state['slot_machine'].current_balance += initial

    performance_container.write('Balance: ' + str(st.session_state['slot_machine'].current_balance))


def play():
    slot_machine = st.session_state['slot_machine']

    if bet > slot_machine.current_balance or slot_machine.current_balance == 0:
        st.error('Bet cannot be bigger than balance!')
    else:
        slot_machine.bet = bet
        slot_machine.play_slot_machine()
        display_container.title(translate_symbol())
        display_container.write('Prize: ' + str(slot_machine.prize))

    performance_container.write('Balance: ' + str(slot_machine.current_balance))
    print_performance()


# addin objects to controller container
deposit = controller_container.number_input('Deposit')
if controller_container.button('Deposit'):
    make_deposit(deposit)

bet = controller_container.number_input('Bet')

if controller_container.button('Bet'):
    play()

if controller_container.button('Reset'):
    st.session_state['slot_machine'] = Slot_Machine_Model.SlotMachine(0, 3)
    controller_container.write('Balance: ' + str(st.session_state['slot_machine'].current_balance))
