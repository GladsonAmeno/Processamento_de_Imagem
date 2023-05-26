import cv2
import os

# Carrega a imagem "teste.jpg" utilizando o OpenCV
img = cv2.imread(os.path.join('.', "teste.jpg"))

# Converte a representação de cores da imagem de BGR para RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Converte a imagem para escala de cinza
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Exibe a imagem original em uma janela com o título 'img'
cv2.imshow('img', img)

# Exibe a imagem convertida para RGB em uma janela com o título 'img_rgb'
cv2.imshow('img_rgb', img_rgb)

# Exibe a imagem em escala de cinza em uma janela com o título 'img_gray'
cv2.imshow('img_gray', img_gray)

# Aguarda até que uma tecla seja pressionada para fechar as janelas
cv2.waitKey(0)
