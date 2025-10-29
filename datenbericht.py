import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

from datetime import datetime, timedelta
import time


# Seitenlayout konfigurieren

st.set_page_config(
    page_title="Agathon_LabCheckAI",
    layout="wide"
)


# Custom CSS für dunklen Hintergrund und weiße Schrift
st.markdown("""
    <style>
            
        div[data-testid="stTabs"] {
            display: flex;
            justify-content: center; /* Tabs zentrieren */
        }
        div[data-testid="stTabs"] button {
            font-size: 18px;
            padding: 12px 24px;
            margin: 0 8px;
            border-radius: 8px;
            background-color: #004080;
            color: white;
            border: none;
        }
        div[data-testid="stTabs"] button:hover {
            background-color: #0059b3;
        }
        div[data-testid="stTabs"] button:focus {
            background-color: #0073e6;
            font-weight: bold;
        }
            


        /* Rahmen des Expanders */
        div[data-testid="stExpander"] {
            border: 2px solid black; /* Schwarzer Rahmen */
            border-radius: 8px;
        }

        /* Hintergrundfarbe bei geöffnetem Zustand */
        div[data-testid="stExpander"] > details[open] {
            background-color: #004080; /* Blau */
            color: white; /* Textfarbe */
            padding: 15px;
        }

        /* Titel des Expanders */
        div[data-testid="stExpander"] > details > summary {
            font-size: 20px;
            background-color: #003366; /* Dunkelblau für Titel */
            color: white;
            padding: 10px;
            border-radius: 8px;
        }
            
        /* Hintergrund und Schriftfarbe */
        body, .stApp {
            background-color: #001f3f;
            color: white;
        }

        h1, h2, h3, h4, h5, h6, p {
            color: white;
        }

        /* Tabs größer und besser sichtbar machen */
        div[data-testid="stTabs"] button {
            font-size: 56px;
            padding: 32px 42px;
            margin-right: 12px;
            border-radius: 12px;
            background-color: #003366;
            color: white;
            border: none;
        }

        div[data-testid="stTabs"] button:hover {
            background-color: #004080;
        }
            

        div[data-testid="stTabs"] button:focus {
            background-color: #0059b3;
            font-weight: bold;
        }

        /* Expander-Titel und Inhalt bei geöffnetem Zustand */
        div[data-testid="stExpander"] > details[open] > summary {
            background-color: #003366;
            color: #3399ff;
            font-size: 18px;
        }

        div[data-testid="stExpander"] > details[open] {
            color: #3399ff;
        }

        /* Hintergrund für h3-Überschriften */
        h2 {
            background-color: #004080;
            color: white;
            padding: 10px;
            border-radius: 6px;
            text-align: center;
        }
            
        h3 {
            padding: 10px;
            border-radius: 6px;
            text-align: center;
        }
        

        h1 {
            text-align: center;
        }

    </style>
""", unsafe_allow_html=True)


st.write("")
image = Image.open(r"C:\Users\Magnus.Senfter\OneDrive - AGAPLESION gAG\Dokumente\Projects\Agathon\Dashboards\AGAthon.png")
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(image)
st.write("")
st.title("🧪 Agathon - LabCheckAI – Laboranalyse für die Notaufnahme")
st.write("")




st.markdown("""
    <div style="padding: 40px 60px; background-color: #ffffff; border-radius: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
        <h2 style="color: #003366; font-size: 32px; margin-bottom: 20px; background-color: #ffffff; padding: 10px 20px; border-radius: 8px;">
            Willkommen im Analyse-Dashboard für die Aufgabe <em>'LabAI Check'</em> des Agathons 2025
        </h2>
        <p style="font-size: 18px; line-height: 1.8; color: #333;">
            Beim <strong>AGAthon</strong> von AGAPLESION treffen kreative Köpfe aus verschiedenen Disziplinen aufeinander, 
            um innovative Ideen für die Gesundheitsversorgung von morgen zu gestalten.
            <br><br>
            <span style="font-weight: bold;">📅 31. Oktober – 01. November 2025</span> | <span style="font-style: italic;">Frankfurt am Main</span><br>
            Durchgeführt mit technischer Unterstützung von <strong>Campana &amp; Schott</strong>.
            <br><br>
            Hier findest du eine strukturierte Übersicht über die Daten, Vorverarbeitungsschritte und erste Einblicke.
        </p>
    </div>
""", unsafe_allow_html=True)


st.write("")

with st.expander("### 🗓️ Programmübersicht"):


    col1, col2 = st.columns(2)

    table_style = """
    <style>
        .styled-table {
            margin-left: auto;
            margin-right: auto;
            border-collapse: collapse;
            font-size: 16px;
            min-width: 300px;
            background-color: #003366;
            color: white;
            border-radius: 8px;
            overflow: hidden;
        }
        .styled-table th, .styled-table td {
            padding: 12px 15px;
            border: 1px solid #004080;
            text-align: center;
        }
        .styled-table th {
            background-color: #004080;
            font-weight: bold;
        }
        .styled-table tr:nth-child(even) {
            background-color: #002244;
        }
    </style>
    """

    st.markdown(table_style, unsafe_allow_html=True)

    with col1:
        st.markdown("### 📅 1. Tag")
        st.markdown("""
        <table class="styled-table">
            <tr><th>Zeit</th><th>Programmpunkt</th></tr>
            <tr><td>12:00–12:20 Uhr</td><td>Ankunft und Kennenlernen</td></tr>
            <tr><td>12:20–12:30 Uhr</td><td>Ansprache Vorstand AGAPLESION</td></tr>
            <tr><td>12:30–12:50 Uhr</td><td>Vortrag Voize</td></tr>
            <tr><td>12:50–13:10 Uhr</td><td>Vortrag ZD KI AGAPLESION</td></tr>
            <tr><td>13:10–13:30 Uhr</td><td>Vortrag Microsoft</td></tr>
            <tr><td>13:30–13:40 Uhr</td><td>Pause</td></tr>
            <tr><td>13:40–14:10 Uhr</td><td>Vorstellung der Challenges</td></tr>
            <tr><td>14:10–14:30 Uhr</td><td>Bildung der Teams</td></tr>
            <tr><td>ab 14:30 Uhr</td><td>Time to Hack</td></tr>
        </table>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("### 📅 2. Tag")
        st.markdown("""
        <table class="styled-table">
            <tr><th>Zeit</th><th>Programmpunkt</th></tr>
            <tr><td>bis 11:00 Uhr</td><td>Time to Hack</td></tr>
            <tr><td>11:00–11:15 Uhr</td><td>Vorbereitung Pitches</td></tr>
            <tr><td>11:15–12:30 Uhr</td><td>Pitching der Gruppen</td></tr>
            <tr><td>12:30–13:00 Uhr</td><td>Juryberatung</td></tr>
            <tr><td>13:00–13:30 Uhr</td><td>Siegerehrung mit Preisverleihung</td></tr>
            <tr><td>13:30–15:00 Uhr</td><td>Mittagsimbiss und Vernetzen</td></tr>
        </table>
        """, unsafe_allow_html=True)
st.write("")

st.markdown("## Informationen zur Aufgabe")
st.write("")


st.markdown("""
    <div style="background-color: #ffffff; padding: 40px 60px; border-radius: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
        <h3 style="color: #003366;">🔬 AI LabCheck in der Notaufnahme</h3>
        
""", unsafe_allow_html=True)
st.write("")
st.markdown("### Hintergrund Informationen")
st.write("")
    
st.markdown("""
    <div style="background-color: #ffffff; padding: 40px 60px; border-radius: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
        <h3 style="color: #003366;">📘 Beispieltext</h3>
        <p style="font-size: 18px; line-height: 1.8; color: #333;">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
            <br><br>
            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
            Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
    </div>
""", unsafe_allow_html=True)
st.write("")
st.markdown("## 📁Daten für LabAI Check")

import streamlit as st
st.write("")
# Tabs erstellen
tab1, tab2, tab3, tab4 = st.tabs(["📊 Manchester Triage System", "📋 Diagnosen", "⚙️ Laboranforderungen","🧪 Laborwerte",])

            
st.write("")
with tab1:
    with st.expander("🆔 Fallnummer"):
        st.markdown("Eindeutige Kennung des Falls im Krankenhausinformationssystem.")

    with st.expander("🎂 Alter"):
        st.markdown("Alter des Patienten zum Zeitpunkt der Aufnahme.")

    with st.expander("⚧ Geschlecht"):
        st.markdown("Geschlecht des Patienten (z. B. männlich, weiblich, divers).")

    with st.expander("📅 Admin. Fall-Aufnahmedatum"):
        st.markdown("Datum der administrativen Fallaufnahme im Krankenhausinformationssystem.")

    with st.expander("📌 Fallstatus"):
        st.markdown("Aktueller Status des Falls (z. B. offen, abgeschlossen, archiviert).")

    with st.expander("🏥 Aufnahme ZNA"):
        st.markdown("Gibt an, ob die Aufnahme über die Zentrale Notaufnahme erfolgt ist.")

    with st.expander("📆 Wochentag"):
        st.markdown("Wochentag der Aufnahme (z. B. Montag, Dienstag).")

    with st.expander("❓ Grund des Kommens"):
        st.markdown("Vom Patienten genannter oder dokumentierter Anlass für die Vorstellung.")

    with st.expander("🏥 Primäre Fachrichtung (Code)"):
        st.markdown("Fachabteilung, die primär für den Fall zuständig ist (z. B. Innere Medizin, Chirurgie).")

    with st.expander("📈 Schmerzskala-Einstufung"):
        st.markdown("Subjektive Einschätzung des Schmerzniveaus durch den Patienten (z. B. 0–10).")

    with st.expander("📊 MTS Diagramm"):
        st.markdown("Visualisierung der Ersteinschätzung nach Manchester Triage System.")

    with st.expander("📍 Indikator"):
        st.markdown("Spezifischer Hinweis oder Marker zur Einschätzung des Patientenstatus.")

    with st.expander("📋 MTS Einstufung"):
        st.markdown("Einstufung der Dringlichkeit nach Manchester Triage System.")

    with st.expander("🩸 BG"):
        st.markdown("Angabe zur Blutgruppe des Patienten (falls bekannt).")

    with st.expander("💉 Tetanusschutz"):
        st.markdown("Information über bestehenden Tetanusschutz des Patienten.")

    with st.expander("⚠️ Allergien"):
        st.markdown("Bekannte Allergien des Patienten, relevant für Behandlung und Medikation.")

    with st.expander("📄 Einweisung"):
        st.markdown("Information zur Art der Einweisung (z. B. durch Hausarzt, Rettungsdienst).")

    with st.expander("🚑 Transport"):
        st.markdown("Art des Transports zur Klinik (z. B. Rettungswagen, selbstständig).")

    with st.expander("🦠 Isolation"):
        st.markdown("Gibt an, ob der Patient isoliert werden musste (z. B. bei Infektionsverdacht).")

    with st.expander("⏰ Entlassungszeit"):
        st.markdown("Uhrzeit der Entlassung des Patienten.")

    with st.expander("📅 Admin. Fall-Entlassdatum"):
        st.markdown("Datum der administrativen Entlassung im Krankenhausinformationssystem.")

    with st.expander("🏁 Entlassung Ambulant (Ja/Nein)"):
        st.markdown("Gibt an, ob der Patient ambulant entlassen wurde.")

    with st.expander("📄 Entlassung"):
        st.markdown("Art der Entlassung (z. B. nach Hause, in andere Einrichtung).")

    with st.expander("📊 Gesamtaufenthaltsdauer"):
        st.markdown("Gesamtdauer des Aufenthalts in Tagen.")

    with st.expander("🚨 Notfall- oder Elektivpatient"):
        st.markdown("Kennzeichnung, ob es sich um einen Notfall oder eine geplante Aufnahme handelt.")

    with st.expander("🩺 Blutdruck"):
        st.markdown("Gemessener Blutdruck bei Aufnahme (z. B. 120/80 mmHg).")

    with st.expander("❤️ Puls"):
        st.markdown("Herzfrequenz des Patienten bei Aufnahme (Schläge pro Minute).")

    with st.expander("🌡️ Temperatur"):
        st.markdown("Körpertemperatur bei Aufnahme (in °C).")

    with st.expander("💨 Atemfrequenz"):
        st.markdown("Anzahl der Atemzüge pro Minute bei Aufnahme.")

    with st.expander("🩸 Blutzucker"):
        st.markdown("Gemessener Blutzuckerwert bei Aufnahme (mg/dL oder mmol/L).")

    with st.expander("🫁 Sauerstoffsättigung"):
        st.markdown("Sauerstoffsättigung im Blut bei Aufnahme (in %).")


with tab2:
    with st.expander("🆔 Fallnummer"):
        st.markdown("Eindeutige Kennung des Falls im Krankenhausinformationssystem.")

    with st.expander("📅 Vorstationäre Aufnahme"):
        st.markdown("Datum der vorstationären Aufnahme, falls vorhanden.")

    with st.expander("🏥 Aufnahme"):
        st.markdown("Datum der stationären Aufnahme des Patienten.")

    with st.expander("📤 Entlassung"):
        st.markdown("Datum der Entlassung des Patienten aus der stationären Behandlung.")

    with st.expander("🔑 Schlüssel"):
        st.markdown("Kodierungsschlüssel für die Diagnose oder Prozedur gemäß Katalog.")

    with st.expander("📚 Kürzel Diagnosenkatalog"):
        st.markdown("Abkürzung des verwendeten Diagnosenkatalogs (z. B. ICD-10).")

    with st.expander("🩺 Diagnose"):
        st.markdown("Diagnose, die im Rahmen des Falls dokumentiert wurde.")

    with st.expander("🔠 Kürzel"):
        st.markdown("Abkürzung oder Code der Diagnose oder Prozedur.")

    with st.expander("📅 Festgestellt am"):
        st.markdown("Datum, an dem die Diagnose festgestellt wurde.")

    with st.expander("🔢 Schlüssel-Nr."):
        st.markdown("Nummer des Kodierungsschlüssels für die Diagnose oder Prozedur.")

    with st.expander("📘 Kürzel Prozedurenkatalog"):
        st.markdown("Abkürzung des verwendeten Prozedurenkatalogs (z. B. OPS).")

    with st.expander("🛠️ Prozedur"):
        st.markdown("Durchgeführte medizinische Maßnahme oder Operation.")

    with st.expander("🏥 OP-Bezug"):
        st.markdown("Gibt an, ob die Prozedur im Rahmen einer Operation durchgeführt wurde.")

    with st.expander("📅 Durchgeführt am"):
        st.markdown("Datum, an dem die Prozedur durchgeführt wurde.")

    with st.expander("📖 Langbezeichnung Diagnosenkatalog"):
        st.markdown("Ausgeschriebene Bezeichnung der Diagnose gemäß Katalog.")

    with st.expander("📌 Diagnoseart"):
        st.markdown("Art der Diagnose (z. B. Hauptdiagnose, Nebendiagnose, Aufnahmegrund).")
            

with tab3:
    st.markdown("""  """)
    with st.expander("🆔 Fallnummer"):
        st.markdown("Eindeutige Kennung des Falls im Krankenhausinformationssystem.")
    with st.expander("🧍 Patienten-ID"):
        st.markdown("Anonymisierte ID zur Identifikation des Patienten.")
    with st.expander("📅 Aufn.datum"):
        st.markdown("Datum, an dem der Laborbefund angefordert wurde.")
    with st.expander("🧾 Liste an Befunden (ja/Nein)"):
        st.markdown("Gibt an, ob für den Fall Laborbefunde vorliegen.")

with tab4:
    st.markdown("""
    """)
    with st.expander("🆔 Fallnummer"):
        st.markdown("Eindeutige Kennung des Falls im Krankenhausinformationssystem.")

    with st.expander("🧍 Patienten-ID"):
        st.markdown("Anonymisierte ID zur Identifikation des Patienten.")

    with st.expander("📅 Aufn.datum"):
        st.markdown("Datum der Aufnahme des Patienten in die Einrichtung.")

    with st.expander("🧪 Befunddatum"):
        st.markdown("Datum, an dem der Laborbefund erstellt wurde.")

    with st.expander("🔬 Befund"):
        st.markdown("Bezeichnung des untersuchten Laborparameters.")

    with st.expander("📊 Befundwert"):
        st.markdown("Gemessener Wert des Laborparameters.")

    with st.expander("⚖️ Einheit"):
        st.markdown("Einheit, in der der Befundwert angegeben ist (z. B. mg/dL, mmol/L).")

    with st.expander("📝 Befundtext"):
        st.markdown("Zusätzlicher Freitext oder Kommentar zum Befund.")

    with st.expander("⚠️ Abnorm"):
        st.markdown("Kennzeichnung, ob der Befund außerhalb des Referenzbereichs liegt.")

    with st.expander("📏 Referenzbereich"):
        st.markdown("Normalbereich für den jeweiligen Laborparameter zur Bewertung des Befundwerts.")

    
            
# Weitere Felder hier...
st.markdown("## Datenschutz")
st.write("")
st.markdown("""
<div style="background-color: #ffffff; padding: 40px 60px; border-radius: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
    <p style="font-size: 18px; line-height: 1.8; color: #333;">
        Diese Anwendung verarbeitet <strong>klinische Daten</strong>, die zwar <strong>anonymisiert</strong> wurden, aber dennoch als <strong>hoch sensibel</strong> gelten.<br>
        Die Nutzung dieser Daten erfolgt ausschließlich im Rahmen des Projekts <strong>Agathon 2025</strong> und unterliegt strengen Datenschutzrichtlinien.
        <br><br>
        <strong>Wichtige Hinweise:</strong><br>
        🔒 Eine <strong>Veröffentlichung</strong> der Daten außerhalb des Projektrahmens ist <strong>nicht gestattet</strong>.<br>
        🛑 Jegliche <strong>private Nutzung</strong> oder Weitergabe – insbesondere außerhalb von Agathon 2025 – ist <strong>strikt untersagt</strong>.<br>
        ✅ Alle Daten wurden gemäß geltender Datenschutzvorgaben pseudonymisiert und technisch gesichert.
        <br><br>
        Bitte beachte: Die Einhaltung dieser Richtlinien ist Voraussetzung für die Nutzung der Anwendung und den verantwortungsvollen Umgang mit Gesundheitsdaten.
    </p>
</div>
""", unsafe_allow_html=True)
