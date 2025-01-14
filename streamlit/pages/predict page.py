import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Used Cars Price Predictor",
    page_icon="🚘",
    layout="wide",
    initial_sidebar_state="expanded"
)

import base64
st.markdown(
    """<a href="https://syarah.com">
    <img src="data:image/png;base64,{}" max_container_windth=True">
    </a>""".format(base64.b64encode(open("test.webp", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
appear_text_html = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            margin: 0;
            padding: 0;
            background-color: #222;
            color: white;
            font-family: Arial, sans-serif;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .appearing-text {
            font-size: 3rem;
            font-weight: bold;
            opacity: 0;
            animation: fadeIn 3s forwards;
        }

        @keyframes fadeIn {
            0% {
                opacity: 0;
                transform: translateY(50px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style>
</head>
<body>
    <div class="appearing-text">
          🚘 Used Cars Predictor 🚘
    </div>
</body>
</html>
"""
st.markdown(appear_text_html, unsafe_allow_html=True)

# Sidebar with improved layout
st.sidebar.header("🚘 Car Information 🚘")
st.sidebar.markdown("---")
import pickle
def user_input_features():
    df=pd.read_csv('data_clean.csv').loc[:,'Type':]
    list_make = []
    list_type = []

    for make in sorted(df['Make'].unique()) :
        type = sorted(list(df[df['Make']==make]['Type'].unique()))
        list_type.append(type)
        list_make.append(make)

    df_maketype = pd.DataFrame()
    df_maketype['Make'] = list_make
    df_maketype['Type'] = list_type

    make_list = df_maketype['Make'].tolist()

    Make = st.sidebar.selectbox("Select Make (Brand of Car)", options=make_list)

    type_list = df_maketype[df_maketype['Make'] == Make]['Type'].tolist()[0]

    Type = st.sidebar.selectbox("Select Type", options=type_list)


     # Origin & Region
    list_Origin = []
    list_Region = []

    for origin in sorted(df['Origin'].unique()) :
        region = sorted(list(df[df["Origin"]==origin]['Region'].unique()))
        list_Region.append(region)
        list_Origin.append(origin)

    df_origin_region = pd.DataFrame()
    df_origin_region['Origin'] = list_Origin
    df_origin_region['Region'] = list_Region
    df_origin_region = df_origin_region.loc[[0,3,2]]


    origin_allowed_values = df_origin_region['Origin'].tolist()

    Origin = st.sidebar.selectbox("Select Origin", options=origin_allowed_values)


    Region_allowed_values = df_origin_region[df_origin_region['Origin'] == Origin]['Region'].tolist()[0]

    Region = st.sidebar.selectbox("Select Region", options=Region_allowed_values)


    gear=st.sidebar.radio('Gear Type:', df['Gear_Type'].unique().tolist(), horizontal=True)
    options=st.sidebar.radio('Options:', df['Options'].unique().tolist(), horizontal=True)
    year=st.sidebar.select_slider('Year',options=list(df['Year'].unique()))
    engine=st.sidebar.number_input('Engine Size',1.0,9.0,1.0)
    mileage=st.sidebar.number_input('Mileage',0,4500000)

    df=pd.DataFrame()
    df['Type']=[Type]
    df['Region']=[Region]
    df['Make']=[Make]
    df['Gear_Type']=[gear]
    df['Origin']=[Origin]
    df['Options']=[options]
    df['Year']=[year]
    df['Engine_Size']=[engine]
    df['Mileage']=[mileage]

    return df

df_usedcars=user_input_features()
df_usedcars.index=['value']

model_loaded=pickle.load(open('model_catboost.sav','rb'))
price=model_loaded.predict(df_usedcars)

col1,col2=st.columns([10,4])
#bagian kiri
with col1:
    st.subheader('Passenger Features:')
    st.write(df_usedcars)
    

with col1:
    st.subheader('Price prediction:')
    st.markdown(f"""
    <div style="border: 3px solid #4CAF50; padding: 10px; width: 320px; margin: auto;">
        <h3 style="color: #4CAF50; font-size: 50px; font-weight: bold;">
            SAR {price[0]:,.0f}
        </h3>
    </div>
""", unsafe_allow_html=True)