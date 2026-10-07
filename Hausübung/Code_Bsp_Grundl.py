import datetime as dt
## Python Kontrollstrukturen Übung

## if, schleifen, break, pass, try-except je ein beispiel
## if:
datum = dt.datetime.now()

print(datum)

if dt.datetime.now() <= datum:
    print("kann nicht ausgegeben werden")

elif datum <= dt.datetime.now():
    print("Muss ausgegeben werden da die datum var vor der if definiert wird und dadurch älter ist als der vergleichswert")

print ('####################################################################################################')


## Schleifen:
## for mit break:
reihe = [1,2,3,4,5,6,7,8,9,]
for i in reihe:
    print(i)
    if i== 6:
        break
    

print ('####################################################################################################')

## while:

i = 0
while i < 10:
    i += 1
    print(i)


print ('####################################################################################################')

## pass

class Haus:
    pass            ## da passiert nicht weil pass als platzhalter dient für noch nicht implementierte sachen (wie in dem fall die Klasse Haus)

## try except: 

try:                    ## ist wie try, catch in java. except ist hier einfach das catch
    print(91/0)
                        ## try catch finally in java
                        ## in python gibt es try, except, else, finally
except ZeroDivisionError:
    print("Division durch 0")
else:
    print("Keine Division durch 0")
finally:                    ## wird immer ausgeführt das man Rückmeldung gibt, keine Daten verloren gehen, wenn man datei öffnet 
                            ## dann fehler läuft dann ist datei immer noch offen gleich wie in datenbank offen ist. 
                            ## Deshalb im finally für ressourcen die was großes aufmachen und bearbeiten das es geschlossen wird
    print("Dieser Code wird immer ausgeführt")

print ('####################################################################################################')


## Bedingte Ausdrücke

## ist dafür da das man sachen kürzer darstellen kann 
x =4
print("ist größer als 5" if x > 5 else "Kleiner als 5")       

print ('####################################################################################################')

## Match Case (Switch Case in Java) 

day = "Mittwoch"

match day:
    case "Montag" | "Dienstag" | "Mittwoch" | "Donnerstag" | "Freitag":
        print("Wochentag")
    case "Samstag" | "Sonntag":
        print("Wochenende")