import random
import os
os.system("cls")

# Pergunta quantos itens o usuário quer cadastrar
total_itens = int(input("Quantos itens você quer digitar? "))

# Lista para armazenar os itens
itens = []

# Loop para coletar os itens individualmente
for i in range(total_itens):
    item = input(f"Digite o item {i + 1}: ")
    itens.append(item)

# Verifica a quantidade máxima de sorteios possíveis (sem repetir)
max_sorteios = len(itens)

# Pergunta quantos sorteios devem ser feitos
quantidade = int(input(f"Quantos sorteios você deseja fazer? (máximo {max_sorteios}): "))

# Garante que não ultrapasse o número de itens disponíveis
if quantidade > max_sorteios:
    print(f"Você pediu mais sorteios do que itens disponíveis. Serão realizados {max_sorteios} sorteios.")
    quantidade = max_sorteios

# Embaralha os itens e seleciona os primeiros `quantidade`
random.shuffle(itens)

print("\nSorteios (sem repetição):")
for i in range(quantidade):
    print(f"{i + 1}: {itens[i]}")
