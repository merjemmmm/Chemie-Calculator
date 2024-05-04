import streamlit as st

# Funktion für die Startseite der App
def homepage():
    st.title('Herzlich willkommen auf unserer App - Chemie Calculator')
    st.write('Diese App bietet Ihnen die Möglichkeit, häufig verwendete Aufgaben im Chemie Labor zu berechnen.')

    # Balken für Log-in und Sign-up
    login = st.button('Log-in')
    signup = st.button('Sign-up')

    if login:
        login_page()
    elif signup:
        signup_page()

# Funktion für die Log-in-Seite
def login_page():
    st.title('Log-in')
    username = st.text_input('Benutzername')
    password = st.text_input('Passwort', type='password')

    # Hier würde normalerweise die Log-in-Logik eingefügt werden
    # Für dieses Beispiel lassen wir es jedoch weg

    if st.button('Einloggen'):
        st.success('Erfolgreich eingeloggt!')
        home_page()

# Funktion für die Sign-up-Seite
def signup_page():
    st.title('Sign-up')
    gender = st.radio('Anrede', ['Männlich', 'Weiblich'])
    first_name = st.text_input('Vorname')
    last_name = st.text_input('Nachname')
    email = st.text_input('E-Mail')
    education = st.text_input('Ausbildung')
    username = st.text_input('Benutzername')
    password = st.text_input('Passwort', type='password')

    # Hier würde normalerweise die Sign-up-Logik eingefügt werden
    # Für dieses Beispiel lassen wir es jedoch weg

    if st.button('Account erstellen'):
        st.success('Account erfolgreich erstellt!')
        home_page()

# Funktion für den Homebildschirm
def home_page():
    st.title('Homebildschirm')
    st.write('Wählen Sie eine Funktion aus und klicken Sie darauf.')

    # Balken für verschiedene Funktionen
    selected_option = st.selectbox('Funktion wählen', ['Stoffmenge ausrechnen', 'Gramm in mol umrechnen', 'pH-Wert Rechner', 'Theoretische Ausbeute'])

    if selected_option == 'Stoffmenge ausrechnen':
        molar_calculator()
    elif selected_option == 'Gramm in mol umrechnen':
        gram_to_mol_calculator()
    elif selected_option == 'pH-Wert Rechner':
        ph_calculator()
    elif selected_option == 'Theoretische Ausbeute':
        yield_calculator()

# Funktion für den Stoffmengenrechner
def molar_calculator():
    st.title('Stoffmenge ausrechnen')
    mass_unit = st.selectbox('Einheit für Masse', ['Gramm', 'Milligramm'])
    mass = st.number_input('Masse')
    molar_mass = st.number_input('Molare Masse (g/mol)')
    
    if mass_unit == 'Milligramm':
        mass /= 1000  # Umrechnung von Milligramm in Gramm

    result = mass / molar_mass
    st.write('Das Ergebnis beträgt:', result, 'mol')

# Funktion für den Gramm-zu-Mol-Umrechner
def gram_to_mol_calculator():
    st.title('Gramm in mol umrechnen')
    mass = st.number_input('Masse')
    molar_mass = st.number_input('Molare Masse (g/mol)')
    
    result = mass / molar_mass
    st.write('Das Ergebnis beträgt:', result, 'mol')

# Funktion für den pH-Wert-Rechner
def ph_calculator():
    st.title('pH-Wert Rechner')
    # Hier kann die Logik für den pH-Wert-Rechner implementiert werden

# Funktion für die Berechnung der theoretischen Ausbeute
def yield_calculator():
    st.title('Theoretische Ausbeute')
    # Hier kann die Logik für die Berechnung der theoretischen Ausbeute implementiert werden

# Hauptfunktion für die Streamlit-Anwendung
def main():
    homepage()

# Ausführen der Hauptfunktion
if __name__ == "__main__":
    main()


