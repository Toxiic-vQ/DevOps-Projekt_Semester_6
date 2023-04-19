# DevOps-Projekt Semester 6

Erstellung einer Webapplikation bzw. einer API

## Inhaltsverzeichnis

- [Zum Projekt](#zum-projekt)
- [Projektaufbau](#projektaufbau)
- [Zur API](#zur-api)
- [API mit Docker ausführen](#api-mit-docker-ausführen)
- [API testen](#api-testen)
- [Zur Datenbank](#zur-datenbank)
<br>

## Zum Projekt

**Thema des Projekts:** Ausgaben-Tracker <br>
**Zweck:** Anwendung zum Erfassen von getätigten Ausgaben <br>
<br>
<img src="Abbildungen README/Frontend.png" alt="Übersicht mit Frontend des Projekts" title="Frontend des Projekts">
<br>

### Projektaufbau

<img src="Abbildungen README/Projektaufbau.png" alt="Übersicht mit Projektaufbau" title="Projektaufbau">
<br>

## Zur API

Die API ist in Python mit dem Flask-Framework geschrieben. <br>
Die Datenbank ist in SQLite erstellt und wird mit SQLAlchemy verwaltet. <br>
<br>
Die API ist ueber http://127.0.0.1:5000/ lokal erreichbar. (Port 5000 ist Standard für Flask-Anwendungen) <br>
<br>

### API mit Docker ausführen

Zur Ausführung der Anwendung in einem Docker-Container wurde speziell ein Dockerfile angefertigt. <br>

1. Dateien aus diesem Verzeichnis lokal herunterladen <br>
2. Ins Verzeichnis wechseln <br>
3. Docker-Container bauen mit  ``` sudo docker build -t webapp . ``` <br>
4. Nach erfolgreichem Bauen kann der Container gestartet werden mit ``` sudo docker run -it -p 5000:5000 webapp ``` <br>
<br>
Die API ist jetzt unter http://127.0.0.1:5000/ lokal erreichbar. <br>
<br>

### API testen

Die Funktionen der API können mit dem Linux-Befehl ``` curl ``` oder beispielsweise der Anwendung Postman getestet werden. <br>
<br>

#### GET - Alle Einträge ausgeben

z.B. mit <br> ``` curl --request GET 'http://127.0.0.1:5000/ausgaben' ```
<br>

#### GET - Einen Eintrag ausgeben (mit ID)

z.B. mit <br> ``` curl --request GET 'http://127.0.0.1:5000/ausgaben/1' ```
<br>

#### POST - Einen Eintrag hinzufügen

**Hinweis:** Aufgrund einer automatischen Umleitung kann es zu einer Fehlermeldung kommen, die Änderungen werden jedoch umgesetzt.
z.B. mit <br> ``` curl --request POST 'http://127.0.0.1:5000/ausgaben' --data 'name=Tanken&betrag=79.99&datum=16.04.2023&kategorie=Auto' ```
<br>

#### PUT  - Einen Eintrag ändern (mit ID)

**Hinweis:** Die Daten müssen zwingend als JSON übergeben werden. <br>
z.B. mit <br>  ``` curl --location --request PUT 'http://127.0.0.1:5000/update/1' --header 'Content-Type: application/json' --data '{"name": "Parken","betrag": "0.50","datum": "13.04.2023","kategorie": "Auto"}' ```
<br>

#### DELETE - Einen Eintrag löschen (mit ID)

z.B. mit <br> ``` curl --location --request DELETE 'http://127.0.0.1:5000/delete/1' ``` |
<br>

## Zur Datenbank

Die Datenbank basiert auf SQLite und ist innerhalb der Datei instance/ausgaben.db gespeichert. <br>
Aufgrund der geringen Komplexität der Webanwendung enthält die Datenbank nur eine Tabelle. <br>
<br>
| Spalte | Eigenschaften |
|--------|---------------|
| id     | Integer, primary_key=True |
| name   | String(80), nullable=False |
| betrag | Numeric(10,2), nullable=False|
| datum  | String(9), nullable=False|
| kategorie | db.String(80), nullable=False |