from random import choice
import unicodedata

#bloco que inicializa as variaveis
palavras=['Banana','Bacon','Cartão','Jogo','Pão','Bolo','Leão','Formiga','Kiwi']
palavra=choice(palavras)
resposta=''
letras_chutadas=[]
vidas=5

print("#"*len(palavra))

#jogo
while resposta != palavra:

    
    #bloco de interação com o jogador       
    print(f'Você tem {vidas} vidas')    
    chute=input('Digite o seu palpite:')
    
    #verifica se o chute foi valido
    if len(chute) == 1 and chute!=' ':
        
        #limpa acentuação
        letra_limpa=chute
        letra_limpa = unicodedata.normalize("NFD", letra_limpa)        
        letra_limpa = letra_limpa.encode("ascii", "ignore")
        letra_limpa = letra_limpa.decode("utf-8")
        
        if letra_limpa.lower() in letras_chutadas:
            print(f"Você já tinha escolhido '{letra_limpa.lower()}'")
        else:

            #limpa acentuação da palavra
            palavra_limpa=palavra
            palavra_limpa = unicodedata.normalize("NFD", palavra_limpa)        
            palavra_limpa = palavra_limpa.encode("ascii", "ignore")
            palavra_limpa = palavra_limpa.decode("utf-8")
           
            if letra_limpa.lower() in palavra_limpa.lower():                    
                print(f"Parabéns! '{letra_limpa.lower()}' está na palavra")           
            else:
                print(f"Que pena! '{letra_limpa.lower()}' não está na palavra")
                vidas-=1
            letras_chutadas.append(letra_limpa.lower())
            if vidas == 0:
                print(f"Que pena, você perdeu, a palavra era '{palavra}'")
                break
            
    #bloco chute invalido   
    else:
        print(f"'{chute.lower()}' não é uma opcao valida")
        

         
    #bloco que atualiza a palavra encontrada e printa na tela
    resposta=''
    for letra in palavra:
            
        #limpa acentuação
        letra_limpa=letra 
        letra_limpa = unicodedata.normalize("NFD", letra_limpa)        
        letra_limpa = letra_limpa.encode("ascii", "ignore")
        letra_limpa = letra_limpa.decode("utf-8")
            
        if letra_limpa.lower() in letras_chutadas:
            print(f'{letra}',end='')
            resposta+=f'{letra}'
        else:
            print('#',end='')
            resposta+='#'
    print()

#mensagem de vitória    
else:
    print('Parabéns! Você encontrou a palavra')
        
