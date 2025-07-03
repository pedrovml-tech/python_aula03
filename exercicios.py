### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

# quantidade = 10
# preco = 39.99

# if quantidade > 0 and preco > 0:
#     print("Dados válidos.")
# else:
#     print("Dados inválidos.")

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

# temperatura = 18

# if temperatura < 18:
#     print("Baixa")
# elif 18 >= temperatura <= 26:
#     print("Média")
# else:
#     print("Alta")

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

# if log['level'] == 'ERROR':
#     print(log['message'])

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# idade = 18
# email = "useremail@gmail.com"

# if not 18 <= idade <= 65:
#     print("Idade inválida.")

# if "@" not in email or "." not in email:
#     print("Email inválido")


### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

# transacao = {'valor': 2000, 'hora': 19}

# valor = transacao['valor']
# hora = transacao['hora']

# if valor > 10000 or not 9 < hora < 20:
#     print("Transação suspeita")
# else:
#     print("Transação ok.")

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

# texto = "Essa será uma semana produtiva, ao contrário da semana passada"

# texto_formatado = texto.replace(",", "")

# lista_palavras = texto_formatado.split() # Sem passar parametros o split considera o "espaço" por default.

# dict_palavras = {}

# for palavra in lista_palavras:
#     if palavra in dict_palavras:
#         dict_palavras[palavra] += 1
#     else:
#         dict_palavras[palavra] = 1

# print(dict_palavras)

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

# numeros = [10, 20, 30, 40, 50]
# minimo = min(numeros)
# maximo = max(numeros)
# normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

# print(normalizados)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

# usuarios = [
#     {"nome": "Alice", "email": "alice@example.com"},
#     {"nome": "Bob", "email": ""},
#     {"nome": "Carol", "email": "carol@example.com"}
# ]

# for usuario in usuarios:
#     for campo in usuario:
#         if usuario[campo] == "":
#             print(f"O campo {campo} do usuario {usuario["nome"]} está vazio")



### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

# lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# pares = []

# for numero in lista:
#     if numero % 2 == 0:
#         pares.append(numero)

# print(pares)


# numeros = range(0, 11)
# pares = [x for x in numeros if x % 2 == 0]

# print(pares)


### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

# vendas = [
#     {"categoria": "eletrônicos", "valor": 1200},
#     {"categoria": "livros", "valor": 200},
#     {"categoria": "eletrônicos", "valor": 800}
# ]

# resultado = {}

# for venda in vendas:
#     categoria = venda['categoria']
#     valor = venda['valor']

#     if categoria in resultado:
#         resultado[categoria] += valor
#     else:
#         resultado[categoria] = valor

# print(resultado)

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

# palavra = ""

# while palavra != 'sair':
#     palavra = input("Digite algo: ")

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

# numero = -1

# while numero < 0 or numero > 10:
#     numero = int(input("Digite um número entre 0 e 10: "))


### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

# pagina_atual = 1
# paginas_totais = 5  # Simulação, na prática, isso viria da API

# while pagina_atual <= paginas_totais:
#     print(f"Lendo a pagina {pagina_atual} de {paginas_totais}")
#     pagina_atual += 1

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

# tentativa = 1
# limite = 3

# while tentativa <= limite:
#     print(f"Tentativa de conexão {tentativa} de {limite}")
#     tentativa += 1


### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

# itens = [1, 2, 3, "parar", 4, 5]

# i = 0

# while i < len(itens):
#     if itens[i] == "parar":
#         print(f"Encontrado o ponto de parada na posição de índice {i}")
#         break

#     print(f"Processando o item {itens[i]} - Índice {i}")
#     i += 1
