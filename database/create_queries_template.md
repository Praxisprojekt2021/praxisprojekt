# Query Vorlagen
###***Subject to Change***  
Ansprechpartner: Timo Bücher  
Stand: 18.03.2021  


## Objekte

### Metriken
 ```
 CREATE (`Ausfälle`: Metric 
 { 
    name: 'Ausfälle', 
    description: 'Anzahl von Ausfällen pro Jahr'
 })
 ```

### Komponenten
 ```
 CREATE (`Frontend API`: Component 
 {
    name: 'Frontend API', 
    description: 'API für die Frontend View', 
    creation_timestamp: datetime(), 
    last_timestamp: datetime(), 
    category: 'API'
 })
 ```

### Prozesse
 ```
CREATE (`Kunde Anlegen`: Process 
{
    name: 'Kunde anlegen', 
    description: 'Kunde anlegen im System', 
    creation_timestamp: datetime(), 
    last_timestamp: datetime()
})
 ```

## Beziehungen

### Prozess beinhaltet Komponente
```
MATCH
  (a:Process),
  (b:Component)
WHERE a.name = 'Kunde löschen' AND b.name = 'Frontend API'
CREATE (a)-[r:includes{weight: '2'}]->(b)
RETURN type(r)
```

### Komponente hat IST-Wert einer Metrik
```
MATCH
  (a:Component),
  (b:Metric)
WHERE a.name = 'Webserver' AND b.name = 'Ausfallzeit'
CREATE (a)-[r:IS {IS: 5}]->(b)
RETURN type(r)
```

### Komponente hat Soll-Wert einer Metrik
```
MATCH
  (a:Process),
  (b:Metric)
WHERE a.name = 'Kunde anlegen' AND b.name = 'Ausfallzeit'
CREATE (a)-[r:should {should: 5}]->(b)
RETURN type(r)
```
