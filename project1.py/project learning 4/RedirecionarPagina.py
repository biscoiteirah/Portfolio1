from flask import Flask, redirect
import webbrowser
import requests

def obter_usuario_instagram(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            print(f"Usuário encontrado: {url}")
        else:
            print(f"Usuário não encontrado: {resposta.status_code}")
    except Exception as e:
        print(f"Erro ao acessar o Instagram: {e}")

def abrir_instagram(url):
    try:
        webbrowser.open(url, new=2)  # Abre em uma nova aba do navegador
        print(f"Abrindo o Instagram do usuário: {url}")
    except Exception as e:
        print(f"Erro ao abrir o Instagram: {e}")

app = Flask(__name__)
usuario = 'https://www.instagram.com//moniquezezza/'
obter_usuario_instagram(usuario)
abrir_instagram(usuario)

@app.route('/redirecionar_instagram/<usuario>')
def redirecionar_instagram(usuario):
    url_instagram = f'https://www.instagram.com/{usuario}'
    return redirect(url_instagram)

if __name__ == '__main__':
    app.run(debug=True)