# Repository Dokumentation

Autoren: \
Tom Hinzmann \
Jasmin Čapka

Stand: 03.04.2021

## Repo Struktur

Dieses Repository umfasst Frontend und Backend Komponenten und wird gemeinsam im Rahmen des Google Cloud Build deployed.
Zugriff auf die Dienste erfolgt durch eine Flask REST API, die sowohl statische Inhalte als auch Berechnungen,
Datenstrukturen und Metadaten in Form von JSON Objekten liefert. Die Architektur orientiert sich damit an dem Aufbau einer
Python Django App, bleibt dabei aber uneingeschränkt flexibel im Aufbau.

```
- .github/
  - CODEOWNERS
  - pull_request_template.md
- api/
  - endpoints.py
```
    
In dem `api/` Verzeichnis liegen die Files, die der Flask App angehören, die wiederum durch die `main.py` gestartet wird.
In der `endpoints.py` Datei werden die Endpoints der Flask REST API definiert, die die Schnittstelle zum Frontend bilden.
Dort sollen die Anfragen angenommen und selektiv an die "Task Engine" `core.py`, die jegliche Logik enthält und Datenflüsse
managed.

```
- core/
  - core.py
  - error_handler.py
  - success_handler.py
```
In dem `core/`-Verzeichnis liegen die Dateien, die die Kernfunktionalitäten der Anwendung abdecken.

- processing/
  - calculations.py
  - typeconversion.py
```

Der `processing/` folder soll alle Funktionalitäten zur Berechnung von Metriken und Aggregation von Werten einzelner
Prozesskomponenten bereitstellen. Hier erfolgt die Ergebnisermittlung.

```
- database/
  - handler/
    - component_handler.py
    - metric_handler.py
    - process_handler.py
  - config.py
  - create_queries_template.md
  - init_db.cypher
  - metrics.csv
```

Der `database/` Ordner soll alle Datenbank-bezogenen Inhalte und Funktionen enthalten, darunter die Queries (abhängig
davon, ob wir mit einem Object Mapper arbeiten können) und das Database Handler Modul, das auf den Neo4j Driver aufbaut
und die Backend-seitige Schnittstelle zur Datenbank darstellt.

```
- docu/
  - Coding Richtlinie.md
  - IntelliJ.md
  - JSON_objects_definitions.py
  - Neomodel.md
  - Repository.md
```

Das `docu/` Verzeichnis soll alle wichtigen Projektdokumentationen, Leitfäden und Guidelines enthalten, die im Repository liegen.

```
- frontend/
  - static/
    - content/
      - component-sections.json
      - de.json
      - en.json
      - mapping_metrics_definition.py
    - css/
      - einzelkomponente.css
      - styles.css
    - i18next/
    - images/
      - favicon.png
      - info.png
      - logo.png
      - penIcon.png
      - trashIcon.png
    - js/
      - dashboard-renderer.js
      - component-editor.js
      - helper.js
      - translator.js
  - templates
    - component.html
    - index.html
```

Der `frontend/` folder soll alle Inhalte für das Frontend enthalten. Im `static/` Ordner werden daher grundsätzlich alle
statischen Inhalte hinterlegt. Der Unterordner `content/` soll daher ein JSON file enthalten, worin alle Texte spezifiziert
werden, um die Templates zu entlasten und Redundanzen vermeiden zu können. Der Unterordner `css/` enthält seinem Namen
entsprechend die CSS files, in denen alle Styles definiert werden - dies dient ebenfalls der Entlastung der Templates,
in denen kein Inline-CSS verwendet werden soll. Der `i18next/` Ordner enthält die Dateien der Softwarebibliothek i18next, die für die Lokalisierung/Internationalisierung des Projekts verwendet wird. Im `images/` Unterordner sollen Bilder und Icons abgelegt werden, die
im Frontend eingesetzt werden. Hierbei ist auf die Dateigröße der Bilder zu achten, die eine bestimmte Größe nicht
überschreiten sollen. Der Unterordner `js/` enthält JavaScript Funktionen, die individuell in die Templates importiert
werden können.\
Der Ordner `templates/` soll alle Views enthalten, also eine Sammlung an HTML Templates, die an bestimmte Endpoints
angeknüpft werden.

```
- .gcloudignore
- .gitignore
- app.yaml
- cloudbuild.yaml
- config.js
- create-metrics.py
```

Die `core.py` ist die "Task Engine", die jegliche Logik enthält und Datenflüsse managed. Von hier werden alle Datenbank
Funktionalitäten, alle Berechnungsfunktionen, alle Helper angesprochen und bedient.

```
- main.py
```

Die `main.py` enthält die Flask App und startet damit die Software. Front- und Backend sind nun über die API erreichbar.

```
- README.md
```

Die `README.md` enthält wichtige Informationen zum Aufsetzen des Projektes und zum lokalen Testing.

```
- requirements.txt
```

Die `requirements.txt` enthält alle essenziellen Module, die im (virtuellen) Environment installiert werden müssen, um
das Projekt lokal zu testen.
