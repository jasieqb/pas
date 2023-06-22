## Wykorzystując protokół telnet, oraz wybrany serwer POP3, usuń wiadomość o najmniejszym rozmiarze

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
DELE 3
+OK Message deleted.
```
