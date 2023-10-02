import sqlite3
import pandas as pd

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
                    " id_pac INTEGER, "
                    " id_dent INTEGER, "
                    " atendimento TEXT, "
                    " FOREIGN KEY (id_dent) REFERENCES dentista(id_dent), "
                    " FOREIGN KEY (id_pac) REFERENCES pacientes(id_pac) );")
        print("Tabela consulta criada com sucesso")
    except:
            print('As tabelas ja existem')

def inseredentista(nome_dent, idade_dent, cpf_dent, telefone, obs_dent, especializacao):
    cursor.execute("INSERT INTO dentista (nome_dent, idade_dent, cpf_dent, telefone, obs_dent, especializacao) VALUES (?, ?, ?, ?, ?, ?)",
                    (nome_dent, idade_dent, cpf_dent, telefone, obs_dent, especializacao)) 
    conexao.commit()


dados = pd.read_sql('SELECT * FROM dentista', conexao)
idade = pd.read_sql('SELECT SUM(idade_dent) FROM dentista',conexao )

mediaIdade = idade / 4

print("As idade são ",dados)
print("A media das idades é ", mediaIdade)
