# DevOps-Projekt Semester 6

Erstellung einer Webapplikation bzw. einer API

## Inhaltsverzeichnis

- [Zum Projekt](#zum-projekt)
- [Zur API](#zur-api)
- [Funktionen der API](#funktionen-der-api)
- [API mit Docker ausführen](#api-mit-docker-ausführen)
- [Zur Datenbank](#zur-datenbank)
<br>

## Zum Projekt

Thema des Projekts: Ausgaben-Tracker <br>
Zweck: Anwendung zum Erfassen von getätigten Ausgaben <br>
<br>
erstellt von Felix Mayer, PIB20 <br>
<br>

## Zur API

Die API ist in Python mit dem Flask-Framework geschrieben. <br>
Die Datenbank ist in SQLite erstellt und wird mit SQLAlchemy verwaltet. <br>
Die Funktionen der API (GET, POST, PUT, DELETE) wurden mit der Anwendung Postman getestet. <br>
<br>
Die API ist ueber http://127.0.0.1:5000/ lokal erreichbar. (Port 5000 ist Standard für Flask-Anwendungen) <br>
<br>

### Funktionen der API

| Funktion | Route | Beschreibung |
|----------|-------|--------------|
| GET | http://127.0.0.1:5000/ausgaben | alle Ausgaben anzeigen |
| GET | http://127.0.0.1:5000/ausgaben/id | eine bestimmte Ausgabe anzeigen |
| POST | http://127.0.0.1:5000/ausgaben | neue Ausgabe hinzufügen |
| PUT | http://127.0.0.1:5000/ausgaben/id | bestimme Ausgabe ändern |
| DELETE | http://127.0.0.1:5000/ausgaben/id | bestimme Ausgabe löschen |
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

## Zur Datenbank

Die Datenbank basiert auf SQLite und ist innerhalb der Datei instance/ausgaben.db gespeichert. <br>
Aufgrund der geringen Komplexität der Webanwendung enthält die Datenbank nur eine Tabelle. <br>
<br>
| Spalte | Eigenschaften |
|--------|---------------|
| id     | Integer, primary_key=True |
| name   | String(80), nullable=False |
| betrag | Numeric(10,2), nullable=False|
| datum  | String(9)|