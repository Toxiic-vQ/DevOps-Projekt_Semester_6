# DevOps-Projekt Semester 6

Titel: Erstellung einer Webapplikation bzw. einer API

## Inhaltsverzeichnis

- [Zum Projekt](#zum-projekt)
- [Zur API](#zur-api)
- [Funktionen der API](#funktionen-der-api)
- [API mit Docker ausführen](#api-mit-docker-ausführen)
- [API lokal ausführen](#api-lokal-ohne-docker-ausführen)


## Zum Projekt

Thema des Projekts: Ausgaben-Tracker <br>
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

GET http://127.0.0.1:5000/ausgaben        --> alle Ausgaben anzeigen <br>
GET http://127.0.0.1:5000/ausgaben/id     --> eine bestimmte Ausgabe anzeigen <br>
POST http://127.0.0.1:5000/ausgaben       --> neue Ausgabe hinzufügen <br>
PUT http://127.0.0.1:5000/ausgaben/id     --> bestimme Ausgabe ändern <br>
DELETE http://127.0.0.1:5000/ausgaben/id  --> bestimme Ausgabe löschen <br>
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
### API lokal (ohne Docker) ausführen

Hierfür müssen die notwendigen Python-Installationen lokal vorhanden sein. <br>
<br>
1. Dateien aus diesem Verzeichnis lokal herunterladen <br>
2. Ins Verzeichnis wechseln <br>
3. Flask-Anwendung mit dem Skript start.sh ausführen <br>
<br>
Die API ist jetzt unter http://127.0.0.1:5000/ lokal erreichbar. <br>