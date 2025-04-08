import math
import random
import pygame
import sys
from collections import deque 
import pygame.gfxdraw # Importando o módulo gfxdraw para desenhar formas
import pygame.freetype # Importando o módulo freetype para renderizar texto



def salvar_desenho():
    pygame.image.save(canvas, 'desengo.png')  # Salva a tela como uma imagem PNG
    print("Desenho salvo como 'desengo.png'")
    
    
    
# Definindo as cores
CORES = {
'Vermelho': (255, 0, 0),  
'Verde': (0, 255, 0),  
'Azul': (0, 0, 255),  
'Amarelo': (255, 255, 0), 
'Laranja': (255, 165, 0),  
'Roxo': (128, 0, 128),  
'Ciano': (0, 255, 255),  
'Rosa': (255, 192, 203),  
'Cinza': (128, 128, 128),  
'Preto': (0, 0, 0),  
'Branco': (255, 255, 255) 
}



#configurações iniciais
pygame.init()
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Desenho com Pygame")
cor_fundo = (255, 255, 255)  # Branco
tamanho_pincel = 5
cor_atual = CORES['Preto']  # Cor padrão
tela.fill(cor_fundo)



# Criando uma superfície para desenhar
canvas = pygame.Surface((largura, altura))
canvas.fill(cor_fundo)



# Criando uma fila para armazenar os pontos desenhados
pontos = deque(maxlen=1000)  # Limite de pontos na fila
ferramenta_1 = 'pincel'  # Ferramenta padrão
ferramenta_2 = 'borracha'  # Ferramenta padrão
ferramenta_3 = 'lapis'  # Ferramenta padrão
ferramenta_4 = 'spray'  # Ferramenta padrão
ferramenta_5 = 'balde'  # Ferramenta padrão
forma_selecionada = None
ponto_inicial = None



def desenhar_ui():
    ferramentas = ['pincel', 'borracha', 'lapis', 'spray', 'balde', 'retângulo', 'círculo',
                   'linha', 'polígono', 'texto', 'triangulo', 'quadrado', 'pentagono']
    cores = ['Preto', 'Branco', 'Vermelho', 'Ciano', 'Cinza', 'Rosa', 'Azul', 'Laranja', 'Roxo', 'Amarelo', 'Verde']
    valores_cores = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 255), (128, 128, 128), (255, 192, 203),
                     (0, 0, 255), (255, 165, 0), (128, 0, 128), (255, 255, 0), (0, 255, 0)]
    
    fonte = pygame.font.Font(None, 24)  # Define the font and size
    
    # Draw tool buttons
    for i, ferramenta in enumerate(ferramentas):
        texto = fonte.render(ferramenta, True, (0, 0, 0))  # Render the text
        largura_texto, altura_texto = texto.get_size()  # Get text dimensions
        largura_botao = largura_texto + 20  # Add padding to the button width
        altura_botao = altura_texto + 10  # Add padding to the button height
        
        # Draw the button
        pygame.draw.rect(tela, (200, 200, 200), (50, 10 + i * (altura_botao + 10), largura_botao, altura_botao))  # Button background
        pygame.draw.rect(tela, (0, 0, 0), (50, 10 + i * (altura_botao + 10), largura_botao, altura_botao), 2)  # Button border
        
        # Draw the text
        tela.blit(texto, (50 + 10, 10 + i * (altura_botao + 10) + 5))  # Center the text within the button
    
    # Draw color palette
    for i, cor_nome in enumerate(cores):
        pygame.draw.rect(tela, valores_cores[i], (200 + i * 40, 10, 30, 30))  # Draw color box
        pygame.draw.rect(tela, (0, 0, 0), (200 + i * 40, 10, 30, 30), 2)  # Draw border
 
        
# implementação do balde de tinta
def flood_fill(pos, cor_nova):
    x, y = pos
    cor_alvo = canvas .get_at((x, y))
    if cor_alvo == cor_nova:
        return
    fila = deque([(x, y)])
    fila.append((x, y))
    
    while fila:
        x, y = fila.popleft()
        if canvas.get_at((x, y)) == cor_alvo:
            canvas.set_at((x, y), cor_nova)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < largura and 0 <= ny < altura:
                    fila.append((nx, ny))
                    


def desenhar_forma(pos_final):
    global ponto_inicial
    if forma_selecionada == 'retângulo':
        rect = pygame.Rect(ponto_inicial, (pos_final[0]-ponto_inicial[0], pos_final[1]-ponto_inicial[1]))
        pygame.draw.rect(canvas, cor_atual, rect, tamanho_pincel)
        
    elif forma_selecionada == 'círculo':
        raio = int(((pos_final[0]-ponto_inicial[0])**2 + (pos_final[1]-ponto_inicial[1])**2)**0.5)
        pygame.draw.circle(canvas, cor_atual, ponto_inicial, raio, tamanho_pincel)
        
    elif forma_selecionada == 'triangulo':
        pontos = [
            ponto_inicial,
            (pos_final[0], ponto_inicial[1]),
            ((ponto_inicial[0] + pos_final[0]) // 2, pos_final[1])
        ]
        pygame.draw.polygon(canvas, cor_atual, pontos, tamanho_pincel)
        
    elif forma_selecionada == 'quadrado':
        lado = min(abs(pos_final[0]-ponto_inicial[0]), abs(pos_final[1]-ponto_inicial[1]))
        rect = pygame.Rect(ponto_inicial, (lado, lado))
        pygame.draw.rect(canvas, cor_atual, rect, tamanho_pincel)
    
    elif forma_selecionada == 'pentagono':
        centro_x = (ponto_inicial[0] + pos_final[0]) // 2
        centro_y = (ponto_inicial[1] + pos_final[1]) // 2
        raio = max(abs(pos_final[0]-ponto_inicial[0]), abs(pos_final[1]-ponto_inicial[1])) // 2
        
        pontos = []
        for i in range(5):
            angulo = math.radians(72 * i - 90)  # Ajuste para centralizar o pentágono
            x = centro_x + raio * math.cos(angulo)
            y = centro_y + raio * math.sin(angulo)
            pontos.append((x, y))
        pygame.draw.polygon(canvas, cor_atual, pontos, tamanho_pincel)
        
    elif forma_selecionada == 'linha':
        pygame.draw.line(canvas, cor_atual, ponto_inicial, pos_final, tamanho_pincel)



# Loop principal        
texto_digitado = ""  # To store the text being typed
ferramenta = 'pincel'  # Default tool
ponto_inicial = None  # Starting point for shapes
desenhando = False  # Flag to track if the user is drawing
pontos_poligono = []  # To store the vertices of the polygon

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            
            # Check if a tool button is clicked
            ferramentas = ['pincel', 'borracha', 'lapis', 'spray', 'balde', 'retângulo', 'círculo',
                           'linha', 'polígono', 'texto', 'triangulo', 'quadrado', 'pentagono']
            fonte = pygame.font.Font(None, 24)
            for i, ferramenta_nome in enumerate(ferramentas):
                texto = fonte.render(ferramenta_nome, True, (0, 0, 0))
                largura_texto, altura_texto = texto.get_size()
                largura_botao = largura_texto + 20
                altura_botao = altura_texto + 10
                
                if 50 <= x <= 50 + largura_botao and 10 + i * (altura_botao + 10) <= y <= 10 + i * (altura_botao + 10) + altura_botao:
                    ferramenta = ferramenta_nome
                    forma_selecionada = ferramenta if ferramenta in ['retângulo', 'círculo', 'triangulo', 'quadrado', 'pentagono', 'linha'] else None
                    print(f"Ferramenta selecionada: {ferramenta}")
            
            # Check if a color is selected
            cores = ['Preto', 'Branco', 'Vermelho', 'Ciano', 'Cinza', 'Rosa', 'Azul', 'Laranja', 'Roxo', 'Amarelo', 'Verde']
            valores_cores = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 255), (128, 128, 128), (255, 192, 203),
                             (0, 0, 255), (255, 165, 0), (128, 0, 128), (255, 255, 0), (0, 255, 0)]
            for i, cor in enumerate(valores_cores):
                if 200 + i * 40 <= x <= 200 + i * 40 + 30 and 10 <= y <= 40:
                    cor_atual = cor
                    print(f"Cor selecionada: {cores[i]}")
            
            # Handle text tool
            if ferramenta == 'texto':
                texto_digitado = ""  # Reset text input
                ponto_inicial = pygame.mouse.get_pos()
            
            # Handle shape tools
            if forma_selecionada:
                ponto_inicial = pygame.mouse.get_pos()
                desenhando = True  # Start drawing the shape
            
            # Handle polygon tool
            if ferramenta == 'polígono':
                pontos_poligono.append(pygame.mouse.get_pos())
                if len(pontos_poligono) > 2:
                    pygame.draw.polygon(canvas, cor_atual, pontos_poligono, tamanho_pincel)
        
        if evento.type == pygame.MOUSEBUTTONUP:
            if forma_selecionada and desenhando:
                pos_final = pygame.mouse.get_pos()
                desenhar_forma(pos_final)  # Draw the shape
                desenhando = False  # Stop drawing
        
        if evento.type == pygame.KEYDOWN:
            if ferramenta == 'texto':
                if evento.key == pygame.K_RETURN:  # Finish typing on Enter
                    fonte = pygame.font.Font(None, 36)
                    texto = fonte.render(texto_digitado, True, cor_atual)
                    canvas.blit(texto, ponto_inicial)
                    texto_digitado = ""
                elif evento.key == pygame.K_BACKSPACE:  # Handle backspace
                    texto_digitado = texto_digitado[:-1]
                else:
                    texto_digitado += evento.unicode  # Add typed character
            
            # Finalize polygon
            if ferramenta == 'polígono':
                if evento.key == pygame.K_RETURN and len(pontos_poligono) > 2:
                    pygame.draw.polygon(canvas, cor_atual, pontos_poligono, tamanho_pincel)
                    pontos_poligono = []  # Clear the points after drawing
                elif evento.key == pygame.K_BACKSPACE and pontos_poligono:
                    pontos_poligono.pop()  # Remove the last point
        
        # Continuous painting/erasing
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            if ferramenta == 'pincel':
                pygame.draw.circle(canvas, cor_atual, pos, tamanho_pincel)
            elif ferramenta == 'lapis':
                pygame.draw.circle(canvas, cor_atual, pos, 1)
            elif ferramenta == 'borracha':
                pygame.draw.circle(canvas, cor_fundo, pos, tamanho_pincel)
            elif ferramenta == 'spray':
                for i in range(100):
                    angulo = random.uniform(0, 2 * math.pi)
                    raio = random.uniform(0, tamanho_pincel)
                    x_offset = int(raio * math.cos(angulo))
                    y_offset = int(raio * math.sin(angulo))
                    pygame.draw.circle(canvas, cor_atual, (pos[0] + x_offset, pos[1] + y_offset), 1)
    
    # Render the canvas
    tela.blit(canvas, (0, 0))  # Draw the canvas on the screen
    
    # Render dynamic polygon while adding points
    if ferramenta == 'polígono' and len(pontos_poligono) > 1:
        pygame.draw.polygon(tela, cor_atual, pontos_poligono, tamanho_pincel)
    
    # Render dynamic text while typing
    if ferramenta == 'texto' and texto_digitado:
        fonte = pygame.font.Font(None, 36)
        texto = fonte.render(texto_digitado, True, cor_atual)
        tela.blit(texto, ponto_inicial)  # Render the current text dynamically
    
    # Render the UI
    desenhar_ui()  # Draw the UI
    
    # Update the display
    pygame.display.flip()  # Update the display
    pygame.time.delay(30)  # Delay to control frame rate