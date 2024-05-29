import os
import tubes
import time

def clear_scr(): # Fungsi buat clear layar terminal
    os.system('cls')

def tampilanAwal():
    print("\t\t------------------------------------")
    print("\t\t|                                  |")
    print("\t\t| SELAMAT DATANG DI GAME TICTACTOE |")
    print("\t\t|                                  |")
    print("\t\t------------------------------------")
    key = input("\t\tklik 'N' untuk lanjut ")
    if key=='n' or key=='N':
        pilihan()
    else:
        ("\t\t pencet n hey")

def pilihan():
    for i in range(0,3):
        print("\t\t LOADING. . .")
        time.sleep(1)
    clear_scr()
    key = input("\t\tklik 'N' untuk lanjut atau klik 'B' untuk kembali ")
    clear_scr()
    if key=='n' or key=='N':
        tubes.mainkan()
    elif key=='b' or key=='B':
        tampilanAwal()
    else: 
        print("HEH PENCET B APA N COK")