import random 
print()
questoes = [['Quais os dois possíveis eventos que ocasionaram a extinção dos dinossauros?', 'asteroide e o vulcanismo', 'contaminação atmosférica e asteroide', 'chuvas ácidas e o efeito estufa', 'a'], ['O que significa o nome do dinossauro Triceratops e do Micropaquicefalossauro, respectivamente?', 'Rei lagarto tirano e dinossauro dos braços curtos', 'Três garras e lagarto de cabeça pequena', 'Cabeça com três chifres e pequeno lagarto de cabeça grossa', 'c'], ['A extinção do Cretáceo-Paleógeno foi uma extinção em massa, ocorrida há mais ou menos 65,5 milhões de anos, que marca:', 'O fim do período Jurássico e o início do Cretáceo', 'O fim do período Cretáceo e o início do Paleógeno', 'O fim do período Jurássico e o início do Paleógeno', 'b'], ['Qual dinossauro era o rei do “pum”?', 'Tiranossauro Rex', 'Giganotosaurus', 'Saurópode', 'c'], ['Segundo estudos, quais aves são os parentes vivos mais próximos do Tiranossauro Rex?', 'Ema e Galinha', 'Galinha e Avestruz', 'Casuar e avestruz', 'b'], ['Sabemos que o T-rex é conhecido por seus braços curtos, mas existiu um dinossauro, em termos de proporção, que possuía braços ainda menores. Que dinossauro é esse?', 'Giganotossauro', 'Allosaurus', 'Carnotauro', 'c'], ['Segundo estudos, existiu um dinossauro que teria evoluído para conseguir cavar a terra em busca de água e comida. Que criatura é esta?', 'Anquilossauro', 'Stegosaurus', 'Triceratops', 'a'], ['Qual dinossauro os paleontólogos acreditavam que era uma das espécies mais inteligentes e ágeis entre todos os dinossauros?', 'Sauroposeidon', 'Troodonte', 'Pteranodontes', 'b'], ['Qual a era da escala do tempo geológico é conhecida como “era dos dinossauros”?', 'Paleozoico', 'Fanerozóico', 'Mesozóico', 'c'], ['Qual era o dinossauro que pesava cerca de duas toneladas, mas que seu cérebro apresentava apenas 80 gramas?', 'Giganotosaurus', 'Estegossauro', 'Alossauro', 'b']]
curiosidades = []
pontos = 0
qa = 0
nome = input('Olá, vamos começar!\nQual seu nome? ')
for i in range(len(questoes)):
    print(f'Questão {i+1}:')
    qa = random.randint(0, len(questoes)-1)
    resposta = input(f'{questoes[qa][0]}\na){questoes[qa][1]}\nb){questoes[qa][2]}\nc){questoes[qa][3]}\nResposta: ')
    if resposta.upper() == questoes[qa][4].upper():
        print(f'\nParabéns, {nome.title()} você acertou!\nVocê ganhou 1 ponto\n')
        pontos +=1
    else:
        print(f'\nErrou, {nome.title()}:(\n')
print(f'\nFIM DE JOGO\nVocê foi bem, conseguiu {pontos} pontos' if pontos >= 3 else '\nVocê não foi bem. Boa sorte na próxima')
