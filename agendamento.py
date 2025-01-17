import pyautogui
import time
import datetime
import getpass

n = int(input("Quantos dias você quer agendar? "))
login = input("Digite seu login do SIGAA: ")
senha = getpass.getpass("Digite a sua senha do SIGAA: ")
nav = input("Escolha um navegador para acessar o SIGAA: ")

pyautogui.hotkey("win", 'r')
pyautogui.typewrite(nav)
pyautogui.press("enter")
time.sleep(5)

pyautogui.hotkey("ctrl", 't')
pyautogui.typewrite('https://si3.ufc.br/sigaa/verTelaLogin.do')
pyautogui.press("enter")

time.sleep(2)
pyautogui.typewrite(login)
pyautogui.press("tab")
pyautogui.typewrite(senha)
pyautogui.press("enter")
time.sleep(2)
for i in range(4):
    pyautogui.press("tab") # Pular aba da avaliacao institucional
pyautogui.press("enter") # pular aba da avaliacao institucional

time.sleep(3)
for i in range(7): # abrir o menu discente
    pyautogui.press("tab")

pyautogui.press("enter") 
time.sleep(3)

time.sleep(5)
pyautogui.click(x=186, y=161) # abrir o menu de agendamento
for i in range(7):
    pyautogui.press("tab")

pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("enter")

diaAgendado = datetime.date.today() + datetime.timedelta(days=1)  # Inicializa com a data de amanha

for i in range(n):
    agendouAlmoco = False
    for j in range(2):  # almoco e jantar

        while diaAgendado.weekday() in [5, 6]:  # pula fins de semana (sabado ou domingo)
            diaAgendado += datetime.timedelta(days=1)

        time.sleep(2)
        pyautogui.click(x=296, y=356)
        pyautogui.press("tab")

        s = diaAgendado.strftime("%d/%m/%Y")  # converte a data para o formato DD/MM/YYYY
        pyautogui.typewrite(s) # campo data da refeicao
        time.sleep(1)
        pyautogui.press("tab")  # campo tipo da refeicao (almoco ou jantar)
        if agendouAlmoco:
            pyautogui.press("down")
            pyautogui.press("down") # jantar
        else:
            pyautogui.press("down") # almoco

        if agendouAlmoco:
            print(f"Jantar do dia {s} agendado")
        else:
            print(f"Almoço do dia {s} agendado")

        time.sleep(1)
        pyautogui.press("tab")  # Campo horário
        pyautogui.press("down")
        pyautogui.press("tab")  # Confirma agendamento
        pyautogui.press("enter")

        agendouAlmoco = True  # Passa para o jantar

    # Incrementa a data para o próximo dia
    diaAgendado += datetime.timedelta(days=1)
    while diaAgendado.weekday() in [5, 6]:  # Pula fins de semana novamente
        diaAgendado += datetime.timedelta(days=1)
