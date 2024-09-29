# Enunciado: Crie um programa que receba a nota de 5 alunos e exiba quantos foram aprovados (nota maior ou igual a 7).
quant_alunos = 5
quant_aprovados = 0

for cont in range(0,quant_alunos):
    nota = float(input('Digite um valor: '))
    if nota >= 7:
        quant_aprovados = quant_aprovados + 1
        
print(f'O total de aprovados com nota maior ou igual a 7 é = {quant_aprovados}')