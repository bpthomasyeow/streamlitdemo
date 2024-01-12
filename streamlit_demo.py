#Pokażę parę fajnych rzeczy
import streamlit as st
import numpy as np

#Moduł streamlit całkowicie eliminuje konieczność używania
#HTML/JS/CSS w sytuacjach, gdzie nie musimy spersonalizować
#wygląd strony
st.markdown("# Witam!")
st.markdown("---")

#Następujący string pokazuje się na stronie, bez żadnych dodatków
"Yoo, wassup"

#To również działa w przypadku innych typów zmiennych
#tu deklarujemy
liczba = 777
#a tu wysyłamy do strony
liczba
#jak dbamy o wyglądu jakiegoś elementu,
#zawsze możemy wcisnąć HTML/CSSa
st.markdown(f"<h2 style='text-align: center;'>{liczba}</h2>",
unsafe_allow_html = True)

tabela = np.random.randn(5,10)
#tą linią pokażesz tabelę
st.dataframe(tabela)

#prosty user input, zmienia wartość zmiennej 'wartosc' poniżej
wartosc = st.text_input("User input: ", "boop")
st.write(wartosc)

#download button - dodaje _ po każdej literce w wartosc
txt_for_download = "_".join(list(wartosc))
st.download_button(
    label="Pobierz zmodyfikowany input",
    data=txt_for_download,
    file_name=f'{wartosc}.txt'
    )