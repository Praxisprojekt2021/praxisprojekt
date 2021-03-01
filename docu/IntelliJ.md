# Arbeiten mit der IntelliJ IDE

Autor: Tom Hinzmann, Stand: 01.03.2021 \
Hast du Fragen zur Bedienung von IntelliJ? Melde dich gern bei mir.

## Warum IntelliJ?

Die Frage ist einfach zu beantworten: IntelliJ ist eine sehr umfangreiche und doch überschaubare Entwicklungsumgebung,
die (fast) alle Sprachen und Frameworks unterstützt und dabei immer die vertraute IDE bietet.

Als Hauptprodukt der Firma JetBrains ist IntelliJ die Kombination aus der bekannten Python IDE PyCharm und weiteren,
insofern wird also tatsächlich nur diese eine Software benötigt, egal ob mit Frontend oder Backend Technologien
programmiert wird.

## IntelliJ herunterladen

Als Student ist die Vollversion der IntelliJ IDE kostenlos, man kann sich direkt anmelden und erhält den Zugriff für ein
Jahr, den man anschließend wiederum kostenlos verlängern kann.

Hier ist das Anmeldeformular: https://www.jetbrains.com/shop/eform/students

Sobald man sich mit der studentischen E-Mail registriert hat, steht die Vollversion der Softwares zum Download zur
Verfügung.

## Workspace konfigurieren

Im Prinzip reichen die Standardeinstellungen der IDE vollkommen aus, allerdings bietet IntelliJ einen hervorragenden
Dark Mode, der dir sehr ans Herz gelegt wird. Also triff ruhig deine präferierten Einstellungen. Die Appearance lässt
sich ansonsten später noch über Preferences einrichten.

### Plugins installieren

Einige Plugins sollten installiert werden, damit die IDE alle nötigen Funktionen hat, um alle Sprache und Dateitypen
handlen zu können. Dies geschieht ebenfalls über Preferences.

Frontend:
1. Apache config (.htaccess)

Backend:
1. Python

### Code Checker

IntelliJ bietet standardmäßig verschiedene Möglichkeiten zur automatisierten Code-Überprüfung. Bitte übernimm die von
uns vorgeschlagenen Einstellungen, damit erleichterst du dir selbst die Programmierung von sauberem Code. Oben in deiner
Menuleiste findest du außerdem den Punkt "Code -> Reformat Code", damit kannst du deinen Code automatisch aufräumen.

Bitte aktiviere die folgenden Optionen. Vergiss nicht, deine Änderungen zu "Applien":

Frontend
1. Preferences | Editor | Code Style | JavaScript \
   Hier bitte die Spaces & Indents Standardeinstellungen 4, 4, 4 nutzen.
2. Preferences | Editor | Inspections | JavaScript and TypeScript \
   JavaScript and TypeScript | Code quality tools | Standard code style

Backend
1. Preferences | Editor | Code Style | Python \
   Hier bitte die Spaces & Indents Standardeinstellungen 4, 4, 8 nutzen.
2. Preferences -> Editor -> Inspections -> Python \
   Python | Missing or empty docstring \
   Python | Missing type hinting for function definition

### git Versionsverwaltung

Die Versionsverwaltung mit git ist in IntelliJ von Beginn an enthalten. Wenn du also IntelliJ startest, wirst du
gefragt, ob du ein neues Projekt starten, ein vorhandenes öffnen oder ein Projekt von git klonen möchtest ("Get from VCS"). Falls du
das Praxisprojekt git Repository nicht schon lokal geklont hast, kannst du das Projekt also hiermit direkt klonen und
anschließend lokal bearbeiten.

Du findest außerdem im Projekt oben in der Menuleiste den Punkt "VCS" oder "Git", dahinter verbirgt sich die git Versionsverwaltung, die du
idealerweise mit dem git Repo verknüpfst, sollte dies nicht schon der Fall sein. Hat dies erfolgreich funktioniert, findest du hier die Standard-Funktionen
von git, kannst entsprechend vom Repo pullen, deine Commits auf den Feature-Branch pushen und ähnliches. 
Außerdem findest du ab sofort unten links in einer weiteren Menu Leiste den Punkt Git. Dort siehst du deine Local Changes,
kannst dir entsprechende Änderungen lokal anzeigen lassen und vieles mehr.

Wenn du soweit bist und deine User Story ganz oder teilweise hinsichtlich Tests und Kriterien umgesetzt hast, kannst du mehrere
veränderte Dateien auswählen und gemeinsam auf deinen Feature-Branch committen. Hierfür gelten die Richtlinien, also
bitte halte dich an die Vorgaben, andernfalls werden deine Changes von den Reviewern abgelehnt und landen wieder bei dir.

### BACKEND - Python installieren

Wir nutzen Python 3.8 für dieses Projekt. Bitte lade die korrekte Version von https://www.python.org/downloads/
herunter und lege sie in IntelliJ als Projekt SDK an. Dazu klickst du rechts oben den Ordner mit den drei blauen Quadraten
an und gelangst so zu den Project Settings.

Es sei die nahegelegt, dass du ein virtuelles Entwicklungs-Environment anlegst, um die Packages nicht global installieren
zu müssen, da dies ggf. Konflikte mit anderen Python Projekten mit sich bringen könnte. Also lege idealerweise eine
Virtualenv oder Pipenv Umgebung als SDK an.

Für die Verwaltung der Python Packages werden meist die pip oder Anaconda package Dienste genutzt, du kannst gern eines
oder sogar beide nutzen. Pip ist etwas einfacher zu nutzen, bietet aber etwas weniger Funktionalität. Wenn dies dein
erstes Python-Projekt ist, kann ich dir pip sehr ans Herz legen, andernfalls, wenn du etwas fortgeschrittener bist, bist
du mit Anaconda sehr gut beraten.

### Requirements

Im Verlauf des Projektes wird das Repo eine Requirements.txt Datei enthalten. Darin sind die zu importierenden Module
aufgelistet. Solltest du diese Module noch nicht importiert haben, wird IntelliJ dich fragen, ob du die Module
aus der Requirements Datei automatisch herunterladen möchtest, was zu empfehlen ist, da die Module ohne dein dazutun
in der korrekten Version in das Projekt importiert werden. Sollte dies nicht der Fall sein, installiere die entsprechenden
Module, indem du einen Rechtsklick auf die Module in der Requirements.txt Datei ausführst und auswählst, dass die Requirements
installiert werden sollen.

Sollten hierbei Fehler auftreten, stelle sicher, dass dein Projekt korrekt mit dem (virtuellen) Entwicklungs-Environment
verknüpft ist.
