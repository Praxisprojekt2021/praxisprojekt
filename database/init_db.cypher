//Delete all nodes and relationships
MATCH (n)
DETACH DELETE n

//Create all nodes and relationships
CREATE
  (`Process 1`:Process {name:               'Kunde anlegen', description: 'Kunde anlegen im System',
                        creation_timestamp: datetime(),
                        last_timestamp:     datetime()})
    -[:should {should: 10}]->(Ausfallzeit:Metric {name:        'Ausfallzeit',
                                                  description: 'Durchschnittliche Ausfallzeit in Minuten pro Tag'})
    <-[:IS {IS: 3}]-(`Frontend API`:Component {name:               'Frontend API',
                                               description:        'API für die Frontend View',
                                               creation_timestamp: datetime(), last_timestamp: datetime(),
                                               category:           'API'})
    <-[:includes {weight: '1,5'}]-(`Process 1`)-[:includes {weight: 1}]->
  (`Oracle DB`:Component {name:               'Oracle Datenbank', description: 'Kundendatenbank',
                          creation_timestamp: datetime(),
                          last_timestamp:     datetime(), category: 'Datenbank'})
    -[:IS {IS: 10000}]->(Codezeilen:Metric {name: 'Codezeilen', description: 'Anzahl von Codezeilen'})
    <-[:should {should: 5000}]-(`Process 1`),
  (`Ausfälle`:Metric {name: 'Ausfälle', description: 'Anzahl von Ausfällen pro Jahr'})<-
  [:IS {should: 3}]-(`Notification API`:Component {name:               'Notification API',
                                                   description:        'API für die Frontend View',
                                                   creation_timestamp: datetime(),
                                                   last_timestamp:     datetime(), category: 'API'})
    -[:IS {IS: 3}]->(Ausfallzeit)
    <-[:should {should: 10}]-(`Process 2`:Process {name:               'Kunde löschen',
                                                   description:        'Kunde löschen im System',
                                                   creation_timestamp: datetime(), last_timestamp: datetime()})
    -[:should {should: 5}]->(`Ausfälle`)<-[:should {should: 5}]-(`Process 1`)
    -[:includes {weight: 2}]->(Webserver:Component {name:               'Webserver',
                                                    description:        'Webserver auf dem die Frontend View läuft',
                                                    creation_timestamp: datetime(), last_timestamp: datetime(),
                                                    category:           'Server'})-[:IS {IS: 1500}]->(Codezeilen)
    <-[:IS {IS: 5000}]-(`Frontend API`),
  (Ausfallzeit)<-[:IS {IS: 5}]-(Webserver)-[:IS {IS: 3}]->(`Ausfälle`),
  (Codezeilen)<-[:should {should: 5000}]-(`Process 2`)-[:includes {weight: 1}]->(`Oracle DB`),
  (`Process 2`)-[:includes {weight: '1,5'}]->(`Notification API`)

//Show the result
match (n) return n
