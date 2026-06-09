import qrcode 
import time 

def gerar_qr_code(link,nome_arquivo):
    print(f'Aguarde o qr code {nome_arquivo} esta sendo gerado..')
    time.sleep(3)

    qr = qrcode.make(link)

    qr.save(f'{nome_arquivo}.png')

    print(f'QR code {nome_arquivo} criado com sucesso!!')



print('Seja bem vindo ao gerador de qr code')

link = input('Envie o link que você quer transforar em qr code:')

nome_arquivo = input('Digite o nome que seu arquivo será salvo:')

gerar_qr_code(link, nome_arquivo)