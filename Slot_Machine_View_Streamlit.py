import streamlit as st
import Slot_Machine_Model
import pandas as pd

def make_deposit(initial):
    if 'slot_machine' not in st.session_state:
        st.session_state['slot_machine'] = Slot_Machine_Model.SlotMachine(initial)
    else:
        st.session_state['slot_machine'].initial_balance += initial
        st.session_state['slot_machine'].current_balance += initial

    st.title('Balance: ' + str(st.session_state['slot_machine'].current_balance))


def play():
    slot_machine = st.session_state['slot_machine']

    if bet > slot_machine.current_balance:
        st.title('Bet cannot be bigger than balance!')
    else:
        slot_machine.bet = bet
        slot_machine.play_slot_machine()
        if slot_machine.prize > 0:
            text1 = ':green[' + str(slot_machine.wheels_state) + '] :sunglasses:'
            text2 = 'Prize:' + str(slot_machine.prize)
            st.title(text1)
            st.title(text2)
        else:
            text1 = ':red[' + str(slot_machine.wheels_state) + '] :sob:'
            text2 = 'Prize:' + str(slot_machine.prize)
            st.title(text1)
            st.title(text2)

        chart_data = pd.DataFrame(
            {
                "Performance": ["Current", "Initial"],
                "Money": [slot_machine.initial_balance, slot_machine.current_balance]
            }
        )
        chart_data.sort_values(by=['Performance'])
        st.bar_chart(chart_data, x="Performance", y="Money")

    st.title('Balance: ' + str(slot_machine.current_balance))


deposit = st.number_input('Deposit money')

if st.button('Deposit'):
    make_deposit(deposit)

bet = st.number_input('Bet amount')

if st.button('Bet'):
    play()


if st.button('Reset'):
    st.session_state['slot_machine'] = Slot_Machine_Model.SlotMachine(deposit)
