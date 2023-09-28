import streamlit as st

deposit = 1

deposit = st.number_input('Depisit money')
st.write('The current balance is ', deposit)

bet = st.slider('Bet amount', 0, 1, 0)
st.write(bet)
