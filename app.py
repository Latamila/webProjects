#ESTES SÃO INSTALADOS VIA TERMINAL NO VSCODE
#pip install types-openpyxl
#pip install pyautogui
#pip install pillow 
#pip install openpyxl



import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui



webbrowser.open('https://web.whatsapp.com/',)
sleep(30)
workbook = openpyxl.load_workbook('clientes.xlsx')#CONFECCIONE SUA LISTA SEM CABEÇALHO, CONTENDO NOME, TELEFONE E DATA DE VENCIMENTO PARA COBRANÇA.
pagina_clientes = workbook['Planilha1']

for linha in pagina_clientes.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = linha[1].value
    vencimento = linha[2].value

    mensagem = f'Olá, {nome} to testando automação do envio de cobranças pelo whatsapp. seu boleto vence no dia {vencimento}. Evite multas e atrasos.'
    
    link_msg_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
    
    webbrowser.open(link_msg_whatsapp)
    sleep(10)
    try:  
        seta = pyautogui.locateCenterOnScreen('setaoficial.png')#IMAGEM ESTÁ NO REPOSITORIO
        sleep(5)
        pyautogui.click(seta[0],seta[1])
        sleep(5)
        pyautogui.hotkey('ctrl','w')
        sleep(5)
    except:
        print('Não foi possível enviar  mensagem para {nome}')
        with open('erros.csv','a',newline='', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome}, {telefone}')
