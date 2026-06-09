import qrcode 
import time 
import os 

def gerar_qr_code(link,nome_arquivo):
    print(f'Aguarde o qr code {nome_arquivo} esta sendo gerado..')
    time.sleep(3)

    qr = qrcode.make(link)

    os.makedirs('qrcodes', exist_ok= True)

    qr.save(f'qrcodes/{nome_arquivo}.png')

    print(f'QR code {nome_arquivo} criado com sucesso!!')



executado = 0 

while True:

    print('Seja bem vindo ao gerador de qr code')

    link = input('Envie o link que você quer transforar em qr code:')

    nome_arquivo = input('Digite o nome que seu arquivo será salvo:')

    gerar_qr_code(link, nome_arquivo)

    executado += 1

    continuar = input('Deseja criar outro? (s/n):')

    if continuar.lower() != 's':
        print(f'Total de qr code gerados: {executado}')
        print('Agradecemos por utilizar!!')

        break