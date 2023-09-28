import streamlit as st
import Slot_Machine_Model

slot_machine = Slot_Machine_Model.SlotMachine(100)

def create_slot_machine(initial):
    st.write(initial)

deposit = st.number_input('Depisit money', on_change=create_slot_machine)
if st.button('Deposit'):
    create_slot_machine(deposit)


bet = st.number_input('Bet amount')
st.write('The current bet is ', bet)

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


st.write(slot_machine)
st.write(slot_machine.bet)
st.write(slot_machine.current_balance)
st.write(slot_machine.initial_balance)
st.write(slot_machine.performance)
st.write(slot_machine.prize)
st.write(slot_machine.wheels)