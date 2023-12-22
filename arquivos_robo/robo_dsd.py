import pyautogui as p
from random import choice
import pyperclip as pclp
import pandas as pd


def botao_gerar_pessoa():
    p.click(1600, 500)
    p.press("pageup", presses=3)
    x, y = p.locateCenterOnScreen(r'C:\Curso\APRTECH_Cadastro_De_Pessoas\arquivos_robo\images\gerar_pessoa.png',
                                region = (709, 870, 1450, 1017), minSearchTime=2)
    p.click(x, y)
    p.sleep(5)

def localizar_clicar_colar(arquivo):
    x, y = p.locateCenterOnScreen(rf'C:\Curso\APRTECH_Cadastro_De_Pessoas\arquivos_robo\images\{arquivo}', 
                                  region=(709, 200, 1448, 1017), minSearchTime=2)
    p.click(x, y, clicks=2, duration=0.2)
    p.hotkey('ctrl', 'c')
    chave = pclp.paste()
    p.click(x+30, y+30, duration=0.2)
    p.hotkey('ctrl', 'c')
    valor = pclp.paste()
    return {chave : valor}

def pegar_valore_na_tela(paths):
    pessoa = {}
    for path in paths:
        pessoa.update(localizar_clicar_colar(path))
        if paths.index(path) == 7:
            p.press('pagedown')
            p.sleep(0.5)
    return pessoa


caminho = 'C:\Curso\APRTECH_Cadastro_De_Pessoas\arquivos_robo\images'
paths = ('nome.png', 'cpf.png', 'rg.png', 'data_nascimento.png', 'sexo.png', 'signo.png', 
         'mae.png', 'pai.png', 'cep.png', 'endereco.png', 'numero.png', 'bairro.png', 'cidade.png',
         'estados.png')


pessoas=[]
for _ in range(2):
    botao_gerar_pessoa()
    pessoas.append(pegar_valore_na_tela(paths))
for pessoa in pessoas:
    tempValor=[]
    for valor, chave in zip(pessoa.values(), pessoas.keys()):
        



