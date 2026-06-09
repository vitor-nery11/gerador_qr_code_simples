import qrcode 
import time 

print('Seja bem vindo ao gerador de qr code')

link = input('Envie o link que você quer transforar em qr code:')
nome_arquivo = input('Digite o nome que seu arquivo será salvo:')
print('aguarde, seu qr code esta sendo gerado')
time.sleep(3)

qr = qrcode.make(link)

qr.save(f'{nome_arquivo}.png')

print('QR code criado com sucesso!!')