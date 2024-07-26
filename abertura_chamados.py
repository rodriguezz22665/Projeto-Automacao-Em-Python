import pyautogui
import time

import pandas as pd
tabela = pd.read_csv(r"C:\Users\jcsil\OneDrive\Documentos\Teste Projeto Automacao\cliente-assunto-descricao.csv")

pyautogui.PAUSE = 1.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=220, y=61)
pyautogui.write("https://suporte.starsoft.com.br/portal/pt/myarea?viewId=126587000053257095")
pyautogui.press("Enter")
time.sleep (3)
pyautogui.click(x=1111, y=282)



for linha in tabela.index:
    pyautogui.click(x=308, y=514)
    pyautogui.doubleClick(x=298, y=468)
    nome_da_conta = tabela.loc[linha, "nome_da_conta"]
    pyautogui.write(str(nome_da_conta))
    pyautogui.press("enter")
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.write("Melhorias")
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.write("Folha de Pagamento")
    pyautogui.press("enter")
    pyautogui.press("tab")

    assunto = tabela.loc[linha, "assunto"]
    pyautogui.write(str(assunto))
    pyautogui.press("enter")
    pyautogui.press("tab")

    descricao = tabela.loc[linha, "descricao"]
    pyautogui.write(str(descricao))
    pyautogui.press("enter")
    pyautogui.press("tab")

    pyautogui.scroll(-5000)
    pyautogui.click(x=640, y=738)
    pyautogui.press("enter")






