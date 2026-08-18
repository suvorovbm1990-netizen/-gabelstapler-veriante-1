{
            "question": "4. Sie wollen mit einem zum Straßenverkehr zugelassenen Gabelstapler mit einer Höchstgeschwindigkeit von 18 km/h und einem zulässigenОшибка `SyntaxError: unterminated string literal` означает, что текстовая строка в коде не была закрыта кавычкой до перехода на новую строку. Это произошло из-за обрыва текста в середине вопроса.

Ниже приведен чистый код без обрывов.

### Инструкция по исправлению:
1. Откройте файл `main.py` в вашем репозитории на GitHub.
2. Нажмите на иконку карандаша (**Edit this file**).
3. **Полностью удалите** всё текущее содержимое.
4. Вставьте код, приведенный ниже, и нажмите **Commit changes**.

```python
import streamlit as st

st.set_page_config(
    page_title="Gabelstapler - Variante 1", page_icon="🚜", layout="centered"
)

RAW_IMG_URL = "[https://raw.githubusercontent.com/suvorovbm1990-netizen/gabelstapler-variante-1/main/](https://raw.githubusercontent.com/suvorovbm1990-netizen/gabelstapler-variante-1/main/)"

if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = [
        {
            "question": "1. Worauf muessen Sie beim Tanken eines Diesel-Gabelstaplers achten?",
            "choices": [
                "a) Dem Diesel muss Motoroel im Verhaeltnis 1 : 25 beigemischt werden;",
                "b) Motor abstellen, striktes Rauchverbot;",
                "c) Die richtige Oktanzahl muss beachtet werden;",
                "d) Batterienstecker ziehen;",
                "e) Es darf nur bleifrei getankt werden."
            ],
            "correct": ["b) Motor abstellen, striktes Rauchverbot;"]
        },
        {
            "question": "2. Der Fahrer moechte mit den Gabelzinken zwischen der unteren und oberen Box einfahren. Wie beurteilen Sie seinen Versuch?",
            "image": RAW_IMG_URL + "q2_einfahren.jpg",
            "choices": [
                "a) Der Fahrer macht seine Sache gut;",
                "b) Das Hubgeruest muesste senkrecht stehen, damit die Zinken nicht an der unteren Box haengen bleiben;",
                "c) Das Hubgeruest muss beim Einfahren immer nach vorn geneigt sein;",
                "d) Das Hubgeruest muss immer zurueckgeneigt sein beim Einfahren zwischen unterer und oberer Box."
            ],
            "correct": ["b) Das Hubgeruest muesste senkrecht stehen, damit die Zinken nicht an der unteren Box haengen bleiben;"]
        },
        {
            "question": "3. Worauf muessen Sie achten, wenn Sie Lasten mit unterschiedlichen Ausmassen und Gewichten transportieren wollen?",
            "choices": [
                "a) Auf gar nichts, wenn der Gabelstapler gross genug ist;",
                "b) Ich muss immer eine Sackkarre zur Hand haben;",
                "c) Ich muss die Gabelbreite dem jeweiligen Transportgut anpassen;",
                "d) Gabelstapler sind nur fuer bestimmte Lasten zugelassen."
            ],
            "correct": [
                "c) Ich muss die Gabelbreite dem jeweiligen Transportgut anpassen;",
                "d) Gabelstapler sind nur fuer bestimmte Lasten zugelassen."
            ]
        },
        {
            "question": "4. Sie wollen mit einem zum Strassenverkehr zugelassenen Gabelstapler mit einer Hoechstgeschwindigkeit von 18 km/h und einem zulaessigen Gesamtgewicht von 4 Tonnen auf oeffentlichen Strassen fahren. Welche Fahrerlaubnis nach der Fahrerlaubnis-Verordnung (FeV) benoetigen Sie mindestens?",
            "choices": [
                "a) Fuehrerschein Klasse L;",
                "b) Fuehrerschein Klasse BCE;",
                "c) Fuehrerschein Klasse T;",
                "d) Keinen Fuehrerschein."
            ],
            "correct": ["a) Fuehrerschein Klasse L;"]
        },
        {
            "question": "5. Duerfen auf der Gabel eines Gabelstaplers Personen mitgenommen werden?",
            "image": RAW_IMG_URL + "q5_personen.jpg",
            "choices": [
                "a) Ja, wenn eine stabile Ladung befoerdert wird, die festgehalten werden muss;",
                "b) Ja, wenn nicht schneller als 8 km/h und mit besonderer Vorsicht gefahren wird;",
                "c) Nein;",
                "d) Nein, ausser wenn es sich um eine Ueberpruefung durch den Sicherheitsingenieur handelt;",
                "e) Ja, wenn die Gabel sich nicht bewegen kann und die Person gesichert ist."
            ],
            "correct": ["c) Nein;"]
        },
        {
            "question": "6. Auf was muessen Sie beim Stapeln einer Last in ein Palettenregal besonders achten?",
            "choices": [
                "a) Der Abstand zwischen Gabelstapler und Regal darf 75 cm nicht unterschreiten;",
                "b) Beim Stapeln in mehr als 5 m Hoehe ist eine 2. Person als Einweiser vorgeschrieben;",
                "c) Eine Stapelhoehe von 7,5 m darf keinesfalls ueberschritten werden;",
                "d) Die maximale Tragfaehigkeit (Fach- und Feldlast) darf nicht ueberschritten werden."
            ],
            "correct": ["d) Die maximale Tragfaehigkeit (Fach- und Feldlast) darf nicht ueberschritten werden."]
        },
        {
            "question": "7. Duerfen Gabelstapler mit Last in Aufzuegen zwischen verschiedenen Stockwerken befoerdert werden?",
            "choices": [
                "a) Ja, aber nur Elektro-Gabelstapler, die die Luft nicht belasten;",
                "b) Nein, Gabelstapler duerfen grundsaetzlich nicht in Aufzuegen befoerdert werden (§ 3 UVV);",
                "c) Ja, wenn der Aufzug dafuer zugelassen ist und die Tragfaehigkeit des Aufzuges nicht ueberschritten wird;",
                "d) Nur, wenn es sich um einen Personenaufzug handelt, bei dem der Fahrer aus Sicherheitsgruenden nicht auf dem Gabelstapler sitzen darf;",
                "e) Nein, ein Gabelstapler ist zu schwer fuer einen Aufzug."
            ],
            "correct": ["c) Ja, wenn der Aufzug dafuer zugelassen ist und die Tragfaehigkeit des Aufzuges nicht ueberschritten wird;"]
        },
        {
            "question": "8. Welche Aussagen treffen fuer das linke der beiden nachfolgenden Bilder im Vergleich zum rechten Bild zu?",
            "image": RAW_IMG_URL + "q8_schwerpunkt.jpg",
            "choices": [
                "a) Die Kippgefahr des Gabelstaplers hat sich durch das Neigen des Hubgeruestes erhoeht;",
                "b) Der Gesamtschwerpunkt hat sich durch das Neigen des Hubgeruestes veraendert;",
                "c) Der Gesamtschwerpunkt des beladenen Gabelstaplers hat sich nach hinten verschoben;",
                "d) Durch das Neigen des Hubgeruestes erreicht der Gabelstapler eine hoehere Geschwindigkeit."
            ],
            "correct": [
                "a) Die Kippgefahr des Gabelstaplers hat sich durch das Neigen des Hubgeruestes erhoeht;",
                "b) Der Gesamtschwerpunkt hat sich durch das Neigen des Hubgeruestes veraendert;"
            ]
        },
        {
            "question": "9. Welche Massnahmen ergreifen Sie, um ein Abheben des Gabelstaplers an den Hinterraedern zu verhindern?",
            "choices": [
                "a) Zwei Kollegen setzen sich auf das Gegengewicht;",
                "b) Auf das Gegengewicht so viel Ballast aufladen, dass der Gabelstapler wieder festen Stand hat;",
                "c) Eine solche Last darf mit diesem Gabelstapler nicht transportiert werden;",
                "d) Vorsichtig und nur langsam fahren;",
                "e) Die Last verringern."
            ],
            "correct": [
                "c) Eine solche Last darf mit diesem Gabelstapler nicht transportiert werden;",
                "e) Die Last verringern."
            ]
        },
        {
            "question": "10. Von welcher Stelle des Gabelstaplers aus wird der Lastschwerpunktabstand gemessen?",
            "choices": [
                "a) Von der Mitte der Vorderachse aus;",
                "b) Vom Gabelruecken aus;",
                "c) Der Lastschwerpunktabstand liegt immer in der Mitte des Hubgeruestes;",
                "d) Vom Schwerpunkt des Gabelstaplers aus;",
                "e) Der Lastschwerpunkt liegt etwa in der Mitte zwischen Vorder- und Hinterachse."
            ],
            "correct": ["b) Vom Gabelruecken aus;"]
        },
        {
            "question": "11. Was laesst sich allgemein ueber gefaehrliche Stellen wie eine Oelpfuetze, ein abgeknicktes Gelaender, oder vorstehende Hindernisse usw. sagen?",
            "choices": [
                "a) Gefaehrliche Stellen sind zu beseitigen, abzusichern oder zu melden;",
                "b) Sind keine anderen Massnahmen moeglich, sind sie deutlich zu kennzeichnen;",
                "c) Ich muss nichts unternehmen, da hierfuer der Sicherheitsbeauftragte zustaendig ist."
            ],
            "correct": [
                "a) Gefaehrliche Stellen sind zu beseitigen, abzusichern oder zu melden;",
                "b) Sind keine anderen Massnahmen moeglich, sind sie deutlich zu kennzeichnen;"
            ]
        },
        {
            "question": "12
