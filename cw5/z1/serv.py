# Napisz program serwera, który działając pod adresem 127.0.0.1 oraz na określonym porcie TCP będzie
# losował liczbę i odbierał od klienta wiadomości. W przypadku, gdy w wiadomości klient przyśle do serwera
# coś innego, niż liczbę, serwer powinien poinformować klienta o błędzie. Po odebraniu liczby od klienta,
# serwer sprawdza, czy otrzymana liczba jest:
# • mniejsza od wylosowanej przez serwer
# • równa wylosowanej przez serwer
# • większa od wylosowanej przez serwer
# A następnie odsyła stosowną informację do klienta. W przypadku, gdy klient odgadnie liczbę, serwer
# powinien zakończyć działanie.
