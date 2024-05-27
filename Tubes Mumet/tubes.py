board = ["1","2","3",
        "4","5","6",
        "7","8","9"]
gameMain = True
playerX = input("Nama pemain 1: ")
playerY = input("Nama pemain 2: ")
currPlayer = playerX
winner = None

def cetakBoard(board): # Fungsi mencetak board tictactoe
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("------")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("------")
    print(board[6] + "|" + board[7] + "|" + board[8])

def inputPlayer(board): # Fungsi inputan dari player
    global gakGanti
    inp = int(input(f"{currPlayer} Masukkan angka sesuai plot board: "))
    if inp>=1 and inp<=9:
        if board[inp-1]!="X" and board[inp-1]!="O":
            gakGanti = 0
            if currPlayer == playerY:
                board[inp-1] = "O"
            elif currPlayer == playerX:
                board[inp-1] = "X"
        else:
            print("WEH, dia udah punya yang lain")
            gakGanti = 1
    else:
        print("Ikutin perintah dong brother...")

def cekHoriz(board): # Fungsi cek keadaan horizontal kalo menang
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
    elif board[5]==board[6]==board[7]:
        if board[5] == "X":
            winner = playerX
        elif board[5] == "O":
            winner = playerY
        return True

def cekVerti(board): # Fungsi cek keadaan vertikal kalo menang
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

def cekDiag(board): # Fungsi cek keadaan diagonal kalo menang
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

def cekMenang(): # Fungsi kalo udah ada yg menang
    global gameMain
    global currPlayer
    if cekDiag(board) or cekHoriz(board) or cekVerti(board):
        print(f"Selamat pemenangnya adalah {currPlayer}")
        gameMain = False

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
        
def main():
    while gameMain:
        cetakBoard(board)
        print(f"{currPlayer} Main")
        inputPlayer(board)
        # print(f"BEFORE: {currPlayer}")
        # print(f"AFTER: {currPlayer})")
        cekMenang()
        gantian()
    cetakBoard(board)
