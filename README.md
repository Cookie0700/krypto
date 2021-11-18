# krypto

### Allgemeines
Wichtigste Methoden zum Angriff auf symmetrische Chiffren
-> differenzielle Kryptanalyse
-> lineare Kryptanalyse

### Aufgabe 
-> 5-Runden S-Box-Algorithmus
-> 10 Bit Plaintext P
-> Schlechte S-Boxen

a) Charakteristik mit hoher Wahrscheinlichkeit (-> Schlüsselberechnung)
b) dominante Approximation

| Name                                       | Vorlesung                    | Code |
|:-------------------------------------------|:-----------------------------|:-----|
| S-Box 1, nicht linear                      | S1                           |      |
| S-Box 2, nicht linear                      | S2                           |      |
| Runden                                     | r = 5                        |      |
| Blocklänge                                 | n = 10 bit                   |      |
| Permutation                                | -                            |      |
| Eingabepaar erste Runde                    | P, P'                        |      |
| Eingabepaar Runde r                        | Tr, Tr'                      |      |
| Ausgabepaar letzte Runde                   | C, C'                        |      |
| Eingabedifferenz                           | ΔE = T0 + TO'                |      |
| Ausgabedifferenz                           | ΔA                           |      |
| Schlüssel zur Verschlüsselung              | K                            |      |
| Wahrscheinlichkeit für Differenzenübergang | p                            |      |
| Charakteristik                             | D = (D0 = D1 = D2 = D3 = D4) |      |
| Übereinstimmung Eingabe                    | RE                           |      |
| Übereinstimmung Ausgabe                    | RA                           |      |
| Anzahl an Übereinstimmungen                | RE & RA                      |      |

### Nichtlinearität
* Bruteforce z.B. 2^64 Versuche -> linear: 64 Versuche
* Lineare S-Box mit gewähltem P (= chosen plaintext) sehr unsicher!
* Nicht-linear = Nicht additiv/homogen

```
# Überprüfung (vgl. S. 140):
110 = S1(011) = S1(101 + 110) /= S1(101) + S1(110) = 111 + 101 = 010
100 = S2(110) = S2(100 + 010) /= S2(100) + S2(010) = 000 + 010 = 010
```

### Charakteristik
* unterschiedliche Paare der Eingabedifferenz
--> unterschiedliche Paare der Ausgabedifferenz
* Charakteristik = Folge von Differenzen (an D0, D1 bereits erkennbar)
* Dieselbe Eingabe (P, P') liefert mehrere Möglichkeiten für Charakteristiken
--> Gewisse WSK für jede Charakteristik

### Differenzentabelle
* Ausgabedifferenz ΔA hängt von Eingabedifferenz ΔE und P bzw. P' ab
```
ΔA (ΔE, P)
```
* Bei n Bit auch 2^n mögliche Differenzen
--> Blocklänge 10 bit -> ΔE von 0 bis (2^10 = 1024) 1023

### Schlüsselkandidaten
* Mit Dr-1 (hier: vorletzte Runde -> D4) Menge an Kandidaten für richtigen Schlüssel
* Übergangswahrscheinlichkeiten berechnen
--> Beim Zurückrechnen zu WSK X der richtige Schlüssel

__Beispiel__

| D0   | 01110 | 01110 | 01110 | 01110 | 01110                          |
|:-----|:------|:------|:------|:------|:-------------------------------|
| D1   | ...   | ...   | ...   | ...   | ... (2^5 Ausgabemöglichkeiten) |
| D2   | ...   | ...   | ...   | ...   | ...                            |
| ...  | ...   | ...   | ...   | ...   | ...                            |
| Dr-1 | 10000 | 01000 | 00100 | 00011 | ...                            |
| WSK  | 0.6   | 0.1   | 0.1   | 0.05  | ... (0.15)                     |

--> Prozentuale Gleichverteilung = Erhöhte Sicherheit

### (Lineare Approximation)
__Beispiel__

| Input          | `x1` | `x2` | `x3` | x4 | x5 |
|:---------------|:-----|:-----|:-----|:---|:---|
| Output (S-Box) | y1   | `y2` | `y3` | y4 | y5 |

* Zusammenhang zwischen Input und Output? 
* Betrachtung für jede Eingabe
* Wie wahrscheinlich ist es, dass aus Input der Output folgt?
--> Lineare Approximation: `1/2 ± ε`
* Schlechte S-Box: Erstes Input-Bit stimmt mit letztem Output-Bit überein

### Verwendete Tools
__Programme:__
* Visual Studio Code
* Markdown Editor
* Sublime Text
* obsidian

__Websites:__
* github.com
* draw.io

__Visual Studio Code Erweiterungen:__
* Git Graph
* Edit csv
* Markdown All in One
* Rainbow CSV
* Draw.io Integration