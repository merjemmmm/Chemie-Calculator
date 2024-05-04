import streamlit as st
 
# Funktion für die Startseite der App
def homepage():
    st.title('Herzlich willkommen auf unserer App - Chemie Calculator')
    st.subheader("🧪 Chemie Calculator")
    st.write('Diese App bietet Ihnen die Möglichkeit, häufig verwendete Aufgaben im Chemie Labor zu berechnen.')
    st.write('Wählen Sie eine Funktion aus und klicken Sie darauf.')
    # Balken für verschiedene Funktionen
    selected_option = st.selectbox('Funktion wählen', ['Stoffmenge ausrechnen', 'Gramm in mol umrechnen', 'Theoretische Ausbeute', 'Konzentration berechnen', 'pH-Rechner'])
    if selected_option == 'Stoffmenge ausrechnen':
        molar_calculator()
    elif selected_option == 'Gramm in mol umrechnen':
        gram_to_mol_calculator()
    elif selected_option == 'Theoretische Ausbeute':
        yield_calculator()
    elif selected_option == 'Konzentration berechnen':
        concentration_calculator()
    elif selected_option == 'pH-Rechner':
        ph_calculator()
 
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
    Die Konzentration einer Lösung gibt an, wie viel von einem Stoff in einer gegebenen Menge an Lösungsmittel enthalten ist. Die Einheiten für die Konzentration können Mol pro Liter (mol/L) oder Gramm pro Liter (g/L) sein. Geben Sie die Stoffmenge (in Mol), das Volumen der Lösung (in Litern) und die gewünschte Einheit für die Konzentration ein, um die Konzentration zu berechnen.
    """)
    substance_amount = st.number_input('Stoffmenge (in Mol)')
    solution_volume = st.number_input('Volumen der Lösung (in Litern)')
    concentration_unit = st.selectbox('Einheit für die Konzentration', ['Mol pro Liter (mol/L)', 'Gramm pro Liter (g/L)'])
    if substance_amount != 0 and solution_volume != 0:  # Überprüfen, ob die Stoffmenge und das Volumen der Lösung nicht Null sind
        if concentration_unit == 'Mol pro Liter (mol/L)':
            concentration = substance_amount / solution_volume
            st.write('Die Konzentration beträgt:', concentration, 'mol/L')
        elif concentration_unit == 'Gramm pro Liter (g/L)':
            # Hier benötigen Sie die molare Masse des gelösten Stoffs, um von Mol auf Gramm umzurechnen
            molar_mass = st.number_input('Molare Masse des gelösten Stoffs (g/mol)')
            if molar_mass != 0:
                concentration = (substance_amount * molar_mass) / solution_volume
                st.write('Die Konzentration beträgt:', concentration, 'g/L')
            else:
                st.write('Bitte geben Sie die molare Masse des gelösten Stoffs ein.')
    else:
        st.write('Die Stoffmenge und das Volumen der Lösung können nicht Null sein.')

# Funktion für den pH-Rechner

def ph_calculator():

    st.title('pH-Rechner')

    st.markdown("""

    Der pH-Wert ist ein Maß für die Wasserstoffionenkonzentration in einer Lösung. Er gibt an, wie sauer oder basisch eine Lösung ist. Geben Sie die Konzentration einer Säure oder Base in Mol pro Liter (mol/L) ein, um den pH-Wert zu berechnen.

    """)

    solution_property = st.selectbox('Solution Properties wählen', ['Konzentration einer Säure', 'Konzentration einer Base'])

    if solution_property == 'Konzentration einer Säure':

        acid = st.selectbox('Säure wählen', ['HCl', 'H2SO4', 'HNO3', 'CH3COOH'])

        concentration = st.number_input('Konzentration der Säure (mol/L)')

        if concentration != 0:

            ph = -1 * st.math.log10(concentration)

            st.write('Der pH-Wert beträgt:', ph)

        else:

            st.write('Bitte geben Sie die Konzentration der Säure ein.')

    elif solution_property == 'Konzentration einer Base':

        base = st.selectbox('Base wählen', ['NaOH', 'KOH', 'NH4OH'])

        concentration = st.number_input('Konzentration der Base (mol/L)')

        if concentration != 0:

            poh = -1 * st.math.log10(concentration)

            ph = 14 - poh

            st.write('Der pH-Wert beträgt:', ph)

        else:

            st.write('Bitte geben Sie die Konzentration der Base ein.')

