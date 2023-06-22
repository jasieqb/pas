# Napisz program serwera, który działając pod adresem 127.0.0.1 oraz na określonym porcie TCP, będzieserwerem poczty, obsługującym protokół IMAP. Nie realizuj faktycznego pobierania e-maili, tylko zasymu-luj jego działanie tak, żeby napisany wcześniej klient IMAP mógł pobrac wiadomosci. Pamiętaj o obsłudzeprzypadku, gdy klient poda nie zaimplementowaną przez serwer komendę.

import socket

class EmailData:
    
    def __init__(self, subject, from_, to, body):
        self.subject = subject
        self.from_ = from_
        self.to = to
        self.body = body
        self.flags = []
        
    def __str__(self):
        return f'Subject: {self.subject}\r\nFrom: {self.from_}\r\nTo: {self.to}\r\n\r\n{self.body}\r\n'
    
    def __bytes__(self):
        return str(self).encode()
    
    def __len__(self):
        return len(str(self))
    
    def __getitem__(self, key):
        return str(self)[key]
    
    def __setitem__(self, key, value):
        raise NotImplementedError
        
    def __delitem__(self, key):
        raise NotImplementedError
    
    def set_flag(self, flag):
        self.flags.append(flag)
    
    def remove_flag(self, flag):
        self.flags.remove(flag)
        
    def has_flag(self, flag) -> bool:
        return flag in self.flags
    
    def __len__(self):
        return len(str(self))
    
    
class Mailbox:
    
    def __init__(self, name, emails):
        self.name = name
        self.emails = emails
    
    def __str__(self):
        return self.name
    
    def add_email(self, email):
        self.emails.append(email)
        
    def remove_email(self, email):
        self.emails.remove(email)
        
    def __len__(self):
        return len(self.emails)
    
    def __getitem__(self, num):
        return self.emails[num]

# Sample email data to be returned by the server
# EMAILS_DATA = [[b'Subject: Test email\r\n',        b'From: sender@example.com\r\n',        b'To: recipient@example.com\r\n',        b'\r\n',        b'This is a test email.\r\n'],
#                [b'Subject: Hello World\r\n',        b'From: john@example.com\r\n',        b'To: jane@example.com\r\n',        b'\r\n',
#                    b'Hello Jane,\r\n\r\nJust wanted to say hello and see how you\'re doing.\r\n\r\nBest regards,\r\nJohn\r\n'],
#                [b'Subject: Project Update\r\n',        b'From: sarah@example.com\r\n',        b'To: mike@example.com\r\n',        b'\r\n',
#                    b'Hi Mike,\r\n\r\nI wanted to give you a quick update on the project we\'ve been working on.\r\n\r\nWe\'ve made significant progress over the past week and are on track to complete the project on time. I\'ll be sending a detailed report to you and the rest of the team later today.\r\n\r\nLet me know if you have any questions or concerns.\r\n\r\nBest regards,\r\nSarah\r\n']
#                ]

EMAILS_DATA = [EmailData('Test email', 'John Doe', 'Jane Doe', 'This is a test email.'), 
               EmailData('Hello World', 'John Doe', 'Jane Doe', 'Hello Jane,\r\n\r\nJust wanted to say hello and see how you\'re doing.\r\n\r\nBest regards,\r\nJohn'),
                EmailData('Project Update', 'Sarah Smith', 'Mike Smith', 'Hi Mike,\r\n\r\nI wanted to give you a quick update on the project we\'ve been working on.\r\n\r\nWe\'ve made significant progress over the past week and are on track to complete the project on time. I\'ll be sending a detailed report to you and the rest of the team later today.\r\n\r\nLet me know if you have any questions or concerns.\r\n\r\nBest regards,\r\nSarah')
               ]

mailboxes = [Mailbox('INBOX', EMAILS_DATA), Mailbox('Sent', [])]


def handle_client(conn):
    conn.send(b'* OK IMAP4rev1 Service Ready\r\n')
    username = None
    auth = False
    
    mailboxes = {'INBOX': Mailbox('INBOX', EMAILS_DATA), 
                 'Sent': Mailbox('Sent', [])}
    active_mailbox = 'INBOX'
    
    
    while True:
        request = conn.recv(1024).decode('utf-8').strip()
        
        tag = request.split(' ')[0]
        
        if not request:
            break
        
        if request.startswith('LOGIN '):
            username, password = request[6:].split(' ')
            if username == 'test' and password == 'test':
                conn.send(b'* OK Logged in\r\n')
                auth = True
            else:
                conn.send(b'* NO Invalid username or password\r\n')

        elif request.startswith("LIST ") and auth:
            if request == 'LIST "" *':
                
                for mailbox in mailboxes:
                    response = f'* LIST () "." "{mailbox}"\r\n'
                    exists = len(mailboxes[mailbox])
                    response += f'* {exists} EXISTS\r\n'
                    response += f'* {exists} RECENT\r\n'
                    conn.send(response.encode())
                conn.send(b'* OK Completed (Success)\r\n')
            



        # elif request == 'LIST "" *' and auth:
            
            # len_ma = len(mailboxes)
            # response = f'* LIST () "." "{active_mailbox}"\r\n'
            # for i, email in enumerate(mailboxes[active_mailbox].emails, start=1):
            #     response += f'* {i} EXISTS\r\n'
            #     response += f'* {i} RECENT\r\n'
            # response += '* OK Completed (Success)\r\n'
            # conn.send(response.encode())

        elif request.startswith('FETCH ') and auth:
            email_num = int(request.split(' ')[1])
            if email_num <= 0 or email_num > len(EMAILS_DATA):
                conn.send(b'* NO Invalid email number\r\n')
            else:
                email = EMAILS_DATA[email_num - 1]
                response = f'* {email_num} FETCH (BODY[TEXT] {len(email)}\r\n'
                response += str(email)
                response += ')\r\n'
                conn.send(response.encode())
                
        elif request.startswith('CREATE ') and auth:
            mailbox = request.split(' ')[1]
            mailboxes[mailbox] = []
            conn.send(b'* OK Mailbox created\r\n')
            
        elif request.startswith('DELETE ') and auth:
            mailbox = request.split(' ')[1]
            if mailbox in mailboxes:
                del mailboxes[mailbox]
                conn.send(b'* OK Mailbox deleted\r\n')
            else:
                conn.send(b'* NO Mailbox does not exist\r\n')
                
        elif request.startswith('RENAME ') and auth:
            old_mailbox, new_mailbox = request.split(' ')[1:]
            if old_mailbox in mailboxes:
                mailboxes[new_mailbox] = mailboxes[old_mailbox]
                del mailboxes[old_mailbox]
                conn.send(b'* OK Mailbox renamed\r\n')
            else:
                conn.send(b'* NO Mailbox does not exist\r\n')
            
        elif request.startswith('SELECT ') and auth:
            mailbox = request.split(' ')[1]
            if mailbox in mailboxes:
                active_mailbox = mailbox
                conn.send(b'* OK Mailbox selected\r\n')
        
        elif request.startswith('STORE ') and auth:
            mail, flag = request.split(' ')[1:]

            if flag.startswith('+'):
                mailboxes[active_mailbox][int(mail) - 1].flags.add(flag[1:])
            
            elif flag.startswith('-'):
                mailboxes[active_mailbox][int(mail) - 1].flags.remove(flag[1:])
            
            else:
                conn.send(b'* NO Invalid flag\r\n')
            
            conn.send(b'* OK Flag updated\r\n')
        
        elif request.startswith('SEARCH ') and auth:
            params = request.split(' ')[1:]
            
            if len(params) == 1 and params[0] == 'ALL':
                response = '* SEARCH '
                for i, email in enumerate(mailboxes[active_mailbox], start=1):
                    response += str(i)
                    if i < len(mailboxes[active_mailbox]):
                        response += ' '
                response += '\r\n'
                conn.send(response.encode())
            
            elif len(params) == 1 and params[0] == 'NEW':
                response = '* SEARCH '
                
                for i, email in enumerate(mailboxes[active_mailbox], start=1):
                    if not '\Seen' in email.flags:
                        response += str(i)
                        if i < len(mailboxes[active_mailbox]):
                            response += ' '
                response += '\r\n'
                conn.send(response.encode())
                
            else:
                
                conn.send(b'* NO Invalid search criteria\r\n')
            
        
        elif request == 'LOGOUT':
            conn.send(b'* BYE IMAP4rev1 Server logging out\r\n')
            auth = False
            break

        else:
            conn.send(b'* BAD Command not recognized\r\n')

    conn.close()


while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 1431))
    s.listen(1)
    conn, addr = s.accept()
    print("Connected by", addr)
    handle_client(conn)
