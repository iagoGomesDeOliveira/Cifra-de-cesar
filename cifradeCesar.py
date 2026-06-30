import string
alf = string.ascii_lowercase

def main():
      process(perguntar())

def process(num : int):
    while num != 0 and num !=1 and num !=2:
          print("1 ou 2 ou 0")
          process(perguntar())
    else:
        if num != 0:
            texto = str(input('\n\ndigite um texto: ')).lower()
            chave = int(input('digite uma chave: '))

        if num == 1:
            print(f'\n\n{encriptar(texto, chave)}')
            pass

        elif num == 2:
            print(f'\n\n{descriptar(texto, chave)}')
            pass
        
        print("encerrando")


# funcionalidades

def perguntar():
    return int(input("\n\n[1] encriptar | [2] descriptar | [0] para sair: "))

def encriptar(texto, chave):
    enc = ""
    for ord in texto:
        enc+=alf[(alf.index(ord)+chave)%(len(alf))]
    return enc

def descriptar(texto, chave):
    enc = ""
    for ord in texto:
        enc+=alf[(alf.index(ord)-chave)%(len(alf))]
    return enc

main()