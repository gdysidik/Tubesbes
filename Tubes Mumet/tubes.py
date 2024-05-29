from collections import deque
from colorama import Fore
import fitur

board = ["1","2","3",
        "4","5","6",
        "7","8","9"]
 
def setGame():
    global board # Tabel main tictactoe
    global board_copy # Tabel tictactoe copy-an
    global step_playerX # Buat nyimpen langkah yg udh diambil playerX
    global step_playerY # Buat nyimpen langkah yg udh diambil playerY
    global gameMain # Boolean buat gamenya masih main atau engga
    global playerX # Pemain 1
    global playerY # Pemain 2
    global currPlayer # Pemain yang sekarang lagi giliran jalan
    global winner # Pemenang game
    
    board_copy = board.copy()
    step_playerX = deque([])
    step_playerY = deque([])
    gameMain = True
    playerX = input(Fore.GREEN + "Nama pemain 1: ")
    playerY = input(Fore.GREEN + "Nama pemain 2: ")
    currPlayer = playerX
    winner = None
    fitur.clear_scr()

def cetakBoard(): # Fungsi mencetak board tictactoe
    print("\t\t   |   |  ")
    print("\t\t " + board[0] + " | " + board[1] + " | " + board[2])
    print("\t\t   |   |  ")
    print("\t\t-----------")
    print("\t\t   |   |  ")
    print("\t\t " + board[3] + " | " + board[4] + " | " + board[5])
    print("\t\t   |   |  ")
    print("\t\t-----------")
    print("\t\t   |   |  ")
    print("\t\t " + board[6] + " | " + board[7] + " | " + board[8])
    print("\t\t   |   |  ")

def inputPlayer(): # Fungsi inputan dari player
    global gakGanti
    global step_playerX
    global step_playerY
    global currPlayer
    print(f"\n\n\t\tSekarang giliran {currPlayer}")
    inp = int(input(Fore.MAGENTA + f"\t\t{currPlayer} bisa masukkan angka sesuai plot board: "))
    if inp>=1 and inp<=9:
        if board[inp-1]!="X" and board[inp-1]!="O":
            fitur.clear_scr()
            gakGanti = 0
            if currPlayer == playerY:
                board[inp-1] = "O"
                step_playerY.append(inp)
            elif currPlayer == playerX:
                board[inp-1] = "X"
                step_playerX.append(inp)
        else:
            fitur.clear_scr()
            print(Fore.RED + "\t\tWEH, dia udah punya yang lain")
            gakGanti = 1
    else:
        fitur.clear_scr()
        print(Fore.RED + "\t\tIkutin perintah dong brother...")
        gakGanti = 1

def cekHoriz(): # Fungsi cek keadaan horizontal kalo menang
    global winner
    global playerX
    global playerY
    if board[0]==board[1]==board[2]:
        if board[0] == "X":
            winner = playerX
        elif board[0] == "O":
            winner = playerY
        return True
    elif board[3]==board[4]==board[5]:
        if board[3] == "X":
            winner = playerX
        elif board[3] == "O":
            winner = playerY
        return True
    elif board[6]==board[7]==board[8]:
        if board[5] == "X":
            winner = playerX
        elif board[5] == "O":
            winner = playerY
        return True
    return False

def cekVerti(): # Fungsi cek keadaan vertikal kalo menang
    global winner
    global playerX
    global playerY
    if board[0]==board[3]==board[6]:
        if board[0] == "X":
            winner = playerX
        elif board[0] == "O":
            winner = playerY
        return True
    elif board[1]==board[4]==board[7]:
        if board[1] == "X":
            winner = playerX
        elif board[1] == "O":
            winner = playerY
        return True
    elif board[2]==board[5]==board[8]:
        if board[5] == "X":
            winner = playerX
        elif board[5] == "O":
            winner = playerY
        return True
    return False

def cekDiag(): # Fungsi cek keadaan diagonal kalo menang
    global winner
    global playerX
    global playerY
    if board[0]==board[4]==board[8]:
        if board[0] == "X":
            winner = playerX
        elif board[0] == "O":
            winner = playerY
        return True
    elif board[2]==board[4]==board[6]:
        if board[3] == "X":
            winner = playerX
        elif board[3] == "O":
            winner = playerY
        return True
    return False

def cekMenang(): # Fungsi kalo udah ada yg menang
    global gameMain
    global currPlayer
    global board
    if cekDiag() or cekHoriz() or cekVerti():
        fitur.clear_scr()
        print(Fore.GREEN + f"\n\n\t\tSelamat pemenangnya adalah {currPlayer}")
        cetakBoard()
        gameMain = False
        return True
    return False
        
def cekLanjut(): # Fungsi biar main terus tanpa ada hasil imbang
    global step_playerY
    global step_playerX
    global board_copy
    global board
    if len(step_playerX)==4 and not cekMenang():
        id_apus = step_playerX[0]
        board[id_apus-1] = board_copy[id_apus-1]
        step_playerX.popleft()
    if len(step_playerY)==4 and not cekMenang():
        id_apus = step_playerY[0]
        board[id_apus-1] = board_copy[id_apus-1]
        step_playerY.popleft()

def gantian(): # Fungsi player main ganti2an
    global currPlayer
    global playerX
    global playerY
    if gakGanti == 0:
        if currPlayer == playerX:
            currPlayer = playerY
        elif currPlayer == playerY:
            currPlayer = playerX
    elif gakGanti == 1:
        if currPlayer == playerX:
            currPlayer = playerX
        elif currPlayer == playerY:
            currPlayer = playerY

def mainkan(): # Fungsi play tictactoe
    fitur.clear_scr()
    setGame()
    while gameMain:
        cetakBoard()
        inputPlayer()
        if not cekMenang():
            cekLanjut()
        gantian()
    # cetakBoard(board)
