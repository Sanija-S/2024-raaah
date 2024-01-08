# ka nolasa faila daus csv json utt
#izveidojam loga izkartojumu
import PysimpleGUI as sg
layout=[
    [sg.InputText(key="-DISPLAY-", size=(20,1), justificator="right", readonly=True)]

]
# izveidosim logu ar ieprieks definetu izkartojumu
window=sg.Window("Kalkulators", layout, resizable= True)

# balstoties uz notkumiem veidosim ciklu, like previous lināa nekas nenotiek
while True:
    # ir notikumi, vertibas
    event, values=window.read # si metode tikai nolasa logu ar visam vertibam
# LOGS JAIZTAISA CIet
    window.close