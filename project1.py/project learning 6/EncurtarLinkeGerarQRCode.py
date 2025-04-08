import pyshorteners
import qrcode
from PIL import Image  # Import Pillow to display the QR code

def encurtar_link(link):
    # Use a supported shortener service (e.g., TinyURL)
    shortener = pyshorteners.Shortener()
    short_link = shortener.tinyurl.short(link)  # Use TinyURL for shortening
    return short_link

def gerar_qrcode(link, nome_arquivo):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    
    qr.add_data(link)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(nome_arquivo)
    return nome_arquivo  # Return the file name of the saved QR code

# Input the original link
link_original = input('Digite o link original: ')

# Shorten the link
link_encurtado = encurtar_link(link_original)

# Print the shortened link
print(f"Link encurtado: {link_encurtado}")

# Generate and save the QR Code
nome_arquivo_qrcode = gerar_qrcode(link_encurtado, nome_arquivo='qrcode.png')

print(f"QR Code salvo como '{nome_arquivo_qrcode}'.")

# Display the QR Code
img = Image.open(nome_arquivo_qrcode)  # Open the saved QR code image
img.show()  # Display the QR code in a separate window