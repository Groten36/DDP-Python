
def user():
    anu = True
    while anu:
        print("""
        1.Zapisz sie do konferencji
        2.Wypisz sie z konferecji
        3.Wyswietl konferencje w ktorych uczestniczysz
        """)
        anu = int(input("Wybor: "))
        if anu == 1:
            print("Dodawanie do konferencji")
        elif anu == 2:
            print("Wypisywanie z konferencji")
        elif anu == 3:
            print("Twoje konferencje")


def admin():
    ana = True
    while ana:
        print("""
        1.Dodaj konferencje
        2.Usun konferencje
        3.Wyswietl wszystkie konferencje
        """)
        ana = int(input("Wybor: "))
        if ana == 1:
            print("Dodawanie konferencji")
        elif ana ==2:
            print("Usuwanie konferencji")
        elif ana ==3:
            print("KOnferencje: ")



ans = True
while ans:
    print("""
    1.Administrator
    2.Uczestnik
    """)
    ans = int(input("Kim jestes? "))
    if ans == 1:
        print("Administrator")
        admin()
    elif ans == 2:
        print("Uczestnik")
        user()

