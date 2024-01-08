"""
# ka nolasa faila daus csv json utt
#izveidojam loga izkartojumu
import PySimpleGUI as sg
#paligmainigie, kuri uzglaba ievades datus
# iekseja funkc kas veic aprekinus
def calculate(num1,num2,opperation):
   try: # TAS KO NOLASA NO TEkstA LAUkA IR TEksts
      num1=float(num1)
      num2=float(num2)
      if opperation =="+":
         rezultats= num1+num2
      elif opperation =="-":
         rezultats= num1-num2
      else:
         rezultats=None
         return rezultats
   except ValueError: #paredz ka pie kadas darb var rasties kluuda
      return "kĻūda"
current_input=""
current_opperation=""
layout=[
    [sg.InputText(key="-DISPLAY-", size=(20,1), justification="right", readonly=True)],
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
    event, values=window.read() # si metode tikai nolasa logu ar visam vertibam
# LOGS JAIZTAISA CIet
    
    # ja notiek aizversanas notikums vai poga EXIT, tad iziet no cikla(aizver logu)

    if event==sg.WIN_CLOSED or event=="EXIT":#pie pogas exit atgriezas sei tun pievieno notikumu
        break
    # ja ievada ciparu tad to piievino teksta laukam tad to pievieno teksta ievades laukā
    elif event == "1234567890": # ja ciparpoga ir nos
      current_input = event
      window["-DISPLAY-"].update(current_input)
    # ja darbibas poga ir nospiesta , saglaba darbibu un notira ievades lauku
    elif event == "+":
       current_opperation= event
       current_input = event
       window["-DISPLAY-"].update(current_input)
    # ja nospiests "C", tad notira teksta laukā ievaditos ciparus un darbibas
    elif event == "+":
       current_opperation= "C"
       current_input = event
       window["-DISPLAY-"].update(current_input)

    # ja ir nospiesta "=", javeic aprekins un jaatjauno teksta lauks aar rezultatu
    elif event == "=":
       rezultats= calculate(current_input,values["-DISPLAY-"], current_opperation)# kalkulate= funkcija (kurai 3 vertibas)(1. kuru ievadam, 2 masivais/ nultais elements, 3 operatorss ar ko stradasim)
       window["-DISPLAY-"].update (rezultats if rezultats is not None else "")
       current_input=int(rezultats) if rezultats is not None else ""# ko tas dos? 1.tas ko mes rekinam tas ir skaitli, japarveido uz int.
    
    window.close()
    """


# skolotajas piemers/ risinajums


"""
# Iekšējā funkcija, kas veic aprēķinus
import PySimpleGUI as sg
sg.theme("LightGreen2")
#pip install pyinstaller
#pyinstaller  --onefile --windowed -- icon= star.ico kalkulators.py
def calculate(num1, num2, operation):
    try:
        num1 = float(num1)
        num2 = float(num2)
        if operation == '+':
            result = num1 + num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '-':
            result = num1 - num2

        else:
            result = None
        return result
    except ValueError:
        return "Kļūda :("
 
# Palīgmaine, lai uzglabātu ievades datus
current_input = ''
current_operation = ''
 
# Izveidojiet GUI loga izkārtojumu
layout = [
    [sg.InputText(key='-DISPLAY-', size=(20, 1), justification='right', readonly=True)],
    [sg.Button('Exit', key='-EXIT-'), sg.Button('Delete')],
    [sg.Button('1'), sg.Button('2'), sg.Button('3')],
    [sg.Button('4'), sg.Button('5'), sg.Button('6')],
    [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('0')],
     [sg.Button('+'), sg.Button('-'), sg.Button('*'),sg.Button('=')],
   
]


# Izveidojiet logu ar iepriekš definēto izkārtojumu
window = sg.Window('Kalkulators', layout, resizable=True)
 
# Balstoties uz notikumu ciklu
while True:
    event, values = window.read()
 
    # Ja loga aizvēršanas notikums vai Exit poga tiek nospiesta, tad iziet no cikla
    if event == sg.WIN_CLOSED or event == '-EXIT-':
        break
 
    # Ja skaitļu poga tiek nospiesta, pievieno to skaitļu teksta ievades laukam
    elif event in '1234567890':
        current_input += event
        window['-DISPLAY-'].update(current_input)
 
    # Ja darbības poga tiek nospiesta, saglabā šo darbību un notīra teksta ievades lauku
    elif event in ['+', '*','-']:
        current_operation = event
        current_input = ''
        window['-DISPLAY-'].update(current_input)
 
    # Ja "C" poga tiek nospiesta, notīra teksta ievades lauku un darbību
    elif event == 'Delete':
        current_input = ''
        current_operation = ''
        window['-DISPLAY-'].update(current_input)
 
    # Ja "=" poga tiek nospiesta, veic kalkulācijas un atjauno teksta ievades lauku ar rezultātu
    elif event == '=':
        result = calculate(current_input, values['-DISPLAY-'], current_operation)
        window['-DISPLAY-'].update(result if result is not None else '')
        current_input = str(result) if result is not None else ''
 
# Aizveriet GUI logu
window.close()
    """



#atjaunota real versija- tikai nez kas ar ikonnu


import PySimpleGUI as sg
# Iestatīt tēmu (vizuālo izskatu)
sg.theme('LightGreen2') # Reddit  Dark2 Green Tan
 
# Attēls pie loga nosaukuma ===*.ico
bilde='star.ico'
 
# Iekšējā funkcija, kas veic aprēķinus
def calculate(num1, num2, operation):
    try:
        num1 = float(num1)
        num2 = float(num2)
        if operation == '+':
            result = num1 + num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '-':
            result=num1-num2
        else:
            result = None
        return result
    except ValueError:
        return "Kļūda :("
 
# Palīgmaine, lai uzglabātu ievades datus
current_input = ''
current_operation = ''
 
# Izveidojiet GUI loga izkārtojumu
layout = [
    [sg.InputText(key='-DISPLAY-', size=(20, 1), justification='right', readonly=True)],
    [sg.Button('Exit', key='-EXIT-'), sg.Button('Delete')],
    [sg.Button('1'), sg.Button('2'), sg.Button('3')],
    [sg.Button('4'), sg.Button('5'), sg.Button('6')],
    [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('0')],
     [sg.Button('+'), sg.Button('-'), sg.Button('*'),sg.Button('=')],
   
]
 
# Izveidojiet logu ar iepriekš definēto izkārtojumu
window = sg.Window('Kalkulators', layout, resizable=True, icon=bilde)
 
# Balstoties uz notikumu ciklu
while True:
    event, values = window.read()
 
    # Ja loga aizvēršanas notikums vai Exit poga tiek nospiesta, tad iziet no cikla
    if event == sg.WIN_CLOSED or event == '-EXIT-':
        break
 
    # Ja skaitļu poga tiek nospiesta, pievieno to skaitļu teksta ievades laukam
    elif event in '1234567890':
        current_input += event
        window['-DISPLAY-'].update(current_input)
 
    # Ja darbības poga tiek nospiesta, saglabā šo darbību un notīra teksta ievades lauku
    elif event in ['+', '*', '-']:
        current_operation = event
        current_input = ''
        window['-DISPLAY-'].update(current_input)
 
    # Ja "C" poga tiek nospiesta, notīra teksta ievades lauku un darbību
    elif event == 'C':
        current_input = ''
        current_operation = ''
        window['-DISPLAY-'].update(current_input)
 
    # Ja "=" poga tiek nospiesta, veic kalkulācijas un atjauno teksta ievades lauku ar rezultātu
    elif event == '=':
        result = calculate(current_input, values['-DISPLAY-'], current_operation)
        window['-DISPLAY-'].update(result if result is not None else '')
        current_input = str(result) if result is not None else ''
 
# Aizveriet GUI logu
window.close()