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

#Port 5000 freigeben
EXPOSE 5000

#Starten der Anwendung
ENTRYPOINT ["/usr/src/app/start.sh"]