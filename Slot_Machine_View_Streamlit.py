import streamlit as st

deposit = st.number_input('Depisit money')
st.write('The current balance is ', number)

bet = st.slider('Bet amount', 0, deposit, 0)
st.write(bet)
