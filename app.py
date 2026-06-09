import qrcode 

link = 'https://www.google.com/search?q=gravata&oq=gravata+&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDExNTFqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8'

qr = qrcode.make(link)

qr.save('qrcode.png')

print('QR code criado com sucesso!!')