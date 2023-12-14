import streamlit as st

# Função para calcular o IMC
def calcular_imc(peso, altura):
    altura_m = altura / 100
    imc = peso / (altura_m ** 2)
    return imc

# Função para calcular o GEB usando a fórmula de Harris-Benedict
def calcular_geb(genero, peso, altura, idade):
    if genero == 'Masculino':
        geb = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade)
    else:
        geb = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * idade)
    return geb

# Título da página
st.title('Calculadora de IMC e Gasto Energético Basal (GEB)')

# Adicionando uma imagem
st.image('nutri.png', caption='Nutrição', width=130)

# Entrada de dados do usuário
peso = st.number_input('Digite seu peso (em kg):')
altura = st.number_input('Digite sua altura (em cm):')
idade = st.number_input('Digite sua idade:')
genero = st.radio('Selecione seu gênero:', ('Masculino', 'Feminino'))

# Botão para calcular
if st.button('Calcular'):
    # Cálculos
    imc = calcular_imc(peso, altura)
    geb = calcular_geb(genero, peso, altura, idade)

    # Exibição dos resultados
    st.write(f'Seu IMC é: {imc:.2f}')

    st.write(f'Seu GEB é: {geb:.2f} calorias por dia')
