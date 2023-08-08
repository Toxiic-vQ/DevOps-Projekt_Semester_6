#Container zur Ausfuehrung der Anwendung
#leichtgewichtiger Python-Container basierend auf Alpine Linux mit Python 3.10.0
FROM python:3.10.0-alpine

#Aktualisierung der Paketliste
RUN apk update

#Installieren von pipenv
RUN pip install pipenv

#Erstellen eines Arbeitsverzeichnisses
WORKDIR /usr/src/app

#Kopieren der Projektdateien
COPY . /usr/src/app

#Installieren der Abhaengigkeiten
RUN pipenv install --system --deploy

#Installieren von der Pakete "pytest" und "requests" im globalen Python-System
#Diese Pakete werden fuer die Ausfuehrung der bereits definierten Testfaelle benoetigt
RUN pip install pytest requests

#Port 5000 freigeben
EXPOSE 5000

#Starten der Anwendung
CMD ["pipenv", "run", "flask", "run", "--host=0.0.0.0", "--port=5000"]