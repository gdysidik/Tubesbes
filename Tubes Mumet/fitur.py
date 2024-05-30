import sys
import os
import tubes
import time
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
    elif key=='q' or key=='Q':
        idx=0
        clear_scr()
        print(Fore.GREEN+"\t\tokh ckp tw, trms\n\t\tbye")
        time.sleep(0.7)
    else:
        print(Fore.RED + "\t\tpencet n hey")
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
        # time.sleep(1)
        return False

def histori():
    global listPemenang
    global idx
    
    clear_scr()
    no = 0
    print(Fore.LIGHTBLUE_EX)
    print("\t\t---------------------------")
    print("\t\t DAFTAR PEMENANG TICTACTOE")
    print("\t\t---------------------------")
    if len(listPemenang)==0:
        idx=2
        print("\t\tBelum ada pemenang, main gamenya dulu coy")
        time.sleep(1)
    else:
        listPemenang.append(tubes.getWinner())
        for i in listPemenang:
            no+=1
            print(f"\t\t{no}.\t" + i)
            print("")
        key = input("\n\t\tKetik 'B' untuk kembali dan 'R' untuk reset histori ")
        if key=='b' or key=='B':
            idx=2
        elif key=='r' or key=='R':
            idx=5
        else:
            idx=4
            print(Fore.RED + "\t\tgausah ngaco hee")
    if idx==5:
        idx=2
        listPemenang.clear()
        print("\t\tLIST PEMENANG SUDAH BERHASIL DIHAPUS")
        time.sleep(1)

def jalankanFitur():
    clear_scr()
    global idx
    global fiturnya
    while fiturnya==True:
        print(idx)
        if idx==1:
            tampilanAwal()
        elif idx==2:
            tampilanFitur()
        elif idx==3:
            tubes.mainkan()
            tubes.resetGame()
            idx-=1
            time.sleep(1.5)
        elif idx==4:
            histori()
        elif idx==0:
            fiturnya = False
