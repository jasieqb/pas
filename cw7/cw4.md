## Wykorzystując protokół telnet, oraz wybrany serwer POP3, wyświetl treść wiadomości o największym rozmiarze.

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
RETR 1
+OK 1 octets
Subject: Project Update
From: sarah@example.com
To: mike@example.com

Hi Mike,
I wanted to give you a quick update on the project we\'ve been working on.We\'ve made significant progress over the past week and are on track to complete the project on time. I\'ll be sending a detailed report to you and the rest of the team later today.
Let me know if you have any questions or concerns.
Best regards,
Sarah'
.
```
