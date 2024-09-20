import random 
lista =[random.randint(0,20) for _ in range (10000000)]
nova_lista = sorted(lista)
def Soma_de_dados(nova_lista):
    inicio=0
    fim=len(nova_lista) -1
    while inicio<=fim:
        soma=nova_lista[inicio] + nova_lista[fim]
        if soma == 10:
            print(f'Soma de 10 encontrada: {nova_lista[inicio]} + {nova_lista[fim]} = {soma} , Cordenadas: {inicio} e {fim}')
            return
        inicio += 1
        fim -= 1
    print('Nenhum resultado foi encontrado!')
Soma_de_dados(nova_lista)


