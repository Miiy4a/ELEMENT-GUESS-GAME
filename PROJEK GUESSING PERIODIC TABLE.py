import random

def main():
    """Start a elemen guessing game."""
    print("Selamat datang di game elemen")
    print("Dibawah telah diberi pilihan simbol elemen, sila jawab soalan berikut")

    elemen = [
        "H",
        "Li",
        "Ti",
        "Sr",
        "Hs",
        "In",
        "Sn",
        "Si",
        "C",
        ]

    x = random.choice(elemen)
    print("Ini adalah simbol elemen anda: ",x)
    print("__________________________________________________________")

main()

    
class element:
    def __init__(self, sym, name, no, typ, row, col):
        self.symbol = sym
        self.name = name
        self.atomic_number = no
        self.elem_type = typ
        self.row = row
        self.column = col


def viewElement(element, n):
    print("Name: " + element.name)
    if n == 2 or n == 3:
        print("Symbol: " + element.symbol)
    if n == 2 or n == 4:
        print("Atomic Number: " + str(element.atomic_number))
    if n == 2 or n == 5:
        print("Type: " + element.elem_type)
    if n == 2 or n == 6:
        print("Row: " + str(element.row))
    if n == 2 or n == 7:
        print("Column: " + str(element.column))

    print("\n")



if __name__ == "__main__":
    elem_dict = {}

    while 1:
        print("Main Menu")
        print("1.Masukkan elemen")
        print("2.TAMAT")
        choice = int(input("Masukkan pilihan anda: "))

        if choice == 1:
            sym = input("Masukkan simbol elemen: ")
            name = input("Masukkan nama elemen: ")
            atom = int(input("Masukkan nombor atom: "))
            typ = input("Masukkan jenis elemen: ")
            row = int(input("Masukkan nombor baris elemen: "))
            col = int(input("Masukkan nombor lajur elemen: "))
        

            if sym not in elem_dict.keys():
                e1 = element(sym, name, atom, typ, row, col)
                elem_dict[sym] = e1
                print(sym + " added\n")
            else:
                print("Elemen dijumpai")

        elif choice == 2:
            print("TAMAT")
            break
        
        else:
            print("Sila cuba lagi")

