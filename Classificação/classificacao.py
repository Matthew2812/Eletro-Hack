import csv, pygame

pygame.init()
pygame.font.init()

def organizaDadosOutro(dados):
    texto = ''
    try:
        for i in range(11):
            texto += (dados[i][0] + '\t' + dados[i][1] + '\n')
    except(IndexError):
        texto +=('-------------------------\n')
    return texto

def CSVReader():         
    lista = []
    with open('file.csv', newline = '') as csvfile:
        leitor = csv.reader(csvfile, delimiter = '\t')
        lista = list(leitor)
        lista_ordenada = sorted(lista, key = lambda dado: int(dado[1]), reverse = True)
        csvfile.close()
        return lista_ordenada


def CSVWriter(nome,pontos):
    with open('file.csv','a',newline = '') as csvfile:
        escritor = csv.writer(csvfile, delimiter='\t')
        escritor.writerow([nome, pontos])
        csvfile.close()

def organizaDados(dados):
    lista_nome = []
    lista_pontos = []
    try:
        for i in range(11):
            lista_nome.append(dados[i][0])
            lista_pontos.append(dados[i][1])
    except(IndexError):
        print('-------------------------\n')
    return lista_nome


fonte = 'HACKED.ttf'
fonteTitulo = pygame.font.Font(fonte, 60)
fonteLinhas = pygame.font.Font(fonte, 35)

branco = (255,255,255)

#Largura e Altura da tela
width = 960
height = 600

screen = pygame.display.set_mode((width, height))

ranking = fonteTitulo.render("Ranking", True, branco)

def telaInicial():
    screen.blit(ranking,(360,5))
    dados = CSVReader()
    texto = ''
    posi = 100
    i = 0
    while i < len(dados) or i <= 10:
        try:
            texto = (dados[i][0])
            numero = (dados[i][1])
            text = fonteLinhas.render(texto, True, branco)
            pontos = fonteLinhas.render(numero, True, branco)
            screen.blit(text,(150,posi))
            screen.blit(pontos,(700,posi))
            posi += 35
        except(IndexError):
            texto +=('-------------------------\n')
        i += 1

telaInicial()
pygame.display.flip()


#nome = input('Digite seu nome: ')
#pontos = input('Digite a pontuação: ')
#CSVWriter(nome,pontos)
#organizaDados(CSVReader())
