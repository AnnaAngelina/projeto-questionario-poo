print()
questoes = [['Qual ano foi proclamado a independência do brasil?\n', '1834', '1900', '1822', 'c'], ['Normalmente, quantos litros de sangue uma pessoa tem?\n', '4 a 6 litros', '2 a 4 litros', '7 litros', 'a'], ['Qual o livro mais vendido no mundo a seguir à Bíblia?', 'O senhor dos Aneis', 'Dom Quixote', 'O pequeno príncipe', 'b'], ['Quantas casas decimais tem o número pi?', 'Duas', 'Centenas', 'Infinitas', 'c']]
pontos = 0
nome = input('Olá, vamos começar!\nQual seu nome? ')
for i in range(len(questoes)):
    print(f'Questão {i+1}:')
    resposta = input(f'{questoes[i][0]}a){questoes[i][1]}\nb){questoes[i][2]}\nc){questoes[i][3]}\nResposta: ')
    if resposta.upper() == questoes[i][4].upper():
        print(f'\nParabéns, {nome.title()} você acertou!\nVocê ganhou 1 ponto\n')
        pontos +=1
    else:
        print(f'Errou, {nome.title()}:(\n')
print(f'\nFIM DE JOGO\nVocê foi bem, conseguiu {pontos} pontos' if pontos >= 3 else '\nVocê não foi bem. Boa sorte na próxima')
