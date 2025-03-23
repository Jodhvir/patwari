import streamlit as st
import common_funcs

st.title('Share Owned - Simple')
options = ['Bigha/Biswa', 'Kanal/Marla']

# Initialize session state for inputs
if "value1" not in st.session_state:
    st.session_state.value1 = ''
    st.session_state.value2 = ''
    st.session_state.value3 = ''
    st.session_state.ratio_nr = ''
    st.session_state.ratio_dr = ''

# Reset input fields function
def reset_fields():
    st.session_state.value1 = ''
    st.session_state.value2 = ''
    st.session_state.value3 = ''
    st.session_state.ratio_nr = ''
    st.session_state.ratio_dr = ''

# Select measurement type
col7, col8, col9 = st.columns(3)
measurement_type = col7.selectbox('Select Measurement', options, key="measurement_type")

# Reset input fields when measurement type changes
if st.session_state.measurement_type != st.session_state.get("previous_type", ""):
    reset_fields()
    st.session_state.previous_type = st.session_state.measurement_type

# Define labels based on the selected type
if measurement_type == 'Bigha/Biswa':
    label1, label2, label3 = 'Enter Bigha', 'Enter Biswa', 'Enter Biswasi'
else:
    label1, label2, label3 = 'Enter Kanal', 'Enter Marla', 'Enter Sarsahi'

# First row of inputs
col1, col2, col3 = st.columns(3)
value1 = col1.text_input(label1, st.session_state.value1, key="value1")
value2 = col2.text_input(label2, st.session_state.value2, key="value2")
value3 = col3.text_input(label3, st.session_state.value3, key="value3")

# Second row of inputs (for ratio)
col4, col5, col6 = st.columns(3)
ratio_nr = col4.text_input('Enter Ratio Numerator', st.session_state.ratio_nr, key="ratio_nr")
ratio_dr = col5.text_input('Enter Ratio Denominator', st.session_state.ratio_dr, key="ratio_dr")

# Add Submit and Reset buttons
col_submit, col_reset = st.columns(2)
with col_submit:
    submitted = st.button('Submit')

with col_reset:
    reset = st.button('Reset', on_click=reset_fields)

# Handle Submit button click
if submitted:
    try:
        # Convert text values to float for calculation
        value1 = float(value1) if value1 else 0
        value2 = float(value2) if value2 else 0
        value3 = float(value3) if value3 else 0
        ratio_nr = float(ratio_nr) if ratio_nr else 1  # Default to 1 if empty
        ratio_dr = float(ratio_dr) if ratio_dr else 1  # Default to 1 if empty

        # Calculate the final values
        FINAL_BIGHA, FINAL_BISWA, FINAL_BISWASI = common_funcs.calculate_individual_share(
            measurement_type, value1, value2, value3, ratio_nr, ratio_dr
        )
        st.subheader(f'{FINAL_BIGHA}-{FINAL_BISWA}-{FINAL_BISWASI}')

    except ValueError:
        st.error('Please enter valid numbers.')
