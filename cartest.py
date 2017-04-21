'''
Program "Car Manager"
1.Auta
    1.1.Wyswietl wszystkie auta
    1.2.Dodaj nowe auto
    1.3.Usun auto
2.Trasy
    2.1.Pokaz dostepne trasy
    2.2.Dodaj trase
    2.3.Usun trase
3.O Autorze
'''
MainList= [
'1-Auta',
'2-Trasy',
'3-Informacje o programie',
"4-Spis funkcji programu",
"0-Wyjście z programu"]
AutaList= [
"1-Wyswietl wszystkie auta",
"2-Dodaj nowe auto",
"3-Usun auto",
"4-Powrót do Głównego menu"]
TrasyList= [
"1-Pokaz dostepne trasy",
"2-Dodaj trase",
"3-Usun trase",
"4-Powrót do Głównego menu"]
AutorList= [
"0-Powrót do Głównego menu",
"ASDASDASD"
]
SpisList= [
"0-Powrót do Głównego menu"
]

# START PROGRAMU
def start_program():
    print (31*"-")
    print (" Project: Program \"Car Manager\"")
    print (" START date: 16.04.2017")
    print (31*"-")
    for i in MainList:
        print (i)
    def CHOICE_START():
            my_choice = int(input("\nWybierz opcję: "))
            print (31*"-")
            print("Wybrano:",MainList[(my_choice-1)])
            print (31*"-")
            if my_choice==0:
                return exit()
            elif my_choice==1:
                #for i in AutaList:
                #    print(i)
                Auta()

            elif my_choice==2:
                    for i in TrasyList:
                        print(i)
            elif my_choice==3:
                    o_Autorze()
            elif my_choice==4:
                    Spis_tresci()
    CHOICE_START()

# AUTA
def Auta():
    '''
    AutaList= [
    "1-Wyswietl wszystkie auta",
    "2-Dodaj nowe auto",
    "3-Usun auto",
    "4-Powrót do Głównego menu"]
    '''
    def CHOICE_AUTA():
        my_choice = int(input("\nWybierz opcję: "))
        print (31*"-")
        print("Wybrano:",MainList[(my_choice-1)])
        print (31*"-")
        #if my_choice==0:
        #    return exit()
        if my_choice==1:
            print ("Twoje auta:")
        elif my_choice==2:
            print ("Dodaj nowe auto:")
        elif my_choice==3:
            print ("Usuń auta:")
        elif my_choice==4:
                start_program()
    CHOICE_AUTA()




# INFORMACJE O AUTORZE
def o_Autorze():
    print ("\nAutorem programu jest Tomek")
    print ("startcode.pl")
    print ("kontakt@startcode.pl \n")
    for i in AutorList:
        print(i)
    def CHOICE_AUTOR():
        my_choice = int(input("\nWybierz opcję: "))
        print (31*"-")
        print("Wybrano:",MainList[(my_choice-1)])
        print (31*"-")
        if my_choice==0:
            start_program()
    CHOICE_AUTOR()


#SPIS TRESCI PROGRAMU
def Spis_tresci():
    main_len=0
    while main_len < len(MainList):
        print (MainList[main_len])
        if main_len==0:
            for i in AutaList:
                print("   ->",i)
        elif main_len==1:
            for i in TrasyList:
                print("   ->",i)
        elif main_len==2:
            for i in AutorList:
                print("   ->",i)
        elif main_len==3:
            for i in SpisList:
                print("   ->",i)
        main_len=main_len+1
    for i in SpisList:
        print ("\n"+15*"-"+"OPCJE"+15*"-")
        print(i)
        print (31*"-")
    def CHOICE_SPIS_TRESCI():
        my_choice = int(input("\nWybierz opcję: "))
        if my_choice > ((len(SpisList))-1):
            print (31*"-")
            print ("Wybrana opcja nie istnieje. Wybierz z poniższych:")
            for i in SpisList:
                print("   ->",i)
                print (31*"-")
        elif my_choice == 0:
            print("Wybrano:",SpisList[(my_choice)])
            start_program()
        CHOICE_SPIS_TRESCI()

    CHOICE_SPIS_TRESCI()



#MAIN INPUT
def MAIN_CHOICE():
    my_choice = int(input("\nWybierz opcję: "))
    print (31*"-")
    print("Wybrano:",MainList[(my_choice-1)])
    print (31*"-")
    if my_choice==0:
        for i in AutaList:
            print(i)
    elif my_choice==2:
            for i in TrasyList:
                print(i)
    elif my_choice==3:
            o_Autorze()
    elif my_choice==4:
            Spis_tresci()
