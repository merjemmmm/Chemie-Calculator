import streamlit as st

# Funktion für die Startseite der App
def homepage():
    st.title('Herzlich willkommen auf unserer App - Chemie Calculator')
    st.subheader("🧪 Chemie Calculator")
    st.write('Diese App bietet Ihnen die Möglichkeit, häufig verwendete Aufgaben im Chemie Labor zu berechnen.')
    st.write('Wählen Sie eine Funktion aus und klicken Sie darauf.')

    # Balken für verschiedene Funktionen
    selected_option = st.selectbox('Funktion wählen', ['Stoffmenge ausrechnen', 'Gramm in mol umrechnen', 'Theoretische Ausbeute', 'Konzentration berechnen'])

    if selected_option == 'Stoffmenge ausrechnen':
        molar_calculator()
    elif selected_option == 'Gramm in mol umrechnen':
        gram_to_mol_calculator()
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
    
    if mass != 0 and molar_mass != 0:  # Überprüfen, ob die Masse und die molare Masse nicht Null sind
        if mass_unit == 'Milligramm':
            mass /= 1000  # Umrechnung von Milligramm in Gramm

        result = mass / molar_mass
        st.write('Das Ergebnis beträgt:', result, 'mol')
    else:
        st.write('Die Masse und die molare Masse können nicht Null sein.')

# Funktion für den Gramm-zu-Mol-Umrechner
def gram_to_mol_calculator():
    st.title('Gramm in mol umrechnen')
    mass = st.number_input('Masse')
    molar_mass = st.number_input('Molare Masse (g/mol)')
    
    result = mass / molar_mass
    st.write('Das Ergebnis beträgt:', result, 'mol')

# Funktion für die Berechnung der theoretischen Ausbeute
def yield_calculator():
    st.title('Theoretische Ausbeute')
    # Hier kann die Logik für die Berechnung der theoretischen Ausbeute implementiert werden

# Funktion für die Berechnung der Konzentration
def concentration_calculator():
    st.title('Konzentration berechnen')
    st.markdown("""
    Die Konzentration einer Lösung wird als das Verhältnis der Menge des gelösten Stoffs zur Menge der Lösung definiert. Geben Sie die Anzahl der Mole des gelösten Stoffs und das Volumen der Lösung ein, um die Konzentration zu berechnen.
    """)

    moles = st.number_input('Anzahl der Mole')
    volume = st.number_input('Volumen der Lösung (in Liter)')
    
    if moles != 0 and volume != 0:  # Überprüfen, ob die Anzahl der Mole und das Volumen nicht Null sind
        concentration = moles / volume
        st.write('Die Konzentration beträgt:', concentration, 'mol/L')
    else:
        st.write('Die Anzahl der Mole und das Volumen können nicht Null sein.')

# Hauptfunktion für die Streamlit-Anwendung
def main():
    homepage()

# Ausführen der Hauptfunktion
if __name__ == "__main__":
    main()


