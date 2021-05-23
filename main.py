#!/usr/bin/env python3

import streamlit as st
from src.algorytmy.crc import Crc
from src.algorytmy.parity import Parity
from src import utils
from src import SessionState


sess = SessionState.get(data="", interfered_data="", ile_zakloc=1)

st.header("Detekcja i korekcja błędów w transmisji danych")

option = st.selectbox("", ("kontrola parzystości", "kodowanie Humminga", "CRC"))
st.write("You selected:", option)
if option == "CRC":
    algo = Crc()
elif option == "kontrola parzystości":
    algo = Parity()
else:
    pass


st.subheader("Nadawca")
with st.form("nadawca"):
    data = st.text_input("Dane wejściowe")
    koduj = st.form_submit_button("Koduj")
    if koduj:
        sess.data = data
with st.form("generator"):
    qty = st.number_input("Wygeneruj dane", 8, 64, step=8)
    generuj = st.form_submit_button("Generuj")
    if generuj:
        random_bits_l = utils.generate_random_bits(qty)
        data = utils.list_to_str(random_bits_l)
        sess.data = data


st.subheader("Odbiorca")
st.write(f"Dane zakodowane: {sess.data}")

checkboxes = []
with st.form("zakloc"):
    inpt = st.empty()
    bity_zakloc = inpt.text_input("Które bity zakłócić", value="")
    sess.ile_zakloc = st.number_input("Liczba bitów", 1, len(sess.data))
    zakloc = st.form_submit_button("Zakłóć")
if zakloc:
    print(f"bity_zakloc: {bity_zakloc}")
    if bity_zakloc:
        sess.interfered_data = utils.interfere_bits(sess.data, bity_zakloc)
        bity_zakloc = inpt.text_input("Które bity zakłócić", value="", key=1)
    else:
        data = utils.interfere_data(sess.data, sess.ile_zakloc)
        sess.interfered_data = utils.list_to_str(data)
    st.write(f"Zakłocone dane: {sess.interfered_data}")
    result = algo.encode(sess.data)
    st.write(algo.decode(result, sess.interfered_data))  # TODO: wyświetlanie w podsumowaniu
st.subheader("Podsumowanie")
st.write(f"Przesłane bity danych:")
st.write(f"Przesłane bity kontrolne:")
st.write(f"Błędy wykryte:")
st.write(f"Błędy skorygowane:")
st.write(f"Błędy niewykryte:")

st.subheader("Legenda")
st.markdown("<font color='green'>&#9679;</font> poprawny bit danych", unsafe_allow_html=True)
st.markdown("<font color='red'>&#9679;</font> przekłamany bit danych", unsafe_allow_html=True)
st.markdown("<font color='yellow'>&#9679;</font> niepweny bit danych", unsafe_allow_html=True)
st.markdown("<font color='red'>&#9679;</font> poprawny bit redundantny", unsafe_allow_html=True)
st.markdown("<font color='red'>&#9679;</font> przekłamany bit redundantny", unsafe_allow_html=True)
st.markdown("<font color='red'>&#9679;</font> niepewny bit redundantny", unsafe_allow_html=True)
