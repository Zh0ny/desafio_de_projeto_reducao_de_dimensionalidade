import cv2
import os
import numpy as np

INPUT_DIR = ["D:/Dev/Courses/DIO/BairesDev - Machine Learning Practitioner/desafio_de_projeto_reducao_de_dimensionalidade/coruja_da_igreja_dataset_augmented", "D:/Dev/Courses/DIO/BairesDev - Machine Learning Practitioner/desafio_de_projeto_reducao_de_dimensionalidade/Arara_caninde_dataset_augmented"]
OUTPUT_DIR = ["D:/Dev/Courses/DIO/BairesDev - Machine Learning Practitioner/desafio_de_projeto_reducao_de_dimensionalidade/coruja_da_igreja_dataset_augmented_binary_gray", "D:/Dev/Courses/DIO/BairesDev - Machine Learning Practitioner/desafio_de_projeto_reducao_de_dimensionalidade/Arara_caninde_dataset_augmented_binary_gray"]
show_images = input("Deseja exibir as imagens? (s/n): ")
show_images = show_images.lower() == 's'

for index in range(len(INPUT_DIR)):
    if not os.path.exists(OUTPUT_DIR[index]):
        os.makedirs(OUTPUT_DIR[index])
    for img_name in os.listdir(INPUT_DIR[index]):
        img_path = os.path.join(INPUT_DIR[index], img_name)
        img = cv2.imread(img_path)

        if img is not None:

            # Convert image to grayscale
            grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            grayscale_output_path = os.path.join(OUTPUT_DIR[index], "grayscale_" + img_name)
            cv2.imwrite(grayscale_output_path, grayscale_img)

            #Convert grayscale image to binary image
            binary_img = cv2.threshold(grayscale_img, 128, 255, cv2.THRESH_BINARY)[1]
            binary_output_path = os.path.join(OUTPUT_DIR[index], "binary_" + img_name)
            cv2.imwrite(binary_output_path, binary_img)
            print(OUTPUT_DIR[index])
            if show_images:
                # Convert grayscale and binary images to 3-channel images
                grayscale_img_3ch = cv2.cvtColor(grayscale_img, cv2.COLOR_GRAY2BGR)
                binary_img_3ch = cv2.cvtColor(binary_img, cv2.COLOR_GRAY2BGR)

                concatenated_img = np.concatenate((img, grayscale_img_3ch, binary_img_3ch), axis=1) #concatenate along width
                cv2.imshow("Imagem original | Imagem em escala de cinza | Imagem binarizada", concatenated_img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
