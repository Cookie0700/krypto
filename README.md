# krypto

### Aufgabe 
-> ca. 5-Runden S-Box Algorithmus
-> 10-20 Bit Plain-Text

a) Charakteristik mit hoher Wahrscheinlichkeit
b) dominante Approximation

| Name                                       | Vorlesung                    | Variable |
|:-------------------------------------------|:-----------------------------|:---------|
| S-Box                                      | nicht linear, "schlecht"     |          |
| Permutation                                | -                            |          |
| Runden                                     | r = 5                        |          |
| Blocklänge                                 | n = 10 bit                   |          |
| Eingabedifferenz                           | ΔE                           |          |
| Ausgabedifferenz                           | ΔA                           |          |
| S-Box 1                                    | S1                           |          |
| S-Box 2                                    | S2                           |          |
| Wahrscheinlichkeit für Differenzenübergang | p                            |          |
| Charakteristik                             | D = (D0 = D1 = D2 = D3 = D4) |          |
| Kandidaten für richtige Schlüssel          | Dr-1                         |          |




### Nichtlinearität überprüfen (S. 140)
Nicht-linear = Nicht additiv/homogen
110  = S1(011) = S1(101 + 110) /= S1(101) + S1(110) = 111 + 101 = 010
100 = S2(110) = S2(100 + 010) a/= S2(100) + S2(010) = 000 + 010 = 010

### Differenzentabelle
Charakteristik = Folge von Differenzen (an D0, D1 bereits erkennbar)
Blocklänge 10 bit -> ΔE von 0 bis (2^10 = 1024) 1023

### Schlüsselkandidaten
Dr-1 -> D0 - D4
2^5 Ausgabemöglichkeiten für D0
