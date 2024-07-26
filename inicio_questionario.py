import random 
import os
import time
print()
os.system('cls')

#As chaves e o .format servem para formatar a string de forma a deixar colorido apenas as partes que quero, que é o dinossauro.
frame_dinossauro = [['                {}__{}'.format('\033[1;32m', '\033[m'),
                     '               {}/ _){}'.format('\033[1;32m', '\033[m'),
                     '      {}_.----._/ /{}'.format('\033[1;32m', '\033[m'),
                     '____ {}/         /{}__________________________________________'.format('\033[1;32m', '\033[m'),
                     '  {}__/ (  | (  \{}          .           .           .  '.format('\033[1;32m', '\033[m'), 
                     ' {}/__.-\'|_|-- \_\{}  . ^          .         .            .'.format('\033[1;32m', '\033[m'),
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
                     '________ {}/         /{}_____________________________________'.format('\033[1;32m', '\033[m'),
                     '    . {}__/ (  | (  \ {}     .           .           .  '.format('\033[1;32m', '\033[m'), 
                     ' .   {}/__.-\'|_|-- \_\{} ^         .         .            .'.format('\033[1;32m', '\033[m'),
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
                     '_____________ {}/         /{}________________________________'.format('\033[1;32m', '\033[m'),
                     '    .  ^   {}__/ (  | (  \{}   .           .           .  '.format('\033[1;32m', '\033[m'), 
                     ' .        {}/__.-\'|_|-- \_\{}      .         .            .'.format('\033[1;32m', '\033[m'),
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
                     '__________________ {}/         /{}___________________________'.format('\033[1;32m', '\033[m'),
                     '    .  ^     .  {}__/ (  | (  \{}          .           .  '.format('\033[1;32m', '\033[m'), 
                     ' .      .      {}/__.-\'|_|-- \_\{} .         .            .'.format('\033[1;32m', '\033[m'),
                     '.           .         .     ^      .         .          .',
                     '    .               .                     .    ^    .']
                      ]

print('{:^88}'.format('.::::::.  :::   :: ::: :::::::'))
print('{:^88}'.format(':::   ::  :::   ::          .\''))
print('{:^88}'.format(':::   ::  :::   :: :::   .:\'  '))
print('{:^88}'.format('::: ..::  :::   :: ::: :\'     '))
print('{:^88}'.format('\'::::::\': \'::::::\' ::: :::::::'))

print('::::::.  ::: :::.   :: .:::::. .:::::: .::::::  .::::.  :::   :: ::::::. .:::::. .::::::')
print(':::   ::     ::: .  :: :::  :: :::.    :::.    :::   :: :::   :: :::  :: :::  :: :::.   ')
print(':::   :: ::: :::  . :: :::  :: ::::::. ::::::. :::::::: :::   :: :::..:\' :::  :: ::::::.')
print(':::   :: ::: :::   .:: :::  ::  \'\'\':::  \'\'\'::: :::   :: :::   :: :::.    :::  ::  \'\'\':::')    
print(':::...:\' ::: :::    :: \':::::\' ::::::\' ::::::\' :::   :: \'::::::\' ::: \'.  \':::::\' ::::::\'')  
time.sleep(5)
os.system('cls')

questoes = [['Quais os dois possíveis eventos que ocasionaram a extinção dos dinossauros?', 'asteroide e o vulcanismo', 'contaminação atmosférica e asteroide', 'chuvas ácidas e o efeito estufa', 'a'], ['O que significa o nome do dinossauro Triceratops e do Micropaquicefalossauro, respectivamente?', 'Rei lagarto tirano e dinossauro dos braços curtos', 'Três garras e lagarto de cabeça pequena', 'Cabeça com três chifres e pequeno lagarto de cabeça grossa', 'c'], ['A extinção do Cretáceo-Paleógeno foi uma extinção em massa, ocorrida há mais ou menos 65,5 milhões de anos, que marca:', 'O fim do período Jurássico e o início do Cretáceo', 'O fim do período Cretáceo e o início do Paleógeno', 'O fim do período Jurássico e o início do Paleógeno', 'b'], ['Qual dinossauro era o rei do “pum”?', 'Tiranossauro Rex', 'Giganotosaurus', 'Saurópode', 'c'], ['Segundo estudos, quais aves são os parentes vivos mais próximos do Tiranossauro Rex?', 'Ema e Galinha', 'Galinha e Avestruz', 'Casuar e avestruz', 'b'], ['Sabemos que o T-rex é conhecido por seus braços curtos, mas existiu um dinossauro, em termos de proporção, que possuía braços ainda menores. Que dinossauro é esse?', 'Giganotossauro', 'Allosaurus', 'Carnotauro', 'c'], ['Segundo estudos, existiu um dinossauro que teria evoluído para conseguir cavar a terra em busca de água e comida. Que criatura é esta?', 'Anquilossauro', 'Stegosaurus', 'Triceratops', 'a'], ['Qual dinossauro os paleontólogos acreditavam que era uma das espécies mais inteligentes e ágeis entre todos os dinossauros?', 'Sauroposeidon', 'Troodonte', 'Pteranodontes', 'b'], ['Qual a era da escala do tempo geológico é conhecida como “era dos dinossauros”?', 'Paleozoico', 'Fanerozóico', 'Mesozóico', 'c'], ['Qual era o dinossauro que pesava cerca de duas toneladas, mas que seu cérebro apresentava apenas 80 gramas?', 'Giganotosaurus', 'Estegossauro', 'Alossauro', 'b'], ['Qual foi o primeiro dinossauro a mostrar evidências que alimentava seus filhotes enquanto ainda estavam no ninho?', 'Maiassauro', 'Majungassauro', 'Mussauro', 'a'], ['Qual o sítio paleontológico com a maior incidência de pegadas de dinossauro do MUNDO?', 'Floresta Fóssil de Gilboa (Estados Unidos- Nova York)', 'Vale dos Dinossauros (Brasil- Paraíba)', 'Formação La Colônia (Argentina- Província de Chubut)', 'b']]

curiosidades = ['Os dinossauros costumam ser nomeados de acordo com a sua aparência, comportamento ou outras características relevantes como sua localidade, mas muitas vezes eles recebem nomes que homenageiam o cientista que o descobriu', 'Acredita-se que o Saurópode, um tipo de dinossauro com corpo enorme e pescoço muito comprido, tinha um estômago tão grande e elaborado que funcionava como uma espécie de câmara de fermentação. Ou seja, por um lado as bactérias auxiliavam a processar toda sua enorme dieta fibrosa, mas por outro, resultava em uma grande proporção de pesadas flatulências, ou seja, o Saurópode era o rei dos grandes, sonoros e provavelmente nada cheirosos, puns!', 'Você sabe por que o Tiranossauro Rex  e outros carnívoros tinham braços curtos? De acordo com estudos, as patas dianteiras dos grandes tiranossauros teriam sido reduzidas porque representavam um perigo para a sobrevivência de indivíduos suficientemente grandes já que durante a alimentação em grupo com outros predadores, as patas dianteiras ficavam vulneráveis a lesões que poderiam levar à morte. Além disso, seu grande crânio e suas mandíbulas forneceram todos os mecanismos predatórios necessários', 'Os dinossauros, como aparecem nos filmes, não conseguiam colocar a língua para fora, como fazem os lagartos. Na maioria dos dinossauros os ossos da língua são muito pequenos e simples, conectados a uma língua sem muita mobilidade, assim como ocorre nos aligátores e crocodilos, sendo que, em alguns deles, a língua ficava presa à base da boca como o T-rex, por exemplo', 'Você sabia que existiu um dinossauro que engatinhava quando era jovem e passou a andar sobre as patas traseiras na idade adulta? O dinossauro Mussaurus à medida que ia crescendo ficava pesado o suficiente para permitir ao animal equilibrar-se sobre duas patas', 'O Tiranossauro Rex possuía cerca de 60 grandes e afiados dentes. Como eram carnívoros, usavam os dentes para cortar e rasgar a carne dos animais abatidos. Após caírem, os dentes dos tiranossauros nasciam novamente']
pontos = 0
qa = 0
qc = 0
quest = 0 #variavel para imprimir a questão em ordem
jaforam_perguntas = []
jaforam_curiosidades = []
nome = input('Olá, vamos começar!\nQual seu nome?\n>> ')

while len(jaforam_perguntas) < len(questoes):
    qc = random.randint(0, len(curiosidades)-1)
    qa = random.randint(0, len(questoes)-1)

    if qa not in jaforam_perguntas:
        quest +=1
        print(f'Questão {quest}:')
        resposta = input(f'{questoes[qa][0]}\na){questoes[qa][1]}\nb){questoes[qa][2]}\nc){questoes[qa][3]}\nResposta: ')
        jaforam_perguntas.append(qa)
        acertos = 0

        for p in range(1, 5):
            if resposta.upper() == questoes[qa][p].upper():
                pontos +=1
                print(f'\nParabéns, {nome.title()} você acertou!\nVocê ganhou 1 ponto\nVocê tem {pontos} pontos\n...')
                time.sleep(3)
                os.system('cls')
                acertos+=1

        if acertos == 0:
            print(resposta, questoes[qa][p])
            print(f'\nErrou, {nome.title()}:(\n...')
            time.sleep(3)
            os.system('cls')   

        if (quest)%2 == 0:
            if qc not in jaforam_curiosidades:
                jaforam_curiosidades.append(qc)
                #for para acessar a "imagem":
                for indice_d in range(len(frame_dinossauro)):
                    #for para imprimir cada linha da "imagem":
                    for indice_fd in range(len(frame_dinossauro[indice_d])):
                        print(frame_dinossauro[indice_d][indice_fd])
                    print(f'\033[3;49;93mVocê sabia?:\n\033[m {curiosidades[qc]}\n')
                    time.sleep(1.8)
                    os.system('cls')
        
        else:
            for indice_d in range(len(frame_dinossauro)):
                for indice_fd in range(len(frame_dinossauro[indice_d])):
                    print(frame_dinossauro[indice_d][indice_fd])
                time.sleep(0.5)
                os.system('cls')
                                    
print(f'\nFIM DE JOGO\nVocê foi bem, conseguiu {pontos} pontos' if pontos >= 3 else '\nVocê não foi bem. Boa sorte na próxima')
