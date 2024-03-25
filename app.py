import streamlit as st
st.set_page_config(initial_sidebar_state="collapsed")
st.title('Nutrition Goals')
gender = st.radio(
    "What's your gender?",
    ["***Laki-laki***", "***Perempuan***"])

option = st.selectbox(
   "Age Group",
   ("10-12 tahun", "13-15 tahun", "16-18 tahun", "19-29 tahun", "30-49 tahun", "50-64 tahun", "65-80 tahun"),
   index=None,
   placeholder="Select age...",
)

st.write('You selected:', option)

if option == None :
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

if gender == "***Perempuan***" :
    if option == "10-12 tahun" :
        fat = st.text_input('Fat', value='65.00')
        proteins = st.text_input('Protein', value='55')
        calories = st.text_input('Kalori', value='1900')
        carbohydrate = st.text_input('Karbohidrat', value='280')

        valid = False
        try:
            calories, proteins, fat, carbohydrate = [float(val) for val in [calories, proteins, fat, carbohydrate]]
            valid = True
            
        except:
            st.error('Value must be a float or number!')
    elif option == "13-15 tahun":
        fat = st.text_input('Fat', value='70.00')
        proteins = st.text_input('Protein', value='65')
        calories = st.text_input('Kalori', value='2050')
        carbohydrate = st.text_input('Karbohidrat', value='300')

        valid = False
        try:
            calories, proteins, fat, carbohydrate = [float(val) for val in [calories, proteins, fat, carbohydrate]]
            valid = True
            
        except:
            st.error('Value must be a float or number!')
    elif option == "16-18 tahun":
        fat = st.text_input('Fat', value='70.00')
        proteins = st.text_input('Protein', value='65')
        calories = st.text_input('Kalori', value='2100')
        carbohydrate = st.text_input('Karbohidrat', value='300')

        valid = False
        try:
            calories, proteins, fat, carbohydrate = [float(val) for val in [calories, proteins, fat, carbohydrate]]
            valid = True
            
        except:
            st.error('Value must be a float or number!')
    elif option == "19-29 tahun":
        fat = st.text_input('Fat', value='65.00')
        proteins = st.text_input('Protein', value='60')
        calories = st.text_input('Kalori', value='2250')
        carbohydrate = st.text_input('Karbohidrat', value='360')

        valid = False
        try:
            calories, proteins, fat, carbohydrate = [float(val) for val in [calories, proteins, fat, carbohydrate]]
            valid = True
            
        except:
            st.error('Value must be a float or number!')
    elif option == "30-49 tahun":
        fat = st.text_input('Fat', value='60.00')
        proteins = st.text_input('Protein', value='60')
        calories = st.text_input('Kalori', value='2150')
        carbohydrate = st.text_input('Karbohidrat', value='340')

        valid = False
        try:
            calories, proteins, fat, carbohydrate = [float(val) for val in [calories, proteins, fat, carbohydrate]]
            valid = True
            
        except:
            st.error('Value must be a float or number!')
    elif option == "50-64 tahun":
        fat = st.text_input('Fat', value='50.00')
        proteins = st.text_input('Protein', value='60')
        calories = st.text_input('Kalori', value='1800')
        carbohydrate = st.text_input('Karbohidrat', value='280')

        valid = False
        try:
            calories, proteins, fat, carbohydrate = [float(val) for val in [calories, proteins, fat, carbohydrate]]
            valid = True
            
        except:
            st.error('Value must be a float or number!')
    elif option == "65-80 tahun":
        fat = st.text_input('Fat', value='45.00')
        proteins = st.text_input('Protein', value='58')
        calories = st.text_input('Kalori', value='1550')
        carbohydrate = st.text_input('Karbohidrat', value='230')

        valid = False
        try:
            calories, proteins, fat, carbohydrate = [float(val) for val in [calories, proteins, fat, carbohydrate]]
            valid = True
            
        except:
            st.error('Value must be a float or number!')

elif gender == "***Laki-laki***" :
    if option == "10-12 tahun":
        fat = st.text_input('Fat', value='65.00')
        proteins = st.text_input('Protein', value='50')
        calories = st.text_input('Kalori', value='2000')
        carbohydrate = st.text_input('Karbohidrat', value='300')

        valid = False
        try:
            calories, proteins, fat, carbohydrate = [float(val) for val in [calories, proteins, fat, carbohydrate]]
            valid = True
            
        except:
            st.error('Value must be a float or number!')
    elif option == "13-15 tahun":
        fat = st.text_input('Fat', value='80.00')
        proteins = st.text_input('Protein', value='70')
        calories = st.text_input('Kalori', value='2400')
        carbohydrate = st.text_input('Karbohidrat', value='350')

        valid = False
        try:
            calories, proteins, fat, carbohydrate = [float(val) for val in [calories, proteins, fat, carbohydrate]]
            valid = True
            
        except:
            st.error('Value must be a float or number!')
    elif option == "16-18 tahun":
        fat = st.text_input('Fat', value='85.00')
        proteins = st.text_input('Protein', value='75')
        calories = st.text_input('Kalori', value='2650')
        carbohydrate = st.text_input('Karbohidrat', value='400')

        valid = False
        try:
            calories, proteins, fat, carbohydrate = [float(val) for val in [calories, proteins, fat, carbohydrate]]
            valid = True
            
        except:
            st.error('Value must be a float or number!')
    elif option == "19-29 tahun":
        fat = st.text_input('Fat', value='75.00')
        proteins = st.text_input('Protein', value='65')
        calories = st.text_input('Kalori', value='2650')
        carbohydrate = st.text_input('Karbohidrat', value='430')

        valid = False
        try:
            calories, proteins, fat, carbohydrate = [float(val) for val in [calories, proteins, fat, carbohydrate]]
            valid = True
            
        except:
            st.error('Value must be a float or number!')
    elif option == "30-49 tahun":
        fat = st.text_input('Fat', value='70.00')
        proteins = st.text_input('Protein', value='65')
        calories = st.text_input('Kalori', value='2550')
        carbohydrate = st.text_input('Karbohidrat', value='415')

        valid = False
        try:
            calories, proteins, fat, carbohydrate = [float(val) for val in [calories, proteins, fat, carbohydrate]]
            valid = True
            
        except:
            st.error('Value must be a float or number!')
    elif option == "50-64 tahun":
        fat = st.text_input('Fat', value='60.00')
        proteins = st.text_input('Protein', value='65')
        calories = st.text_input('Kalori', value='2150')
        carbohydrate = st.text_input('Karbohidrat', value='340')

        valid = False
        try:
            calories, proteins, fat, carbohydrate = [float(val) for val in [calories, proteins, fat, carbohydrate]]
            valid = True
            
        except:
            st.error('Value must be a float or number!')
    elif option == "65-80 tahun":
        fat = st.text_input('Fat', value='50.00')
        proteins = st.text_input('Protein', value='64')
        calories = st.text_input('Kalori', value='1800')
        carbohydrate = st.text_input('Karbohidrat', value='275')

        valid = False
        try:
            calories, proteins, fat, carbohydrate = [float(val) for val in [calories, proteins, fat, carbohydrate]]
            valid = True
            
        except:
            st.error('Value must be a float or number!')
    st.markdown(f'calories, proteins, fat, carbohydrate: {(calories, proteins, fat, carbohydrate)}')

submit = st.button('Next', type='primary')
if submit:
    gizi_target = [calories, proteins, fat, carbohydrate]
    st.session_state['gizi_target'] = gizi_target
    st.switch_page("pages/nutrition_search.py")