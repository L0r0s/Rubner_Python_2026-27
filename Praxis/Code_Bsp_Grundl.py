import datetime as dt
## Python Kontrollstrukturen Übung

## if, schleifen, break, pass, try-except je ein beispiel
## if:
datum = dt.datetime.now()

print(datum)

if datum <= dt.datetime.now():
    print("Muss ausgegeben werden da die datum var vor der if definiert wird und dadurch älter ist als der vergleichswert")

if dt.datetime.now() <= datum:
    print("kann nicht ausgegeben werden")