# swps_zaliczenie_2026
Projekt zaliczeniowy na przedmiot projektowanie aplikacji webowych 

## Opis pomysłu
Aplikacja (Django REST API) do wymiany książkami, podręcznikami i notatkami dla studentów psychologii na SWPS w Warszawie. Użytkownicy będą mogli publikować ogłoszenia, zgłaszać chęć wymiany, rezerwować materiały oraz wystawiać oceny po zakończonej transakcji.

## Wymagania techniczne
- Python 3.12+
- Django 5.2.*
- Django REST Framework
- Git
- IDE (np. Visual Studio Code)
- Baza danych (np. PostgreSQL lub SQLite w zależności od konfiguracji)

## Uruchomienie projektu lokalnie

```bash
# utworzenie środowiska wirtualnego
python -m venv venv

# aktywacja środowiska
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux / macOS

# instalacja zależności
pip install -r requirements.txt

# migracje bazy danych
python manage.py migrate

# uruchomienie serwera
python manage.py runserver

## Założenia funkcjonalne

### Modele danych

1. **User**  
   Rozszerzony model użytkownika (student / administrator).

2. **Material**  
   Książki, podręczniki lub notatki:
   - tytuł
   - autor
   - typ materiału
   - stan
   - opis
   - rok studiów (1–5)
   - przedmiot (np. psychologia poznawcza, społeczna itd.)

3. **Listing**  
   Ogłoszenia dotyczące materiałów:
   - właściciel ogłoszenia
   - tryb (sprzedaż / wymiana / oba)
   - status (aktywne / zarezerwowane / zamknięte)
   - lokalizacja
   - opis

4. **ExchangeRequest**  
   Zgłoszenia chęci wymiany lub rezerwacji ogłoszenia.

5. **Review**  
   System ocen użytkowników:
   - użytkownik wystawiający ocenę
   - użytkownik oceniany
   - ocena (1–5)
   - komentarz

---

## Uwierzytelnianie i autoryzacja

- Token-based authentication (DRF Authtoken)
- Role użytkowników:
  - **admin**
  - **user**
- Dostęp do endpointów API wymaga uwierzytelnienia tokenem
- Tylko właściciel zasobu może go edytować lub usuwać

---

### Endpointy (CRUD)
- CRUD dla wszystkich modeli.
- Rejestracja użytkownika (obowiązkowo).

### Endpointy niestandardowe (min. 2)
- Lista ogłoszeń aktywnych dla konkretnego użytkownika.
- Lista materiałów zaczynających się od wskazanego prefiksu.

## Organizacja pracy
- Repozytorium na GitHub z dostępem prowadzącego.
- W pracy grupowej obie osoby dodane jako collaborators: Zuzanna Bochenek i Natalia Żaboklicka.