from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from ttkthemes import ThemedTk
import bd_conex

def criar_entrada_label(root, texto, coluna, linha, rowspan=1, padx=5, pady=2, entry_width=30):
    estilo_label = {'font': ('Helvetica', 10), 'fg': 'black'}
    estilo_entrada = {'font': ('Helvetica', 10), 'bg': 'lightgray', 'fg': 'black', 'width': entry_width,
                      'borderwidth': 0, 'relief': 'flat'}
    label = Label(root, text=texto, **estilo_label)
    label.grid(column=coluna, row=linha, rowspan=rowspan, padx=padx, pady=pady, sticky=W)
    entrada = Entry(root, **estilo_entrada)
    entrada.grid(column=coluna, row=linha + 1, rowspan=rowspan, padx=padx, pady=pady, sticky=W)

    return entrada

def criar_combobox_label(root, texto, opcoes, coluna, linha, padx=5, pady=2):
    label = Label(root, text=texto)
    label.grid(column=coluna, row=linha, padx=padx, pady=pady, sticky=W)
    combobox = ttk.Combobox(root, values=opcoes)
    combobox.grid(column=coluna, row=linha + 1, padx=padx, pady=pady, sticky=W)
    return combobox

def criar_botao(root, texto, comando, coluna, linha, padx=5, pady=2):
    botao = Button(root, text=texto, command=comando, font=("Arial", 12), background="#4CAF50", fg="white", relief=GROOVE)
    botao.grid(column=coluna, row=linha, padx=padx, pady=pady, sticky="ew")
    return botao

def analiseDadosMostrarNatela():
    total_atendimentos = bd_conex.tiposdeAtendPac()
    totalMediaIdadePac = bd_conex.mediaIdadePacientes()
    totalEscpecializacaoDent = bd_conex.especializacaoDent()
    totalMediaIdadeDEnt = bd_conex.mediaIdadeDentista()
    totalOrtodontia = bd_conex.especializacaoDent1()
    totalDeconsultas = bd_conex.TotaldeConsultas()
    TotaldeDentistas = bd_conex.TotaldeDentistas()
    TotaldePacientes = bd_conex.TotaldePacientes()

    textoDesaidaa0 = Label(root, text=f'Total de Dentistas: {TotaldeDentistas}')
    textoDesaidaa0.grid(column=4, row=3, padx=2, pady=2)

    textoDesaidaa1 = Label(root, text=f'Total de Pacientes: {TotaldePacientes}')
    textoDesaidaa1.grid(column=4, row=4, padx=2, pady=2)

    textoDesaida = Label(root, text=f'Total de atendimentos: {totalDeconsultas}')
    textoDesaida.grid(column=4, row=5, padx=2, pady=2)

    textoDesaida0 = Label(root, text=f'Atendimentos relacionados a Ortodontia: {totalOrtodontia}')
    textoDesaida0.grid(column=4, row=6, padx=2, pady=2)

    textoDesaida = Label(root, text=f'Atendimentos relacionados a Limpeza e exames Dentários: {total_atendimentos}')
    textoDesaida.grid(column=4, row=7, padx=2, pady=2)

    textoDesaida1 = Label(root, text=f'A media das idades dos pacientes é: {"{:.2f}".format(totalMediaIdadePac)}')
    textoDesaida1.grid(column=4, row=8, padx=2, pady=2)

    textoDesaida2 = Label(root, text=f'Total de ClinicoGeral: {totalEscpecializacaoDent}')
    textoDesaida2.grid(column=4, row=9, padx=2, pady=2)

    textoDesaida3 = Label(root, text=f'A media das idades dos dentista é: {"{:.2f}".format(totalMediaIdadeDEnt)}')
    textoDesaida3.grid(column=4, row=10, padx=2, pady=2)

def bt_botaoEnviarDados():
    nome_dent = entrada1.get()
    idade_dent = entrada2.get()
    CPF_dent = entrada3.get()
    telefone_dent = entrada4.get()
    Especializacao_dent = entrada5.get()
    Obs_dent = entrada6.get()

    bd_conex.inseredentista(nome_dent, idade_dent, CPF_dent, telefone_dent, Especializacao_dent, Obs_dent)

def bt_botaoEnviarDadosPac():
    nome_paciente = entrada7.get()
    idade_paciente = entrada8.get()
    cpf_paciente = entrada9.get()
    telefone_paciente = entrada10.get()
    obs_paciente = entrada11.get()

    bd_conex.inserepacientenobd(nome_paciente, idade_paciente, cpf_paciente, telefone_paciente, obs_paciente)

def botaoEnviaDadosConsulta():
    tipoDeAtendimento = entrada13.get()
    dataDaConsulta = calendarioConsulta.get_date()
    nomePaciente = entrada14.get()
    nomeDentista = entrada15.get()

    bd_conex.insereconsultabd(tipoDeAtendimento, dataDaConsulta, nomePaciente, nomeDentista)

    ultimaconsulta = bd_conex.ultimaConsultaMarcada()
    paciente = bd_conex.ultimaConsultaMarcadaPaciente()
    dentista = bd_conex.ultimaConsultaMarcadDentista()

    textoultimaconsulta = Label(root, text=f'Ultima Consulta marcada para o dia: {ultimaconsulta} ')
    textoultimaconsulta2 = Label(root, text=f'Paciente: {paciente} ')
    textoultimaconsulta3 = Label(root, text=f'Dentista: {dentista} ')

    textoultimaconsulta.grid(column=3, row=15, padx=5, pady=2)
    textoultimaconsulta2.grid(column=3, row=16, padx=5, pady=2)
    textoultimaconsulta3.grid(column=3, row=17, padx=5, pady=2)
root = ThemedTk(theme="arc")
root.title("Sistema de Odontologia")

#entradas e combobox para dentistas
entrada1 = criar_entrada_label(root, 'Digite o nome do dentista', 1, 1, rowspan=3)
entrada2 = criar_entrada_label(root, 'Digite a idade do dentista', 1, 4)
entrada3 = criar_entrada_label(root, 'Digite o CPF do dentista', 1, 6)
entrada4 = criar_entrada_label(root, 'Digite o Telefone do dentista', 1, 8)
entrada5 = criar_combobox_label(root, 'Digite a Especialização do dentista',
                                ["Clinico Geral", "Ortodontia", "Implantodontia", "Traumatologia", "Periodontia",
                                 "Endodontia", "Dentistica", "Harmonização Orofacial"], 1, 10)
entrada6 = criar_entrada_label(root, 'Digite alguma Observação do dentista', 1, 12)

#entradas para pacientes
entrada7 = criar_entrada_label(root, 'Digite o nome do Paciente', 2, 1, rowspan=3)
entrada8 = criar_entrada_label(root, 'Digite a idade do Paciente', 2, 4)
entrada9 = criar_entrada_label(root, 'Digite o CPF do Paciente', 2, 6)
entrada10 = criar_entrada_label(root, 'Digite o Telefone do Paciente', 2, 8)
entrada11 = criar_entrada_label(root, 'Digite alguma Observação do Paciente', 2, 10)

#calendario e combobox para consulta
calendarioConsulta = Calendar(root, selectmode='day', year=2023, month=10, day=21)
calendarioConsulta.grid(column=3, row=2, padx=5, pady=2, rowspan=5)

entrada13 = criar_combobox_label(root, 'Selecione o tipo do atendimento',
                                 ["Limpeza e exames Dentários", "Tratamento de Caries",
                                  "Tratamento de Gengivite e Periodontite", "Tratamento de Canal Radicular",
                                  "Extrações Dentárias", "Protese Dentárias", "Ortodontia", "Implantes Dentários",
                                  "Odontopediatria", "Odontologia Estetica", "Tratamento de disfunção",
                                  "Odontologia Preventiva", "Cirurgia Oral", "Odontologia Geriatrica"], 3, 7)

todospac = bd_conex.SelecionaPacientes()
todosdent = bd_conex.SelecionaDentista()

entrada14 = criar_combobox_label(root, 'Pacientes', todospac, 3,9 )
entrada15 = criar_combobox_label(root, 'Dentista', todosdent, 3,11 )

#botoes
analiseDados_button = criar_botao(root, 'Analisar Dados e Mostrar na Tela', analiseDadosMostrarNatela, 4, 14)
botaoEnviarDados = criar_botao(root, 'Enviar Dados do dentista', bt_botaoEnviarDados, 1, 14)
botaoEnviarDadosPac = criar_botao(root, 'Enviar Dados do paciente', bt_botaoEnviarDadosPac, 2, 14)
botaoEnviarDadosConst = criar_botao(root, 'Enviar Dados da Consulta', botaoEnviaDadosConsulta, 3, 14)

root.geometry("1100x500")
root.mainloop()
