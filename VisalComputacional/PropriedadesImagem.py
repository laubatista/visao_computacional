# Importação das bibliotecas do opencv, é  obrigatória para utilizar suas funções.
import cv2

#Leitura da imagem com a função imread()
#Usada para abrir a imagem, e tem como argumento o nome do arquivo em disco.
imagem = cv2.imread('paisagem.jpg')

print('Largura em pixels:', end='')
print(imagem.shape[1]) # Largura da imagem
print('Altura em pixels:', end='')
print(imagem.shape[0]) #altura da imagem
print('quantidade de canais:', end='')
print(imagem.shape[2])

#Mostra a imagem com a função imshow
cv2.imshow("Primeira imagem", imagem)
cv2.waitKey(0) # espera pressionar qualquer tecla

# Salvar a imagem no disco com a função imwrite()
cv2.imwrite("Teste01.jpg", imagem)
