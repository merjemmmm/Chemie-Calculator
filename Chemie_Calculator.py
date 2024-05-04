import streamlit as st
import pandas as pd
# Hauptfunktion für die Streamlit-Anwendung
def main():
    st.title('Willkommen auf unserer App - Chemie Calculator')
    st.write('Hier finden Sie verschiedene chemische Berechnungen und Informationen.')

# Funktion zur Berechnung der Stoffmenge
def berechne_stoffmenge(masse, molare_masse):
    stoffmenge = masse / molare_masse
    return stoffmenge

# Hauptfunktion für die Streamlit-Anwendung
def main():
    st.title("Willkommen auf unserer App - Chemie Calculator")
    # Login und Sign In Optionen
    login = st.checkbox("Login")
    sign_in = st.checkbox("Sign In")
    
    # Option zur Berechnung der Stoffmenge
    if st.button("Stoffmenge berechnen"):
        # Eingabefelder für Masse und molare Masse
        masse = st.number_input("Masse (in g):")
        molare_masse = st.number_input("Molare Masse (in g/mol):")
        
        # Berechnen und Anzeigen der Stoffmenge
        if masse and molare_masse:
            stoffmenge = berechne_stoffmenge(masse, molare_masse)
            st.write("Die Stoffmenge beträgt:", stoffmenge, "mol")

# Ausführen der Hauptfunktion
if __name__ == "__main__":
    main()
import streamlit as st

# Funktion zum Anzeigen des Periodensystems als Bild
def show_periodic_table():
    # Lade das Bild des Periodensystems
    image = "periodic_table.jpg"
    # Anzeige des Bildes
    st.image(image, caption='Periodensystem', use_column_width=True)

# Hauptfunktion für die Streamlit-Anwendung
def main():
    st.title('Periodensystem-App')
    st.write('Willkommen zur Periodensystem-App! Hier ist das Periodensystem: ')
    
    # Aufrufen der Funktion zum Anzeigen des Periodensystems
    show_periodic_table()

# Ausführen der Hauptfunktion
if __name__ == "__main__":
    main()
