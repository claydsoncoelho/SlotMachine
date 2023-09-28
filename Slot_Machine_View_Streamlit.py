import streamlit as st
import pandas as pd
import Slot_Machine_Model

balance_container = st.container()

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
        if slot_machine.prize > 0:
            text1 = ':green[' + slot_machine.wheels[0].current_symbol + slot_machine.wheels[1].current_symbol + slot_machine.wheels[2].current_symbol + '] :sunglasses:'
            st.title(text1)
        else:
            text1 = ':red[' + slot_machine.wheels[0].current_symbol + slot_machine.wheels[1].current_symbol + slot_machine.wheels[2].current_symbol + '] :sob:'
            st.title(text1)

        st.title('Prize:' + str(slot_machine.prize))

    balance_container.title('Balance: ' + str(slot_machine.current_balance))
    print_performance()


# sidebar
deposit = st.sidebar.number_input('Deposit money')

if st.sidebar.button('Deposit'):
    make_deposit(deposit)

bet = st.sidebar.number_input('Bet amount')

if st.sidebar.button('Bet'):
    play()

if st.sidebar.button('Reset'):
    st.session_state['slot_machine'] = Slot_Machine_Model.SlotMachine(0)
    balance_container.title('Balance: ' + str(st.session_state['slot_machine'].current_balance))
