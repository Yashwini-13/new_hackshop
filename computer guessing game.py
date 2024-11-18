import streamlit as st
import random

st.title("Computer Guessing Game")
st.write("Think of a number between 1 and 100!")

if 'low' not in st.session_state:
    st.session_state.low, st.session_state.high = 1, 100

guess = random.randint(st.session_state.low, st.session_state.high)
st.write(f"Is your number {guess}?")

if st.button("Lower"): st.session_state.high = guess - 1
elif st.button("Higher"): st.session_state.low = guess + 1
elif st.button("Correct"): st.write(f"Yay! I guessed it!")
