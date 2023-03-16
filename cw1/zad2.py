import os


def z1():
    path = input("Podaj ścieżkę do pliku: ")
    if os.path.isfile(path):
        print("Plik istnieje")
    else:
        print("Plik nie istnieje")
        exit()

    with open(path, "rb") as file_read, open('lab1zad2.png', "wb") as file_write:
        data = file_read.read()
        file_write.write(data)


if __name__ == "__main__":
    z1()
