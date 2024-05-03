import streamlit as st


def main():
    st.title('Herzlich Willkommen auf meine App!')
    st.sidebar.title('Dies ist eine einfache Seitenleiste.')
    st.sidebar.write('Hier kannst du Widgets hinzufügen:')
    st.write('')
 
    st.subheader('Willkommen bei Merjems Streamlit', divider='orange')
    st.subheader('_Data elements_ :heart:')
    st.subheader(' ',divider='orange')

    # Data elements
    import pandas as pd
    import numpy as np

    data = {
        'Name': ['Hans', 'Alice', 'Franz', 'Lisa'],
        'Age': [30, 25, 35, 28],
        'City': ['New York', 'Paris', 'London', 'Tokyo']
    }
    df = pd.DataFrame(data)

    st.table(df)
    st.subheader('_Chart elements_ :heart:')
    st.subheader(' ',divider='orange')

    # Chart elements
    chart_data = pd.DataFrame({
        "Category": ['A', 'B', 'C', 'D'],
        "Values": [20, 30, 25, 35]
    })

    st.bar_chart(chart_data.set_index('Category'))

    st.subheader('_Input Widgets_ :heart:')
    st.subheader(' ',divider='orange')

    # Input Widgets
    import datetime

    birth_date = st.date_input("Dein Geburtstag:", datetime.date(2003, 4, 20))
    st.write('Dein Geburtstag ist:', birth_date)

    text_input = st.text_input('Schreibe hier etwas:', 'Hallo Welt')
    slider_value = st.slider('Wähle einen Wert', 0, 100, 50)

if __name__ == '__main__':
    main()
 