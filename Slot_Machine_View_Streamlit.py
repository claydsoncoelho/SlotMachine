import streamlit as st
import Slot_Machine_Model

deposit = 1

deposit = st.number_input('Depisit money')
st.write('The current balance is ', deposit)

bet = st.slider('Bet amount', 0, int(deposit), 0)
st.write(bet)

slot_machine = Slot_Machine_Model.SlotMachine(deposit)
slot_machine.bet = bet
slot_machine.play_slot_machine()

st.write(slot_machine.prize)
