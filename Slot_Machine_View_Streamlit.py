import streamlit as st
import pandas as pd
import Slot_Machine_Model

balance_container = st.container()
botton_container = st.container()

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
    chart_data = pd.DataFrame(
            {
                "Performance": ["Deposit", "Final"],
                "Money": [slot_machine.initial_balance, slot_machine.current_balance]
            }
        )
    chart_data.sort_values(by=['Performance'])
    st.bar_chart(chart_data, x="Performance", y="Money")

    if slot_machine.performance > 0:
        text1 = f'Performance: :green[{slot_machine.performance:.2f}] % :sunglasses:'
        st.title(text1)
    else:
        text1 = f'Performance: :red[{slot_machine.performance:.2f}] % :sob:'
        st.title(text1)


def make_deposit(initial):
    if 'slot_machine' not in st.session_state:
        st.session_state['slot_machine'] = Slot_Machine_Model.SlotMachine(initial)
    else:
        st.session_state['slot_machine'].initial_balance += initial
        st.session_state['slot_machine'].current_balance += initial

    balance_container.title('Balance: ' + str(st.session_state['slot_machine'].current_balance))


def play():
    slot_machine = st.session_state['slot_machine']

    if bet > slot_machine.current_balance:
        st.title('Bet cannot be bigger than balance!')
    else:
        slot_machine.bet = bet
        slot_machine.play_slot_machine()
        st.title(translate_symbol())
        st.title('Prize:' + str(slot_machine.prize))

    balance_container.title('Balance: ' + str(slot_machine.current_balance))
    print_performance()


# bottom container
deposit = botton_container.number_input('Deposit money')

if botton_container.button('Deposit'):
    make_deposit(deposit)

bet = botton_container.number_input('Bet amount')

if sbotton_container.button('Bet'):
    play()

if botton_container.button('Reset'):
    st.session_state['slot_machine'] = Slot_Machine_Model.SlotMachine(0)
    balance_container.title('Balance: ' + str(st.session_state['slot_machine'].current_balance))
