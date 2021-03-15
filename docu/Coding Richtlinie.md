# Richtlinie

## Das Board

* **To Do**: enthält User Stories, die umgesetzt werden sollen (gerne zuweisen und daran arbeiten)
* **In Progress**: enthält User Stories, die zugewiesen sind und an denen gerade gearbeitet wird
* **In Review**: enthält User Stories, an denen gearbeitet wurde, für die nun ein Pull Request erstellt wurde. Diese User Stories warten auf eine Review.
* **Done**: enthält User Stories, die eine Review erhalten haben und in Master gemergt wurden

Zum Trello-Board geht es [hier](https://trello.com/b/AqaojpJG/technische-gilde).

## Der Entwicklungsprozess

Für jede Implementation einer User Story sollten die folgenden Schritte durchgeführt werden:

1. Aussuchen einer User Story aus **To Do** zur Entwicklung je nach abgesprochener Priorität, basierend auf eigenen Fähigkeiten
2. Zuweisen der beteiligten Studierenden zu der User Story und verschieben nach **In Progress**
4. Die Entwicklung sollte auf der aktuellsten Version des __master branch__ basiert werden und ein __feature branch__ pro User Story für die erforderlichen Umsetzungen angelegt werden. Dabei sollte dem Namen des __feature branches__ die Kartennummer der User Story vorangestellt sein:
    ```
    git checkout master
    git pull
    # The branches should always have a meaningful title
    git checkout -b XXX_small_description 
    ```

   (Ein __feature branch__ mit dem Namen "XXX_small_description" ist hierbei ein eigenständiger Branch, der nur für die Entwicklung dieser einen User Story verwendet und dafür extra angelegt wird.)
   (Die Kartennummer findet sich auf der Trello-Karte unter "Teilen".)

5. Lokales Entwickeln und Testen der Änderungen auf diesem __feature branch__, dabei immer wieder commiten und pushen ins GitHub repository zur gemeinsamen Arbeit (auch hier ist die User Story Nummer der commit-Message vorangestellt):
    ```
    git add file1.js ...
    git commit -m "XXX: Description of the code changes"
    # First push
    git push -u origin XXX_small_description
    # Following pushes
    git push XXX_small_description
    ```

7.  Erstellen eines pull request (aka "merge request") von __feature branch__ in __master branch__ basierend auf dem pull request template. Als Titel des pull request sollte der Titel, sowie die Nummer der User Story verwendet werden:
    ```
    XXX: User Story Titel
    ```

8. Ausfüllen aller Informationen in dem pull request template, sowie Hinzufügen des fachlichen Verantwortlichen als (funktionalen) Reviewer und Zuweisen des pull requests an den funktionalen Reviewer.
9. Bewegen der User Story in **In Review**
10. Lösen aller Konflikte, die angezeigt werden, wenn der pull request erstellt wurde. Dabei sollten lokal die letzten Änderungen im __master branch__ gezogen werden, der __master branch__ in den __feature branch__ germergt werden und alle auftretenden Konflikte auf dem __feature branch__ gelöst werden:
    ```
    # checkout the master branch and get the latest changes
    git checkout master
    git pull
    git checkout XXX_feature_branch
    git merge master
    # at this point conflicts are typically shown, marked in files with <<< and >>> characters. The conflicts should be resolved and the files need to be added and commited to the feature branch
    git add some_conflict_file.js
    # Once done, git status command should show no conflicts on the feature branch
    git status
    # create a merge commit for the changes
    git commit 
    # push the feature branch to gitlab
    git push origin XXX_feature_branch
    ```

9. Funktionale Review:
    12. Eine funktionale Review enthält:
        1.  Frontend: Prüfung der Funktionalität und der Acceptance Criteria
        2.  Backend: Prüfung der Funktionalität und vorhandener UnitTests
        3.  Database: Prüfung der Funktionalität
    13. Jegliche erforderlichen funktionalen Anpassungen werden zur Nachvollziehbarkeit direkt auf GitHub über die Kommentarfunktion dokumentiert. Dabei wird der entsprechende User Story Ansprechpartner kontaktiert.
    14. Wenn Änderungen vorgeschlagen werden, markiert der funktionale Reviewer den pull requestmit einem `WIP: ` Präfix und weist diesen dem User Story Ansprechpartner zu.
    15. Lösen aller Änderungen durch die verantwortlichen Studierenden auf dem __feature branch__ und pushen der neuen Version auf GitHub. Entfernen des WIP Präfix, sodass der pull request erneut gereviewt werden kann und Zuweisen an den funktionalen Reviewer.
    16. Erneute Review des pull request - Wiederholen des Prozesses ab Schritt 9 (auch mehrere Wiederholungen möglich)
    17. Keine Änderungen mehr nötig: Approve durch den funktionalen Reviewer und Zuweisen an die Code Reviewer

10. Code Review:
    11. Der pull request wird von einem Code Reviewer (Jonathan oder Jasmin) aufgenommen, dieser weist nur sich den pull request zu
    12. Eine Code Review enthält:
        1.  Review des Codes mit Überprüfung auf mögliche Verbesserungen und potentielle Probleme.
        2.  Prüfen, ob das in der User Story beschriebene Feature programmiert ist.
    13. Jegliche erforderlichen Code-Anpassungen werden zur Nachvollziehbarkeit direkt auf GitHub über die Kommentarfunktion dokumentiert. Dabei wird der entsprechende User Story Ansprechpartner kontaktiert.
    14. Wenn Änderungen vorgeschlagen werden, markiert der Code Reviewer den pull requestmit einem `WIP: ` Präfix und weist diesen dem User Story Ansprechpartner zu.
    15. Lösen aller Änderungen durch die verantwortlichen Studierenden auf dem __feature branch__ und pushen der neuen Version auf GitHub. Entfernen des WIP Präfix, sodass der pull request erneut gereviewt werden kann und Zuweisen an den Code Reviewer.
    16. Erneute Code Review des pull request - Wiederholen des Prozesses ab Schritt 9 (funktionale Review) (auch mehrere Wiederholungen möglich)
    17. Keine Änderungen mehr nötig: Approve durch den Code Reviewer

17. Bei erfolgreicher Umsetzung: mergen des __feature branches__ in den __master branch__ durch den Reviewer.
18. Bewegen der User Story in **Done** durch den Reviewer

## Das Programmieren

### Allgemein

Für das Entwickeln sollten folgende Punkte beachtet werden:

* Der Code ist ein Gemeinschaftswerk. Es ist das Anliegen von jedem, den Code weiterzuentwickeln und dabei zu verbessern.
* Anmerkungen und Änderungskommentare zum Code (beispielsweise durch eine Review) sind daher keine persönliche, sondern konstruktive Kritik und sollten auf einer objektiven Ebene kommuniziert werden.
* Der Code ist angemessen zu dokumentieren:
    * docstrings zur Funktions- bzw Methodendefinition \
      Python:
      ```
      def subtract(minuend: int, subtrahend: int) -> int:
          """
          Subtracts two numers and returns the result
      
          :param minuend: The minuend to be subtracted from
          :type minuend: int
          :param subtrahend: The subtrahend to subtract
          :type subtrahend: int
          :return: The difference
          """
      ```

      Javascript:
      ```
      /**
      * Returns x raised to the n-th power.
      *
      * @param {number} x The number to raise.
      * @param {number} n The power, must be a natural number.
      * @return {number} x raised to the n-th power.
      */
      function pow(x, n) {
      ...
      }
      ```

    * Inline-Kommentare \
      Python:
      ```
      # calculate the difference
      difference = minuend - subtrahend
      ```

      Javascript:
      ```
      // calculate the difference
      difference = minuend - subtrahend
      ```

* Alle Klassen, Methoden, Funktionen und Variablen sind auf Englisch und aussagekräftig zu benennen (also ohne Grund nicht num1, num2, res, ...).
* Der python Code sollte der PEP 8 Richtlinie genügen.
* Es ist modular und objektorientiert zu programmieren.
    * ...
    
### Frontend-Besonderheiten

Statische Inhalte sollen nicht inline in den Views referenziert werden, weder inline, noch gesammelt in etwa `<script>`
oder `<style>` Tags, sondern in Dateien ausgelagert werden. Darunter fallen insbesondere folgende statische Inhalte:
* CSS Styles, die unter `static/css/style.css` abgelegt werden sollten
* JS Funktionen, die unter `static/js/<filename>.js` abgelegt werden sollten
* Statische Texte, die im i18next JSON file unter `static/content` ablegt werden sollten
* Statische Inhalte wie Icons, Images und sonstige Dateien, die unter `static/images` abgelegt werden sollten und deren
  Dateigröße 500kB im Normalfall nicht überschreiten sollte
