import os


def z1():
    path = input("Podaj ścieżkę do pliku: ")
    if os.path.isfile(path):
        print("Plik istnieje")
    else:
        print("Plik nie istnieje")
        exit()

    with open(path, "r") as file_read, open('lab1zad1.txt', "w") as file_write:
        data = file_read.read()
        file_write.write(data)


if __name__ == "__main__":
    z1()
