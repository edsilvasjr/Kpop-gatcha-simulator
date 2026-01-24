import random

start = int(input('Olá, seja bem vindo ao KPOP GATCHA. Para jogar digite 1, caso não queira Annyeong! Digite 2 para sair '))
comum = ['Poster', 'Sticker', 'Fanart', 'Mini Poster']
packs = {
'girls generation': ['Taeyeon', 'Jessica', 'Sunny', 'Tiffany', 'Yuri', 'Yoona', 'Sooyoung', 'Hyoyeon', 'Seohyun'],
'blackpink': ['Jennie', 'Rosé', 'Jisoo', 'Lisa'],
'twice': ['Jihyo', 'Nayeon', 'Sana', 'Momo', 'Mina', 'Tzuyu', 'Dahyun', 'Jeongyeon', 'Chaeyoung'],
'red velvet': ['Irene', 'Joy', 'Yeri', 'Seulgi', 'Wendy'],
'aespa': ['Karina', 'NingNing', 'Winter', 'Giselle'],
'2ne1': ['CL', 'Minzy', 'Bom', 'Dara']
}


def escolher_pack(packs):
    grupo = (input('Em qual pack você deseja atirar?: ')).strip().lower()
    while grupo not in packs:
        grupo = input('Pack inválido! Escolha entre Girls Generation, Blackpink, Twice, Red Velvet, Aespa, 2NE1').strip().lower()
    return grupo
   

if start == 1:
    print('Annyeong!! Você escolheu jogar nosso gatcha de photocards. Banners disponíveis: Girls Generation, Blackpink, Twice, Red Velvet, Aespa, 2NE1.')

    
    grupo = escolher_pack(packs)
    raro = packs[grupo]
    
    tentativa = 0
    credito = 5

    while True:
            
        tentativa += 1
        credito -= 1
        
        item = random.choices(
        population = comum + raro,
        weights = [90]*len(comum) + [10]*len(raro),
        k=1
    )[0]
       
    
        print(f' \n Tentativa {tentativa}: Você conseguiu {item}. Créditos restantes: {credito} créditos')
        if item in raro:
            print(f'\n 🎉 PARABÉNS!!! Você conseguiu o photocard da {item} em {tentativa} tentativas!')
            break
        if credito == 0:
            ans = input('Opa, parece que seus créditos acabaram. Deseja comprar mais créditos? Sim/Não').strip().lower()

            while ans not in('sim','s','não','n'):
                ans = input('Não consegui entender sua resposta.. Deseja comprar mais créditos? Sim/Não').strip().lower()

            if ans in('não', 'n'):
                print('❌ Fim de jogo!! Obrigado por jogar!')
                break
            else:
                buycredito = int(input('Quantos créditos deseja recarregar?'))
                credito += buycredito
                continue
        
            
            
                 
else:
    print('Saindo do jogo.. Até a próxima! Annyeong!')