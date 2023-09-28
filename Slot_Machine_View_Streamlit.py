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

if slot_machine.prize > 0:
    text1 = ':green[' + str(slot_machine.wheels_state) + '] :sunglasses:'
    text2 = 'Prize:' + str(slot_machine.prize)
    st.title('_Streamlit_ is :blue[cool] :sunglasses:')
    st.title(text1)
    st.title(text2)
else:
    text1 = ':red[' + str(slot_machine.wheels_state) + '] :sob:'
    text2 = 'Prize:' + str(slot_machine.prize)
    st.title('_Streamlit_ is :red[cool] :sunglasses:')
    st.title(text1)
    st.title(text2)
