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
            
         /* Headerbereich */
        .custom-header {
            background-color: #00264d; /* Dunkelblau */
            color: white;
            padding: 40px 60px;
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            border-radius: 0 0 12px 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            letter-spacing: 1px;
          }
            
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
        
        
        
        /* Tabs zentrieren und gestalten */
        div[data-testid="stTabs"] {
            display: flex;
            justify-content: center;
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

        /* Expander mit fester Breite */
        div[data-testid="stExpander"] {
            width: 1000px; /* feste Breite für geschlossen und geöffnet */
            border: 2px solid black;
            border-radius: 8px;
            margin: auto; /* zentriert */
        }

        /* Inhalt des Expanders */
        .streamlit-expanderContent {
            width: 100%; /* passt sich der Expander-Breite an */
        }

        /* Hintergrundfarbe bei geöffnetem Zustand */
        div[data-testid="stExpander"] > details[open] {
            background-color: #004080;
            color: white;
            padding: 15px;
        }

        /* Titel des Expanders */
        div[data-testid="stExpander"] > details > summary {
            font-size: 20px;
            background-color: #003366;
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
image = Image.open("logo/AGAthon.png")
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

st.markdown("## 🔬 AI LabCheck in der Notaufnahme")
st.write("")
st.markdown("""
    <div style="background-color: #ffffff; padding: 40px 60px; border-radius: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
        <h3 style="color: #003366;">Aufgabenbeschreibung</h3>
        <p style="font-size: 18px; line-height: 1.8; color: #333;">
            Die eingewiesene Verdachtsdiagnose liefert einen ersten Anhaltspunkt für den möglichen Verlauf der Patient:innen. Allerdings kann sich die Diagnose im Verlauf ändern, wenn sich Verdachtsmomente nicht bestätigen oder andere Ursachen gefunden werden.
            Labore werden oft auf Basis der Verdachtsdiagnose beauftragt, doch manchmal reichen die Werte nicht aus und müssen nachgefordert werden.
            Das ist problematisch, da die Laborergebnisse den weiteren Behandlungsverlauf bestimmen. Es kann auch passieren, dass Labore beauftragt werden, die später durch die finale Diagnose nicht abgedeckt sind, was zu finanziellen Nachteilen führen kann, da die Krankenkassen diese Kosten nicht übernehmen. Eine Anwendung sollte daher sicherstellen, dass ausreichend Laborparameter beauftragt werden, um Verzögerungen in der Behandlung zu vermeiden, und gleichzeitig das Risiko von nicht gedeckten Laborkosten minimieren.
            Die besondere Schwierigkeit liegt darin, dass mit sehr wenigen Informationen eine Entscheidung getroffen werden soll, bei der möglichst wenig Fehler gemacht werden soll. 
        </p>
    </div>
""", unsafe_allow_html=True)

st.write("")
st.markdown("### 🧠 Hintergrundinformationen")
st.write("")

# Stil für die weiße Box (Card)
st.markdown("""
    <style>
    .white-box {
        background-color: #ffffff;
        padding: 40px 60px;
        border-radius: 16px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        font-size: 18px;
        line-height: 1.8;
        color: #333333;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Text in die Box setzen
st.markdown("""
<div class="white-box">
Für die Entwicklung der Anwendung stehen **vier strukturierte Datensätze** aus dem Krankenhausinformationssystem (KIS) zur Verfügung:
            
- **MTS (Manchester Triage System):** enthält Informationen zur Ersteinschätzung der Patient:innen in der Notaufnahme.  
- **Diagnose:** dokumentiert die Verdachtsdiagnosen und den Diagnoseverlauf.  
- **Laboranforderungen:** zeigt, welche Laborparameter zu welchem Zeitpunkt angefordert und wann sie gemessen wurden. 
- **Laborwerte:** enthält die Ergebnisse der durchgeführten Tests inklusive Zeitstempel.  

### 🎯 Mögliche Ziele der Anwendung
Entwicklung einer **KI-gestützten Anwendung**, die:
1. den klinischen Verlauf und die Vitalparameter der Patient:innen übersichtlich darstellt,  
2. basierend auf MTS-Kategorie und Verdachtsdiagnose sinnvolle Laboranforderungen vorschlägt,  
3. die voraussichtliche Dauer bis zum Eintreffen der Laborergebnisse prognostiziert, und  
4. potenzielle Lücken oder Überanforderungen erkennt, um medizinische Qualität und ökonomische Effizienz zu verbessern.  


</div>
""", unsafe_allow_html=True)

with open("plots/zeitstrahl_interaktiv.html", "r", encoding="utf-8") as f:
    html = f.read()
st.markdown("### Beispielhafter Zeitstrahl einer Fallnummer")
st.components.v1.html(html, height=500, scrolling=True)

st.markdown("## 📁Daten für LabAI Check")

st.write("")
# Tabs erstellen
tab1, tab2, tab3, tab4 = st.tabs(["📊 Manchester Triage System", "📋 Diagnosen", "⚙️ Laboranforderungen","🧪 Laborwerte",])

            
st.write("")
with tab1:
    with st.expander("🆔 ﻿Patienten ID"):
        st.markdown("Die Patienten-ID ist eine eindeutige Kennung, die jedem Patienten im Krankenhausinformationssystem zugewiesen wird. Sie ermöglicht die zuverlässige Zuordnung aller medizinischen Informationen zu einer Person.")

    with st.expander("🆔 Fallnummer"):
        st.markdown("Die Fallnummer identifiziert einen konkreten Behandlungsfall eindeutig. Sie ist besonders wichtig für die Dokumentation und Abrechnung medizinischer Leistungen.")

    with st.expander("🎂 Alter"):
        st.markdown("Das Alter des Patienten zum Zeitpunkt der Aufnahme kann wichtige Hinweise auf Risikofaktoren und typische Krankheitsverläufe geben. Es wird meist automatisch aus dem Geburtsdatum berechnet.")

    with st.expander("⚧ Geschlecht"):
        st.markdown("Das Geschlecht des Patienten wird zur medizinischen Dokumentation und für statistische Auswertungen erfasst. Es kann auch Einfluss auf Diagnostik und Therapie haben.")

    with st.expander("📅 Admin. Fall-Aufnahmedatum"):
        st.markdown("Dieses Datum markiert den Beginn des administrativen Falls im Krankenhausinformationssystem. Es dient als Referenzpunkt für die Dauer und Organisation des Aufenthalts.")

    with st.expander("📌 Fallstatus"):
        st.markdown("Der Fallstatus zeigt an, ob ein Fall noch offen, bereits abgeschlossen oder archiviert ist. Er hilft bei der Übersicht über den Bearbeitungsstand im klinischen Prozess.")

    with st.expander("🏥 Aufnahme ZNA"):
        st.markdown("Gibt an, ob die Aufnahme über die Zentrale Notaufnahme erfolgt ist. Dies kann auf eine akute Versorgungssituation hinweisen und ist relevant für die Fallklassifikation.")

    with st.expander("📆 Wochentag"):
        st.markdown("Der Wochentag der Aufnahme kann für Analysen zur Auslastung und Planung von Ressourcen genutzt werden. Er erlaubt auch Rückschlüsse auf typische Muster im Patientenaufkommen.")

    with st.expander("📈 Schmerzskala-Einstufung"):
        st.markdown("Die Schmerzskala ist eine subjektive Einschätzung des Schmerzniveaus durch den Patienten. Sie hilft bei der Priorisierung und Auswahl geeigneter Schmerztherapien.")

    with st.expander("📊 MTS Diagramm"):
        st.markdown("Das MTS-Diagramm visualisiert die Ersteinschätzung nach dem Manchester Triage System. Es zeigt die Dringlichkeit und unterstützt die strukturierte Notfallversorgung.")

    with st.expander("📍 Indikator"):
        st.markdown("Ein Indikator ist ein spezifischer Marker zur Einschätzung des klinischen Zustands. Er kann z. B. auf eine bestimmte Symptomatik oder Risikogruppe hinweisen.")

    with st.expander("📋 MTS Einstufung"):
        st.markdown("Die MTS-Einstufung legt fest, wie dringend ein Patient behandelt werden muss. Sie basiert auf definierten Kriterien und unterstützt die Priorisierung in der Notaufnahme.")

    with st.expander("🩸 BG"):
        st.markdown("Die Blutgruppe des Patienten ist relevant für Transfusionen und Notfallmaßnahmen. Sie wird, sofern bekannt, dokumentiert und kann lebensrettend sein.")

    with st.expander("📄 Einweisung"):
        st.markdown("Die Art der Einweisung gibt an, wie der Patient ins Krankenhaus gelangt ist – z. B. durch Hausarzt oder Rettungsdienst. Dies kann Hinweise auf die Dringlichkeit geben.")

    with st.expander("🚑 Transport"):
        st.markdown("Der Transportweg zur Klinik (z. B. Rettungswagen, selbstständig) liefert Informationen über die Mobilität und den Zustand des Patienten bei Aufnahme.")

    with st.expander("⏰ Entlassungszeit"):
        st.markdown("Die Uhrzeit der Entlassung dokumentiert den Zeitpunkt, zu dem der Patient die Notaufnahmeverlassen hat.")

    with st.expander("📅 Admin. Fall-Entlassdatum"):
        st.markdown("Das administrative Entlassdatum markiert das Ende des Falls im Krankenhausinformationssystem. Es dient als Basis für statistische und organisatorische Auswertungen.")

    with st.expander("🏁 Entlassung Ambulant (Ja/Nein)"):
        st.markdown("Dieses Merkmal zeigt, ob der Patient ambulant entlassen wurde. Es ist relevant für die Nachsorgeplanung und die Abgrenzung stationärer Leistungen.")

    with st.expander("📄 Entlassung"):
        st.markdown("Die Art der Entlassung beschreibt, wohin der Patient nach dem Aufenthalt geht – z. B. nach Hause oder in eine andere Einrichtung. Sie beeinflusst die weitere Versorgung.")

    with st.expander("📄 LeftWithoutBeingSeen"):
        st.markdown("Kennzeichnet Fälle, in denen Patienten die Klinik verlassen haben, ohne ärztlich gesehen worden zu sein. Dies ist ein wichtiger Qualitätsindikator in der Notaufnahme.")

    with st.expander("📊 Gesamtaufenthaltsdauer"):
        st.markdown("Die Gesamtaufenthaltsdauer gibt an, wie viele Tage der Patient im Krankenhaus war. Sie ist zentral für die Ressourcenplanung und Leistungsabrechnung.")

    with st.expander("🚨 Notfall- oder Elektivpatient"):
        st.markdown("Dieses Merkmal unterscheidet zwischen ungeplanten Notfällen und geplanten Aufnahmen. Es beeinflusst die Organisation und Priorisierung der Versorgung.")

    with st.expander("🩺 Blutdruck"):
        st.markdown("Der Blutdruck bei Aufnahme ist ein Basiswert zur Einschätzung des Kreislaufzustands. Abweichungen können auf akute oder chronische Erkrankungen hinweisen.")

    with st.expander("❤️ Puls"):
        st.markdown("Die Herzfrequenz bei Aufnahme zeigt die aktuelle Belastung des Herz-Kreislauf-Systems. Sie ist ein wichtiger Vitalparameter in der Erstuntersuchung.")

    with st.expander("🌡️ Temperatur"):
        st.markdown("Die Körpertemperatur bei Aufnahme kann Hinweise auf Infektionen oder andere Erkrankungen geben. Sie ist ein Standardwert in der klinischen Basisdiagnostik.")

    with st.expander("💨 Atemfrequenz"):
        st.markdown("Die Atemfrequenz ist ein Indikator für die respiratorische Stabilität. Abweichungen können auf Atemnot oder metabolische Störungen hinweisen.")

    with st.expander("🩸 Blutzucker"):
        st.markdown("Der Blutzuckerwert bei Aufnahme ist wichtig zur Erkennung von Diabetes oder akuten Stoffwechselentgleisungen. Er wird oft routinemäßig erhoben.")

    with st.expander("🫁 Sauerstoffsättigung"):
        st.markdown("Die Sauerstoffsättigung zeigt, wie gut der Körper mit Sauerstoff versorgt ist. Sie ist essenziell zur Beurteilung der Atemfunktion und bei Notfällen.")


with tab2:
    with st.expander("🆔 Fallnummer"):
        st.markdown("Die Fallnummer ist eine eindeutige Kennung für den konkreten stationären Aufenthalt eines Patienten. Sie dient der Zuordnung aller medizinischen und administrativen Daten zu diesem Fall.")

    with st.expander("📅 Vorstationäre Aufnahme"):
        st.markdown("Das Datum der vorstationären Aufnahme zeigt, wann der Patient erstmals im Rahmen dieses Falls Kontakt zur Klinik hatte. Es kann z. B. bei ambulanten Voruntersuchungen oder präoperativen Gesprächen relevant sein.")

    with st.expander("🏥 Aufnahme"):
        st.markdown("Das Aufnahmedatum markiert den Beginn der stationären Behandlung. Es ist entscheidend für die Berechnung der Aufenthaltsdauer und die Abrechnung stationärer Leistungen.")

    with st.expander("📤 Entlassung"):
        st.markdown("Das Entlassungsdatum zeigt, wann der Patient die stationäre Versorgung beendet hat. Es bildet zusammen mit dem Aufnahmedatum die Grundlage für die Aufenthaltsstatistik.")

    with st.expander("🔑 Schlüssel"):
        st.markdown("Der Schlüssel ist ein standardisierter Code für Diagnosen oder Prozeduren gemäß einem offiziellen Katalog. Er ermöglicht eine einheitliche Dokumentation und Abrechnung im Gesundheitssystem.")

    with st.expander("📚 Kürzel Diagnosenkatalog"):
        st.markdown("Das Kürzel gibt an, welcher Diagnosenkatalog verwendet wurde – z. B. ICD-10. Dies ist wichtig für die Interpretation der Schlüssel und die internationale Vergleichbarkeit.")

    with st.expander("🩺 Diagnose"):
        st.markdown("Die Diagnose beschreibt die medizinische Einschätzung des Krankheitsbildes im Rahmen des Falls. Sie ist zentral für die Therapieplanung und die klinische Dokumentation.")

    with st.expander("🔠 Kürzel"):
        st.markdown("Das Kürzel ist die kodierte Form der Diagnose oder Prozedur, meist in Form eines alphanumerischen Codes. Es dient der standardisierten Erfassung und Weiterverarbeitung.")

    with st.expander("📅 Festgestellt am"):
        st.markdown("Dieses Datum zeigt, wann die jeweilige Diagnose im Verlauf des Falls festgestellt wurde. Es kann für die Verlaufskontrolle und medizinische Bewertung von Bedeutung sein.")

    with st.expander("🔢 Schlüssel-Nr."):
        st.markdown("Die Schlüsselnummer ist eine numerische Kennung innerhalb des Kodierungssystems. Sie hilft bei der eindeutigen Identifikation und Zuordnung von Diagnosen oder Prozeduren.")

    with st.expander("📘 Kürzel Prozedurenkatalog"):
        st.markdown("Das Kürzel bezeichnet den verwendeten Prozedurenkatalog, z. B. OPS in Deutschland. Es ist notwendig, um die Prozedurenschlüssel korrekt zu interpretieren.")

    with st.expander("🛠️ Prozedur"):
        st.markdown("Die Prozedur beschreibt eine durchgeführte medizinische Maßnahme, z. B. eine Operation oder diagnostische Untersuchung. Sie ist ein zentraler Bestandteil der Leistungsdokumentation.")

    with st.expander("🏥 OP-Bezug"):
        st.markdown("Dieses Merkmal zeigt, ob die dokumentierte Prozedur im Rahmen einer Operation durchgeführt wurde. Es ist relevant für die OP-Planung und die Abrechnung operativer Leistungen.")

    with st.expander("📅 Durchgeführt am"):
        st.markdown("Das Datum der Durchführung gibt an, wann die medizinische Maßnahme tatsächlich stattgefunden hat. Es ist wichtig für die zeitliche Einordnung im Behandlungsverlauf.")

    with st.expander("📖 Langbezeichnung Diagnosenkatalog"):
        st.markdown("Die Langbezeichnung liefert die ausgeschriebene Form der Diagnose gemäß dem verwendeten Katalog. Sie erleichtert das Verständnis und die Kommunikation im klinischen Alltag.")

    with st.expander("📌 Diagnoseart"):
        st.markdown("Die Diagnoseart klassifiziert die Rolle der Diagnose im Fall, z. B. als Hauptdiagnose oder Nebendiagnose. Diese Unterscheidung ist wichtig für die medizinische Bewertung und Abrechnung.")
            

with tab3:
    with st.expander("🆔 Fall_Nr"):
        st.markdown("Die Fallnummer ist die eindeutige Kennung des stationären Aufenthalts im Krankenhausinformationssystem. Sie verknüpft alle Laboraufträge und Befunde mit dem jeweiligen Fall.")

    with st.expander("🆔 AuftrNr_Lab"):
        st.markdown("Die Auftragsnummer identifiziert den spezifischen Laborauftrag eindeutig. Sie dient der Nachverfolgung und Zuordnung von Analysen innerhalb eines Falls.")

    with st.expander("🧪 Pr_Bez"):
        st.markdown("Die Parameter-Bezeichnung beschreibt die Art der angeforderten Laboruntersuchung, z. B. Blutbild EDTA. Sie ist wichtig für die Interpretation der Ergebnisse.")

    with st.expander("🧪 Leistung_Kurz"):
        st.markdown("Die Kurzbezeichnung der Leistung gibt eine komprimierte Darstellung der angeforderten Untersuchung. Sie erleichtert die schnelle Übersicht im Laborbericht.")

    with st.expander("🧪 Leistungs_Bez"):
        st.markdown("Die Leistungsbezeichnung ist die vollständige Beschreibung der angeforderten Laborleistung. Sie wird für die medizinische Dokumentation und Abrechnung genutzt.")

    with st.expander("📊 NFST"):
        st.markdown("""
    **NFST** ist ein Prioritätsindikator für Laboraufträge. Er steuert die Dringlichkeit und Bearbeitungsreihenfolge im Laborprozess.

    **Kürzel und Bedeutung:**
    - **N** = Notfall (sofortige Bearbeitung)
    - **E** = Eilt (Notfall, Bearbeitung innerhalb von 2 Stunden)
    - **Z** = Zugang (Routine, Abnahme sofort)
    - **R** = Routinebetrieb (normale Bearbeitung)
    - **L** = Lebensgefahr (höchste Priorität)
    """)

    with st.expander("📅 Anl_DatumZeit"):
        st.markdown("Das Anlagedatum zeigt, wann der Laborauftrag im System erfasst wurde. Es ist wichtig für die zeitliche Einordnung der Diagnostik und die Prozesskontrolle.")

    with st.expander("📅 Wert_DatumZeit"):
        st.markdown("Dieses Datum gibt an, wann die Laborwerte gemessen oder dokumentiert wurden. Es dient der Verlaufskontrolle und Qualitätssicherung.")

    with st.expander("📅 FG_DatumZeit"):
        st.markdown("Das Freigabedatum zeigt, wann der Laborbefund abgeschlossen und freigegeben wurde. Es ist entscheidend für die klinische Weiterverarbeitung und Befundübermittlung.")

with tab4:
    with st.expander("🆔 Fallnummer"):
        st.markdown("Die Fallnummer identifiziert eindeutig den stationären Aufenthalt eines Patienten im Krankenhausinformationssystem. Sie verknüpft alle zugehörigen Laborbefunde und medizinischen Maßnahmen mit dem jeweiligen Fall.")

    with st.expander("🧪 Parameter"):
        st.markdown("Der Parameter beschreibt, welcher Laborwert untersucht wurde – z. B. Natrium, Kreatinin oder CRP. Er ist entscheidend für die medizinische Bewertung und Verlaufskontrolle.")

    with st.expander("📝 Ergebnis"):
        st.markdown("Das Ergebnis besteht aus dem gemessenen Wert und der zugehörigen Einheit des Laborparameters. Es bildet die Grundlage für die Interpretation im klinischen Kontext und wird mit Referenzbereichen verglichen.")

    with st.expander("🆔 Auftrag"):
        st.markdown("Das Auftragsdatum zeigt, wann die Laboruntersuchung angefordert wurde. Es hilft, den diagnostischen Verlauf zeitlich einzuordnen und ist relevant für die Dokumentation.")

    with st.expander("📊 Wert"):
        st.markdown("Der Wert ist die numerische Angabe des Messergebnisses, z. B. 5.2 oder 140. Er allein ist ohne die Einheit nicht interpretierbar und muss im Kontext medizinischer Normwerte betrachtet werden.")

    with st.expander("⚖️ Einheit"):
        st.markdown("Die Einheit gibt an, in welchem Maß der Laborwert gemessen wurde – z. B. mmol/L oder mg/dL. Sie ist essenziell für die korrekte Interpretation und Vergleichbarkeit der Ergebnisse.")
    
            
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
