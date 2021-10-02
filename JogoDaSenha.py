import random as rd

cores = ["amarelo", "vermelho", "verde", "azul", "rosa", "laranja", "roxo"]

def criar_senha(tamanho):
    senha_computador = [] #Cria a lista senha_computador
    while len(senha_computador) < tamanho: #Cria a repetição do laço para preencher a lista
        escolha = rd.choice(cores) #Randomiza a escolha de senha_computador
        if (escolha not in senha_computador): #Verifica se a cor já existe na lista
            senha_computador.append(escolha) #Adiciona uma cor na lista senha_computador
    return senha_computador #retorna a senha_computador

def check_resposta(chute, senha):
    check = [] #Criação de lista auxiliar vazia
    for i in range(len(senha)): #Percorre o tamanho da senha
        if chute[i] == senha[i]: #Verifica se a resposta está idêntica ao gabarito
            check.append("Branco")
        elif chute[i] in senha: #Verifica se a reposta está contida no gabarito
            check.append("Preto")
        else:
            check.append("Vazio") #Verifica se a resposta não está contida no gabarito
    return check
        

def bem_vindo():

    print(f"Bem vindo a jogo da senha! \nVocê terá 10 chances para acertar a senha. \nEscolha quatro cores da lista, uma por vez: \n{cores}")

def pegar_cores(cores_atuais): #Função checa se a lista de cores dada pelo usuário é válida
    check_falha = True #Determina a condição inicial do check
    cor = "" #Cria uma string vazia
    while (check_falha == True): #Define a condição para a checagem
        cor = input() #Guarda uma informação dada pelo usuário
        if ((cor in cores) and (cor not in cores_atuais)): #Verifica se a cor digitada já está na senha do jogador e se ela é permitida pelo jogo
            check_falha = False #Muda a condição inicial para poder resetar o loop
        else:
            print("Digite uma cor válida, por favor") #Pede informação ao usuário novamente, após uma falha

    return cor #retorna as cores escolhidas pelo usuário

def pegar_tentativas(tamanho): #Função que pega as 4 tentativas do usuário
    tentativas = [] #cria a lista de tentativas
    contador = 1 #contador que define até quantas cores ele pode botar em lista tentativas
    while len(tentativas) < tamanho: #loopa tudo até quatro
        print(f"Faça seu {contador}o chute: ") #printa pro usuário a a rodada daquela cor dentro da lista
        chute = pegar_cores(tentativas) #define que o chute vai rodar a função pegar_cores e realizar a análise
        tentativas.append(chute) #Adiciona na lsita tentativas o chute dado pelo usuário
        contador += 1 #gira o contador

    return tentativas

def resultado(resultado, senha_inputada):
    print(f"\nSua escolha é {senha_inputada}\nSeu resultado é {resultado} \n Legenda:\n Branco - Cor certa na posição Certa\n Preto - Cor certa na posição errada\n Vazio - A cor não existe na senha") #imprime a senha dada pelo usuário

def jogo_da_senha(tamanho_senha, quantidade_de_chutes): #função que roda o jogo inteiro
    contador = 0 #Quantidade de rodadas, define o número da rodada atual para o usuário
    bem_vindo() #roda a função bem vindo, que printa as primeiras frases do jogo
    senha_do_jogo = criar_senha(tamanho_senha) #Define que a variável senha do jogo é igual a função de criação de senha
    while contador < quantidade_de_chutes: #Mantém o jogo rodando até a quantidade de chutes definida pelo usuário
        print(f"\nVocê ainda tem {quantidade_de_chutes - contador} tentativas.") #avisa quantas tentativas o usuário ainda tem
        chutes = pegar_tentativas(tamanho_senha) #Define que a variável chute é igual a função que pega as tentativas
        verificacao = check_resposta(chutes, senha_do_jogo) #define a variável que vai fazer a comparação da resposta com o gabarito
        resultado(verificacao, chutes) #Imprime para o usuário o que ele escolheu e qual o resultado em comparação à senha do computador
        if verificacao == (["Branco"] * tamanho_senha): #Verifica se a senha está correta para encerrar o jogo
            print("Parabéns, você acertou!")
            break #para o jogo
        contador += 1 #adiciona mais um no contador de rodadas
    if contador == quantidade_de_chutes: #mensagem de falha caso o usuário não termine dentro do número de tentativas
        print("Você teve todas as chances e ainda assim falhou miseravelmente!")

comprimento_da_senha = 2 #Define quantas cores o usuário quer adivinhar
quantidade_de_tentativas = 2 #Define a quantidade de tentativas do usuário
jogo_da_senha(comprimento_da_senha, quantidade_de_tentativas)
    