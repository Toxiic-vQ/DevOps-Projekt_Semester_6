#Diese Datei ist fuer den Test der Rest-API-Funktionen zustaendig.
#Es werden die Funktionen bezueglich GET, POST, PUT und DELETE getestet.

#Importieren der notwendigen Bibliotheken fuer den Test
import pytest
import requests

#Importieren der Flask-App
from app import app, db

#Erstellen der Test-Applikation
#die Test-Datenbank wird nach jedem Testfall geloescht
@pytest.fixture
def test_client():
    #Test-Modus aktivieren
    app.config['TESTING'] = True
    client = app.test_client()

    #Erstellen der Datenbank
    with app.app_context():
        db.create_all()

    yield client

    #Datenbank ggf. loeschen
    with app.app_context():
        db.drop_all()

#Test fuer die GET- und POST-Methoden
def test_get_ausgabe_by_id(test_client):
    #initialen Datensatz anlegen, der dann abgerufen wird
    init_ausgabe = {
        'name': 'Semestergebuehr',
        'betrag': 160.00,
        'datum': '25.04.2023',
        'kategorie': 'Studium'
    }
    #POST-Request an die API senden
    response = test_client.post('/ausgaben', data=init_ausgabe, follow_redirects=True)

    #Ueberpruefen, ob Datensatz hinzugefuegt wurde
    assert response.status_code == 200
    #Ueberpruefen, ob die Zeichenkette "Ausgabe erfolgreich hinzugefuegt" zurueckgegeben wird
    assert b"Ausgabe erfolgreich hinzugefuegt" in response.data

    #GET-Request an die API senden, um den initialen Datensatz abzurufen
    #die ID des erstellten Datensatzes ist immer 1, da die Datenbank nach jedem Testfall geloescht wird
    response = test_client.get(f'/ausgaben/1')

    #Ueberpruefen, ob Datensatz abgerufen wurde
    assert response.status_code == 200
    #Ueberpruefen, ob die Daten des Datensatzes korrekt sind
    assert b"Semestergebuehr" in response.data
    assert b"160.00" in response.data
    assert b"25.04.2023" in response.data
    assert b"Studium" in response.data

#Test fuer die POST- und PUT-Methoden
def test_update_ausgabe(test_client):
    #initialen Datensatz anlegen, der dann aktualisiert wird
    init_ausgabe = {
        'name': 'Tanken',
        'betrag': 79.99,
        'datum': '16.04.2023',
        'kategorie': 'Auto'
    }

    #POST-Request an die API senden
    response = test_client.post('/ausgaben', data=init_ausgabe, follow_redirects=True)
    #Ueberpruefen, ob Datensatz hinzugefuegt wurde
    #Status Code 200 wird erwartet, wenn der Datensatz hinzugefuegt wurde
    assert response.status_code == 200
    #Ueberpruefen, ob die Zeichenkette "Ausgabe erfolgreich hinzugefuegt" zurueckgegeben wird
    assert b"Ausgabe erfolgreich hinzugefuegt" in response.data

    #Neuen Datensatz anlegen, der den alten Datensatz ersetzt
    neue_ausgabe = {
        'name': 'Wocheneinkauf',
        'betrag': 95.00,
        'datum': '20.04.2023',
        'kategorie': 'Lebensmittel'
    }

    #PUT-Request an die API senden, um den initalen Datensatz zu aktualisieren
    #die ID des initialen Datensatzes ist immer 1, da die Datenbank nach jedem Testfall geloescht wird
    response = test_client.put(f'/update/1', json=neue_ausgabe, follow_redirects=True)

    #Ueberpruefen, ob Datensatz aktualisiert wurde
    assert response.status_code == 200
    #Ueberpruefen, ob die Zeichenkette '{"Erfolg":"Ausgabedaten aktualisiert"}' zurueckgegeben wird
    assert b'{"Erfolg":"Ausgabedaten aktualisiert"}' in response.data

#Test fuer die POST- und DELETE-Methoden
def test_delete_ausgabe(test_client):
    #initialen Datensatz anlegen, der dann geloescht wird
    init_ausgabe = {
        'name': 'Tanken',
        'betrag': 79.99,
        'datum': '16.04.2023',
        'kategorie': 'Auto'
    }

    #POST-Request an die API senden
    response = test_client.post('/ausgaben', data=init_ausgabe, follow_redirects=True)
    #Ueberpruefen, ob Datensatz hinzugefuegt wurde
    assert response.status_code == 200
    #Ueberpruefen, ob die Zeichenkette "Ausgabe erfolgreich hinzugefuegt" zurueckgegeben wird
    assert b"Ausgabe erfolgreich hinzugefuegt" in response.data

    #DELETE-Request an die API senden, um den initalen Datensatz zu loeschen
    #die ID des initialen Datensatzes ist immer 1, da die Datenbank nach jedem Testfall geloescht wird
    response = test_client.delete(f'/delete/1', follow_redirects=True)

    #Ueberpruefen, ob Datensatz geloescht wurde
    assert response.status_code == 200
    #Ueberpruefen, ob die Zeichenkette '{"Erfolg":"Ausgabedaten geloescht"}' zurueckgegeben wird
    assert b'{"Erfolg":"Ausgabedaten geloescht"}' in response.data