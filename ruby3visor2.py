import os
import pygame
from pygame.locals import KEYDOWN, K_LEFT, K_RIGHT

# Configuración inicial
pygame.init()
screen = pygame.display.set_mode((800, 600))  # Ventana de tamaño fijo
pygame.display.set_caption("Visor de imágenes con pantalla de inicio")

# Ruta del directorio con las imágenes
image_folder = "./Ruby3-waifu/"
images = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
images.sort()  # Ordenar las imágenes alfabéticamente

# Variables de control
current_image_index = 0
running = True

def show_start_screen():
    """Muestra una pantalla de inicio con el texto 'Hero Soft'."""
    screen.fill((0, 0, 0))  # Fondo negro
    font = pygame.font.Font(None, 74)  # Fuente predeterminada, tamaño 74
    text = font.render("Hero Soft", True, (255, 255, 255))  # Texto en blanco
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.delay(1000)  # Mostrar la pantalla durante 1 segundo

def display_image(index):
    """Muestra la imagen en la ventana respetando el aspecto real."""
    screen.fill((0, 0, 0))  # Fondo negro
    image_path = images[index]
    image = pygame.image.load(image_path)
    
    # Obtener las dimensiones originales
    image_width, image_height = image.get_size()
    screen_width, screen_height = screen.get_size()
    
    # Calcular el escalado proporcional
    scale_factor = min(screen_width / image_width, screen_height / image_height)
    new_width = int(image_width * scale_factor)
    new_height = int(image_height * scale_factor)
    
    # Redimensionar la imagen respetando el aspecto
    resized_image = pygame.transform.smoothscale(image, (new_width, new_height))
    
    # Centrar la imagen en la ventana
    x_offset = (screen_width - new_width) // 2
    y_offset = (screen_height - new_height) // 2
    screen.blit(resized_image, (x_offset, y_offset))
    pygame.display.flip()

# Mostrar la pantalla de inicio
show_start_screen()

# Mostrar la primera imagen si hay imágenes disponibles
if images:
    display_image(current_image_index)

# Bucle principal
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:  # Retroceder imagen
                current_image_index = (current_image_index - 1) % len(images)
                display_image(current_image_index)
            elif event.key == K_RIGHT:  # Avanzar imagen
                current_image_index = (current_image_index + 1) % len(images)
                display_image(current_image_index)
    
    clock.tick(1)  # 1 FPS (1 segundo por imagen si no se presionan teclas)

pygame.quit()
