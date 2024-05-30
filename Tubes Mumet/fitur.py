import sys, os, tubes, time
from colorama import Fore

global fiturnya
fiturnya = True
global idx
idx = 1
global listPemenang
listPemenang = []

def clear_scr(): # Fungsi buat clear layar terminal
    os.system('cls')
    
def tampilanAwal():
    clear_scr()
    global idx
    print(Fore.LIGHTYELLOW_EX)
    patterns = [
    [["\t\tT T T T T       I I I I        C C C C "]],
    [["\t\t    T             II         CC        "]],
    [["\t\t    T             II        CC         "]],
    [["\t\t    T             II        CC         "]],
    [["\t\t    T             II         CC        "]],
    [["\t\t    T           I I I I        C C C C "]],
    [["\t\t======================================="]],
    [["\t\tT T T T T        AAAA         C C C C  "]],
    [["\t\t    T           A    A       CC        "]],
    [["\t\t    T           A    A      CC         "]],
    [["\t\t    T           A AA A      CC         "]],
    [["\t\t    T           A    A       CC        "]],
    [["\t\t    T           A    A        C C C C  "]],
    [["\t\t======================================="]],
    [["\t\tT T T T T        OOOO        E E E E   "]],
    [["\t\t    T          OO    OO      EE        "]],
    [["\t\t    T         OO      OO     E E       "]],
    [["\t\t    T         OO      OO     E E E E   "]],
    [["\t\t    T         OO      OO     E E       "]],
    [["\t\t    T          OO    OO      EE        "]],
    [["\t\t    T            OOOO        E E E E   "]],
    [["\t\t======================================="]],
    ] 
    def print_pattern():
        for row in pattern:
            print("")
            sys.stdout.write("\r" + " ".join(row))
            sys.stdout.flush()
            time.sleep(0.1)         
    for pattern in patterns:
        print_pattern()
    key = input(Fore.MAGENTA + "\n\t\tklik 'N' untuk lanjut dan 'Q' untuk keluar ")
    if key=='n' or key=='N':
        idx=2
        for i in range (0,101,10):
            clear_scr()
            print(Fore.LIGHTRED_EX)
            print(f"\t\tLOADING -- {i}% --")
            time.sleep(0.07)
    elif key=='q' or key=='Q':
        idx=0
        clear_scr()
        print(Fore.GREEN+"\t\tokh ckp tw, trms\n\t\tbye")
        time.sleep(1)
        for i in range (0,101,10):
            clear_scr()
            print(Fore.LIGHTRED_EX+"\n\t\tSedang keluar. . .")
            print(f"\t\tLOADING -- {i}% --")
            print(Fore.RESET)
            time.sleep(0.07)
    else:
        print(Fore.RED + "\t\tpencet yg bener hey")
        time.sleep(2)
        idx+=0
    
def tampilanFitur():
    global idx
    print(Fore.LIGHTCYAN_EX)
    clear_scr()
    print("\t\t------------------------------------")
    print("\t\t|                                  |")
    print("\t\t| SELAMAT DATANG DI GAME TICTACTOE |")
    print("\t\t|                                  |")
    print("\t\t------------------------------------")
    print("\n\t\t1. Mainkan brother\n\t\t2. Yang pernah menang siapa aja ya?\n\t\t3. Balik aja deh")
    key = int(input(Fore.MAGENTA + "\t\tKetik sesuai angka yang ingin dipilih "))
    if key==1:
        idx=3
    elif key==2:
        idx=4
    elif key==3:
        idx=1
    else:
        print(Fore.RED + "\t\tpencet sesuai angka hey")
        time.sleep(1)
        return False
    for i in range (0,101,10):
        clear_scr()
        print(Fore.LIGHTRED_EX)
        print(f"\t\tLOADING -- {i}% --")
        time.sleep(0.07)

def tampilkanRiwayat(): # Fungsi untuk menampilkan history match
    global idx
    clear_scr()
    print(Fore.LIGHTGREEN_EX)
    print("\t\t------------------------------------")
    print("\t\t|          RIWAYAT PERMAINAN        |")
    print("\t\t------------------------------------")
    
    if not os.path.exists('game_history.txt'):
        print("\t\tBelum ada riwayat permainan.")
    else:
        with open('game_history.txt', 'r') as file:
            lines = file.readlines()
            if not lines:
                print("\t\tBelum ada riwayat permainan.")
            else:
                for line in lines:
                    print("\t\t" + line.strip())
    
    key = input(Fore.MAGENTA + "\n\t\tklik 'B' untuk kembali ")
    if key=='b' or 'B':
        idx = 2
    else:
        print(Fore.RED+"\t\tPencet sesuai pilihan woy")
        idx+=0
    for i in range (0,101,10):
        clear_scr()
        print(Fore.LIGHTRED_EX)
        print(f"\t\tLOADING -- {i}% --")
        time.sleep(0.07)

def jalankanFitur(): # Fungsi untuk menjalankan semua fitur game
    clear_scr()
    global idx
    global fiturnya
    while fiturnya==True:
        if idx==1:
            tampilanAwal()
        elif idx==2:
            tampilanFitur()
        elif idx==3:
            tubes.mainkan()
            idx-=1
            for i in range (0,101,10):
                clear_scr()
                print(Fore.LIGHTRED_EX)
                print(f"\t\tLOADING -- {i}% --")
                time.sleep(0.07)
        elif idx==4:
            tampilkanRiwayat()
        elif idx==0:
            fiturnya = False
