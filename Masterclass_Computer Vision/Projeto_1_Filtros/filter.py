import streamlit as st
import numpy as np
import cv2
from PIL import Image,ImageEnhance

OUTPUT_WIDTH = 500

def main():
    our_image = Image.open('empty.jpg')

    # main
    st.title('Filtros em Imagens - Projeto 1 ')
    st.sidebar.title('Barra Lateral')

    # menu com as opções
    option_main = ["Filtros","Sobre"]
    choice = st.sidebar.selectbox('Escolha uma opção',option_main)

    if choice == 'Filtros' :

        # carregar e exibir imagem
        image_file = st.file_uploader("Carregue o arquivo",type=['jpg','jpeg','png'])

          # Carregara a imagem caso image_file esteja vazio
        if image_file is not None:
            our_image = Image.open(image_file)
            st.sidebar.text('Imagem Original')
            st.sidebar.image(our_image,width=150)

        # filtros que podem ser aplicados
        ap_filter = st.sidebar.radio('Filtros',['Original','Grayscale','Desenho'
                                                 ,'Sépia','Blur','Canny', 'Contraste'
                                                ])

        if ap_filter == 'Grayscale' :
            converted_image = np.array(our_image.convert('RGB'))
            gray_image = cv2.cvtColor(converted_image, cv2.COLOR_RGB2GRAY)
            st.image(gray_image,width=OUTPUT_WIDTH)

        if ap_filter == 'Desenho' :
            converted_image = np.array(our_image.convert('RGB'))
            gray_image = cv2.cvtColor(converted_image, cv2.COLOR_RGB2GRAY)
            inv_gray_image = 255 - gray_image
            blur_image = cv2.GaussianBlur(inv_gray_image,(21,21),0,0)
            sketch_image = cv2.divide(gray_image,255 - blur_image,scale=256)
            st.image(sketch_image,width=OUTPUT_WIDTH)

        if ap_filter == 'Sépia' :
            converted_image = np.array(our_image.convert('RGB'))
            converted_image = cv2.cvtColor(converted_image,cv2.COLOR_RGB2BGR)
            kernel = np.array([[0.272, 0.534, 0.131],
                               [0.349, 0.686, 0.168],
                               [0.393, 0.769, 0.189]])
            sepia_image = cv2.filter2D(converted_image, -1, kernel)
            st.image(sepia_image,width=OUTPUT_WIDTH)

        if ap_filter == 'Blur' :
            b_amount = st.sidebar.slider('Kernel (n x n)',3,81,9,step=2)
            converted_image = np.array(our_image.convert('RGB'))
            converted_image = cv2.cvtColor(converted_image,cv2.COLOR_RGB2BGR)
            blur_image = cv2.GaussianBlur(converted_image, (b_amount, b_amount), 0, 0)
            st.image(blur_image, channels='BGR',width=OUTPUT_WIDTH)

        if ap_filter == 'Canny' :
            converted_image = np.array(our_image.convert('RGB'))
            converted_image = cv2.cvtColor(converted_image,cv2.COLOR_RGB2BGR)
            blur_image = cv2.GaussianBlur(converted_image, (11, 11), 0)
            canny_image = cv2.Canny(blur_image, 100, 150)
            st.image(canny_image,width=OUTPUT_WIDTH)

        if ap_filter == 'Contraste' :
            c_amount = st.sidebar.slider('Contraste',0.0,2.0,1.0)
            enhancer = ImageEnhance.Color(our_image)
            contrast_image = enhancer.enhance(c_amount)
            st.image(contrast_image,width=OUTPUT_WIDTH)


        elif ap_filter == 'Original':
            st.image(our_image,width=OUTPUT_WIDTH)

    elif choice == 'Sobre' :
        st.markdown('**Gabriel Marcial** ')
        st.markdown('---')
        st.markdown(''' 
                        - Estudante de Engenharia - (Uerj)
        
                        - Criador do Blog Data Marte 
                        
                        - Estagiario em Data Science''')
        st.markdown('---')

if __name__=="__main__":
    main()