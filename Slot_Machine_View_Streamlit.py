import streamlit as st
import pandas as pd
import Slot_Machine_Model

controller_container = st.container()


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
    
    col1.write('Deposit: ' + str(slot_machine.initial_balance))

    if slot_machine.performance > 0:
        text1 = f'Performance: :green[{slot_machine.performance:.2f}] % :sunglasses:'
        col3.write(text1)
    else:
        text1 = f'Performance: :red[{slot_machine.performance:.2f}] % :sob:'
        col3.write(text1)


def make_deposit(initial):
    if 'slot_machine' not in st.session_state:
        st.session_state['slot_machine'] = Slot_Machine_Model.SlotMachine(initial)
    else:
        st.session_state['slot_machine'].initial_balance += initial
        st.session_state['slot_machine'].current_balance += initial

    col2.write('Balance: ' + str(st.session_state['slot_machine'].current_balance))


def play():
    slot_machine = st.session_state['slot_machine']

    if bet > slot_machine.current_balance:
        st.wirte('Bet cannot be bigger than balance!')
    else:
        slot_machine.bet = bet
        slot_machine.play_slot_machine()
        st.title(translate_symbol())
        st.write('Prize:' + str(slot_machine.prize))

    col2.write('Balance: ' + str(slot_machine.current_balance))
    print_performance()


col1, col2, col3 = st.columns(3)


# addin objects to controller container
deposit = controller_container.number_input('Deposit money')

if controller_container.button('Deposit'):
    make_deposit(deposit)

bet = controller_container.number_input('Bet amount')

if controller_container.button('Bet'):
    play()

if controller_container.button('Reset'):
    st.session_state['slot_machine'] = Slot_Machine_Model.SlotMachine(0)
    col2.write('Balance: ' + str(st.session_state['slot_machine'].current_balance))



