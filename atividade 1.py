import streamlit as st
import pandas as pd
# Criando a base de dados
import streamlit as st
import pandas as pd

# Criando a base de dados
dados = {
    "curso": ["Reforço de Matemática", "Inglês Básico", "Robótica", "Teatro", "Reforço de Português", "Espanhol", "Xadrez", "Pintura"],
    "categoria": ["Exatas", "Idiomas", "Tecnologia", "Arte", "Humanas", "Idiomas", "Tecnologia", "Arte"],
    "valor": [120.0, 150.0, 200.0, 100.0, 120.0, 140.0, 90.0, 110.0],
    "carga_horaria": [4, 3, 5, 2, 4, 3, 2, 3],
    "avaliacao": [4.7, 4.3, 4.9, 4.5, 4.2, 4.4, 4.6, 4.8]
}

df = pd.DataFrame(dados)

# 2. Filtros na barra lateral
st.sidebar.title("Filtros")

categoria_escolhida = st.sidebar.selectbox(
    "Categoria:",
    ["Todas"] + list(df["categoria"].unique())
)

valor_maximo = st.sidebar.slider(
    "Mensalidade máxima (R$):",
    min_value=float(df["valor"].min()),
    max_value=float(df["valor"].max()),
    value=float(df["valor"].max())
)

# 3. Aplicando os filtros
df_filtrado = df[df["valor"] <= valor_maximo]

if categoria_escolhida != "Todas":
    df_filtrado = df_filtrado[df_filtrado["categoria"] == categoria_escolhida]

# 4. Mostrando a tabela filtrada na tela
st.subheader("Cursos filtrados")
st.dataframe(df_filtrado, hide_index=True)

receita_total = df_filtrado["valor"].sum()
avaliacao_media = df_filtrado["avaliacao"].mean() if len(df_filtrado) > 0 else 0

col1.metric("Receita total em mensalidades", f"R$ {receita_total:.2f}")
col2.metric("Avaliação média dos cursos", f"{avaliacao_media:.1f} ⭐")

# 5.As métricas
col1, col2 = st.columns(2)

receita_total = df_filtrado["valor"].sum()
avaliacao_media = df_filtrado["avaliacao"].mean() if len(df_filtrado) > 0 else 0

col1.metric("Receita total em mensalidades", f"R$ {receita_total:.2f}")
col2.metric("Avaliação média dos cursos", f"{avaliacao_media:.1f} ⭐")

st.divider()

# 6. Gráfico
st.subheader("Receita total por curso")

if len(df_filtrado) > 0:
    valor_por_curso = df_filtrado.groupby("curso")["valor"].sum()
    st.bar_chart(valor_por_curso)
else:
    st.warning("Nenhum curso encontrado com esse filtro.")