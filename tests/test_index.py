#Die Datei ist fuer den Test der Index-Seite zustaendig.
#Dieser Test ueberprueft, ob die Index-Seite geladen wird.

#Importieren der notwendigen Bibliotheken fuer den Test
import pytest

#Importieren der Flask-App
from app import app, db, Ausgaben

#Erstellen der Test-Applikation
@pytest.fixture
def client():
    #Datenbank auswaehlen und Test-Modus aktivieren
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['TESTING'] = True

    #Erstellen des Test-Clients
    with app.test_client() as client:
        #Datenbank erstellen
        with app.app_context():
            db.create_all()
        yield client
        #Datenbank ggf. loeschen
        db.drop_all()

#Tests fuer die Index-Seite
def test_index_route(client):
    #Aufrufen der Index-Seite
    response = client.get('/')
    #Ueberpruefen, ob die Seite geladen wurde
    #Status Code 200 wird erwartet, wenn die Seite geladen wurde
    assert response.status_code == 200
    #Ueberpruefen, ob die Zeichenkette "Ausgaben verwalten" auf der Seite vorhanden ist
    assert b"Ausgaben verwalten" in response.data
