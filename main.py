# Serve para dar um delay no programa
from time import sleep


def traduzir(frase):
  
  # A variável Frase está recebendo ela mesmo, só que todo lugar dentro dessa variável que tiver um ESPAÇO ele 'quebra'(coloca) em uma nova posição da lista/vetor.
  frase = frase.split(" ")

  # Cria um dicionário contendo as palavras e traduções.
  dicionario = {
    'senhor': 'matey',
    'hotel': 'fleabag inn',
    'estudante': 'swabbie',
    'garoto': 'matey',
    'madame': 'proud beauty',
    'professor': 'foul blaggart',
    'restaurante':'galley',
    'seu':'yer',
    'com licença': 'arr',
    'estudantes': 'swabbies',
    'são': 'be',
    'advogado': 'foul blaggart',
    'o': "th'",
    'banheiro':'head',
    'meu':'me',
    'oi':'avast',
    'é':'be',
    'homem':'matey'
  }
  linguaPirata = ""
  print('\n')
  print('    Traduzindo...    ')
  print('\n')
  # Para da um delay na hora de retornar o valores.
  sleep(2)
  for i in frase:
    # Faz um verficação. Se existir a palavra na da variável i dentro do dicionario, vai concatenar...
    if i in dicionario :
      linguaPirata = linguaPirata + " " + dicionario[i]
    # Se não, mostra um erro ao usuário e para a função.
    else:
      print('-----   Ocorreu um ERRO!   -----\n')
      print('A palavra: ' + i.upper() + ', não existe na Língua Pirata')
      consultarDicionario()
      break;
  
  return print(linguaPirata)


def consultarDicionario():
    dicionario = {
      'senhor': 'matey',
      'hotel': 'fleabag inn',
      'estudante': 'swabbie',
      'garoto': 'matey',
      'madame': 'proud beauty',
      'professor': 'foul blaggart',
      'restaurante':'galley',
      'seu':'yer',
      'com licença': 'arr',
      'estudantes': 'swabbies',
      'são': 'be',
      'advogado': 'foul blaggart',
      'o': "th'",
      'banheiro':'head',
      'meu':'me',
      'oi':'avast',
      'é':'be',
      'homem':'matey'
    }
    print("\n-----   Dicionário   -----\n")
    print("\nPortuguês | Pirata   \n")
    for i in dicionario.items():
      print(i)
      
      
      

    




frase = input("Digite uma Frase: ").lower()

traduzir(frase)

consultarDicionario()







