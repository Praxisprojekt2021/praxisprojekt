#Object Mapper
>_Neomodel ist ein Object Mapper für neo4j.  
Die Datenbank kann dadurch komplett ohne die eigene DQL Cypher genutzt werden._

##Nodes
Jede Art von Node, die wir in der Datenbank vorfinden muss als Klasse in unserem Handler hinterlegt sein. Lesen wir dann Nodes aus der Datenbank aus, werden diese dann als Python-Objekte zurückgegeben ud können auch so weiter verarabeitet werden. 
Jedes Merkmal, dass unsere Node haben soll muss als Attribut in der Klasse angelegt werden. Dazu gehören auch Relationships (siehe unten). Der Datentyp sollte für jedes Attribut analog zum Datentyp in der Neo4j-Datenbank angelegt werden. Dafür stehen uns verschiedene hinterlegte Klassen zur Verfügung.:

> AliasProperty  
> IntegerProperty
ArrayProperty	        JSONProperty
BooleanProperty	        RegexProperty
DateProperty	        StringProperty (Notes)
DateTimeProperty        UniqueIdProperty
DateTimeFormatProperty  PointProperty
FloatProperty

Für die Änderung der Attribute werden Getter und Setter Methoden genutzt. Diese müssen ebenfalls pro Node (und Attribut) erstellt werden. Wir schreiben nicht direkt mit unseren Handlerfunktionen in die Objekte rein! 

Eine Klasse, die einen Node darstellt kann so aussehen:

```
class Person(Structured Node):
    id = UniqueIdProperty()
    name = StringProperty()
    age = IntegerProperty()
```

Eine Getter Methode sieht so aus:

```
def return_age(id):
    person = Person.nodes.get(id=id)
    return person.age
```

Eine Setter Methode sieht so aus:
```
def change_age(name, new_age):
    person = Person.nodes.get(id=id)
    person.age = new_age
    person.save()   
```

##Relationships
Nodes=Klassen=Komponenten können in Beziehungen zueinander stehen.  
Beispielhaft:
```
class Person(StructuredNode):
    vorname = StringProperty() 
    car = RelationshipTo('Car', 'OWNS', cardinality=One) 

class Car(StructuredNode):
    fahrgestell_nr = UniqueIdProperty()
    owner = RelationshipFrom('Person', 'OWNS', cardinality=One)
```
Schema:
> identifier = "Relationship(From/To/)('Ziel / Herkunft', 'Label', cardinality=_)"

Diese Beziehungen haben funktionale Ähnlichkeit mit joins relationaler Datenbanken

###Kardinalität
Cardinality kann folgende Werte annehmen:
> ZeroOrMore (default)  
> ZeroOrOne  
> One  
> OneOrMore

##Aufrufe
In database/handler/component_handler.py implementiert sind die Methoden:
> ___get_component_list___ gibt mehrere Komponenten zurück  
> ___get_component___ gibt eine Komponente zurück  
>
> ___add_component___ fügt eine Komponente hinzu  
> ___update_component___ ändert eine vorhandene Komponente  
> ___delete_component___ löscht eine vorhandene Komponente


##Offizielle Dokumentation
>https://github.com/neo4j-contrib/neomodel  
>https://neomodel.readthedocs.io/en/latest/  
>https://pypi.org/project/neomodel/  
