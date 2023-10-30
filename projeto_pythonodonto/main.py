import requests
import banco
from tkinter import *

banco.conexaoBanco()

janelaPrincipal = Tk()
janelaPrincipal.geometry("400x400")
janelaPrincipal.title("Questionario Odonto")

texto_sobreProjeto = Label(janelaPrincipal, text="Projeto Questionario Big data")
texto_sobreProjeto.pack()
Digiteseunome = Label(janelaPrincipal, text="Digite o seu nome")
Digiteseunome.pack()

Digitesuaidade = Label(janelaPrincipal, text="Digite a sua idade")
Digitesuaidade.pack()


def DadosPessoais():
    perguntaNome = Entry(Digiteseunome, textvariable='teste')
    perguntaNome.pack()

    perguntaIdade = Entry(Digitesuaidade)
    perguntaIdade.pack()

    botaoTeste = Button(janelaPrincipal, text="Iniciar", cursor='watch')
    botaoTeste.pack()
    


def perguntasFormulario():   
    pergunta01 = Label(janelaPrincipal, text='1) Pergunta numero  um sobre odonto selecione uma das respostas: ')
    pergunta01.pack()
    botaoRadio = Radiobutton(janelaPrincipal, text='resposta1', value='valorResposta1')
    botaoRadio.pack()
    botaoRadio_2 = Radiobutton(janelaPrincipal, text='resposta2', value='valorResposta2')
    botaoRadio_2.pack()

    pergunta02 = Label(janelaPrincipal, text='2) Pergunta numero  um sobre odonto selecione uma das respostas: ')
    pergunta02.pack()
    botaoRadio_3 = Radiobutton(janelaPrincipal, text='resposta1', value='valorResposta3')
    botaoRadio_3.pack()
    botaoRadio_4 = Radiobutton(janelaPrincipal, text='resposta2', value='valorResposta4')
    botaoRadio_4.pack()

def botaoEnviaFormulario():
    botaoTeste = Button(janelaPrincipal, text="Enviar respostas")
    botaoTeste.pack()

DadosPessoais()
perguntasFormulario()
botaoEnviaFormulario()
janelaPrincipal.mainloop()

