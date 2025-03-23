import streamlit as st
import common_funcs

st.title('Share Owned - Simple')
options = ['Bigha/Biswa', 'Kanal/Marla']

# Initialize session state for inputs
if "value1" not in st.session_state:
    st.session_state.value1 = ''
    st.session_state.value2 = ''
    st.session_state.value3 = ''
    st.session_state.value4 = ''
    st.session_state.value5 = ''
    st.session_state.value6 = ''

# Select measurement type
col7, col8, col9 = st.columns(3)
measurement_type = col7.selectbox('Select Measurement', options, key="measurement_type")

# Reset input fields when measurement type changes
if st.session_state.measurement_type != st.session_state.get("previous_type", ""):
    st.session_state.value1 = ''
    st.session_state.value2 = ''
    st.session_state.value3 = ''
    st.session_state.value4 = ''
    st.session_state.value5 = ''
    st.session_state.value6 = ''
    
    st.session_state.previous_type = st.session_state.measurement_type

# Define labels based on the selected type
if measurement_type == 'Bigha/Biswa':
    label1, label2, label3 = 'Enter Bigha', 'Enter Biswa', 'Enter Biswasi'
else:
    label1, label2, label3 = 'Enter Kanal', 'Enter Marla', 'Enter Sarsahi'

# First row of inputs
st.subheader('Enter Original Area')
col1, col2, col3 = st.columns(3)
value1 = col1.text_input(label1, st.session_state.value1, key="value1")
value2 = col2.text_input(label2, st.session_state.value2, key="value2")
value3 = col3.text_input(label3, st.session_state.value3, key="value3")

# Add or subtract Land
col10, col11, col12 = st.columns(3)
add_or_subtract = col10.selectbox('Add or Subtract?', ['Add', 'Subtract'])

# Second row of inputs (for adding or subtracting area)
st.subheader('Enter Area to Add or Subtract')
col4, col5, col6 = st.columns(3)
value4 = col4.text_input(label1, st.session_state.value4, key="value4")
value5 = col5.text_input(label2, st.session_state.value5, key="value5")
value6 = col6.text_input(label3, st.session_state.value6, key="value6")

# Add a submit button
submitted = st.button('Submit')

if submitted:
    try:
        # Convert text values to float for calculation
        value1 = float(value1) if value1 else 0
        value2 = float(value2) if value2 else 0
        value3 = float(value3) if value3 else 0
        value4 = float(value4) if value4 else 0
        value5 = float(value5) if value5 else 0
        value6 = float(value6) if value6 else 0

        # Calculate the final values
        FINAL_BIGHA, FINAL_BISWA, FINAL_BISWASI = common_funcs.land_add_subtract(
            measurement_type, value1, value2, value3, value4, value5, value6, add_or_subtract
        )
        st.subheader(f'{FINAL_BIGHA}-{FINAL_BISWA}-{FINAL_BISWASI}')

    except ValueError:
        st.error('Please enter valid numbers.')
