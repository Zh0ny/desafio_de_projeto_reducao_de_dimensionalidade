# desafio_de_projeto_reducao_de_dimensionalidade Com dataset da Arara Canindé e Coruja da Igreja

Este repositório contém um script Python que processa imagens de aves, convertendo-as para escala de cinza e binárias, além de oferecer a opção de exibir as imagens resultantes.

## Descrição

O script `dimensionality_reduction.py` realiza as seguintes tarefas:

1.  **Carrega imagens:** Lê imagens de dois diretórios de entrada, cada um contendo imagens de uma espécie de ave diferente (Coruja da Igreja e Arara Canindé).
2.  **Conversão para escala de cinza:** Converte as imagens coloridas para escala de cinza.
3.  **Binarização:** Binariza as imagens em escala de cinza usando um limiar fixo.
4.  **Salva imagens:** Salva as imagens em escala de cinza e binárias em diretórios de saída separados.
5.  **Exibição (opcional):** Permite ao usuário exibir as imagens originais, em escala de cinza e binárias lado a lado.
6. **Conjunto de Dados:**
    - Foram utilizadas 2 classes: Arara Canindé e Coruja da Igreja.
    - Cada Classe contém 100 imagens com licença creative commons.
    - Esse conjunto de dados utiliza técnicas de data augmentation.
    - Link para download: https://drive.google.com/drive/folders/1xq0g7YDThdUgcDaUpjTmQB1hOyDEycQK?usp=sharing

## Pré-requisitos

* Python 3.x
* OpenCV (cv2)
* NumPy

Você pode instalar as dependências usando o pip:

```bash
pip install opencv-python numpy

## Estrutura de Diretórios

seu_repositorio/
├── dimensionality_reduction.py
├── coruja_da_igreja_dataset_augmented/
│   ├── imagem1.jpg
│   ├── imagem2.png
│   └── ...
├── Arara_caninde_dataset_augmented/
│   ├── imagem1.jpg
│   ├── imagem2.png
│   └── ...
├── coruja_da_igreja_binary_gray/
│   ├── grayscale_imagem1.jpg
│   ├── binary_imagem1.jpg
│   └── ...
└── Arara_caninde_augmented_binary_gray/
    ├── grayscale_imagem1.jpg
    ├── binary_imagem1.jpg
    └── ...

coruja_da_igreja_dataset_augmented/ e Arara_caninde_dataset_augmented/: Diretórios contendo as imagens originais das aves.
coruja_da_igreja_binary_gray/ e Arara_caninde_augmented_binary_gray/: Diretórios onde as imagens processadas serão salvas.

## Como Executar

Clone o repositório:

Bash

git clone [https://github.com/Zh0ny/desafio_de_projeto_reducao_de_dimensionalidade.git](https://github.com/Zh0ny/desafio_de_projeto_reducao_de_dimensionalidade.git)
cd [desafio_de_projeto_reducao_de_dimensionalidade]
Execute o script Python:

Bash

python dimensionality_reduction.py
O script perguntará se você deseja exibir as imagens. Digite "s" para sim ou "n" para não.

## Observações
Certifique-se de que os caminhos dos diretórios de entrada e saída no script estejam corretos.
O limiar de binarização (128) pode ser ajustado no script para obter diferentes resultados.
O código exibe as imagens concatenadas horizontalmente, mostrando a imagem original, a imagem em escala de cinza e a imagem binarizada lado a lado.
