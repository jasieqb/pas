## Wykorzystując protokół telnet, oraz wybrany serwer POP3, sprawdź, ile bajtów zajmuje każda wiadomość(z osobna) znajdująca się w skrzynce.

```bash
telnet localhost 110
USER test
+OK
PASS test
+OK Logged in.
LIST
+OK 3 messages (160 bytes)
1 180
2 80
3 0
. 
```
