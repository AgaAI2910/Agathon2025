import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import os

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
image = Image.open("logo/AGAthon.png")
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
        <h3 style="color: #003366;">📘 Tumorboard2.0-  – KI-gestützte Vorarbeit für Tumorkonferenzen</h3>
        <p style="font-size: 18px; line-height: 1.8; color: #333;">
            Die Tumorkonferenz ist ein zentrales Instrument in der Behandlung von Krebserkrankungen. 
            Besprochen werden jedoch nur die zuvor zusammengestellten Informationen. Da Patientenhistorien oft sehr umfangreich sind, kommt es häufig zu doppelten Einträgen oder fehlenden Angaben – beides erschwert die Festlegung der passenden Therapieoption.
        </p>
        <p style="font-size: 18px; line-height: 1.8; color: #333;">
            Ein KI-Tool soll hier unterstützen, indem es die Vorarbeit übernimmt. Der behandelnde Arzt müsste dann nur noch prüfen. 
            Das Tool soll insbesondere aufzeigen, welche Informationen fehlen und ggf. von anderen Behandler:innen angefordert werden müssen, oder welche Angaben veraltet und durch neuere ersetzt wurden.
        </p>
        <p style="font-size: 18px; line-height: 1.8; color: #333;">
            Eine Empfehlung zur weiteren Behandlung nach Leitlinien wäre der nächste Schritt. Häufig fehlt es an einer soliden Grundlage – für die klassischen „Dr. House“-Szenen, in denen fünf Ärzt:innen tagelang einen Fall analysieren, fehlt in der Realität schlicht die Zeit.
        </p>
        <p style="font-size: 18px; line-height: 1.8; color: #333;">
            Das Raussuchen relevanter Informationen ist eine klassische untergeordnete Aufgabe, die oft unterbrochen oder auf mehrere Personen verteilt wird. 
            Eine gute Vorarbeit ist entscheidend, denn ohne vollständige Informationen ist eine fundierte Entscheidungsfindung nicht möglich. 
            Besonders Lücken oder unschlüssige Ergebnisse stellen hier eine große Herausforderung dar.
        </p>
    </div>
""", unsafe_allow_html=True)
st.write("")

st.markdown("### Ablauf einer Tumorkonferenz")
st.markdown("""
<div style="background-color: #f9f9f9; padding: 30px 50px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
    <p style="font-size: 18px; line-height: 1.8; color: #333;">
        Tumorkonferenzen sind interdisziplinäre Besprechungen, bei denen Fachärzt:innen verschiedener Disziplinen gemeinsam über die optimale Therapie für Krebspatient:innen entscheiden. 
        Die Konferenzen finden regelmäßig statt und basieren auf zuvor zusammengestellten Patientendaten.
    </p>
    <ul style="font-size: 18px; line-height: 1.8; color: #333;">
        <li>Vorbereitung durch die fallführende Abteilung</li>
        <li>Zusammenstellung relevanter Befunde (Radiologie, Pathologie, Labor etc.)</li>
        <li><strong>Einladung relevanter Fachrichtungen</strong> basierend auf dem konkreten Fall (z. B. Chirurgie, Onkologie, Radiologie, Gynäkologie)</li>
        <li>Präsentation des Falls im Tumorboard</li>
        <li>Diskussion und Konsensfindung zur Therapieempfehlung basierend auf Leitlinien</li>
        <li>Dokumentation der Empfehlung im Tumorprotokoll</li>
    </ul>
    <p style="font-size: 18px; line-height: 1.8; color: #333;">
        Weitere relevante Dokumente für ein besseres Verständnis des Ablaufs eines Tumorboards sind hier zu finden:
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
        st.image("plots/Fallnummer_haeufigkeit_mit_nan.png",  use_container_width=True)

    with st.expander("Geschlecht"):
        st.markdown("Geschlecht des Patienten.")
        st.image("plots/G_haeufigkeit_mit_nan.png",  use_container_width=True)

    with st.expander("Datum"):
        st.markdown("Datum an dem die Tumorkonferenz durchgeführt wird")

    with st.expander("Procedere"):
        st.markdown("Geplantes Vorgehen oder Behandlungsschritte (z. B. OP, Chemotherapie, Nachsorge). Enthält oft Freitext mit hoher Variabilität.")
        st.markdown("Beispiel: 'Es zeigt sich ein Lokalprogress in der Leber. Im Sinne einer Oligoprogression ergeht die Empfehlung zur Lokaltherapie der Leber und zur Fortführung der subkutanen Therapie. Allgemeinchirurgische Vorstellung zur Beratung bezüglich Resektion der Lebermetastase, alternativ lokal ablatives Verfahren, wobei aufgrund der Möglichkeit einer erneuten Histologiegewinnung und Tezeptorstatustestung eine OP präferiert wird.'")

    with st.expander("Vorst AdHoct"):
        st.markdown("Kennzeichnet, ob die Vorstellung des Patienten im Tumorboard ad hoc erfolgt ist, also ungeplant und kurzfristig (z. B. bei dringendem Therapiebedarf oder Notfall).")
        st.image("plots/Vorst AdHoc_haeufigkeit_mit_nan.png",  use_container_width=True)
    
    with st.expander("Vorst Elektiv"):
        st.markdown("Kennzeichnet, ob die Vorstellung im Tumorboard elektiv erfolgt ist, also geplant und regulär im Rahmen der üblichen Abläufe (z. B. nach Diagnosestellung oder vor Therapieentscheidung).")
        st.image("plots/Vorst Elektiv_haeufigkeit_mit_nan.png",  use_container_width=True)

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
        st.image("plots/Staging Klin cT_haeufigkeit_mit_nan.png",  use_container_width=True)

    with st.expander("Staging Klin M"):
        st.markdown("Normalbereich für den jeweiligen Laborparameter zur Bewertung des Befundwerts.")
        st.image("plots/Staging Klin M_haeufigkeit_mit_nan.png",  use_container_width=True)

    with st.expander("Staging Klin N"):
        st.markdown("Normalbereich für den jeweiligen Laborparameter zur Bewertung des Befundwerts.")
        st.image("plots/Staging Klin N_haeufigkeit_mit_nan.png",  use_container_width=True)

    with st.expander("Staging Klin UICC"):
        st.markdown("Normalbereich für den jeweiligen Laborparameter zur Bewertung des Befundwerts.")
        st.image("plots/Staging Klin UICC_haeufigkeit_mit_nan.png",  use_container_width=True)

    with st.expander("Staging Path M"):
        st.markdown("Kennzeichnung, ob der Befund außerhalb des Referenzbereichs liegt.")
        st.image("plots/Staging Path M_haeufigkeit_mit_nan.png",  use_container_width=True)

    with st.expander("Staging Path N"):
        st.markdown("Normalbereich für den jeweiligen Laborparameter zur Bewertung des Befundwerts.")
        st.image("plots/Staging Path N_haeufigkeit_mit_nan.png",  use_container_width=True)

    with st.expander("Staging Path pT"):
        st.markdown("Normalbereich für den jeweiligen Laborparameter zur Bewertung des Befundwerts.")
        st.image("plots/Staging Path pT_haeufigkeit_mit_nan.png", use_container_width=True)

    with st.expander("Staging Path UICC"):
        st.markdown("Normalbereich für den jeweiligen Laborparameter zur Bewertung des Befundwerts.")
        st.image("plots/Staging Path UICC_haeufigkeit_mit_nan.png",  use_container_width=True)

    with st.expander("Nebendiagnosen"):
        st.markdown("Weitere Diagnosen neben der Hauptdiagnose (z. B. Diabetes, Hypertonie).")

    with st.expander("bisher Therapie"):
        st.markdown("Bisher durchgeführte Therapien (z. B. OP, Chemo, Bestrahlung). Enthält oft Freitext.")

    with st.expander("Fragestellung"):
        st.markdown("Bisher durchgeführte Therapien (z. B. OP, Chemo, Bestrahlung). Enthält oft Freitext.")

    with st.expander("kurativ"):
        st.markdown("Bisher durchgeführte Therapien (z. B. OP, Chemo, Bestrahlung). Enthält oft Freitext.")
        st.image("plots/kurativ_haeufigkeit_mit_nan.png",  use_container_width=True)

    with st.expander("palliativ"):
        st.markdown("Bisher durchgeführte Therapien (z. B. OP, Chemo, Bestrahlung). Enthält oft Freitext.")
        st.image("plots/palliativ_haeufigkeit_mit_nan.png",  use_container_width=True)

    with st.expander("pall Anbindung"):
        st.markdown("Bisher durchgeführte Therapien (z. B. OP, Chemo, Bestrahlung). Enthält oft Freitext.")
        st.image("plots/pall Anbindung_haeufigkeit_mit_nan.png",  use_container_width=True)

    with st.expander("Alter"):
        st.markdown("Alter des Patienten zum Zeitpunkt der Aufnahme oder zum Zeitpunkt der Tumorboard-Dokumentation. Dieses Feld ist relevant für die Risikoeinschätzung, Therapieplanung und statistische Auswertungen.")
        st.image("plots/Alter_haeufigkeit_mit_nan.png", use_container_width=True)


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