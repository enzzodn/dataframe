import pandas as pd
import os

os.system('cls')

def head():
    print(
    '|---------------------------------------------------------|\n'
    '|--------------- BOLETIM GERAL (MATEMÁTICA) --------------|\n'
    '|---------------------------------------------------------|\n'
    )

head()
num_alunos = int(input('Quantidade de alunos: '))

os.system('cls')
head()

i = 1
alunos = []
notas = []

while i <= num_alunos:
    print('\nNomes do alunos:\n')
    aluno = input(f'ALUNO {i}: ')
    nota = float(input(f'NOTA DO ALUNO {i}: '))
    print('  ')
    alunos.append(aluno)
    notas.append(nota)
    i+=1
    os.system('cls')
    head()

print('\n--------------- TABELA ---------------\n')

for i in range(num_alunos):
    print(f'{alunos[i]} => {notas[i]}')

print('\n--------------- DATAFRAME ---------------\n')
df = pd.DataFrame(
    {
        'ALUNO': alunos,
        'NOTA': notas
    }
)
print(df)
df.to_excel('dados_alunos.xlsx')
print('\nDataFrame => Excel [OK]')

print('\n-------------------\n')
esp = input('voce quer mostrar a nota de algum aluno especifico? (s/n): ')

if esp.lower() == 's':
    os.system('cls')
    head()
    print(df)

    linha = int(input('\nLinha: '))
    os.system('cls')
    head()
    print(df.iloc[linha])

    qt = 's'
    while qt.lower() == 's':
        print('\n-------------------\n')
        qt = input('Voce quer mostrar a nota de outro aluno? (s/n): ')

        if qt.lower() == 's':
            os.system('cls')
            head()
            print(df)

            linha = int(input('\nLinha: '))
            os.system('cls')
            head()
            print(df.iloc[linha])
        else:
            os.system('cls')
            break

elif esp.lower() == 'n':
    os.system('cls')
    print('   ')

head()
print("\n---------- RELATORIO GERAL ----------\n")
print(df)

maior = df.sort_values('NOTA')
print('\n--------------- MENOR => MAIOR ---------------\n')
print(maior)

max = df['NOTA'].max()
min = df['NOTA'].min()
med = df['NOTA'].mean()
print(f'\nMAIOR NOTA: {max}')
print(f'MENOR NOTA: {min}')
print(f'MEDIA GERAL DA TURMA: {med}\n')