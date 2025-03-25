import streamlit as st
import common_funcs

st.title('Share Owned - Simple')
options = ['Bigha/Biswa', 'Kanal/Marla']

# Initialize session state for inputs
if "rows" not in st.session_state:
    st.session_state.rows = []

if "value1" not in st.session_state:
    st.session_state.value1 = ''
    st.session_state.value2 = ''
    st.session_state.value3 = ''

# Select measurement type
col7, col8, col9 = st.columns(3)
measurement_type = col7.selectbox('Select Measurement', options, key="measurement_type")

# Reset input fields when measurement type changes
if st.session_state.measurement_type != st.session_state.get("previous_type", ""):
    st.session_state.value1 = ''
    st.session_state.value2 = ''
    st.session_state.value3 = ''
    st.session_state.rows = []
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

# Add a new row button
def add_row():
    st.session_state.rows.append({"operation": "Add", "val1": '', "val2": '', "val3": ''})

def reset_values():
    st.session_state.value1 = ''
    st.session_state.value2 = ''
    st.session_state.value3 = ''
    st.session_state.rows = []
    st.rerun()

# Dynamic rows for add/subtract
st.subheader('Enter Area to Add or Subtract')

st.button("Add New Row", on_click=add_row)

for idx, row in enumerate(st.session_state.rows):
    col10, col11, col12, col13 = st.columns(4)
    row["operation"] = col10.selectbox(f'Row {idx+1}: Add or Subtract?', ['Add', 'Subtract'], index=0, key=f"op_{idx}")
    row["val1"] = col11.text_input(label1, row["val1"], key=f"val1_{idx}")
    row["val2"] = col12.text_input(label2, row["val2"], key=f"val2_{idx}")
    row["val3"] = col13.text_input(label3, row["val3"], key=f"val3_{idx}")

# Submit and Reset buttons
col_submit, col_reset = st.columns(2)
submitted = col_submit.button('Submit')
reset = col_reset.button('Reset', on_click=reset_values)

if submitted:
    try:
        # Convert text values to float
        value1 = float(value1) if value1 else 0
        value2 = float(value2) if value2 else 0
        value3 = float(value3) if value3 else 0
        
        total_big, total_bis, total_biswasi = value1, value2, value3
        
        for row in st.session_state.rows:
            val1 = float(row["val1"]) if row["val1"] else 0
            val2 = float(row["val2"]) if row["val2"] else 0
            val3 = float(row["val3"]) if row["val3"] else 0
            
            big, bis, biswasi = common_funcs.land_add_subtract(
                measurement_type, total_big, total_bis, total_biswasi, val1, val2, val3, row["operation"]
            )
            total_big, total_bis, total_biswasi = big, bis, biswasi

        st.subheader(f'{total_big}-{total_bis}-{total_biswasi}')
    
    except ValueError:
        st.error('Please enter valid numbers.')
