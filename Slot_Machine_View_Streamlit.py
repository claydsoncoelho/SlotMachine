import streamlit as st
import pandas as pd
import Slot_Machine_Model

controller_container = st.container()
display_container = st.container()
performance_container = st.container()


def translate_symbol():
    slot_machine = st.session_state['slot_machine']
    display = ''

    for i in range(3):
        if slot_machine.wheels[i].current_symbol == 'A':
            display += ' :four_leaf_clover: '
        elif slot_machine.wheels[i].current_symbol == 'B':
            display += ' :taco: '
        else:
            display += ':watermelon:'
        
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
        st.session_state['slot_machine'] = Slot_Machine_Model.SlotMachine(initial)
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
    st.session_state['slot_machine'] = Slot_Machine_Model.SlotMachine(0)
    controller_container.write('Balance: ' + str(st.session_state['slot_machine'].current_balance))
