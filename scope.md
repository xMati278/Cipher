# Projekt
# CIPHER

1. ROT13, ROT47 (SZYFR CEZARA) -> [https://pl.wikipedia.org/wiki/Szyfr_Cezara](https://pl.wikipedia.org/wiki/Szyfr_Cezara)
2. Funkcjonalności
    - FileHandler odczyt, zapis do pliku, user podaje nazwe, wyjatki, Gdy chce zapisać do tego samego pliku to append(dodanie do pliku), - Ja polecam format JSON
    - Szyfrowanie i Odszyfrowywanie.
    - Buffer czyli taka lista, która sobie istnieje podczas działania programu, Trzyma zaszyfrowane, odszyfrowane wczytane z pliku, z niego zapisujemy do pliku. 
    - Menu
    - Uruchamianie wybranych funkcji w managerze mozna rozwiązac za pomocą Dict'a ([https://stackoverflow.com/questions/21962763/using-a-dictionary-as-a-switch-statement-in-python]) lub structural pattern matching [https://peps.python.org/pep-0636/]
    - Manager
    - run/main.py -> python main.py | python run.py
    - Exit
    - Wzorzec projektowy: Facade
    - Testy Jednostkowe
   
### struktura obiekt propozycja
- Obiekt Text zaszyfrowany/odszyfrowany to klasa text. Łatwo z klasy zrobić DICT, a dict potrzebujemy żeby zapisać do JSON'a  
- {"text"": xyz, "rot_type": rot13/rot47, "status": encrypted/decrypted}

1. Dodatkowe rzeczy:
    - FactoryMethod/AbstractFactory zalezy od zaimplementowania algorytmu szyfrowania/deszyfrowania.

2. Stylistyka
    - PEP 8
    - GithubFlow
    - Czeste commity
    - Conventional commits
      - NOK -> add new way of handling files
      - OK -> feat: add new way of handling files
      - BEST OK -> feat(filehandler): add new way of handling files
      - NOK -> update .gitignore
      - OK -> chore: update .gitignore
      - BEST OK -> chore(git): update .gitignore
      - NOK -> create unit tests for file handling
      - OK -> test: create unit tests for file handling 
      - BEST OK -> test(filehandler): create unit tests for file handling
      - NOK -> update readme.md about file_handling feature
      - OK -> docs: update readme.md about file_handling feature
      - BEST -> docs(readme): update readme.md about file_handling feature
    - Typing (mypy)
    - Docstring

3. Tools (Ze Stachem)* 
   - Pre-commit (black, flake8) odpala lintery i formatery przy commicie (dokładnie przed)