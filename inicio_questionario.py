import random 
import os
import time

def limpar():
    os.system('cls' if os.name=='nt' else 'clear')

#As chaves e o .format servem para formatar a string de forma a deixar colorido apenas as partes que quero, que é o dinossauro.
def imprimir_dinossauro(num_questao, qc):
    global jaforam_curiosidades, curiosidades
    frame_dinossauro = [['                {}__{}'.format('\033[1;32m', '\033[m'),
                     '               {}/ _){}'.format('\033[1;32m', '\033[m'),
                     '      {}_.----._/ /{}'.format('\033[1;32m', '\033[m'),
                     '____ {}/         /{}__________________________________________'.format('\033[1;32m', '\033[m'),
                     '  {}__/ (  | (  \\{}          .           .           .  '.format('\033[1;32m', '\033[m'), 
                     ' {}/__.-\'|_|-- \\_\\{}  . ^          .         .            .'.format('\033[1;32m', '\033[m'),
                     '.           .         .     ^      .         .          .',
                     '    .               .                     .    ^    .'],
                     
                    ['                  {}__{}'.format('\033[1;32m', '\033[m'),
                     '                 {}/ _){}'.format('\033[1;32m', '\033[m'),
                     '        {}_.----._/ /{}'.format('\033[1;32m', '\033[m'),
                     '______ {}/         /{}________________________________________'.format('\033[1;32m', '\033[m'),
                     '    {}__/ |  ) (  |{}        .           .           .  '.format('\033[1;32m', '\033[m'),
                     ' . {}/__.-/_/---|_|{}  . ^          .         .            .'.format('\033[1;32m', '\033[m'),
                     '.           .         .     ^      .         .          .',
                     '    .               .                     .    ^    .'],

                    ['                    {}__{}'.format('\033[1;32m', '\033[m'), 
                     '                   {}/ _){}'.format('\033[1;32m', '\033[m'),
                     '          {}_.----._/ /{}'.format('\033[1;32m', '\033[m'),
                     '________ {}/         /{}______________________________________'.format('\033[1;32m', '\033[m'),
                     '    . {}__/ (  | (  \\{}     .           .           .  '.format('\033[1;32m', '\033[m'), 
                     ' .   {}/__.-\'|_|-- \\_\\{} ^         .         .            .'.format('\033[1;32m', '\033[m'),
                     '.           .         .     ^      .         .          .',
                     '    .               .                     .    ^    .'], 

                    ['                      {}__{}'.format('\033[1;32m', '\033[m'),
                     '                     {}/ _){}'.format('\033[1;32m', '\033[m'),
                     '            {}_.----._/ /{}'.format('\033[1;32m', '\033[m'),
                     '__________ {}/         /{}____________________________________'.format('\033[1;32m', '\033[m'),
                     '    .  ^{}__/ |  ) (  |{}       .           .           .  '.format('\033[1;32m', '\033[m'),
                     ' .     {}/__.-/_/---|_|{} ^          .         .            .'.format('\033[1;32m', '\033[m'),
                     '.           .         .     ^      .         .          .','    .               .                     .    ^    .'],

                    ['                        {} __{}'.format('\033[1;32m', '\033[m'), 
                     '                        {}/ _){}'.format('\033[1;32m', '\033[m'),
                     '               {}_.----._/ /{}'.format('\033[1;32m', '\033[m'),
                     '_____________ {}/         /{}_________________________________'.format('\033[1;32m', '\033[m'),
                     '    .  ^   {}__/ (  | (  \\{}   .           .           .  '.format('\033[1;32m', '\033[m'), 
                     ' .        {}/__.-\'|_|-- \\_\\{}      .         .            .'.format('\033[1;32m', '\033[m'),
                     '.           .         .     ^      .         .          .',
                     '    .               .                     .    ^    .'],

                    ['                           {}__{}'.format('\033[1;32m', '\033[m'),
                     '                          {}/ _){}'.format('\033[1;32m', '\033[m'),
                     '                 {}_.----._/ /{}'.format('\033[1;32m', '\033[m'),
                     '_______________{} /         /{}_______________________________'.format('\033[1;32m', '\033[m'),
                     '    .  ^     {}__/ |  ) (  |{}  .           .           .  '.format('\033[1;32m', '\033[m'),
                     ' .      .   {}/__.-/_/---|_|{}      .         .            .'.format('\033[1;32m', '\033[m'),
                     '.           .         .     ^      .         .          .','    .               .                     .    ^    .'],
                    
                    ['                              {}__{}'.format('\033[1;32m', '\033[m'), 
                     '                             {}/ _){}'.format('\033[1;32m', '\033[m'),
                     '                   {} _.----._/ /{}'.format('\033[1;32m', '\033[m'),
                     '__________________ {}/         /{}____________________________'.format('\033[1;32m', '\033[m'),
                     '    .  ^     .  {}__/ (  | (  \\{}          .           .  '.format('\033[1;32m', '\033[m'), 
                     ' .      .      {}/__.-\'|_|-- \\_\\{} .         .            .'.format('\033[1;32m', '\033[m'),
                     '.           .         .     ^      .         .          .',
                     '    .               .                     .    ^    .']
                      ]
    
    #for para acessar a "imagem":
    for indice_d in range(len(frame_dinossauro)):
        #for para imprimir cada linha da imagem:
        for indice_fd in range(len(frame_dinossauro[indice_d])):
            print(frame_dinossauro[indice_d][indice_fd])

        #Imprimindo a curiosidade:
        if num_questao%2==0:
            jaforam_curiosidades.append(qc)
            print(f'\033[3;49;93mVocê sabia?:\n\033[m {curiosidades[qc]}\n')
            time.sleep(1.8)
        else:
            time.sleep(0.5)
        limpar()


#função criada para a verificação e manuseio do tempo do jogador ao responder a pergunta
def pontuar(resposta, tempo_resposta, pontos, questoes, num_quest_list, quest_certas): #acertou é uma variável booleana
    global nome
    acertou = False

    #Verificando se a resposta está correta:
    alt = ['a', 'b', 'c']
    for i in range(3): 
        if alt[i] == questoes[num_quest_list][4]: 
            if resposta.upper() == questoes[num_quest_list][i+1].upper() or resposta.lower() == alt[i]:
                print(f'\033[3;49;92m\nParabéns, {nome.title()}, você acertou!')
                acertou = True
                quest_certas +=1

                #verificará se o tempo da resposta foi menor que n segundos e pontuará de acordo.
                if tempo_resposta < 5:
                    win_pontos = 5
                elif tempo_resposta <= 10:
                    win_pontos = 3
                else:
                    win_pontos = 1
                pontos += win_pontos
                print('Você respondeu em {:.1f} segundos. Por isso ganhou {} ponto(s)'.format(tempo_resposta,win_pontos))

    if not acertou:
        #serão subtraídos 2 pontos pelo erro.
        print(f'\033[3;49;91m\nErrou, {nome.title()}:(.\nVocê perdeu 2 pontos!\nBoa sorte na próxima.')
        pontos -= 2
    print(f'>>> Você tem {pontos} pontos\n...\033[m')
    time.sleep(3)
    limpar()  

    return pontos, quest_certas #retornando o total de pontos do usuário e o total de questões que ele acertou


#função criada para mostrar as questões
def exibir_quest(questoes, qa):
    let = ['', 'a)', 'b)', 'c)']
    for n in range(4):
        print(f'{let[n]}{questoes[qa][n]}')


#função criada para a verificação da alternativa caso o jogador digite um nome que não seja igual as alternativas possíveis
def check_quest(alternativas, quest, resposta, qa, tempo_resposta):
    #Se o tempo de resposta for menor que um segundo, a pergunta será impressa novamente.
    if tempo_resposta < 1:    
        limpar()
        print('\033[7;49;91m\nVocê digitou em um tempo muito curto!\033[m')
        print(f'\033[1;7;49;92mQuestão {quest}:\033[m')
        return True
    
    alternativas.extend(['a', 'b', 'c', questoes[qa][1].lower(), questoes[qa][2].lower(), questoes[qa][3].lower()])
    #Se a resposta não for uma das possíveis, a pergunta será impressa novamente.
    if resposta.lower() not in alternativas:
        limpar()
        print('\033[7;49;91m\nDigite uma resposta válida!\033[m')
        print(f'\033[1;7;49;92mQuestão {quest}:\033[m')
        return True
    else:
        return False
    

# Matriz de questões:
questoes = [['Quais os dois possíveis eventos que ocasionaram a extinção dos dinossauros?', 'asteroide e o vulcanismo', 'contaminação atmosférica e asteroide', 'chuvas ácidas e o efeito estufa', 'a'], 
            ['O que significa o nome do dinossauro Triceratops e do Micropaquicefalossauro, respectivamente?', 'Rei lagarto tirano e dinossauro dos braços curtos', 'Três garras e lagarto de cabeça pequena', 'Cabeça com três chifres e pequeno lagarto de cabeça grossa', 'c'], 
            ['A extinção do Cretáceo-Paleógeno foi uma extinção em massa, ocorrida há mais ou menos 65,5 milhões de anos, que marca:', 'O fim do período Jurássico e o início do Cretáceo', 'O fim do período Cretáceo e o início do Paleógeno', 'O fim do período Jurássico e o início do Paleógeno', 'b'], 
            ['Qual dinossauro era o rei do “pum”?', 'Tiranossauro Rex', 'Giganotosaurus', 'Saurópode', 'c'], 
            ['Segundo estudos, quais aves são os parentes vivos mais próximos do Tiranossauro Rex?', 'Ema e Galinha', 'Galinha e Avestruz', 'Casuar e avestruz', 'b'], 
            ['Sabemos que o T-rex é conhecido por seus braços curtos, mas existiu um dinossauro, em termos de proporção, que possuía braços ainda menores. Que dinossauro é esse?', 'Giganotossauro', 'Allosaurus', 'Carnotauro', 'c'], 
            ['Segundo estudos, existiu um dinossauro que teria evoluído para conseguir cavar a terra em busca de água e comida. Que criatura é esta?', 'Anquilossauro', 'Stegosaurus', 'Triceratops', 'a'], 
            ['Qual dinossauro os paleontólogos acreditavam que era uma das espécies mais inteligentes e ágeis entre todos os dinossauros?', 'Sauroposeidon', 'Troodonte', 'Pteranodontes', 'b'], 
            ['Qual a era da escala do tempo geológico é conhecida como “era dos dinossauros”?', 'Paleozoico', 'Fanerozóico', 'Mesozóico', 'c'], 
            ['Qual era o dinossauro que pesava cerca de duas toneladas, mas que seu cérebro apresentava apenas 80 gramas?', 'Giganotosaurus', 'Estegossauro', 'Alossauro', 'b'], 
            ['Qual foi o primeiro dinossauro a mostrar evidências que alimentava seus filhotes enquanto ainda estavam no ninho?', 'Maiassauro', 'Majungassauro', 'Mussauro', 'a'], 
            ['Qual o sítio paleontológico com a maior incidência de pegadas de dinossauro do MUNDO?', 'Floresta Fóssil de Gilboa (Estados Unidos- Nova York)', 'Vale dos Dinossauros (Brasil- Paraíba)', 'Formação La Colônia (Argentina- Província de Chubut)', 'b']]

#Vetor de curiosidades:
curiosidades = ['Os dinossauros costumam ser nomeados de acordo com a sua aparência, comportamento ou outras características relevantes como sua localidade, mas muitas vezes eles recebem nomes que homenageiam o cientista que o descobriu.', 
                'Acredita-se que o Saurópode, um tipo de dinossauro com corpo enorme e pescoço muito comprido, tinha um estômago tão grande e elaborado que funcionava como uma espécie de câmara de fermentação. Ou seja, por um lado as bactérias auxiliavam a processar toda sua enorme dieta fibrosa, mas por outro, resultava em uma grande proporção de pesadas flatulências, ou seja, o Saurópode era o rei dos grandes, sonoros e provavelmente nada cheirosos, puns!', 
                'Você sabe por que o Tiranossauro Rex  e outros carnívoros tinham braços curtos? De acordo com estudos, as patas dianteiras dos grandes tiranossauros teriam sido reduzidas porque representavam um perigo para a sobrevivência de indivíduos suficientemente grandes já que durante a alimentação em grupo com outros predadores, as patas dianteiras ficavam vulneráveis a lesões que poderiam levar à morte. Além disso, seu grande crânio e suas mandíbulas forneceram todos os mecanismos predatórios necessários.', 
                'Os dinossauros, como aparecem nos filmes, não conseguiam colocar a língua para fora, como fazem os lagartos. Na maioria dos dinossauros os ossos da língua são muito pequenos e simples, conectados a uma língua sem muita mobilidade, assim como ocorre nos aligátores e crocodilos, sendo que, em alguns deles, a língua ficava presa à base da boca como o T-rex, por exemplo.',
                'Você sabia que existiu um dinossauro que engatinhava quando era jovem e passou a andar sobre as patas traseiras na idade adulta? O dinossauro Mussaurus à medida que ia crescendo ficava pesado o suficiente para permitir ao animal equilibrar-se sobre duas patas.',
                'O Tiranossauro Rex possuía cerca de 60 grandes e afiados dentes. Como eram carnívoros, usavam os dentes para cortar e rasgar a carne dos animais abatidos. Após caírem, os dentes dos tiranossauros nasciam novamente.']


#90 é o código para a cor cinza, então a é a variável para a cor cinza no código de escape ANSI
a = 90
cores= [92,93,91] # 91= vermelho, 92= verde, 93= amarelo.
b = random.choice(cores) #Sorteando um código de cor aleatório do vetor cores

# for para imprimir interface degradê
for num in range(11):
    ''' O format com {:^88} serve para deixar a string que será impressa no meio de 88 caracteres que o tamanho em largura de "DINOSSAUROS"

    a parte do " a in num<n else b " funciona como um controlador de cor, à medida que "num" (a variável controladora) aumenta, vai haver uma mudança de cor em uma linha.
    '''
    print('\033[1;{}m{:^88}\033[m'.format(a if num<0 else b, '.::::::.  :::   :: ::: :::::::   ::::::.  :::::::'))
    print('\033[1;{}m{:^88}\033[m'.format(a if num<1 else b, ':::   ::  :::   ::          .\'   :::   :: :::    '))
    print('\033[1;{}m{:^88}\033[m'.format(a if num<2 else b, ':::   ::  :::   :: :::   .:\'     :::   :: :::::: '))
    print('\033[1;{}m{:^88}\033[m'.format(a if num<3 else b, '::: ..::  :::   :: ::: :\'        :::   :: :::    '))
    print('\033[1;{}m{:^88}\033[m'.format(a if num<4 else b, '\'::::::\': \'::::::\' ::: :::::::   :::...:\' :::::::'))

    print('\033[1;{}m::::::.  ::: :::.   :: .:::::. .:::::: .::::::  .::::.  :::   :: ::::::. .:::::. .::::::\033[m'.format(a if num<5 else b))
    print('\033[1;{}m:::   ::     ::: .  :: :::  :: :::.    :::.    :::   :: :::   :: :::  :: :::  :: :::.   \033[m'.format(a if num<6 else b))
    print('\033[1;{}m:::   :: ::: :::  . :: :::  :: ::::::. ::::::. :::::::: :::   :: :::..:\' :::  :: ::::::.\033[m'.format(a if num<7 else b))
    print('\033[1;{}m:::   :: ::: :::   .:: :::  ::  \'\'\':::  \'\'\'::: :::   :: :::   :: :::.    :::  ::  \'\'\':::\033[m'.format(a if num<8 else b))    
    print('\033[1;{}m:::...:\' ::: :::    :: \':::::\' ::::::\' ::::::\' :::   :: \'::::::\' ::: \'.  \':::::\' ::::::\'\033[m'.format(a if num<9 else b)) 


    print('                                   _')
    print('                                  /  \\_') 
    print('\033[94m                  /\\ \033[97m           ( _____ )           \033[96m ________\033[m')
    print('\033[94m                 /  \\                              \033[96m \\       _\\______\033[m')
    print('\033[94m     /\\         /    \\   /\\                         \033[96m \\ //  /       /\033[m')
    print('\033[94m    /  \\       /      \\ /  \\                       \033[96m /  /  /       /\033[m')
    print('\033[94m   /    \\     /        \\    \\         ~~          \033[96m / \' /\\ /     .;\033[m')
    print('\033[94m  /      \\   /          \\    .~~   ~    ~        \033[96m <//\\ \\^/     /¬\033[m')
    print('\033[94m /        \\./            \\  ~    ~       ~        \033[96m    \\____,(___>¬\033[m')
    print('\033[94m/                         \\~               ~')
    print('\033[94m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    #o time.sleep serve para que dê tempo observar a interface antes que seja apagada
    time.sleep(0.3)
    limpar() # Além de servir para dar fim à "interface", faz com que ela não apareça um em baixo do outro, fazendo com que fique um efeito bacana.

loop = True
#quest_certas é uma variável que contará a quantidade de acertos do jogador para, no final, podermos verificar se o jogador acertou todas.
quest_certas = 0

#função recursiva criada para substituir o while e garantir a repetição do jogo de acordo com a resposta do jogador que servirá de condição básica para estabelecer o fim ou a continuação do jogo.
def jogar(loop):
    global jaforam_curiosidades, quest_certas, nome
    if loop == False:
        return 'Obrigada por jogar'
    else:
        pontos = 0
        qa = 0 # Variável para escolher a questão 
        qc = 0 # Variável para escolher a curiosidade
        quest = 0 #variavel para imprimir a questão em ordem

        jaforam_perguntas = [] # Lista para por as *questões* que já foram
        jaforam_curiosidades = [] # Lista para por as *curiosidades* que já foram

        print('\033[5;49;92m{}\033[m'.format(18*'-'))
        nome = input('Olá, vamos começar!\nQual seu nome?\n>> ')
        limpar()

        while len(jaforam_perguntas) < len(questoes):
            qc = random.randint(0, len(curiosidades)-1)
            qa = random.randint(0, len(questoes)-1)
            
            #O if permite que nem as perguntas, nem as curiosidades sejam repetidas.
            if qa not in jaforam_perguntas and qc not in jaforam_curiosidades:
                alternativas = []
                quest +=1
                print(f'\033[1;7;49;92mQuestão {quest}:\033[m')

                #Obtendo a resposta do usuário de forma que não entre uma resposta inválida:
                while True:
                    exibir_quest(questoes, qa)
                    inicio_resposta = time.time()
                    resposta = input('> ')
                    fim_resposta = time.time()
                    tempo_resposta = fim_resposta - inicio_resposta
                    '''
                    tempo_resposta é a subtração do fim_resposta (o momento em que o usuário clicou enter) com o inicio_resposta 
                    (o momento em que o sistema começa a esperar a resposta do usuário), resultando no tempo que o usuário demorou a responder
                    '''
                    if check_quest(alternativas, quest, resposta, qa, tempo_resposta) == False:
                        break
                    #O "while" continuará repetindo até check_quest() retornar False, o que significa que a resposta digitada é uma das possíveis.

                acertos = 0
                jaforam_perguntas.append(qa)

                pontos, quest_certas = pontuar(resposta, tempo_resposta, pontos, questoes, qa, quest_certas)    

                #imprimindo o "carregamento de dinossauro"
                imprimir_dinossauro(quest, qc)


    #imprimindo "FIM DE JOGO"
        print('\033[1;93m:::::::: ::: :::.    .::   ::::::.  :::::::      ::: .:::::. .::::::: .:::::.\033[m')
        print('\033[1;93m:::          ::: .  . ::   :::   :: :::          ::: :::  :: :::      :::  ::\033[m')
        print('\033[1;93m:::::::  ::: :::  ::  ::   :::   :: ::::::       ::: :::  :: :::  ::: :::  ::\033[m')
        print('\033[1;93m:::      ::: :::      ::   :::   :: :::      ::. ::: :::  :: :::   :: :::  ::\033[m')
        print('\033[1;93m:::      ::: :::      ::   :::...:\' :::::::  \':::::\' \':::::\' \'::::::\' \':::::\'\033[m')

        if quest_certas == len(questoes):
            print('\n\nUau! Você é um verdadeiro paleontólogo! \nConseguiu {0} pontos e acertou {1} de {2} questões. ( •̀ ω •́ )✧'.format(pontos, quest_certas, len(questoes)))
        elif quest_certas >= 6:
            print(f'\n\nVocê foi bem, conseguiu {pontos} pontos e acertou {quest_certas} de {len(questoes)}.\nParabéns pelo esforço. :)')
        else:
            print(f'\n\nVocê não foi bem: conseguiu {pontos} pontos e acertou {quest_certas} de {len(questoes)}. \nBoa sorte na próxima. :(')
        print('\033[5;49;92m{}\033[m'.format(29*'-'))
        continuar = input('\nVocê deseja jogar novamente?\n>> ')
        # perguntando se o usuário deseja continuar a jogar, dependendo da resposta a variavel loop assumirá um valor para que o while se encerre
        if continuar.upper() != 'S' and continuar.upper() != 'SIM':
            loop = False
        else:
            limpar()
        return jogar(loop)
    
print(jogar(loop))