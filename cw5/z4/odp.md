# Wyniki
## Dla którego z gniazd czas jest krótszy?
TCP: 0.0004508495330810547
UDP: 0.0003097057342529297
**UDP > TCP**
## Z czego wynika krótszy czas?
UDP nie wymaga potwierdzenia odbioru, więc nie musi czekać na potwierdzenie, a TCP musi czekać na potwierdzenie, żeby wysłać kolejny pakiet.

## Jakie są zalety / wady obu rozwiązań?
**TCP:**
+:
* Niezawodny
* Gwarancja dostarczenia
* Kontrola przepływu
-:
* Wolny
* Większy czas oczekiwania przez potwierdzenie
* 

**UDP:**
+:
* Szybki
* Mały czas oczekiwania
-:
* Nie kontroluje dostarczenia

