import streamlit as st
import math
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Verbindung zur SQLite-Datenbank herstellen
conn = sqlite3.connect('user_inputs.db')
c = conn.cursor()

# Tabelle erstellen, falls sie nicht existiert
c.execute('''CREATE TABLE IF NOT EXISTS user_inputs
             (function TEXT, input_value REAL)''')

# CSS für Hintergrundfarbe und Emoji
st.markdown(
    """
    <style>
    .reportview-container {
        background: #d0f0c0;
    }
    .sidebar .sidebar-content {
        background: #d0f0c0;
    }
    .stTextInput, .stNumberInput, .stSelectbox, .stRadio {
        background-color: #e5ffcc;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Funktion für die Startseite der App
def homepage():
    st.title('Herzlich Willkommen auf unserer App - Chemie Calculator')
    st.subheader("🧪 Chemie Calculator")
    st.write('Diese App bietet Ihnen die Möglichkeit, häufig verwendete Aufgaben im Chemie-Labor zu berechnen. Egal, ob Sie die Stoffmenge, die Reaktionsenthalpie oder die Konzentration berechnen möchten, unsere App hilft Ihnen dabei.')
    st.write('Wählen Sie eine Funktion aus und klicken Sie darauf.')
    st.markdown('<div style="font-size: 24px;">🧪🧪🧪</div>', unsafe_allow_html=True)  # Messkolben-Emojis

    # Balken für verschiedene Funktionen
    selected_option = st.selectbox('Funktion wählen', ['Stoffmenge ausrechnen', 'Gramm in mol umrechnen', 'Reaktionsenthalpie berechnen', 'Konzentration berechnen', 'pH-Rechner'])
    if selected_option == 'Stoffmenge ausrechnen':
        molar_calculator()
    elif selected_option == 'Gramm in mol umrechnen':
        gram_to_mol_calculator()
    elif selected_option == 'Reaktionsenthalpie berechnen':
        reaction_enthalpy_calculator()
    elif selected_option == 'Konzentration berechnen':
        concentration_calculator()
    elif selected_option == 'pH-Rechner':
        ph_calculator()
    # Benutzereingabe in Datenbank speichern
    c.execute("INSERT INTO user_inputs (function, input_value) VALUES (?, ?)", (selected_option, 1))
    conn.commit()

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
    st.title('Umwandlung von Mole in Gramm und Gramm in Mole')
    st.markdown("""
    Diese Funktion ermöglicht die Umrechnung einer Masse in Gramm in die entsprechende Stoffmenge in Mol und umgekehrt. Geben Sie die notwendigen Werte ein und wählen Sie die gewünschte Umrechnung.
    """)
    
    st.write("### Substanzformel")
    formula = st.text_input("Substanzformel", "H2O")
    
    convert_option = st.radio("Umwandeln", ("Gramm in Mole", "Mole in Gramm"))
    precision = st.slider("Zahlen nach dem Dezimalpunkt", 0, 5, 3)
    
    # Einfache Periodensystem-Daten
    periodic_table = {
        "H": 1.008, "He": 4.0026, "Li": 6.94, "Be": 9.0122, "B": 10.81, "C": 12.011,
        "N": 14.007, "O": 15.999, "F": 18.998, "Ne": 20.180, "Na": 22.990, "Mg": 24.305,
        "Al": 26.982, "Si": 28.085, "P": 30.974, "S": 32.06, "Cl": 35.45, "Ar": 39.95,
        "K": 39.098, "Ca": 40.078, "Sc": 44.956, "Ti": 47.867, "V": 50.942, "Cr": 51.996,
        "Mn": 54.938, "Fe": 55.845, "Co": 58.933, "Ni": 58.693, "Cu": 63.546, "Zn": 65.38,
        "Ga": 69.723, "Ge": 72.63, "As": 74.922, "Se": 78.971, "Br": 79.904, "Kr": 83.798,
        "Rb": 85.468, "Sr": 87.62, "Y": 88.906, "Zr": 91.224, "Nb": 92.906, "Mo": 95.95,
        "Tc": 98.907, "Ru": 101.07, "Rh": 102.91, "Pd": 106.42, "Ag": 107.87, "Cd": 112.41,
        "In": 114.82, "Sn": 118.71, "Sb": 121.76, "Te": 127.60, "I": 126.90, "Xe": 131.29,
        "Cs": 132.91, "Ba": 137.33, "La": 138.91, "Ce": 140.12, "Pr": 140.91, "Nd": 144.24,
        "Pm": 144.91, "Sm": 150.36, "Eu": 151.96, "Gd": 157.25, "Tb": 158.93, "Dy": 162.50,
        "Ho": 164.93, "Er": 167.26, "Tm": 168.93, "Yb": 173.05, "Lu": 174.97, "Hf": 178.49,
        "Ta": 180.95, "W": 183.84, "Re": 186.21, "Os": 190.23, "Ir": 192.22, "Pt": 195.08,
        "Au": 196.97, "Hg": 200.59, "Tl": 204.38, "Pb": 207.2, "Bi": 208.98, "Th": 232.04,
        "Pa": 231.04, "U": 238.03, "Np": 237.05, "Pu": 244, "Am": 243, "Cm": 247, "Bk": 247,
        "Cf": 251, "Es": 252, "Fm": 257, "Md": 258, "No": 259, "Lr": 262, "Rf": 267, "Db": 270,
        "Sg": 271, "Bh": 270, "Hs": 277, "Mt": 276, "Ds": 281, "Rg": 282, "Cn": 285, "Nh": 286,
        "Fl": 289, "Mc": 290, "Lv": 293, "Ts": 294, "Og": 294
    }
    
    def calculate_molar_mass(formula):
        import re
        elements = re.findall(r'([A-Z][a-z]*)(\d*)', formula)
        molar_mass = 0
        details = []
        for element, count in elements:
            count = int(count) if count else 1
            molar_mass += periodic_table[element] * count
            details.append(f"{count}*{periodic_table[element]}")
        return molar_mass, " + ".join(details)
    
    if formula:
        molar_mass, details = calculate_molar_mass(formula)
        st.write(f"Molare Masse von {formula} = {molar_mass} g/mol")
        st.write(f"Details: {details}")
    
    if convert_option == "Gramm in Mole":
        st.write("### Eingabewerte")
        mass = st.number_input("Masse der Substanz in Gramm")
        if mass != 0 and molar_mass != 0:
            mol = round(mass / molar_mass, precision)
            st.write("### Ergebnis")
            st.write(f"Die Stoffmenge beträgt: {mol} mol")
    else:
        st.write("### Eingabewerte")
        mol = st.number_input("Menge der Substanz in Mole")
        if mol != 0 and molar_mass != 0:
            mass = round(mol * molar_mass, precision)
            st.write("### Ergebnis")
            st.write(f"Die Masse der Substanz beträgt: {mass} g")
    
# Funktion für die Berechnung der Reaktionsenthalpie
def reaction_enthalpy_calculator():
    st.title('Reaktionsenthalpie berechnen')
    st.markdown("""
    Die Reaktionsenthalpie ist die Energiemenge, die bei einer chemischen Reaktion absorbiert oder freigesetzt wird. Sie wird oft in Kilojoule pro Mol (kJ/mol) gemessen. Geben Sie die enthalpischen Werte der beteiligten Stoffe ein und wählen Sie die Art der Reaktion (exotherm oder endotherm), um die Reaktionsenthalpie zu berechnen.
    """)
    substance1 = st.text_input('Name des ersten Stoffes')
    enthalpy1 = st.number_input('Enthalpie des ersten Stoffes (kJ/mol)')
    substance2 = st.text_input('Name des zweiten Stoffes')
    enthalpy2 = st.number_input('Enthalpie des zweiten Stoffes (kJ/mol)')
    reaction_type = st.radio('Art der Reaktion', ['Exotherm', 'Endotherm'])
    if reaction_type == 'Exotherm':
        reaction_enthalpy = enthalpy1 + enthalpy2
    else:
        reaction_enthalpy = enthalpy1 - enthalpy2
    st.write('Die Reaktionsenthalpie beträgt:', reaction_enthalpy, 'kJ/mol')

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
        acid = st.selectbox('Säure wählen', ['HCl', 'H2SO4', 'HNO3', 'H3PO4'])
        concentration = st.number_input('Konzentration der Säure (mol/L)')
        if concentration != 0:
            ph = -1 * math.log10(concentration)
            st.write('Der pH-Wert beträgt:', round(ph, 2))
            st.write('Die Konzentration der H+ beträgt:', concentration, 'mol/L')
        else:
            st.write('Bitte geben Sie die Konzentration der Säure ein.')
    elif solution_property == 'Konzentration einer Base':
        base = st.selectbox('Base wählen', ['NaOH', 'KOH', 'Ca(OH)2', 'NH3'])
        concentration = st.number_input('Konzentration der Base (mol/L)')
        if concentration != 0:
            poh = -1 * math.log10(concentration)
            ph = 14 - poh
            st.write('Der pH-Wert beträgt:', round(ph, 2))
            st.write('Die Konzentration der H+ beträgt:', concentration, 'mol/L')
        else:
            st.write('Bitte geben Sie die Konzentration der Base ein.')

# Zweite Seite für die Datenvisualisierung
def visualize_data():
    st.title('🧪 Datenvisualisierung')
    st.write('Hier werden die Benutzereingaben visualisiert.')
    # Daten aus der Datenbank abrufen
    data = pd.read_sql_query("SELECT * FROM user_inputs", conn)
    st.write(data)

    # Daten für das Balkendiagramm vorbereiten
    function_counts = data['function'].value_counts()

    # Balkendiagramm erstellen
    fig, ax = plt.subplots()
    function_counts.plot(kind='bar', color='green', ax=ax)
    ax.set_title('Benutzereingaben')
    ax.set_xlabel('Funktion')
    ax.set_ylabel('Anzahl der Eingaben')
    st.pyplot(fig)

# Navigation zwischen Startseite und Datenvisualisierung
page = st.sidebar.selectbox('Seiten', ['Startseite', 'Datenvisualisierung'])
if page == 'Startseite':
    homepage()
elif page == 'Datenvisualisierung':
    visualize_data()

# Verbindung zur Datenbank schließen
conn.close()
