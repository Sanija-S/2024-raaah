# ka nolasa faila daus csv json utt
#izveidojam loga izkartojumu
import PysimpleGUI as sg
#paligmainigie, kuri uzglaba ievades datus
# iekseja funkc kas veic aprekinus
def calculate(num1,num2,opperation)
current_input=""
current_opperation=""
layout=[
    [sg.InputText(key="-DISPLAY-", size=(20,1), justificator="right", readonly=True)],
    {sg.Button("1"), sg.Button("2"),sg.Button("3"),sg.Button("+")},
    {sg.Button("4"), sg.Button("5"),sg.Button("6"),sg.Button("-")},
    {sg.Button("7"), sg.Button("8"),sg.Button("9"),sg.Button("C")},
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
    # ja ievada ciparu tad to piievino teksta laukam tad to pievieno teksta ievades laukā
    elif event in "1234567890": # ja ciparpoga ir nos
      current_input = event
      window["-DISPLAY-"].update(current_input)
    # ja darbibas poga ir nospiesta , saglaba darbibu un notira ievades lauku
    elif event in "+":
       current_opperation= event
       current_input = event
       window["-DISPLAY-"].update(current_input)
    # ja nospiests "C", tad notira teksta laukā ievaditos ciparus un darbibas
    elif event in "+":
       current_opperation= "C"
       current_input = event
       window["-DISPLAY-"].update(current_input)

    # ja ir nospiesta "=", javeic aprekins un jaatjauno teksta lauks aar rezultatu
    elif event == "=":
       rezultats= calculate(current_input,values[0], current_opperation)# kalkulate= funkcija (kurai 3 vertibas)(1. kuru ievadam, 2 masivais/ nultais elements, 3 operatorss ar ko stradasim)
       window["-DISPLAY-"].update(current_input)
       current_input=str(rezultats)# ko tas dos? 1.tas ko mes rekinam tas ir skaitli, japarveido uz int.
    
    window.close()