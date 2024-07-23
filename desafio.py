# Escreva um programa em Python que solicita ao usuário para 
# digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. 
# O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o 
# valor do salário em comparação com o bônus recebido
CONSTATNTE_BONUS = 1000
nome_do_usuario = input("Digite seu nome: ")
salario_do_usuario = float(input("Digite o seu salario: "))
bonus_do_ususario = float(input("digite o seu bonus: "))
valor_do_bonus = CONSTATNTE_BONUS + salario_do_usuario * bonus_do_ususario

print(f"O usuário {nome_do_usuario} possui o bonus de {valor_do_bonus}")
