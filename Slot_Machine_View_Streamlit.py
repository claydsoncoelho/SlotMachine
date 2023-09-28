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
    st.title('_Streamlit_ is :blue[cool] :sunglasses:')
    st.title(':green['+'slot_machine.wheels' + '] :sunglasses:')
    st.title('Prize:', slot_machine.prize)
else:
    st.title('_Streamlit_ is :red[cool] :sunglasses:')
    st.title(':red['+'slot_machine.wheels' + '] :sob:')
    st.title('Prize:', slot_machine.prize)
