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

## Założenia funkcjonalne
### Modele (4–5)
1. **User** – konto użytkownika (student, administrator).
2. **Material** – książka/podręcznik/notatka (tytuł, autor, typ, stan, opis, **rok studiów 1–5**, **przedmiot**: psychologia społeczna/psychologia poznawcza/psychologia ogólna/psychologia rozwojowa/neuropsychologia).
3. **Listing** – ogłoszenie wymiany/sprzedaży (status, lokalizacja, opis, **tryb**: tylko sprzedaż/tylko wymiana/sprzedaż i/lub wymiana).
4. **ExchangeRequest** – zgłoszenie wymiany/rezerwacji.
5. **Review** – oceny/komentarze po zakończeniu wymiany.

### Uwierzytelnianie i autoryzacja
- Token-based authentication.
- Co najmniej 2 role: **admin** i **user** z różnymi poziomami dostępu do endpointów.

### Endpointy (CRUD)
- CRUD dla wszystkich modeli.
- Rejestracja użytkownika (obowiązkowo).

### Endpointy niestandardowe (min. 2)
- Lista ogłoszeń aktywnych dla konkretnego użytkownika.
- Lista materiałów zaczynających się od wskazanego prefiksu.

## Kryteria oceniania
- Systematyczność i sens commitów.
- Jakość kodu.
- Implementacja zagadnień z zajęć.
- Złożoność projektu (liczba modeli, endpointy, logika biznesowa).

## Organizacja pracy
- Repozytorium na GitHub z dostępem prowadzącego.
- W pracy grupowej obie osoby dodane jako collaborators.