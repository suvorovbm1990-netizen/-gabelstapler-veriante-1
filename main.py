import random
from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="Gabelstapler - Variante 1", page_icon="🚜", layout="centered"
)

BASE_DIR = Path(__file__).parent

# Исходный список всех вопросов
QUESTIONS = [
    {
        "question": "1. Worauf muessen Sie beim Tanken eines Diesel-Gabelstaplers achten?",
        "choices": [
            "a) Dem Diesel muss Motoroel im Verhaeltnis 1 : 25 beigemischt werden;",
            "b) Motor abstellen, striktes Rauchverbot;",
            "c) Die richtige Oktanzahl muss beachtet werden;",
            "d) Batterienstecker ziehen;",
            "e) Es darf nur bleifrei getankt werden.",
        ],
        "correct": ["b) Motor abstellen, striktes Rauchverbot;"],
    },
    {
        "question": "2. Der Fahrer moechte mit den Gabelzinken zwischen der unteren und oberen Box einfahren. Wie beurteilen Sie seinen Versuch?",
        "image": "q2_einfahren.jpg",
        "choices": [
            "a) Der Fahrer macht seine Sache gut;",
            "b) Das Hubgeruest muesste senkrecht stehen, damit die Zinken nicht an der unteren Box haengen bleiben;",
            "c) Das Hubgeruest muss beim Einfahren immer nach vorn geneigt sein;",
            "d) Das Hubgeruest muss immer zurueckgeneigt sein beim Einfahren zwischen unterer und oberer Box.",
        ],
        "correct": [
            "b) Das Hubgeruest muesste senkrecht stehen, damit die Zinken nicht an der unteren Box haengen bleiben;"
        ],
    },
    {
        "question": "3. Worauf muessen Sie achten, wenn Sie Lasten mit unterschiedlichen Ausmassen und Gewichten transportieren wollen?",
        "choices": [
            "a) Auf gar nichts, wenn der Gabelstapler gross genug ist;",
            "b) Ich muss immer eine Sackkarre zur Hand haben;",
            "c) Ich muss die Gabelbreite dem jeweiligen Transportgut anpassen;",
            "d) Gabelstapler sind nur fuer bestimmte Lasten zugelassen.",
        ],
        "correct": [
            "c) Ich muss die Gabelbreite dem jeweiligen Transportgut anpassen;",
            "d) Gabelstapler sind nur fuer bestimmte Lasten zugelassen.",
        ],
    },
    {
        "question": "4. Sie wollen mit einem zum Strassenverkehr zugelassenen Gabelstapler mit einer Hoechstgeschwindigkeit von 18 km/h und einem zulaessigen Gesamtgewicht von 4 Tonnen auf oeffentlichen Strassen fahren. Welche Fahrerlaubnis nach der Fahrerlaubnis-Verordnung (FeV) benoetigen Sie mindestens?",
        "choices": [
            "a) Fuehrerschein Klasse L;",
            "b) Fuehrerschein Klasse BCE;",
            "c) Fuehrerschein Klasse T;",
            "d) Keinen Fuehrerschein.",
        ],
        "correct": ["a) Fuehrerschein Klasse L;"],
    },
    {
        "question": "5. Duerfen auf der Gabel eines Gabelstaplers Personen mitgenommen werden?",
        "image": "q5_personen.jpg",
        "choices": [
            "a) Ja, wenn eine stabile Ladung befoerdert wird, die festgehalten werden muss;",
            "b) Ja, wenn nicht schneller als 8 km/h und mit besonderer Vorsicht gefahren wird;",
            "c) Nein;",
            "d) Nein, ausser wenn es sich um eine Ueberpruefung durch den Sicherheitsingenieur handelt;",
            "e) Ja, wenn die Gabel sich nicht bewegen kann und die Person gesichert ist.",
        ],
        "correct": ["c) Nein;"],
    },
    {
        "question": "6. Auf was muessen Sie beim Stapeln einer Last in ein Palettenregal besonders achten?",
        "choices": [
            "a) Der Abstand zwischen Gabelstapler und Regal darf 75 cm nicht unterschreiten;",
            "b) Beim Stapeln in mehr als 5 m Hoehe ist eine 2. Person als Einweiser vorgeschrieben;",
            "c) Eine Stapelhoehe von 7,5 m darf keinesfalls ueberschritten werden;",
            "d) Die maximale Tragfaehigkeit (Fach- und Feldlast) darf nicht ueberschritten werden.",
        ],
        "correct": [
            "d) Die maximale Tragfaehigkeit (Fach- und Feldlast) darf nicht ueberschritten werden."
        ],
    },
    {
        "question": "7. Duerfen Gabelstapler mit Last in Aufzuegen zwischen verschiedenen Stockwerken befoerdert werden?",
        "choices": [
            "a) Ja, aber nur Elektro-Gabelstapler, die die Luft nicht belasten;",
            "b) Nein, Gabelstapler duerfen grundsaetzlich nicht in Aufzuegen befoerdert werden (§ 3 UVV);",
            "c) Ja, wenn der Aufzug dafuer zugelassen ist und die Tragfaehigkeit des Aufzuges nicht ueberschritten wird;",
            "d) Nur, wenn es sich um einen Personenaufzug handelt, bei dem der Fahrer aus Sicherheitsgruenden nicht auf dem Gabelstapler sitzen darf;",
            "e) Nein, ein Gabelstapler ist zu schwer fuer einen Aufzug.",
        ],
        "correct": [
            "c) Ja, wenn der Aufzug dafuer zugelassen ist und die Tragfaehigkeit des Aufzuges nicht ueberschritten wird;"
        ],
    },
    {
        "question": "8. Welche Aussagen treffen fuer das linke der beiden nachfolgenden Bilder im Vergleich zum rechten Bild zu?",
        "image": "q8_schwerpunkt.jpg",
        "choices": [
            "a) Die Kippgefahr des Gabelstaplers hat sich durch das Neigen des Hubgeruestes erhoeht;",
            "b) Der Gesamtschwerpunkt hat sich durch das Neigen des Hubgeruestes veraendert;",
            "c) Der Gesamtschwerpunkt des beladenen Gabelstaplers hat sich nach hinten verschoben;",
            "d) Durch das Neigen des Hubgeruestes erreicht der Gabelstapler eine hoehere Geschwindigkeit.",
        ],
        "correct": [
            "a) Die Kippgefahr des Gabelstaplers hat sich durch das Neigen des Hubgeruestes erhoeht;",
            "b) Der Gesamtschwerpunkt hat sich durch das Neigen des Hubgeruestes veraendert;",
        ],
    },
    {
        "question": "9. Welche Massnahmen ergreifen Sie, um ein Abheben des Gabelstaplers an den Hinterraedern zu verhindern?",
        "choices": [
            "a) Zwei Kollegen setzen sich auf das Gegengewicht;",
            "b) Auf das Gegengewicht so viel Ballast aufladen, dass der Gabelstapler wieder festen Stand hat;",
            "c) Eine solche Last darf mit diesem Gabelstapler nicht transportiert werden;",
            "d) Vorsichtig und nur langsam fahren;",
            "e) Die Last verringern.",
        ],
        "correct": [
            "c) Eine solche Last darf mit diesem Gabelstapler nicht transportiert werden;",
            "e) Die Last verringern.",
        ],
    },
    {
        "question": "10. Von welcher Stelle des Gabelstaplers aus wird der Lastschwerpunktabstand gemessen?",
        "choices": [
            "a) Von der Mitte der Vorderachse aus;",
            "b) Vom Gabelruecken aus;",
            "c) Der Lastschwerpunktabstand liegt immer in der Mitte des Hubgeruestes;",
            "d) Vom Schwerpunkt des Gabelstaplers aus;",
            "e) Der Lastschwerpunkt liegt etwa in der Mitte zwischen Vorder- und Hinterachse.",
        ],
        "correct": ["b) Vom Gabelruecken aus;"],
    },
    {
        "question": "11. Was laesst sich allgemein ueber gefaehrliche Stellen wie eine Oelpfuetze, ein abgeknicktes Gelaender, oder vorstehende Hindernisse usw. sagen?",
        "choices": [
            "a) Gefaehrliche Stellen sind zu beseitigen, abzusichern oder zu melden;",
            "b) Sind keine anderen Massnahmen moeglich, sind sie deutlich zu kennzeichnen;",
            "c) Ich muss nichts unternehmen, da hierfuer der Sicherheitsbeauftragte zustaendig ist.",
        ],
        "correct": [
            "a) Gefaehrliche Stellen sind zu beseitigen, abzusichern oder zu melden;",
            "b) Sind keine anderen Massnahmen moeglich, sind sie deutlich zu kennzeichnen;",
        ],
    },
    {
        "question": "12. Welche Aussagen ueber das Eigengewicht eines Gabelstaplers sind richtig?",
        "choices": [
            "a) Das Eigengewicht ist das Gewicht eines Gabelstaplers ohne Nutzlast;",
            "b) Das Eigengewicht ist das gleiche wie das zulaessige Gesamtgewicht;",
            "c) Desto hoeher das Eigengewicht ist, desto mehr Last kann aufgenommen werden;",
            "d) Das Eigengewicht braucht vom Fahrer nicht beachtet zu werden.",
        ],
        "correct": [
            "a) Das Eigengewicht ist das Gewicht eines Gabelstaplers ohne Nutzlast;",
            "c) Desto hoeher das Eigengewicht ist, desto mehr Last kann aufgenommen werden;",
        ],
    },
    {
        "question": "13. Bei welcher Lastaufnahme besteht fuer die Last erhoehte Kippgefahr?",
        "image": "q13_forks.jpg",
        "choices": [
            "a) Option a (Schmale Gabelstellung)",
            "b) Option b (Breite Gabelstellung)",
            "c) Option c (Ungleichmaessige Gabelstellung)",
        ],
        "correct": [
            "a) Option a (Schmale Gabelstellung)",
            "c) Option c (Ungleichmaessige Gabelstellung)",
        ],
    },
    {
        "question": "14. Eine beladene Palette, mit den Massen 800 x 1200 mm, wiegt 1200 kg. Sie soll in ein Hochregal auf einem Fachboden in 4,5 m Hoehe gelagert werden. Ist das mit diesem Gabelstapler moeglich?",
        "image": "q14_diagram.jpg",
        "choices": [
            "a) Nein, maximale Hoehe sind 4 m;",
            "b) Ja, ohne Einschraenkungen, die max. Stapelfaehigkeit ist 1600 kg;",
            "c) Nein, das Hoechstgewicht bei 4,5 m betraegt 680 kg;",
            "d) Nein, Paletten duerfen nur bis max. 4 m Hoehe gestapelt werden;",
            "e) Ja, die Palette muss aber quer aufgenommen werden.",
        ],
        "correct": ["e) Ja, die Palette muss aber quer aufgenommen werden."],
    },
    {
        "question": "15. Was muessen Sie bei der Verwendung von Anbaugeraeten an Ihrem Gabelstapler beachten?",
        "choices": [
            "a) Die Resttragfaehigkeit darf nicht ueberschritten werden;",
            "b) Die Nenntragfaehigkeit des Gabelstaplers wird ueberlastet;",
            "c) Die Hubgenauigkeit wird durch das groessere Gewicht eingeschraenkt;",
            "d) Anbaugeraete muessen durch rot-weisse Streifen markiert werden;",
            "e) Anbaugeraete duerfen nur bestimmungsgemaess verwendet werden.",
        ],
        "correct": [
            "a) Die Resttragfaehigkeit darf nicht ueberschritten werden;",
            "e) Anbaugeraete duerfen nur bestimmungsgemaess verwendet werden.",
        ],
    },
    {
        "question": "16. Wann ist die Kippgefahr bei Gabelstaplern besonders gross?",
        "choices": [
            "a) Gabelstapler koennen nicht umkippen;",
            "b) Die Kippgefahr ist besonders gross bei Kurvenfahrt und im Gefaelle;",
            "c) Die Kippgefahr ist besonders gross bei schlechter Sicht nach vorne;",
            "d) Die Kippgefahr ist besonders gross, wenn die hoechstzulaessige Belastung ueberschritten wird;",
            "e) Die Kippgefahr ist besonders gross beim Bremsen und bei hochgefahrenem Hubgeruest.",
        ],
        "correct": [
            "b) Die Kippgefahr ist besonders gross bei Kurvenfahrt und im Gefaelle;",
            "d) Die Kippgefahr ist besonders gross, wenn die hoechstzulaessige Belastung ueberschritten wird;",
            "e) Die Kippgefahr ist besonders gross beim Bremsen und bei hochgefahrenem Hubgeruest.",
        ],
    },
    {
        "question": "17. Wie oft und von wem wird die Feststell- und Betriebsbremse ueberprueft?",
        "choices": [
            "a) Woechentlich durch den Sicherheitsingenieur;",
            "b) Monatlich durch den Bremsenhersteller;",
            "c) Taeglich durch den Meister (nach Arbeitsbeginn);",
            "d) Taeglich durch den Fahrer (bei Arbeitsbeginn).",
        ],
        "correct": ["d) Taeglich durch den Fahrer (bei Arbeitsbeginn)."],
    },
    {
        "question": "18. Welche Flurfoerderzeuge duerfen in explosionsgefaehrdeten Bereichen fahren?",
        "choices": [
            "a) Nur Fahrzeuge mit Gasbetrieb;",
            "b) Nur besonders zugelassene und gekennzeichnete Fahrzeuge (explosionsgeschuetztes Fahrzeug);",
            "c) Nur mit einer roten Warnfarbe gestrichene und mit einer gelben Rundumleuchte ausgestattete Fahrzeuge;",
            "d) Es gibt keine besonderen Bestimmungen;",
            "e) Nur Geraete mit Ottomotoren.",
        ],
        "correct": [
            "b) Nur besonders zugelassene und gekennzeichnete Fahrzeuge (explosionsgeschuetztes Fahrzeug);"
        ],
    },
    {
        "question": "19. Womit koennen Sie Ihre Berechtigung zum selbstaendigen Steuern eines Gabelstaplers im Unternehmen nachweisen?",
        "choices": [
            "a) Mit dem Fuehrerschein Klasse L;",
            "b) Es ist kein Nachweis erforderlich;",
            "c) Fahrausweis fuer Gabelstapler;",
            "d) Durch die schriftliche Beauftragung des Arbeitgebers;",
            "e) Zeugnis der letzten Arbeitsstelle.",
        ],
        "correct": [
            "c) Fahrausweis fuer Gabelstapler;",
            "d) Durch die schriftliche Beauftragung des Arbeitgebers;",
        ],
    },
    {
        "question": "20. Welcher Gabelstapler faehrt falsch in einer Steigung bzw. in einem Gefaelle?",
        "image": "q20_steigung.jpg",
        "choices": [
            "a) Stapler a",
            "b) Stapler b",
            "c) Stapler c",
            "d) Stapler d",
        ],
        "correct": ["b) Stapler b", "c) Stapler c"],
    },
]

# Инициализация и случайная перемешка вопросов при первом запуске
if "quiz_data" not in st.session_state:
    shuffled_questions = QUESTIONS.copy()
    random.shuffle(shuffled_questions)
    st.session_state.quiz_data = shuffled_questions

if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "submitted" not in st.session_state:
    st.session_state.submitted = False

st.title("🚜 Gabelstapler Prüfung - Variante 1")

total_q = len(st.session_state.quiz_data)
curr_i = st.session_state.current_index

if curr_i < total_q:
    q_data = st.session_state.quiz_data[curr_i]
    st.caption(f"Frage {curr_i + 1} von {total_q}")
    st.subheader(q_data["question"])

    if "image" in q_data:
        file_name = q_data["image"]
        img_path = BASE_DIR / file_name

        if img_path.is_file():
            st.image(str(img_path), use_container_width=True)
        else:
            st.error(
                f"⚠️ Изображение `{file_name}` не найдено в корне репозитория ({BASE_DIR})."
            )

    is_multiselect = len(q_data["correct"]) > 1

    if is_multiselect:
        st.info("💡 Hinweis: Mehrere Antworten können richtig sein.")
        user_choices = []
        for choice in q_data["choices"]:
            if st.checkbox(choice, key=f"q_{curr_i}_{choice}"):
                user_choices.append(choice)
    else:
        user_selection = st.radio(
            "Wählen Sie eine Antwort:",
            q_data["choices"],
            index=None,
            key=f"q_{curr_i}_radio",
        )
        user_choices = [user_selection] if user_selection else []

    if not st.session_state.submitted:
        if st.button("Antworten", type="primary"):
            if not user_choices:
                st.warning("Bitte wählen Sie mindestens eine Antwort aus.")
            else:
                st.session_state.submitted = True
                if sorted(user_choices) == sorted(q_data["correct"]):
                    st.session_state.score += 1
                st.rerun()
    else:
        if sorted(user_choices) == sorted(q_data["correct"]):
            st.success("🟢 Richtig!")
        else:
            st.error("🔴 Falsch!")
            st.write("**Richtige Antwort(en):**")
            for ans in q_data["correct"]:
                st.write(f"- {ans}")

        if st.button("Nächste Frage ➡️"):
            st.session_state.current_index += 1
            st.session_state.submitted = False
            st.rerun()
else:
    st.balloons()
    st.success("🎉 Test abgeschlossen!")
    st.write(f"### Ihr Ergebnis: **{st.session_state.score} / {total_q}**")

    # При перезапуске теста вопросы перемешиваются заново
    if st.button("Test neustarten"):
        shuffled_questions = QUESTIONS.copy()
        random.shuffle(shuffled_questions)
        st.session_state.quiz_data = shuffled_questions
        st.session_state.current_index = 0
        st.session_state.score = 0
        st.session_state.submitted = False
        st.rerun()
