import streamlit as st

# streamlit run patwari_app.py

# Set the page layout to wide
st.set_page_config(layout="wide")

# ----PAGE SETUP----
# Define navigation and multipage layout as you've already done


share_owned_simple_page = st.Page(
    page='views/share_owned_simple.py',
    title='Share Owned Simple',
)


land_add_subtract_page = st.Page(
    page='views/land_add_subtract.py',
    title='Land Add Subtract',
)


# convert_to_share_page = st.Page(
#     page='views/convert_to_share.py',
#     title='Convert to Share',
# )


# create_tatima_page = st.Page(
#     page='views/create_tatima.py',
#     title='Create Tatima',
# )


# land_conversion_page = st.Page(
#     page='views/land_conversion.py',
#     title='Land Conversion',
# )


# share_owned_expert_page = st.Page(
#     page='views/share_owned_expert.py',
#     title='Share Owned Expert',
# )


# find_area_page = st.Page(
#     page='views/find_area.py',
#     title='Find Area',
# )




# ----PAGE NAVIGATION WITH SECTIONS----
pg = st.navigation(
    {
        'ＳＥＬＥＣＴ ＰＡＧＥ': [share_owned_simple_page,land_add_subtract_page]
        }
)
# pg = st.navigation(
#     {
#         'ＳＥＬＥＣＴ ＰＡＧＥ': [share_owned_simple_page,land_add_subtract_page,share_owned_expert_page,find_area_page,convert_to_share_page,create_tatima_page,land_conversion_page]
#         }
# )


# ----RUN NAVIGATION----
pg.run()
