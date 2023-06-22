## Wykorzystując protokół telnet, oraz wybrany serwer POP3, sprawdź, ile wiadomości znajduje się w skrzynce.

```bash
telnet localhost 110
USER test
+OK
PASS test
+OK Logged in.
STAT
+OK 3 160
```
