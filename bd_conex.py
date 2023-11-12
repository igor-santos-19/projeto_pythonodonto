import sqlite3
import pandas as pd
from datetime import datetime

conexao = sqlite3.connect('odontodb')
print('banco conectado sqlite', conexao)

cursor = conexao.cursor()

def cria_tabelas():
    try:
        cursor.execute( 
            " CREATE TABLE pacientes (" 
                        " id_pac INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
                        " nome_pac TEXT NOT NULL, "
                        " idade_pac INTEGER NOT NULL, " 
                        " cpf_pac VARCHAR(11) NOT NULL, "
                        " telefone TEXT, "
                        " obs_pac TEXT "
                        " ); "
                            )
        print('Tabela pacientes criada com sucesso')
        cursor.execute( 
            " CREATE TABLE dentista (" 
                        " id_dent INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
                        " nome_dent TEXT NOT NULL, "
                        " idade_dent INTEGER NOT NULL, " 
                        " cpf_dent VARCHAR(11) NOT NULL, "
                        " telefone TEXT, "
                        " obs_dent TEXT, "
                        " especializacao TEXT "
                        " ); "
                            )
        print('Tabela dentista com sucesso')
        cursor.execute(" CREATE TABLE consultas ( "
                    " id_con INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, "
                    " dataConsulta DATE NOT NULL, "
                    " paciente TEXT, "
                    " dentista TEXT, "
                    " atendimento TEXT ); "
                      )
        print("Tabela consulta criada com sucesso")
    except:
            print('As tabelas ja existem')
# insere dados na tabela

def inseredentista(nome_dent, idade_dent, cpf_dent, telefone, obs_dent, especializacao):
    cursor.execute("INSERT INTO dentista (nome_dent, idade_dent, cpf_dent, telefone, obs_dent, especializacao) VALUES (?, ?, ?, ?, ?, ?)",
                    (nome_dent, idade_dent, cpf_dent, telefone, especializacao, obs_dent )) 
    conexao.commit()

def inserepacientenobd(nome_paciente, idade_paciente, cpf_paciente, telefone_paciente, obs_paciente):
     cursor.execute('INSERT INTO pacientes (nome_pac, idade_pac, cpf_pac, telefone, obs_pac) VALUES(?,?,?,?,?)',
                    (nome_paciente, idade_paciente, cpf_paciente, telefone_paciente, obs_paciente))
     conexao.commit()

def insereconsultabd(tipoDeAtendimento, dataDaConsulta, nomePaciente, nomeDentista):
     cursor.execute('INSERT INTO consultas (atendimento, dataConsulta, paciente, dentista) VALUES (?, ?, ?, ?)',
                    (tipoDeAtendimento, dataDaConsulta, nomePaciente, nomeDentista))
     conexao.commit()
    
#analise dos frames pandas

def mediaIdadeDentista():
    idade = pd.read_sql('SELECT SUM(idade_dent) FROM dentista',conexao ).iloc[0, 0]
    selecionaMaximoId = pd.read_sql('SELECT COUNT(id_dent) FROM dentista', conexao).iloc[0, 0]

    if selecionaMaximoId > 0:
        mediaIdade = float(idade) / float(selecionaMaximoId)
        print("A media das idades dos dentista é", "{:.2f}".format(mediaIdade))
        return mediaIdade
    else:
        print('Não existe nenhum valor por isso nao e possivel tirar media das idades ')
        

def mediaIdadePacientes():
    idade = pd.read_sql('SELECT SUM(idade_pac) FROM pacientes',conexao ).iloc[0, 0]
    selecionaMaximoId = pd.read_sql('SELECT COUNT(id_pac) FROM pacientes', conexao).iloc[0, 0]

    if selecionaMaximoId > 0:
        mediaIdade = float(idade) / float(selecionaMaximoId)
        print("A media das idades dos pacientes é: ", "{:.2f}".format(mediaIdade))
        return mediaIdade
    else:
        print('Não existe nenhum valor por isso nao e possivel tirar media das idades ')
        

def especializacaoDent():   
    TotalClinicoGeral = pd.read_sql('SELECT count(especializacao) from dentista where especializacao = "Clinico Geral"', conexao).iloc[0, 0]
    print("Existem um total de ClinicoGeral dentistas", TotalClinicoGeral)
    return TotalClinicoGeral

def especializacaoDent1():
    TotalOrtodontia = pd.read_sql('SELECT count(especializacao) from dentista where especializacao = "Ortodontia"', conexao).iloc[0, 0]
    print("Existem um total de Ordontntia dentistas", TotalOrtodontia)
    return TotalOrtodontia

def tiposdeAtendPac():
    TotalAtendiPac = pd.read_sql('SELECT count(atendimento) from consultas where atendimento = "Limpeza e exames Dentários"', conexao).iloc[0, 0]
    print(' Existem um total de Limpeza e exames Dentarios', TotalAtendiPac)
    return TotalAtendiPac

def ultimaConsultaMarcada():
    query = pd.read_sql("SELECT dataConsulta FROM consultas ORDER BY id_con DESC LIMIT 1", conexao).iloc[0, 0]

    data_timestamp = datetime.strptime(query, "%m/%d/%y")
    data_formatada = data_timestamp.strftime("%d/%m/%Y")
    return data_formatada

def ultimaConsultaMarcadaPaciente():
    query2 = pd.read_sql("SELECT paciente FROM consultas ORDER BY id_con DESC LIMIT 1", conexao).iloc[0, 0]
    return query2

def ultimaConsultaMarcadDentista():
     query3 = pd.read_sql("SELECT dentista FROM consultas ORDER BY id_con DESC LIMIT 1", conexao).iloc[0, 0]
     return query3

def SelecionaPacientes():
    todosPac = pd.read_sql("SELECT nome_pac FROM PACIENTES", conexao)['nome_pac'].tolist()
    return todosPac

def SelecionaDentista():
    todosDent = pd.read_sql("SELECT nome_dent FROM DENTISTA", conexao)['nome_dent'].tolist()
    return todosDent

def TotaldeConsultas():
    todasconsultas = pd.read_sql("SELECT COUNT(*) as total_tuplas FROM consultas", conexao).iloc[0, 0]
    return todasconsultas

def TotaldeDentistas():
    todosdentistas = pd.read_sql("SELECT COUNT(*) as total_tuplas FROM dentista", conexao).iloc[0, 0]
    return todosdentistas

def TotaldePacientes():
    todospacientes = pd.read_sql("SELECT COUNT(*) as total_tuplas FROM pacientes", conexao).iloc[0, 0]
    return todospacientes

cria_tabelas()
