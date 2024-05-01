# Definindo Banco de Dados SQLite do Python
import sqlite3
# Abrir o Arquivo Fatec.db
conexao= sqlite3.connect('Fatec.db')
# Criar a Tabela
query = '''
CREATE TABLE tabela (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    curso VARCHAR(3) NOT NULL,
    semestre INTEGER NOT NULL,
    diasemana VARCHAR(3) NOT NULL,
    horario VARCHAR(11),
    materia VARCHAR(30),
    professor VARCHAR(30),
    sala VARCHAR(5)
)
'''
#conexao.execute(query)
"""
# Inserir os Dados do Curso
# DSM 1.Semestre
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 1,'SEG','19:00 20:40','ALGORITMOS E LOGICA DE PROGRAMACAO','NILTON',  'LAB1 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 1,'SEG','20:50 22:30','ALGORITMOS E LOGICA DE PROGRAMACAO','NILTON',  'LAB1 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 1,'TER','19:00 20:40','SISTEMAS OPERACIONAIS E REDES',     'FERNANDO','LAB1 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 1,'TER','20:50 22:30','SISTEMAS OPERACIONAIS E REDES',     'FERNANDO','LAB1 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 1,'QUA','19:00 20:40','ENGENHARIA DE SOFTWARE I',          'ORLANDO', 'LAB1 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 1,'QUA','20:50 22:30','ENGENHARIA DE SOFTWARE I',          'ORLANDO', 'LAB1 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 1,'QUI','19:00 20:40','MODELAGEM DE BANCO DE DADOS',       'ANGELA',  'LAB1 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 1,'QUI','20:50 22:30','MODELAGEM DE BANCO DE DADOS',       'ANGELA',  'LAB1 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 1,'SEX','19:00 20:40','DESIGN DIGITAL',                    'LEONARDO','LAB1 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 1,'SEX','20:50 22:30','DESIGN DIGITAL',                    'LEONARDO','LAB1 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 1,'SAB','09:30 11:10','DESENVOLVIMENTO WEB I',             'BRUNO',   'LAB1 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 1,'SAB','11:20 13:00','DESENVOLVIMENTO WEB I',             'BRUNO',   'LAB1 ')")
# DSM 2.Semestre
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 2,'SEG','19:00 20:40','DESENVOLVIMENTO WEB II',    'ORLANDO','LAB5 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 2,'SEG','20:50 22:30','DESENVOLVIMENTO WEB II',    'ORLANDO','LAB5 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 2,'TER','19:00 20:40','ENGENHARIA DE SOFTWARE II', 'BRUNO',  'LAB5 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 2,'TER','20:50 22:30','ENGENHARIA DE SOFTWARE II', 'BRUNO',  'LAB5 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 2,'QUA','19:00 20:40','MATEMATICA PARA COMPUTACAO','VAGNER', 'SALA6')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 2,'QUA','20:50 22:30','MATEMATICA PARA COMPUTACAO','VAGNER', 'SALA6')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 2,'QUI','19:00 20:40','BANCO DE DADOS RELACIONAL', 'NILTON', 'LAB2 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 2,'QUI','20:50 22:30','BANCO DE DADOS RELACIONAL', 'NILTON', 'LAB2 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 2,'SEX','19:00 20:40','TECNICAS DE PROGRAMACAO I', 'JEANE',  'LAB5 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 2,'SEX','20:50 22:30','TECNICAS DE PROGRAMACAO I', 'JEANE',  'LAB5 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 2,'SAB','09:30 11:10','ESTRUTURA DE DADOS',        'ORLANDO','LAB2 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 2,'SAB','11:20 13:00','ESTRUTURA DE DADOS',        'ORLANDO','LAB2 ')")
# DSM 3.Semestre
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 3,'SEG','19:00 20:40','ALGEBRA LINEAR',                  'JOAO',         'SALA6')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 3,'SEG','20:50 22:30','ALGEBRA LINEAR',                  'JOAO',         'SALA6')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 3,'TER','19:00 20:40','INGLES I',                        'MARCELO',      'LAB2 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 3,'TER','20:50 22:30','INTERACAO HUMANO COMPUTADOR',     'LEONARDO',     'LAB2 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 3,'QUA','19:00 20:40','TECNICAS DE PROGRAMACAO II',      'ESDRAS',       'LAB2 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 3,'QUA','20:50 22:30','TECNICAS DE PROGRAMACAO II',      'ESDRAS',       'LAB2 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 3,'QUI','19:00 20:40','DESENVOLVIMENTO WEB III',         'ORLANDO',      'LAB4 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 3,'QUI','20:50 22:30','DESENVOLVIMENTO WEB III',         'ORLANDO',      'LAB4 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 3,'SEX','19:00 20:40','BANCO DE DADOS NAO RELACIONAL',   'THIAGO MENDES','LAB2 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 3,'SEX','20:50 22:30','BANCO DE DADOS NAO RELACIONAL',   'THIAGO MENDES','LAB2 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 3,'SAB','09:30 11:10','GESTAO AGIL DE PROJETOS',         'RENATO',       'LAB5 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 3,'SAB','11:20 13:00','GESTAO AGIL DE PROJETOS',         'RENATO',       'LAB5 ')")
# DSM 4.Semestre
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 4,'SEG','19:00 20:40','ESTATISTICA APLICADA',                  'JOSE FIDELI',               'SALA5')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 4,'SEG','20:50 22:30','ESTATISTICA APLICADA',                  'JOSE FIDELI',               'SALA5')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 4,'TER','19:00 20:40','EXPERIENCIA DO USUARIO',                'LEONARDO SOUZA DE LIMA',    'LAB2 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 4,'TER','20:50 22:30','INGLES II',                             'MARCELO LOCOSELLI BRETANHA','SALA5')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 4,'QUA','19:00 20:40','LABORATORIO DE DESENVOLVIMENTO WEB',    'FERNANDO BRYAN FRIZARIN',   'LAB5 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 4,'QUA','20:50 22:30','LABORATORIO DE DESENVOLVIMENTO WEB',    'FERNANDO BRYAN FRIZARIN',   'LAB5 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 4,'QUI','19:00 20:40','INTERNET DAS COISAS E APLICACOES',      'ADRIANO CILHOS DOIMO',      'LAB6 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 4,'QUI','20:50 22:30','INTERNET DAS COISAS E APLICACOES',      'ADRIANO CILHOS DOIMO',      'LAB6 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 4,'SEX','19:00 20:40','PROGRAMACAO PARA DISPOSITIVOS MOVEIS I','JONAS BODE',                'LAB4 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 4,'SEX','20:50 22:30','PROGRAMACAO PARA DISPOSITIVOS MOVEIS I','JONAS BODE',                'LAB4 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 4,'SAB','09:30 11:10','INTEGRACAO E ENTREGA CONTINUA',         'YURI',                      'LAB3 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 4,'SAB','11:20 13:00','INTEGRACAO E ENTREGA CONTINUA',         'YURI',                      'LAB3 ')")
# DSM 5.Semestre
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 5,'SEG','19:00 20:40','FUNDAMENTOS DA REDACAO TECNICA',                        'ANA LUCIA',    'APOI1')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 5,'SEG','20:50 22:30','INGLES III',                                            'NATALIA',      'APOI1')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 5,'TER','19:00 20:40','LABORATORIO DE DESENVOLVIMENTO PARA APLICATIVOS MOVEIS','ESDRAS',       'LAB4 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 5,'TER','20:50 22:30','LABORATORIO DE DESENVOLVIMENTO PARA APLICATIVOS MOVEIS','ESDRAS',       'LAB4 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 5,'QUA','19:00 20:40','COMPUTACAO EM NUVEM I',                                 'SAMA',         'LAB3 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 5,'QUA','20:50 22:30','COMPUTACAO EM NUVEM I',                                 'SAMA',         'LAB3 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 5,'QUI','19:00 20:40','SEGURANCA NO DESENVOLVIMENTO DE APLICACOES',            'JONAS',        'LAB5 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 5,'QUI','20:50 22:30','SEGURANCA NO DESENVOLVIMENTO DE APLICACOES',            'JONAS',        'LAB5 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 5,'SEX','19:00 20:40','PROGRAMACAO PARA DISPOSITIVOS MOVEIS II',               'ESDRAS',       'LAB3 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 5,'SEX','20:50 22:30','PROGRAMACAO PARA DISPOSITIVOS MOVEIS II',               'ESDRAS',       'LAB3 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 5,'SAB','09:30 11:10','APRENDIZAGEM DE MAQUINA',                               'THIAGO MENDES','LAB4 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 5,'SAB','11:20 13:00','APRENDIZAGEM DE MAQUINA',                               'THIAGO MENDES','LAB4 ')")
# DSM 6.Semestre
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 6,'SEG','19:00 20:40','LABORATORIO DESENVOLVIMENTO MULTIPLATAFORMA','ESDRAS',        'LAB4 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 6,'SEG','20:50 22:30','LABORATORIO DESENVOLVIMENTO MULTIPLATAFORMA','ESDRAS',        'LAB4 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 6,'TER','19:00 20:40','QUALIDADE DE TESTE DE SOFTWARE',             'ORLANDO',       'APOI1')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 6,'TER','20:50 22:30','QUALIDADE DE TESTE DE SOFTWARE',             'ORLANDO',       'APOI1')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 6,'QUA','19:00 20:40','ETICA PROFISSIONAL E PATENTE',               'PEDRO',         'APOI1')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 6,'QUA','20:50 22:30','INGLES IV',                                  'NATALIA',       'APOI1')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 6,'QUI','19:00 20:40','MINERACAO DE DADOS',                         'IVONE',         'APOI1')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 6,'QUI','20:50 22:30','MINERACAO DE DADOS',                         'IVONE',         'APOI1')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 6,'SEX','19:00 20:40','COMPUTACAO EM NUVEM II',                     'JONAS FERREIRA','APOI1')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 6,'SEX','20:50 22:30','COMPUTACAO EM NUVEM II',                     'JONAS FERREIRA','APOI1')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 6,'SAB','09:30 11:10','PROCESSAMENTO DE LINGUAGEM NATURAL',         'CLEBERSON',     'LAB6 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('DSM', 6,'SAB','11:20 13:00','PROCESSAMENTO DE LINGUAGEM NATURAL',         'CLEBERSON',     'LAB6 ')")

# GE
# GE 1.Semestre
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 1,'SEG','19:00 20:40','INGLES I',                     'ZENAIDE',  'SALA4')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 1,'SEG','20:50 22:30','INFORMATICA APLICADA A GESTAO','YURI',     'LAB2 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 1,'TER','19:00 20:40','MATEMATICA',                   'JOAO',     'SALA2')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 1,'TER','20:50 22:30','MATEMATICA',                   'JOAO',     'SALA2')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 1,'QUA','19:00 20:40','CONTABILIDADE',                'LUCIANO',  'SALA2')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 1,'QUA','20:50 22:30','METODOS P CONHECIMENTO ',      'LUCIANO',  'SALA2')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 1,'QUI','19:00 20:40','COMUNICACAO E EXPRESSAO',      'ANA LUCIA','SALA6')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 1,'QUI','20:50 22:30','COMUNICACAO E EXPRESSAO',      'ANA LUCIA','SALA6')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 1,'SEX','19:00 20:40','TEORIA DAS ORGANIZACOES',      'ZORZO',    'SALA6')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 1,'SEX','20:50 22:30','TEORIA DAS ORGANIZACOES',      'ZORZO',    'SALA6')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 1,'SAB','09:30 11:10','PROJETO INTEGRADOR',           'AMANDA',   '     ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 1,'SAB','11:20 13:00','PROJETO INTEGRADOR',           'AMANDA',   '     ')")
# GE 2.Semestre
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 2,'SEG','19:00 20:40','ESPANHOL I',             'LUIS ADORNO','MAKER')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 2,'SEG','20:50 22:30','INGLES II',              'ZENAIDE',    'SALA4')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 2,'TER','19:00 20:40','GESTAO DE PESSOAS',      'ZORZO',      'SALA3')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 2,'TER','20:50 22:30','GESTAO DE PESSOAS',      'ZORZO',      'SALA3')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 2,'QUA','19:00 20:40','ECONOMIA',               'NELSON',     'SALA5')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 2,'QUA','20:50 22:30','ECONOMIA',               'NELSON',     'SALA5')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 2,'QUI','19:00 20:40','PROJETO INTEGRADOR II',  'AMANDA',     'LAB3 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 2,'QUI','20:50 22:30','PROJETO INTEGRADOR II',  'AMANDA',     'LAB3 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 2,'SEX','19:00 20:40','CMP TMT. ORGANIZACIONAL','EDUARDO',    'SALA3')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 2,'SEX','20:50 22:30','CMP TMT. ORGANIZACIONAL','EDUARDO',    'SALA3')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 2,'SAB','09:30 11:10','ESTATISTICA',            'CLAYDE',     'SALA3')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 2,'SAB','11:20 13:00','ESTATISTICA',            'CLAYDE',     'SALA3')")
# GE 3.Semestre
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 3,'SEG','19:00 20:40','SISTEMAS DE INFORMACAO','YURI',       'LAB2 ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 3,'SEG','20:50 22:30','ESPANHOL II',           'LUIS ADORNO','MAKER')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 3,'TER','19:00 20:40','DIREITO EMPRESARIAL',   'PEDRO',      'SALA4')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 3,'TER','20:50 22:30','DIREITO EMPRESARIAL',   'PEDRO',      'SALA4')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 3,'QUA','19:00 20:40','INGLES III',            'MARCELO',    'SALA4')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 3,'QUA','20:50 22:30','MATEMATICA FINANCEIRA', 'JOAO',       'SALA3')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 3,'QUI','19:00 20:40','GESTAO DE MARKETING',   'DHEBORA',    'SALA2')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 3,'QUI','20:50 22:30','GESTAO DE MARKETING',   'DHEBORA',    'SALA2')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 3,'SEX','19:00 20:40','GESTAO POR PROCESSOS',  'JOCLENES',   'SALA2')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 3,'SEX','20:50 22:30','GESTAO POR PROCESSOS',  'JOCLENES',   'SALA2')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 3,'SAB','09:30 11:10','PROJETO INTEGRADOR III','DHEBORA',    '     ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 3,'SAB','11:20 13:00','PROJETO INTEGRADOR III','DHEBORA',    '     ')")
# GE 4.Semestre
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 4,'SEG','19:00 20:40','GESTAO DE SERVICOS',               'AMANDA',         'SALA3')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 4,'SEG','20:50 22:30','GESTAO DE SERVICOS',               'AMANDA',         'SALA3')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 4,'TER','19:00 20:40','GESTAO DE OPERACOES E LOGISTICA',  'VAGNER FERREIRA','SALA6')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 4,'TER','20:50 22:30','GESTAO DE OPERACOES E LOGISTICA',  'VAGNER FERREIRA','SALA6')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 4,'QUA','19:00 20:40','GESTAO AMBIENTAL',                 'EDITAL',         'SALA3')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 4,'QUA','20:50 22:30','INGLES IV',                        'MARCELO',        'SALA4')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 4,'QUI','19:00 20:40','MODELAGEM E SIMULACAO DE NEGOCIOS','DAISY',          'SALA3')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 4,'QUI','20:50 22:30','MODELAGEM E SIMULACAO DE NEGOCIOS','DAISY',          'SALA3')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 4,'SEX','19:00 20:40','GESTAO FINANCEIRA',                'LUCIANO',        'SL1A ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 4,'SEX','20:50 22:30','GESTAO FINANCEIRA',                'LUCIANO',        'SL1A ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 4,'SAB','09:30 11:10','PROJETO INTEGRADOR IV',            'DAISY',          '     ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 4,'SAB','11:20 13:00','PROJETO INTEGRADOR IV',            'DAISY',          '     ')")
# GE 5.Semestre
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 5,'SEG','19:00 20:40','GESTAO DA QUALIDADE',              'VAGNER FERREIRA','SL1A ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 5,'SEG','20:50 22:30','GESTAO DE SERVICOS',               'VAGNER FERREIRA','SL1A ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 5,'TER','19:00 20:40','GESTAO EMPREENDEDORA',             'FASSINA',        'SL1B ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 5,'TER','20:50 22:30','GESTAO EMPREENDEDORA',             'FASSINA',        'SL1B ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 5,'QUA','19:00 20:40','GESTAO DE PROJETOS',               'VITAL',          'SL1A ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 5,'QUA','20:50 22:30','GESTAO DE PROJETOS',               'VITAL',          'SL1A ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 5,'QUI','19:00 20:40','GESTAO DA INOVACAO',               'ZORZO',          'SL1A ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 5,'QUI','20:50 22:30','GESTAO DA INOVACAO',               'ZORZO',          'SL1A ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 5,'SEX','19:00 20:40','GESTAO DO CONHECIMENTO',           'LEANDRO',        'SALA5')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 5,'SEX','20:50 22:30','INGLES V',                         'NATALIA',        'SL1B ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 5,'SAB','09:30 11:10','PROJETO INTEGRADOR V',             'VAGNER FERREIRA','     ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 5,'SAB','11:20 13:00','PROJETO INTEGRADOR V',             'VAGNER FERREIRA','     ')")
# GE 6.Semestre
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 6,'SEG','19:00 20:40','SISTEMA DE G INTEGRADOS',              'RENATO',         'SL1B ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 6,'SEG','20:50 22:30','SISTEMA DE G INTEGRADOS',              'RENATO',         'SL1B ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 6,'TER','19:00 20:40','PLANEJAMENTO E G ESTRATEGICA',         'LUCAS SILVESTRE','SL1A ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 6,'TER','20:50 22:30','PLANEJAMENTO E G ESTRATEGICA',         'LUCAS SILVESTRE','SL1A ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 6,'QUA','19:00 20:40','DESENVOLVIMENTO DE NEGOCIOS',          'RENATO',         'SL1B ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 6,'QUA','20:50 22:30','DESENVOLVIMENTO DE NEGOCIOS',          'RENATO',         'SL1B ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 6,'QUI','19:00 20:40','NEGOCIOS INTERNACIONAIS',              'NELSON',         'SL1B ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 6,'QUI','20:50 22:30','NEGOCIOS INTERNACIONAIS',              'NELSON',         'SL1B ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 6,'SEX','19:00 20:40','INGLES VI',                            'NATALIA',        'SL1B ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 6,'SEX','20:50 22:30','RESPONSABILIDADE SOCIAL E EMPRESARIAL','LEANDRO',        'SALA5')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 6,'SAB','09:30 11:10','PROJETO INTEGRADOR VI',                'GUSTAVO',        '     ')")
conexao.execute("INSERT INTO tabela (curso,semestre,diasemana,horario,materia,professor,sala) VALUES('GE', 6,'SAB','11:20 13:00','PROJETO INTEGRADOR VI',                'GUSTAVO',        '     ')")
"""

# Informar Curso e Semestre
curso1    = input("Digite seu CURSO(DSM/GE)--------->: ")
semestre1 = input("Digite seu SEMESTRE(1/2/3/4/5/6) >: ")
diasemana1= input("Digite dia SEG/TER/QUA/QUI/SEX/SAB: ")
curso1=curso1.upper()
diasemana1=diasemana1.upper()
# Exibe uma mensagem usando os dados fornecidos pelo usuário
print("Voce escolheu CURSO/SEMESTRE: ", curso1, semestre1, diasemana1)

# Listar os Dados
# Consulta DSM todos os dias da semana 4.Semestre
#consulta = conexao.execute("SELECT * FROM tabela where curso = 'DSM' and semestre =4")
if semestre1=="":
    busca="SELECT * FROM tabela where curso = '"+curso1+"'"
elif diasemana1=="":
    busca="SELECT * FROM tabela where curso = '"+curso1+"' and semestre = "+semestre1
else:
    busca="SELECT * FROM tabela where curso = '"+curso1+"' and semestre = "+semestre1+" and diasemana = '"+diasemana1+"'"
print(busca)

consulta = conexao.execute(busca)
# Consulta DSM do dia (SEGUNDA) do 4.Semestre
#consulta = conexao.execute("SELECT * FROM tabela where curso = curso1 and semestre = semestre1 and diasemana='QUA'")

# Lista toda a tabela
#consulta = conexao.execute("SELECT * FROM tabela")
for linha in consulta:
    print (linha)

# Gravar e Fechar 
conexao.commit()
conexao.close()
