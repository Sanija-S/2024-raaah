# ka nolasa faila daus csv json utt
#izveidojam loga izkartojumu
import PysimpleGUI as sg
#paligmainigie, kuri uzglaba ievades datus
current_imput=""
current_opperation=""
layout=[
    [sg.InputText(key="-DISPLAY-", size=(20,1), justificator="right", readonly=True)],
    {sg.Button("1"), sg.Button("2"),sg.Button("3"),sg.Button("+")},
    {sg.Button("4"), sg.Button("5"),sg.Button("6"),sg.Button("-")},
    {sg.Button("7"), sg.Button("8"),sg.Button("9"),sg.Button("c")},
    {sg.Button("0"), sg.Button("="),sg.Button("EXIT")}



]
# izveidosim logu ar ieprieks definetu izkartojumu
window=sg.Window("Kalkulators", layout, resizable= True)

# balstoties uz notkumiem veidosim ciklu, like previous lināa nekas nenotiek
while True:
    # ir notikumi, vertibas
    event, values=window.read # si metode tikai nolasa logu ar visam vertibam
# LOGS JAIZTAISA CIet
    
    # ja notiek aizversanas notikums vai poga EXIT, tad iziet no cikla(aizver logu)

    if event==sg.WIN_CLOSED or event=="EXIT":#pie pogas exit atgriezas sei tun pievieno notikumu
        break
    elif
    # ja ciparpoga ir nos
    # pista tad to pievieno teksta ievades laukā
    window.close()