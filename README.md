# bibliotheekreader
A Python script that integrates the goodreads api with the Flemish public library system.
Example output:

```
#####################################################################################
###   Tommy Wieringa                 Caesarion                                         
#####################################################################################
Tommy Wieringa                Caesarion : roman                                 Hoofdbibliotheek     Uitgeleend tot 11-05-2016
Tommy Wieringa                Dit zijn de namen : roman                         Hoofdbibliotheek     Beschikbaar
Onbekend                      Lexicon van literaire werken : besprekingen van N Hoofdbibliotheek     Beschikbaar
#####################################################################################
###   Jeroen Brouwers                Geheime kamers                                    
#####################################################################################
Jeroen Brouwers               Geheime kamers                                    Hoofdbibliotheek     Beschikbaar
Rudi van der Paardt           Een fatale obsessie : over "Geheime kamers" van J Hoofdbibliotheek     Beschikbaar
Ron Elshout                   Een spiegelpaleis : over Geheime kamers van Jeroe Hoofdbibliotheek     Beschikbaar
Karel Segers                  'Het is een poppenkast, hé ? Ik wil de volstrekte Hoofdbibliotheek     Beschikbaar
#####################################################################################
###   Erwin Mortier                  Godenslaap                                        
#####################################################################################
Erwin Mortier                 Godenslaap : roman                                Hoofdbibliotheek     Beschikbaar
Erwin Mortier                 Godenslaap : roman                                Dorpshuis Muizen     Beschikbaar
Erwin Mortier                 Gestameld liedboek : moedergetijden               Hoofdbibliotheek     Uitgeleend tot 03-05-2016
Erwin Mortier                 De spiegelingen : roman                           Hoofdbibliotheek     Beschikbaar
Sven Vitse                    Er zijn te veel woorden : Erwin Mortier oog in oo Hoofdbibliotheek     Beschikbaar
Johanna Cassiers              Godenslaap                                        Hoofdbibliotheek     Beschikbaar
#####################################################################################
###   Tom Lanoye                     Sprakeloos                                        
#####################################################################################
Tom Lanoye                    Sprakeloos                                        Hoofdbibliotheek     Beschikbaar
Tom Lanoye                    Sprakeloos                                        Dorpshuis Heffen     Beschikbaar
Martine Cammaert              Sprakeloos : Tom Lanoye : werkmap voor leesgroepe Hoofdbibliotheek     Beschikbaar
René Appel                    Goesting in taal : interview met schrijver Tom La Hoofdbibliotheek     Beschikbaar
Cor Gerritsma                 Tom Lanoye                                        Hoofdbibliotheek     Beschikbaar
Hans Demeyer                  'Een liefdevolle liquidatie' : het autobiografisc Hoofdbibliotheek     Beschikbaar
Mark Cloostermans             'Sprakeloos', het slot van een lot                Hoofdbibliotheek     Beschikbaar
```

## Bibliotheek API
The script uses a non-production TEST key for Antwerp province from https://docs.google.com/spreadsheets/d/1IMSaNgcQNpE6KC_tgzyCRkXh6yUBF8rn_lyjrd6bUaM/edit#gid=14.
The link also has TEST keys for other provinces. Insert this key into the config.py python file.

## Goodreads API
The goodreads api needs a secret key from https://www.goodreads.com/api. Fill these in in the config.py python file. You also need your id, from your goodreads profile page (e.g. https://www.goodreads.com/user/show/20527584-roel, id=20527584).
