import streamlit as st

deposit = 0

deposit = st.number_input('Depisit money')
st.write('The current balance is ', deposit)

bet = st.slider('Bet amount', 0, 130, 25)
st.write(bet)
