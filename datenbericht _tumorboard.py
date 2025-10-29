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
    page_title="Agathon_Tumorboard",
    layout="wide"
)


st.markdown("""
    <style>
            
        
        

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




            
        /* Hintergrund und Schriftfarbe für die gesamte App */
        body, .stApp {
            background-color: #001f3f;
            color: white;
        }

        /* Header-Bereich anpassen */
        header[data-testid="stHeader"] {
            background-color: #003366 !important;
            color: white !important;
        }

        /* Überschriften und Text */
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

        /* Hintergrund für h2-Überschriften */
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
st.title("Agathon 2025 - Tumorboard")
st.write("")




st.markdown("""
    <div style="padding: 40px 60px; background-color: #ffffff; border-radius: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
        <h2 style="color: #003366; font-size: 32px; margin-bottom: 20px; background-color: #ffffff; padding: 10px 20px; border-radius: 8px;">
            Willkommen im Dashboard für die Aufgabe <em>'Tumorboard 2.0'</em> des Agathons 2025
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

with st.expander("### Datensatz - Tumorboard"):
    st.markdown("""

    Die Laborwertdaten enthalten alle dokumentierten Befunde, die im Rahmen der stationären oder notfallmäßigen Versorgung erhoben wurden.  
    Sie bilden die Grundlage für medizinische Entscheidungen, Verlaufskontrollen und diagnostische Einschätzungen im Projekt **Agathon 2025**
    """)

    with st.expander("Fallnummer"):
        st.markdown("Eindeutige Kennung des Falls im Krankenhausinformationssystem.")
        st.image(r"C:\Users\Magnus.Senfter\OneDrive - AGAPLESION gAG\Dokumente\Projects\Agathon\Dashboards\plots\Fallnummer_haeufigkeit_mit_nan.png",  use_container_width=True)

    with st.expander("Geschlecht"):
        st.markdown("Geschlecht des Patienten.")
        st.image(r"C:\Users\Magnus.Senfter\OneDrive - AGAPLESION gAG\Dokumente\Projects\Agathon\Dashboards\plots\G_haeufigkeit_mit_nan.png",  use_container_width=True)

    with st.expander("Datum"):
        st.markdown("Datum an dem die Tumorkonferenz durchgeführt wird")

    with st.expander("Procedere"):
        st.markdown("Geplantes Vorgehen oder Behandlungsschritte (z. B. OP, Chemotherapie, Nachsorge). Enthält oft Freitext mit hoher Variabilität.")
        st.markdown("Beispiel: 'Es zeigt sich ein Lokalprogress in der Leber. Im Sinne einer Oligoprogression ergeht die Empfehlung zur Lokaltherapie der Leber und zur Fortführung der subkutanen Therapie. Allgemeinchirurgische Vorstellung zur Beratung bezüglich Resektion der Lebermetastase, alternativ lokal ablatives Verfahren, wobei aufgrund der Möglichkeit einer erneuten Histologiegewinnung und Tezeptorstatustestung eine OP präferiert wird.'")

    with st.expander("Vorst AdHoct"):
        st.markdown("Kennzeichnet, ob die Vorstellung des Patienten im Tumorboard ad hoc erfolgt ist, also ungeplant und kurzfristig (z. B. bei dringendem Therapiebedarf oder Notfall).")
        st.image(r"C:\Users\Magnus.Senfter\OneDrive - AGAPLESION gAG\Dokumente\Projects\Agathon\Dashboards\plots\Vorst AdHoc_haeufigkeit_mit_nan.png",  use_container_width=True)
    
    with st.expander("Vorst Elektiv"):
        st.markdown("Kennzeichnet, ob die Vorstellung im Tumorboard elektiv erfolgt ist, also geplant und regulär im Rahmen der üblichen Abläufe (z. B. nach Diagnosestellung oder vor Therapieentscheidung).")
        st.image(r"C:\Users\Magnus.Senfter\OneDrive - AGAPLESION gAG\Dokumente\Projects\Agathon\Dashboards\plots\Vorst Elektiv_haeufigkeit_mit_nan.png",  use_container_width=True)

    with st.expander("Tumordiagnose"):
        st.markdown("Hauptdiagnose des Tumors (z. B. Mammakarzinom). Grundlage für Therapieentscheidungen.")
        st.markdown("Beispiel: '\m1Mammakarzinom links, ED 08/2024 \y:551\Stadium bei Erstdiagnose: \m0\c:FF\  \c:-\cT1c, cN0, M0, G \m1Histologie:\m0 Mammakarzinom Typ NST, G2, ER 90%, PR 70%, Her2neu 1+, Ki-67 5%'")

    with st.expander("Histo Zyto"):
        st.markdown("Histologische oder zytologische Befunde (z. B. Tumorgrading, Zelltyp). Sehr wichtig für die Klassifikation des Tumors.")

    with st.expander("Tumoranamnese"):
        st.markdown("Angaben zur Tumorvorgeschichte (z. B. frühere Tumoren, Rezidive). Hilft bei Risikoeinschätzung.")

    with st.expander("Bildgebung"):
        st.markdown("Ergebnisse bildgebender Verfahren (CT, MRT, PET). Enthält oft Freitext mit Befundbeschreibung.")

    with st.expander("Staging Klin cT"):
        st.markdown("Normalbereich für den jeweiligen Laborparameter zur Bewertung des Befundwerts.")
        st.image(r"C:\Users\Magnus.Senfter\OneDrive - AGAPLESION gAG\Dokumente\Projects\Agathon\Dashboards\plots\Staging Klin cT_haeufigkeit_mit_nan.png",  use_container_width=True)

    with st.expander("Staging Klin M"):
        st.markdown("Normalbereich für den jeweiligen Laborparameter zur Bewertung des Befundwerts.")
        st.image(r"C:\Users\Magnus.Senfter\OneDrive - AGAPLESION gAG\Dokumente\Projects\Agathon\Dashboards\plots\Staging Klin M_haeufigkeit_mit_nan.png",  use_container_width=True)

    with st.expander("Staging Klin N"):
        st.markdown("Normalbereich für den jeweiligen Laborparameter zur Bewertung des Befundwerts.")
        st.image(r"C:\Users\Magnus.Senfter\OneDrive - AGAPLESION gAG\Dokumente\Projects\Agathon\Dashboards\plots\Staging Klin N_haeufigkeit_mit_nan.png",  use_container_width=True)

    with st.expander("Staging Klin UICC"):
        st.markdown("Normalbereich für den jeweiligen Laborparameter zur Bewertung des Befundwerts.")
        st.image(r"C:\Users\Magnus.Senfter\OneDrive - AGAPLESION gAG\Dokumente\Projects\Agathon\Dashboards\plots\Staging Klin UICC_haeufigkeit_mit_nan.png",  use_container_width=True)

    with st.expander("Staging Path M"):
        st.markdown("Kennzeichnung, ob der Befund außerhalb des Referenzbereichs liegt.")
        st.image(r"C:\Users\Magnus.Senfter\OneDrive - AGAPLESION gAG\Dokumente\Projects\Agathon\Dashboards\plots\Staging Path M_haeufigkeit_mit_nan.png",  use_container_width=True)

    with st.expander("Staging Path N"):
        st.markdown("Normalbereich für den jeweiligen Laborparameter zur Bewertung des Befundwerts.")
        st.image(r"C:\Users\Magnus.Senfter\OneDrive - AGAPLESION gAG\Dokumente\Projects\Agathon\Dashboards\plots\Staging Path N_haeufigkeit_mit_nan.png",  use_container_width=True)

    with st.expander("Staging Path pT"):
        st.markdown("Normalbereich für den jeweiligen Laborparameter zur Bewertung des Befundwerts.")
        st.image(r"C:\Users\Magnus.Senfter\OneDrive - AGAPLESION gAG\Dokumente\Projects\Agathon\Dashboards\plots\Staging Path pT_haeufigkeit_mit_nan.png", use_container_width=True)

    with st.expander("Staging Path UICC"):
        st.markdown("Normalbereich für den jeweiligen Laborparameter zur Bewertung des Befundwerts.")
        st.image(r"C:\Users\Magnus.Senfter\OneDrive - AGAPLESION gAG\Dokumente\Projects\Agathon\Dashboards\plots\Staging Path UICC_haeufigkeit_mit_nan.png",  use_container_width=True)

    with st.expander("Nebendiagnosen"):
        st.markdown("Weitere Diagnosen neben der Hauptdiagnose (z. B. Diabetes, Hypertonie).")

    with st.expander("bisher Therapie"):
        st.markdown("Bisher durchgeführte Therapien (z. B. OP, Chemo, Bestrahlung). Enthält oft Freitext.")

    with st.expander("Fragestellung"):
        st.markdown("Bisher durchgeführte Therapien (z. B. OP, Chemo, Bestrahlung). Enthält oft Freitext.")

    with st.expander("kurativ"):
        st.markdown("Bisher durchgeführte Therapien (z. B. OP, Chemo, Bestrahlung). Enthält oft Freitext.")
        st.image(r"C:\Users\Magnus.Senfter\OneDrive - AGAPLESION gAG\Dokumente\Projects\Agathon\Dashboards\plots\kurativ_haeufigkeit_mit_nan.png",  use_container_width=True)

    with st.expander("palliativ"):
        st.markdown("Bisher durchgeführte Therapien (z. B. OP, Chemo, Bestrahlung). Enthält oft Freitext.")
        st.image(r"C:\Users\Magnus.Senfter\OneDrive - AGAPLESION gAG\Dokumente\Projects\Agathon\Dashboards\plots\palliativ_haeufigkeit_mit_nan.png",  use_container_width=True)

    with st.expander("pall Anbindung"):
        st.markdown("Bisher durchgeführte Therapien (z. B. OP, Chemo, Bestrahlung). Enthält oft Freitext.")
        st.image(r"C:\Users\Magnus.Senfter\OneDrive - AGAPLESION gAG\Dokumente\Projects\Agathon\Dashboards\plots\pall Anbindung_haeufigkeit_mit_nan.png",  use_container_width=True)

    with st.expander("Alter"):
        st.markdown("Alter des Patienten zum Zeitpunkt der Aufnahme oder zum Zeitpunkt der Tumorboard-Dokumentation. Dieses Feld ist relevant für die Risikoeinschätzung, Therapieplanung und statistische Auswertungen.")
        st.image(r"C:\Users\Magnus.Senfter\OneDrive - AGAPLESION gAG\Dokumente\Projects\Agathon\Dashboards\plots\Alter_haeufigkeit_mit_nan.png", use_container_width=True)


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