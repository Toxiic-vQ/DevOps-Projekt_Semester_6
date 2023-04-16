#!/bin/sh
#app.py als Datei fuer Flask definieren
export FLASK_APP=app.py
#Flask starten im Debug-Modus mit pipenv
# mit -h 0.0.0.0 wird der Server auf allen Netzwerk-Interfaces lauschen -> wichtig fuer Docker
pipenv run flask --debug run -h 0.0.0.0 -p 5000