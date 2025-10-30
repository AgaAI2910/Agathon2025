import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image


from datetime import datetime, timedelta


# Seitenlayout konfigurieren

st.set_page_config(
    page_title="Agathon_Tumorboard",
    layout="wide"
)

# Automatisches Refresh alle 1 Sekunde


st.markdown("""
    <style>

        /* ================================
           App-Hintergrund und Grundfarben
        ================================== */
        body, .stApp {
            background-color: #001f3f;
            color: white;
        }

        header[data-testid="stHeader"] {
            background-color: #003366 !important;
            color: white !important;
        }

        h1, h2, h3, h4, h5, h6, p {
            color: white;
        }

        /* ================================
           Expander-Styling
        ================================== */
        div[data-testid="stExpander"] {
            border: 2px solid black;
            border-radius: 8px;
        }

        div[data-testid="stExpander"] > details[open] {
            background-color: #004080;
            color: white;
            padding: 15px;
        }

        div[data-testid="stExpander"] > details > summary {
            font-size: 20px;
            background-color: #003366;
            color: white;
            padding: 10px;
            border-radius: 8px;
        }

        div[data-testid="stExpander"] > details[open] > summary {
            background-color: #003366;
            color: #3399ff;
            font-size: 18px;
        }

        div[data-testid="stExpander"] > details[open] {
            color: #3399ff;
        }

        /* ================================
           Tabs
        ================================== */
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

        /* ================================
           Überschriften mit Hintergrund
        ================================== */
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

        /* =====================================
           Link-Button: zentriert & moderner Stil
        ====================================== */
        div[data-testid="stLinkButton"] {
            display: flex;
            justify-content: center;   /* Zentriert den Button horizontal */
            margin-top: 20px;
            margin-bottom: 20px;
        }

        div[data-testid="stLinkButton"] > a {
            width: 250px;  /* << Breite des Buttons hier anpassen */
            text-align: center;
            background: linear-gradient(180deg, #0066cc 0%, #004080 100%) !important;
            color: white !important;
            border: 2px solid #66b2ff !important;
            border-radius: 10px;
            padding: 12px 0;
            font-size: 20px;
            font-weight: 600;
            letter-spacing: 0.5px;
            text-decoration: none !important;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.4);
            transition: all 0.25s ease;
        }

        /* Hover-Effekt */
        div[data-testid="stLinkButton"] > a:hover {
            background: linear-gradient(180deg, #3399ff 0%, #0066cc 100%) !important;
            transform: translateY(-2px);
            box-shadow: 0px 6px 14px rgba(0, 0, 0, 0.6);
            border-color: #99ccff !important;
        }

        /* Klick-Feedback */
        div[data-testid="stLinkButton"] > a:active {
            transform: translateY(1px);
            box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.4);
        }

        /* Pulsieren zur Auffälligkeit */
        @keyframes pulseButton {
            0% { box-shadow: 0 0 0 0 rgba(51, 153, 255, 0.5); }
            70% { box-shadow: 0 0 0 10px rgba(51, 153, 255, 0); }
            100% { box-shadow: 0 0 0 0 rgba(51, 153, 255, 0); }
        }

        div[data-testid="stLinkButton"] > a {
            animation: pulseButton 3s infinite;
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

        .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 80vh; /* vertikal zentriert */
    }

    .headline {
        text-align: center;
        font-size: 26px;
        font-weight: 600;
        color: white;
        margin-bottom: 20px;
    }

    .countdown-box {
        font-family: 'Courier New', monospace;
        font-size: 64px;
        font-weight: 700;
        color: #ff3333;              /* Rot */
        background-color: #000;
        padding: 16px 36px;
        border-radius: 12px;
        letter-spacing: 4px;
        text-align: center;
        border: 2px solid #ff3333;
        box-shadow: 0 0 25px rgba(255, 0, 0, 0.6);
        text-shadow: 0 0 10px rgba(255, 0, 0, 0.8);
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


# Dein Button
st.link_button(
    "💡 Link Dokumente Tumorboard",
    url="https://github.com/AgaAI2910/Agathon2025/tree/main/Infos_Tumorboard",
    type="secondary",
    width='stretch'
)




st.write("")

with st.expander("### Informationen zum Datensatz"):
    st.markdown("""
    Die vorliegenden Daten enthalten strukturierte Tumorbögen, die im Rahmen der stationären oder notfallmäßigen Versorgung dokumentiert wurden.
    Diese Bögen erfassen detaillierte Informationen zur Tumordiagnose, zum Krankheitsverlauf sowie zu therapeutischen Maßnahmen. Sie sind ein zentraler Bestandteil der medizinischen Entscheidungsfindung im Projekt Agathon 2025.
    Ein besonderer Fokus liegt auf der Diagnose von Mammakarzinomen, die in einer Vielzahl der Fälle dokumentiert sind. Die Tumorbögen enthalten unter anderem folgende Merkmale:
    """)

    with st.expander("Fallnummer"):
        st.markdown("Eindeutige Kennung des Falls im Krankenhausinformationssystem. Teilweise gibt es mehrere Tumorbögen pro Fall.")
        st.image("plots/Fallnummer_haeufigkeit_mit_nan.png",  width='stretch')

    with st.expander("Geschlecht"):
        st.markdown("Geschlecht des Patienten.")
        st.image("plots/G_haeufigkeit_mit_nan.png",  width='stretch')

    with st.expander("Datum"):
        st.markdown("Datum an dem die Tumorkonferenz durchgeführt wird")

    with st.expander("Procedere"):
        st.markdown("Geplantes Vorgehen oder Behandlungsschritte (z. B. OP, Chemotherapie, Nachsorge). Enthält oft Freitext mit hoher Variabilität.")
        st.markdown("""Beispiel:
                     'Es zeigt sich ein Lokalprogress in der Leber. Im Sinne einer Oligoprogression ergeht die Empfehlung zur Lokaltherapie der Leber und zur Fortführung der subkutanen Therapie. 
                    Allgemeinchirurgische Vorstellung zur Beratung bezüglich Resektion der Lebermetastase, alternativ lokal ablatives Verfahren, wobei aufgrund der Möglichkeit einer erneuten Histologiegewinnung und Tezeptorstatustestung eine OP präferiert wird.'""")

    with st.expander("Vorst AdHoct"):
        st.markdown("Kennzeichnet, ob die Vorstellung des Patienten im Tumorboard ad hoc erfolgt ist, also ungeplant und kurzfristig (z. B. bei dringendem Therapiebedarf oder Notfall).")
        st.image("plots/Vorst AdHoc_haeufigkeit_mit_nan.png",  width='stretch')
    
    with st.expander("Vorst Elektiv"):
        st.markdown("Kennzeichnet, ob die Vorstellung im Tumorboard elektiv erfolgt ist, also geplant und regulär im Rahmen der üblichen Abläufe (z. B. nach Diagnosestellung oder vor Therapieentscheidung).")
        st.image("plots/Vorst Elektiv_haeufigkeit_mit_nan.png",  width='stretch')

    with st.expander("Tumordiagnose"):
        st.markdown("Hauptdiagnose des Tumors (z. B. Mammakarzinom). Grundlage für Therapieentscheidungen.")
        st.markdown("""Beispiel:
                     '\m1Mammakarzinom links, ED 08/2024 \y:551\
                    Stadium bei Erstdiagnose: \m0\c:FF\  \c:-\cT1c, cN0, M0, G \m1
                    Histologie:\m0 Mammakarzinom Typ NST, G2, ER 90%, PR 70%, Her2neu 1+, Ki-67 5%'""")

    with st.expander("Histo Zyto"):
        st.markdown("Histologische oder zytologische Befunde (z. B. Tumorgrading, Zelltyp). Sehr wichtig für die Klassifikation des Tumors.")
        st.markdown("""
            <div style="
                background-color: #ffffff;
                color: #000000 !important;
                padding: 25px 30px;
                border-radius: 10px;
                margin-top: 20px;
                margin-bottom: 20px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.15);
                font-family: 'Courier New', monospace;
                white-space: pre-wrap;
                line-height: 1.6;
            ">
            <strong style="color:#003366 !important;">Beispiel:</strong><br><br>
            \\f:\\m1Befund Pathologie vom 2024-12-05\\m0<br>
            \\f:12307\\Pathologisch-anatomische Begutachtung<br><br>

            <strong style="color:#003366 !important;">Material/klinische Angaben</strong><br>
            CT-gesteuerte Punktion Pleura rechts – V.a. Pleuracarcinose DD Mesotheliom – 
            Z.n. Mammakarzinom, Ösophaguscarcinom und Urothelcarcinom /jd/aj<br><br>

            <strong style="color:#003366 !important;">Makroskopischer Befund</strong><br>
            Vier bis 15 mm lange Gewebszylinder. Nachträglich blau farbmarkiert.<br><br>

            <strong style="color:#003366 !important;">Pathologisch-Anatomische Diagnose</strong><br>
            Pleura-PE rechts mit einem mäßig differenzierten, nicht verhornenden Plattenepithelkarzinom (G2).<br>
            PD-L1 Status: TPS 20, IC 5, CPS 25.<br>
            Der Befund diskriminiert nicht, sollte ein Plattenepithelkarzinom des Ösophagus vorgelegen haben …<br>
            Eine Metastase des bekannten Urothel- oder Mammakarzinoms erscheint hier unwahrscheinlich.<br>
            ICD-O: C38.4 M8070/6<br><br>

            Die gesetzlich vorgeschriebene Meldung an das Krebsregister Hessen wurde von uns vorgenommen.<br>
            Bitte machen Sie den Patienten auf sein Widerspruchsrecht aufmerksam.
            </div>
        """, unsafe_allow_html=True)



    with st.expander("Tumoranamnese"):
        st.markdown(
            "In diesem Feld werden Angaben zur tumorrelevanten Vorgeschichte der Patientin bzw. des Patienten dokumentiert. "
            "Dazu zählen frühere maligne oder prämaligne Erkrankungen, bereits aufgetretene Rezidive, "
            "Metastasen, Voroperationen oder abgeschlossene onkologische Therapien. "
            "Auch Informationen zu Diagnosedatum, Therapieverlauf und bisherigen Behandlungsergebnissen können hier festgehalten werden. "
            "Die Tumoranamnese ermöglicht eine umfassende Einschätzung des individuellen Krankheitsverlaufs, "
            "unterstützt die Risikoabschätzung für erneutes Tumorwachstum und dient als Grundlage "
            "für die interdisziplinäre Therapie- und Nachsorgeplanung."
        )

    with st.expander("Bildgebung"):
        st.markdown(
            "Hier werden die Ergebnisse der relevanten bildgebenden Untersuchungen dokumentiert, "
            "wie z. B. Computertomographie (CT), Magnetresonanztomographie (MRT), Positronen-Emissions-Tomographie (PET-CT) "
            "oder Sonographie. "
            "Erfasst werden Art und Datum der Untersuchung, auffällige Befunde, Lokalisationen von Primärtumor, "
            "Metastasen oder Lymphknotenveränderungen sowie Verlaufskontrollen im Vergleich zu Voruntersuchungen. "
            "Diese Informationen sind entscheidend für die Beurteilung der Tumorausdehnung, das Staging, "
            "die Therapieplanung und die Erfolgskontrolle der Behandlung. "
            "Das Feld enthält häufig Freitext mit detaillierten Befundbeschreibungen und Beurteilungen."
        )

    with st.expander("Staging Klin cT"):
        st.markdown(
            "Das klinische T-Stadium (cT) beschreibt die Ausdehnung des Primärtumors basierend auf "
            "klinischen Untersuchungen, bildgebender Diagnostik und ggf. endoskopischen Befunden. "
            "Es dient der Einschätzung der Tumorgröße und des lokalen Wachstums vor einer operativen "
            "oder histologischen Sicherung. Die Einordnung erfolgt gemäß TNM-Klassifikation."
        )
        st.image("plots/Staging Klin cT_haeufigkeit_mit_nan.png", width='stretch')

    with st.expander("Staging Klin N"):
        st.markdown(
            "Das klinische N-Stadium (cN) beschreibt das Vorliegen und Ausmaß regionärer Lymphknotenmetastasen "
            "auf Basis bildgebender oder klinischer Befunde. "
            "Die Angabe dient der Beurteilung der lokalen Tumorausbreitung und hat prognostische Bedeutung "
            "für die Therapieplanung."
        )
        st.image("plots/Staging Klin N_haeufigkeit_mit_nan.png", width='stretch')

    with st.expander("Staging Klin M"):
        st.markdown(
            "Das klinische M-Stadium (cM) gibt an, ob Hinweise auf Fernmetastasen vorliegen, "
            "die durch bildgebende Verfahren (z. B. CT, MRT, PET-CT) oder andere klinische Befunde erhoben wurden. "
            "Ein cM0 bedeutet, dass keine Metastasen nachweisbar sind, während cM1 auf Fernmetastasen hinweist."
        )
        st.image("plots/Staging Klin M_haeufigkeit_mit_nan.png", width='stretch')

    with st.expander("Staging Klin UICC"):
        st.markdown(
            "Das klinische UICC-Stadium fasst die cT-, cN- und cM-Klassifikation gemäß der UICC-TNM-Systematik zusammen. "
            "Es beschreibt das klinische Gesamtstadium der Tumorerkrankung und dient als Grundlage für "
            "Therapieentscheidungen und prognostische Einschätzungen vor Beginn der Behandlung."
        )
        st.image("plots/Staging Klin UICC_haeufigkeit_mit_nan.png", width='stretch')

    with st.expander("Staging Path pT"):
        st.markdown(
            "Das pathologische T-Stadium (pT) beschreibt die tatsächliche Tumorausdehnung auf Basis "
            "histopathologischer Untersuchungen nach operativer Entfernung oder Biopsie. "
            "Es stellt die definitive Bestätigung und genauere Beurteilung der lokalen Tumorausbreitung dar."
        )
        st.image("plots/Staging Path pT_haeufigkeit_mit_nan.png", width='stretch')

    with st.expander("Staging Path N"):
        st.markdown(
            "Das pathologische N-Stadium (pN) erfasst das Vorliegen und die Anzahl tumorbefallener "
            "regionärer Lymphknoten auf Grundlage histologischer Befunde. "
            "Diese Information hat hohe prognostische Relevanz und ist entscheidend für die UICC-Stadieneinteilung."
        )
        st.image("plots/Staging Path N_haeufigkeit_mit_nan.png", width='stretch')

    with st.expander("Staging Path M"):
        st.markdown(
            "Das pathologische M-Stadium (pM) beschreibt das Vorhandensein von Fernmetastasen, "
            "die histologisch gesichert wurden. "
            "Da eine pathologische Bestätigung seltener erfolgt, liegt häufig nur ein klinisches M-Stadium (cM) vor."
        )
        st.image("plots/Staging Path M_haeufigkeit_mit_nan.png", width='stretch')

    with st.expander("Staging Path UICC"):
        st.markdown(
            "Das pathologische UICC-Stadium wird nach Abschluss der histopathologischen Untersuchung vergeben "
            "und kombiniert die Parameter pT, pN und pM gemäß der UICC-TNM-Klassifikation. "
            "Es stellt die endgültige stadiengerechte Einordnung der Tumorerkrankung dar und dient als Grundlage "
            "für Prognoseeinschätzung, Therapieplanung und Nachsorge."
        )
        st.image("plots/Staging Path UICC_haeufigkeit_mit_nan.png", width='stretch')


    with st.expander("Nebendiagnosen"):
        st.markdown(
            "Hier werden relevante Begleit- oder Vorerkrankungen der Patientin bzw. des Patienten erfasst, "
            "die zusätzlich zur Hauptdiagnose bestehen (z. B. Diabetes mellitus, arterielle Hypertonie, "
            "kardiovaskuläre oder pulmonale Erkrankungen). "
            "Die Angabe ist wichtig für die ganzheitliche Beurteilung des Gesundheitszustands, "
            "für die Therapieplanung sowie zur Einschätzung möglicher Risiken und Wechselwirkungen."
        )

    with st.expander("Bisherige Therapie"):
        st.markdown(
            "Dieses Feld beschreibt alle bislang durchgeführten Behandlungen im Zusammenhang mit der Tumorerkrankung, "
            "einschließlich operativer Eingriffe, Chemotherapie, Strahlentherapie, Immun- oder zielgerichteter Therapien. "
            "Auch unterstützende Maßnahmen, wie Schmerztherapie oder Ernährungsberatung, können hier dokumentiert werden. "
            "Die Information dient der Nachvollziehbarkeit des bisherigen Therapieverlaufs und der Planung weiterer Schritte."
        )

    with st.expander("Fragestellung"):
        st.markdown(
            "In diesem Feld wird die konkrete Fragestellung an das Tumorboard dokumentiert, "
            "z. B. Entscheidung über eine weiterführende Therapie, Einschätzung der Operabilität "
            "oder Bewertung des Ansprechens auf eine bisherige Behandlung. "
            "Eine präzise Formulierung erleichtert die interdisziplinäre Diskussion "
            "und unterstützt eine zielgerichtete Therapieempfehlung."
        )


    with st.expander("Palliativ / Kurativ (Tumorkonferenz)"):
        st.markdown(
            "Dieses Feld gibt an, ob der Fall im Rahmen der Tumorkonferenz unter palliativem oder kurativem "
            "Behandlungsziel besprochen wurde. "
            "Ein *kuratives* Vorgehen zielt auf Heilung der Erkrankung ab, beispielsweise durch operative Entfernung "
            "des Tumors oder andere potenziell heilende Therapien. "
            "Ein *palliatives* Vorgehen hingegen verfolgt das Ziel, Symptome zu lindern, die Lebensqualität zu erhalten "
            "und Komplikationen vorzubeugen, wenn eine Heilung nicht mehr möglich ist. "
            "Die Angabe dient der klaren Einordnung des therapeutischen Gesamtkonzepts und unterstützt "
            "die weitere Behandlungsplanung sowie die interdisziplinäre Kommunikation im Tumorboard."
        )
        st.image("plots/palliativ_haeufigkeit_mit_nan.png", width='stretch')


    with st.expander("Palliativmedizinische Anbindung"):
        st.markdown(
            "Dieses Feld erfasst, ob die Patientin bzw. der Patient aktuell palliativmedizinisch angebunden ist "
            "oder eine solche Anbindung empfohlen bzw. geplant wird. "
            "Die Angabe dient der frühzeitigen Erkennung eines möglichen Unterstützungsbedarfs im Rahmen der "
            "symptomorientierten, ganzheitlichen Betreuung. "
            "Sie unterstützt die interdisziplinäre Abstimmung zwischen Onkologie, Palliativmedizin, Pflege und "
            "weiteren Fachbereichen, um die Lebensqualität zu sichern und Behandlungsziele individuell abzustimmen. "
            "Ergänzend kann hier dokumentiert werden, welche Maßnahmen bereits erfolgt sind oder in Planung stehen."
        )
        st.image("plots/pall Anbindung_haeufigkeit_mit_nan.png",  width='stretch')

    with st.expander("Alter"):
        st.markdown(
            "Alter der Patientin bzw. des Patienten zum Zeitpunkt der Aufnahme oder zum Zeitpunkt der Tumorboard-Dokumentation. "
            "Diese Angabe ist bedeutsam für die individuelle Risikoeinschätzung, die Planung und Auswahl geeigneter Therapieoptionen "
            "sowie für epidemiologische und statistische Auswertungen im Rahmen der Qualitätssicherung und Forschung."
        )


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