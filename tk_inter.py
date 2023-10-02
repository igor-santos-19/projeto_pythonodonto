from tkinter import *

root = Tk()

textoEntrada1 = Label(root, text='Digite o nome do dentista').pack()
entrada1 = Entry(root)
entrada1.pack()

textoEntrada2 = Label(root, text='Digite a idade do dentista').pack()
entrada2 = Entry(root)
entrada2.pack()

textoEntrada3 = Label(root, text='Digite o CPF do dentista').pack()
entrada3 = Entry(root)
entrada3.pack()

textoEntrada4 = Label(root, text='Digite o Telefone do dentista').pack()
entrada4 = Entry(root)
entrada4.pack()

textoEntrada5 = Label(root, text='Digite a Especialização do dentista').pack()
entrada5 = Entry(root)
entrada5.pack()

textoEntrada6 = Label(root, text='Digite alguma Observação do dentista').pack()
entrada6 = Entry(root)
entrada6.pack()

def bt_botaoEnviarDados():
    import bd_conex
    bd_conex.cria_tabelas()

    nome_dent = entrada1.get()
    idade_dent = entrada2.get()
    CPF_dent = entrada3.get()
    telefone_dent = entrada4.get()
    Especializacao_dent = entrada5.get()
    Obs_dent = entrada6.get()
    
    bd_conex.inseredentista(nome_dent, idade_dent, CPF_dent, telefone_dent, Especializacao_dent, Obs_dent)

botaoEnviarDados = Button(root, text='Enviar Dados', command = bt_botaoEnviarDados).pack()



root.geometry("400x400")
root.mainloop()
