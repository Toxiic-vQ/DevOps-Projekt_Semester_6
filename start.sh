#!/bin/sh
#application.py als Datei fuer Flask definieren
export FLASK_APP=application.py
#Flask starten im Debug-Modus mit pipenv
pipenv run flask --debug run
