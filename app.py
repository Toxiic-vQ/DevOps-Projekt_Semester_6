#Dieses Skript stellt eine API zur Verfuegung, die es erlaubt, Ausgaben in einer Datenbank zu speichern und zu verwalten.
#Die API ist in Python mit dem Flask-Framework geschrieben.
#Die Datenbank ist in SQLite erstellt und wird mit SQLAlchemy verwaltet.

#Die API kann ueber die Datei ./start.sh gestartet werden.
#Die API ist ueber http://127.0.0.1:5000/ erreichbar.

#Importieren der noetigen Bibliotheken
from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

#Erstellen der Flask-App
app = Flask(__name__)

#Schluessel fuer die Verschluesselung
#notwendig fuer Flash-Nachrichten
app.secret_key = "secret key"

#Konfiguration der Datenbank
#Angabe des Dateipfads zur Datenbank und des Datenbanktyps (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
#Deaktivieren der Warnung, dass die Datenbank veraendert wird
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Erstellen der Datenbank
db = SQLAlchemy(app)

#Datenbankmodell erstellen
class Ausgaben(db.Model):
    #Spalte fuer die ID (Primaerschluessel)
    id = db.Column(db.Integer, primary_key=True)
    #Spalte fuer den Namen der Ausgabe
    name = db.Column(db.String(80), nullable=False)
    #Spalte fuer den Betrag der Ausgabe
    #Numeric(10,2) = 10 Stellen insgesamt, 2 Stellen nach dem Komma
    betrag = db.Column(db.Numeric(10,2), nullable=False)
    #Spalte fuer das Datum der Ausgabe
    #Format als String da DateTime die Angabe einer genauen Zeit erfordert
    datum = db.Column(db.String(9), nullable=False)
    #Kategorie der Ausgabe
    kategorie = db.Column(db.String(80), nullable=False)

    #Funktion zum Erstellen eines neuen Objekts
    def __init__(self, name, betrag, datum, kategorie):
        #Uebergeben der Werte an die Attribute
        self.name = name
        self.betrag = betrag
        self.datum = datum
        self.kategorie = kategorie

    #Funktion zum Erstellen eines Strings mit den Daten des Objekts
    def __repr__(self):
        #Rueckgabe der Daten als String
        return f"{self.name} - {self.betrag} - {self.datum} - {self.kategorie}"


#Erstellen der Route
@app.route("/")
#Erstellen der Funktion
def index():
    #alle Ausgaben aus der Datenbank auslesen
    alle_ausgaben = Ausgaben.query.all()
    #Rueckgabe der Daten an die HTML-Seite
    return render_template("index.html", eintraege = alle_ausgaben)

#POST-Methode fuer Ausgaben
@app.route('/ausgaben', methods=['POST'])
#Funktion fuer die POST-Methode
def add_ausgabe():
    #Erstellen eines neuen Ausgabe-Objekts
    ausgabe = Ausgaben(name=request.form['name'], betrag=request.form['betrag'], datum=request.form['datum'], kategorie=request.form['kategorie'])
    #Hinzufuegen des Objekts zur Datenbank
    db.session.add(ausgabe)
    #Speichern der Aenderungen
    db.session.commit()
    #Flash-Nachricht bei erfolgreicher Hinzufuegung
    flash('Ausgabe erfolgreich hinzugefuegt')
    #Rueckgabe der Daten an die HTML-Seite
    return redirect(url_for('index'))

#PUT-Methode fuer Ausgaben
#@app.route('/update/<id>', methods=['PUT'])
#Funktion fuer die PUT-Methode
#def update_ausgabe(id):
#    #Auslesen der Daten aus der Datenbank
#    ausgabe = Ausgaben.query.get(id)
#    #Fehlermeldung wenn ID nicht gefunden wird
#    if ausgabe is None:
#        return {"Fehler": "ID nicht gefunden"}
#    #Ueberschreiben der Daten mit den neuen Werten
#    ausgabe.name = request.form['name']
#    ausgabe.betrag = request.form['betrag']
#    ausgabe.datum = request.form['datum']
#    ausgabe.kategorie = request.form['kategorie']
#    #Speichern der Aenderungen
#    db.session.commit()
#    #Flash-Nachricht bei erfolgreicher Aktualisierung
#    flash('Ausgabe erfolgreich aktualisiert')
#    #Rueckgabemeldung bei erfolgreicher Aktualisierung
#    return {"Erfolg": "Ausgabedaten aktualisiert"}

#Aendern der PUT-Methode auf POST
#die Implementierung im Rahmen dieses Projekts mit PUT funktioniert nicht
#aufgrund von Problemen in der index.html, da in HTML nur GET und POST moeglich sind
#andere untersuchte Flask-Projekte (mit HTML-Frontend) nutzen ebenfalls POST fuer die PUT-Methode
@app.route('/update/', methods=['GET','POST'])
def update_ausgabe():

    if request.method == 'POST':
        #Auslesen der Daten aus der Datenbank
        ausgabe = Ausgaben.query.get(request.form.get('id'))
        #Fehlermeldung wenn ID nicht gefunden wird
        if ausgabe is None:
            return {"Fehler": "ID nicht gefunden"}
        #Ueberschreiben der Daten mit den neuen Werten
        ausgabe.name = request.form['name']
        ausgabe.betrag = request.form['betrag']
        ausgabe.datum = request.form['datum']
        ausgabe.kategorie = request.form['kategorie']
        #Speichern der Aenderungen
        db.session.commit()

        #Flash-Nachricht bei erfolgreicher Aktualisierung
        flash('Ausgabe erfolgreich aktualisiert')
        #Rueckgabemeldung bei erfolgreicher Aktualisierung
        return redirect(url_for('index'))

#DELETE-Methode fuer Ausgaben
@app.route('/delete/<id>', methods=['DELETE'])
#Funktion fuer die DELETE-Methode
def delete_ausgabe(id):
    #Datensatz mit der ID auslesen
    ausgabe = Ausgaben.query.get(id)
    #Fehlermeldung wenn ID nicht gefunden wird
    if ausgabe is None:
        return {"Fehler": "ID nicht gefunden"}
    #Loeschen der Daten aus der Datenbank
    db.session.delete(ausgabe)
    #Speichern der Aenderungen
    db.session.commit()
    #Flash-Nachricht bei erfolgreicher Loeschung
    flash('Ausgabe erfolgreich geloescht')
    return {"Erfolg": "Ausgabedaten geloescht"}