# Base de dados com usuários já classificados.
# Cada registro possui:
# [download, upload, acessos simultâneos, tempo de conexão, perfil]

dados = [
    [120, 10, 3, 250, 'P1'],
    [200, 25, 5, 400, 'P2'],
    [80, 5, 2, 180, 'P1'],
    [300, 30, 6, 500, 'P3'],
    [250, 40, 7, 600, 'P3'],
    [150, 12, 4, 320, 'P2'],
    [90, 8, 3, 200, 'P1'],
    [310, 35, 6, 520, 'P3'],
    [170, 15, 4, 350, 'P2'],
    [85, 6, 2, 190, 'P1'],
    [220, 18, 5, 410, 'P2'],
    [305, 38, 6, 510, 'P3'],
    [130, 11, 3, 270, 'P1'],
    [260, 42, 7, 580, 'P3'],
    [160, 14, 4, 330, 'P2'],
    [100, 9, 2, 210, 'P1'],
    [240, 28, 6, 460, 'P3'],
    [180, 16, 4, 370, 'P2'],
    [95, 7, 2, 195, 'P1'],
    [270, 40, 6, 590, 'P3']
]


# Função para calcular a distância euclidiana entre dois vetores
def distancia_euclidiana(vetor1, vetor2):
    soma = 0

    # Soma dos quadrados das diferenças
    for i in range(len(vetor1)):
        soma += (vetor1[i] - vetor2[i]) ** 2

    # Retorna a raiz quadrada da soma
    return soma ** 0.5


# Função responsável por classificar um novo usuário
def classificar(novo_usuario, dados):

    # Inicializa com infinito para garantir
    # que a primeira distância encontrada seja menor
    menor_distancia = float('inf')

    perfil = ""

    # Percorre todos os registros da base
    for registro in dados:

        # Separa atributos e classe
        atributos = registro[:-1]
        classe = registro[-1]

        # Calcula a distância entre o usuário novo
        # e o registro atual
        distancia = distancia_euclidiana(novo_usuario, atributos)

        # Verifica se encontrou uma distância menor
        if distancia < menor_distancia:
            menor_distancia = distancia
            perfil = classe

    return perfil, menor_distancia


# Quantidade de atributos utilizados na classificação
qtd_atributos = len(dados[0]) - 1

# Lista que armazenará os dados do novo usuário
novo_usuario = []

# Entrada de dados
download = float(input("Download médio diário (MB): "))
upload = float(input("Upload médio diário (MB): "))
acessos = float(input("Número médio de acessos simultâneos: "))
tempo = float(input("Tempo médio de conexão por dia (minutos): "))

# Adiciona os atributos na lista
novo_usuario.append(download)
novo_usuario.append(upload)
novo_usuario.append(acessos)
novo_usuario.append(tempo)

# Realiza a classificação
perfil, distancia = classificar(novo_usuario, dados)

# Exibe o resultado
print("\nResultado da classificação")
print("Perfil:", perfil)
print("Menor distância:", round(distancia, 2))