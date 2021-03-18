#Object Mapper
>_Neomodel ist ein Object Mapper für neo4j.  
Die Datenbank kann dadurch komplett ohne die eigene DQL Cypher genutzt werden._

##Nodes


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
