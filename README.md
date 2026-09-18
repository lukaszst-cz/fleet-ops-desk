# Fleet Ops Desk

**Fleet Ops Desk** to demonstracyjne narzędzie do porządkowania i analizy danych flotowych, przygotowane w Pythonie i SQLite.

Projekt powstał na bazie własnego doświadczenia operacyjnego z flotą oraz sposobu prowadzenia ewidencji i zestawień w arkuszach kalkulacyjnych. Repozytorium wykorzystuje wyłącznie dane testowe i anonimowe — nie zawiera rzeczywistych danych firmowych, kierowców, klientów, pojazdów ani dokumentów.

## Co pokazuje projekt

- ewidencję 18 pojazdów demonstracyjnych,
- status pojazdu: dostępny / w najmie / serwis,
- kontrolę kosztów: paliwo, serwis, ubezpieczenia i ogumienie,
- relacje pomiędzy pojazdami, kosztami, najmem i leasingiem,
- filtrowanie oraz wyszukiwanie pojazdów,
- analizę kosztów w czasie,
- dashboard z podstawowymi wskaźnikami operacyjnymi,
- wykorzystanie relacyjnej bazy SQLite i zapytań SQL,
- prosty interfejs HTML/CSS/JavaScript bez rozbudowanych frameworków.

## Cykl życia pojazdu

Koncepcja projektu odnosi się do praktycznego cyklu życia pojazdu w firmie:

1. **wprowadzenie pojazdu do ewidencji** — podstawowe dane, status i sposób finansowania,
2. **przypisanie do użytkowania lub najmu** — kontrola statusu i dostępności,
3. **bieżąca eksploatacja** — paliwo, koszty, terminy i użytkowanie,
4. **serwis i utrzymanie sprawności** — naprawy, ogumienie, ubezpieczenia i przestoje,
5. **kontrola kosztów i odchyleń** — porównywanie wydatków i identyfikacja pojazdów generujących wyższe koszty,
6. **zwrot / zakończenie najmu lub leasingu** — zamknięcie okresu użytkowania i rozliczenie danych.

Taki system może wspierać pracę operacyjną poprzez zebranie w jednym miejscu informacji, które w praktyce często są rozproszone między arkuszami Excel, dokumentami, wiadomościami i systemami zewnętrznymi. Celem projektu nie jest zastępowanie komercyjnego systemu flotowego, lecz pokazanie sposobu myślenia o danych, procesach i kontroli operacyjnej.

## Dane demonstracyjne

Projekt został celowo przygotowany bez rzeczywistych danych z działalności. Dane są generowane lokalnie na potrzeby demonstracji i obejmują m.in.:

- 18 pojazdów,
- 504 przykładowe rekordy kosztowe,
- umowy najmu,
- umowy leasingu,
- dane do analizy trendu kosztów z lat 2018–2024.

## Uruchomienie

Wymagany jest Python 3. Projekt korzysta wyłącznie z biblioteki standardowej Pythona i SQLite.

```bash
python app.py
```

Po uruchomieniu aplikacja jest dostępna lokalnie pod adresem:

```text
http://127.0.0.1:8000
```

## Szybki test projektu

Bez uruchamiania serwera można sprawdzić, czy demonstracyjna baza została poprawnie utworzona i zawiera oczekiwany zestaw danych:

```bash
python app.py --check
```

Poprawny wynik:

```text
OK: SQLite contains a complete, anonymous demonstration dataset.
```

## Technologie

- Python 3
- SQLite
- SQL
- HTML
- CSS
- JavaScript
- WSGI / Python standard library

## Charakter projektu

To **projekt własny i demonstracyjny**, rozwijany jako część portfolio operacyjnego. Nie jest wdrożeniem komercyjnym ani kopią systemu używanego przez konkretnego pracodawcę.

Projekt pokazuje połączenie praktyki flotowej z podejściem cyfrowym: ewidencją, analizą kosztów, relacyjnymi danymi oraz projektowaniem prostych narzędzi wspierających decyzje operacyjne.

## Portfolio

Projekt jest częścią głównego [portfolio operacyjnego](https://github.com/lukaszst-cz/operations-office-portfolio).
