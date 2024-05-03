import streamlit as st

# Funktion zur Berechnung der Stoffmenge
def berechne_stoffmenge(masse, molare_masse):
    stoffmenge = masse / molare_masse
    return stoffmenge

# Hauptfunktion für die Streamlit-Anwendung
def main():
    st.title("Chemie Rechner")
    
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
