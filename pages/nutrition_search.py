import pandas as pd
import streamlit as st
from scripts.search import search_image, search_gizi
import matplotlib.pyplot as plt
st.set_page_config(initial_sidebar_state="collapsed")

st.title('Food Nutrition Search')
def kurangi_gizi(gizi_target, gizi_usage):
    gizi_target[0] -= gizi_usage.get('calories', 0)
    gizi_target[1] -= gizi_usage.get('proteins', 0)
    gizi_target[2] -= gizi_usage.get('fat', 0)
    gizi_target[3] -= gizi_usage.get('carbohydrate', 0)
    return gizi_target

if 'gizi_target' not in st.session_state:
    st.session_state.gizi_target = [0, 0, 0, 0]

if 'image_result' not in st.session_state:
    st.session_state.image_result = None

tab_image, tab_gizi = st.tabs(['Search by Image', 'Search by Gizi'])
with tab_image:
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file:
        bytes_data = uploaded_file.getvalue()
        st.image(bytes_data)
    gizi_target = st.session_state.get('gizi_target')
    image_result = st.session_state.get('image_result')

    submit = st.button('Submit', type='primary', disabled=uploaded_file is None, key='search_image')
    delta_calories = 0
    delta_proteins = 0
    delta_fat = 0
    delta_carbohydrate = 0
    gizi_awal = gizi_target.copy()
    if submit:
        image_result = search_image(bytes_data)
        st.session_state['image_result'] = image_result
        if image_result:
            gizi_usage = {
                'calories': image_result[0]['calories'],
                'proteins': image_result[0]['proteins'],
                'fat': image_result[0]['fat'],
                'carbohydrate': image_result[0]['carbohydrate']
            }
            gizi_target = st.session_state['gizi_target']
            gizi_hasil = kurangi_gizi(gizi_target, gizi_usage)
            st.session_state['gizi_target'] = gizi_hasil
            delta_calories = round(gizi_awal[0] - gizi_target[0], 1)
            delta_proteins = round(gizi_awal[1] - gizi_target[1], 1)
            delta_fat = round(gizi_awal[2] - gizi_target[2], 1)
            delta_carbohydrate = round(gizi_awal[3] - gizi_target[3], 1)
    
    st.divider()
    st.header('Image Search Result')
    st.subheader('Nutrition Needs')
    gizi_target = st.session_state.get('gizi_target')
    col1, col2, col3, col4= st.columns(4)
    col1.metric("Calories (Kcal)", gizi_target[0], delta_calories)
    col2.metric("Proteins (g)", gizi_target[1], delta_proteins)
    col3.metric("Fat (g)", gizi_target[2], delta_fat)
    col4.metric("Carbohydrate (g)", gizi_target[3], delta_carbohydrate)
    image_result = st.session_state.get('image_result', None)
    if image_result:
        st.json(image_result, expanded=False)
        df = pd.DataFrame(image_result)
        df = df[['image', 'name', 'fat', 'proteins', 'calories', 'carbohydrate']]
        st.dataframe(
            df,
            column_config={
                "image": st.column_config.ImageColumn(
                    "Image", help="Streamlit app preview screenshots"
                )
            },
        )
        gizi_usage = {
            'calories': image_result[0]['calories'],
            'proteins': image_result[0]['proteins'],
            'fat': image_result[0]['fat'],
            'carbohydrate': image_result[0]['carbohydrate']
        }
        labels = ['Calories', 'Proteins',  'Fat', 'Carbohydrate']
        sizes = [gizi_usage[label.lower()] for label in labels]
        remaining = [gizi_awal[i] - sizes[i] if gizi_awal[i] > sizes[i] else 0 for i in range(len(gizi_awal))]

        
        fig, axs = plt.subplots(1, 4, figsize=(20, 6))
        fig.suptitle('Nutritional Information', fontsize=20)


        for i, (label, size, remain) in enumerate(zip(labels, sizes, remaining)):
            ax = axs[i]
            autopct_label = '%1.1f%%' if size > 0 else None
            wedges, texts, autotexts = ax.pie([size, remain], labels=None, autopct=autopct_label, startangle=90, wedgeprops={'width': 0.3}, colors=['#089BAB', '#E8F5F8'])
            plt.setp(autotexts, size=16, weight="bold", color="black") 
            ax.set_title(label, fontsize=16)
            
        fig.legend(['Nutrition', 'Goals'], loc='lower center', ncol=2, bbox_to_anchor=(0.5, -0.05), fontsize=14)

        plt.tight_layout()
        st.pyplot(fig)

with tab_gizi:
    fat = st.text_input('Fat', value='0')
    proteins = st.text_input('Protein', value='0')
    calories = st.text_input('Kalori', value='0')
    carbohydrate = st.text_input('Karbohidrat', value='0')

    valid = False
    try:
        calories, proteins, fat, carbohydrate = [float(val) for val in [calories, proteins, fat, carbohydrate]]
        valid = True
        
    except:
        st.error('Value must be a float or number!')


    st.markdown(f'calories, proteins, fat, carbohydrate: {(calories, proteins, fat, carbohydrate)}')

    submit = st.button('Submit', type='primary', disabled=not valid, key='search_gizi')
    if submit:
        # Call OCR API
        gizi_result = search_gizi(calories, proteins, fat, carbohydrate)
        st.session_state['gizi_result'] = gizi_result
    
    st.divider()
    st.header('Gizi Search Result')
    gizi_result = st.session_state.get('gizi_result', None)
    if gizi_result:
        st.json(gizi_result, expanded=False)
        df = pd.DataFrame(gizi_result)
        df = df[['image', 'name', 'fat', 'proteins', 'calories', 'carbohydrate']]
        st.dataframe(
            df,
            column_config={
                "image": st.column_config.ImageColumn(
                    "Image", help="Streamlit app preview screenshots"
                )
            },
        )

