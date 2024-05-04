import streamlit as st

# Funktion für die Startseite der App
def homepage():
    st.title('Herzlich willkommen auf unserer App - Chemie Calculator')
    st.subheader("🧪 Chemie Calculator")
    st.write('Diese App bietet Ihnen die Möglichkeit, häufig verwendete Aufgaben im Chemie Labor zu berechnen.')
    st.write('Wählen Sie eine Funktion aus und klicken Sie darauf.')

    # Balken für verschiedene Funktionen
    selected_option = st.selectbox('Funktion wählen', ['Stoffmenge ausrechnen', 'Gramm in mol umrechnen', 'pH-Wert Rechner', 'Theoretische Ausbeute', 'Konzentration berechnen'])

    if selected_option == 'Stoffmenge ausrechnen':
        molar_calculator()
    elif selected_option == 'Gramm in mol umrechnen':
        gram_to_mol_calculator()
    elif selected_option == 'pH-Wert Rechner':
        ph_calculator()
    elif selected_option == 'Theoretische Ausbeute':
        yield_calculator()
    elif selected_option == 'Konzentration berechnen':
        concentration_calculator()

# Funktion für den Stoffmengenrechner
def molar_calculator():
    st.title('Stoffmenge ausrechnen')
    st.markdown("""
    Die Stoffmenge (auch Mol genannt) ist eine grundlegende Größe in der Chemie, die die Anzahl der Teilchen in einer Substanz angibt. Ein Mol entspricht etwa 6,022 x 10^23 Teilchen, was als Avogadro-Konstante bekannt ist. Um die Stoffmenge auszurechnen, müssen Sie die Masse der Substanz und ihre molare Masse kennen. Wählen Sie die Einheit für die Masse und geben Sie dann die Masse und die molare Masse ein, um die Stoffmenge zu berechnen.
    """)

    mass_unit = st.selectbox('Einheit für Masse', ['Gramm', 'Milligramm'])
    mass = st.number_input('Masse')
    molar_mass = st.number_input('Molare Masse (g/mol)')
    
    if molar_mass != 0:  # Überprüfen, ob die molare Masse nicht Null ist
        if mass_unit == 'Milligramm':
            mass /= 1000  # Umrechnung von Milligramm in Gramm

        result = mass / molar_mass
        st.write('Das Ergebnis beträgt:', result, 'mol')
    else:
        st.write('Die molare Masse kann nicht Null sein.')

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

# Funktion für die Berechnung der Konzentration
def concentration_calculator():
    st.title('Konzentration berechnen')
    st.markdown("""
    Die Konzentration (c) einer Lösung kann berechnet werden, indem die Stoffmenge (n) durch das Volumen (V) der Lösung geteilt wird. 
    """)

    st.write('Geben Sie die Stoffmenge (in mol) ein:')
    n = st.number_input('Stoffmenge')

    st.write('Geben Sie das Volumen (in Liter) ein:')
    V = st.number_input('Volumen')

    if V != 0:  # Überprüfen, ob das Volumen nicht Null ist
        c = n / V
        st.write('Die Konzentration beträgt:', c, 'mol/L')
    else:
        st.write('Das Volumen kann nicht Null sein.')

# Hauptfunktion für die Streamlit-Anwendung
def main():
    homepage()

# Ausführen der Hauptfunktion
if __name__ == "__main__":
    main()
