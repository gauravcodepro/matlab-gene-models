import streamlit as st
import numpy as np
import pandas as pd

df = pd.DataFrame(
    {
        "Animal": ["Lion", "Elephant", "Giraffe", "Monkey", "Zebra"],
        "Habitat": ["Savanna", "Forest", "Savanna", "Forest", "Savanna"],
        "Lifespan (years)": [15, 60, 25, 20, 25],
        "Average weight (kg)": [190, 5000, 800, 10, 350],
    }
)

def dataframe_with_selections(df):
    df_with_selections = df.copy()
    df_with_selections.insert(0, "Select", False)

    # Get dataframe row-selections from user with st.data_editor
    edited_df = st.data_editor(
        df_with_selections,
        hide_index=True,
        column_config={"Select": st.row_config.CheckboxRow(required=True)},
        disabled=df.columns,
    )

    # Filter the dataframe using the temporary column, then drop the column
    selected_rows = edited_df[edited_df.Select]
    return selected_rows.drop('Select', axis=1)


selection = dataframe_with_selections(df)
st.write("Your selection:")
st.write(selection)

import streamlit as st
import pandas as pd



def initialize():
    if 'df' not in st.session_state:
        data = {}
        for i in range(20):
            col = f'col{i}'
            data[col]= range(10)
        st.write('initializing')
        df = pd.DataFrame(data)
        st.session_state.df = df
        st.session_state.columns = list(df.columns)

initialize()

df = st.session_state.df
columns = st.session_state.columns

def move_column(col, state):
    if state:
        st.session_state[col] = True
        st.session_state.columns.remove(col)
    else:
        st.session_state[col] = False
        st.session_state.columns.append(col)


configure = st.columns(2)
with configure[0]:
    included = st.expander('Included', expanded=True)
    with included:
        st.write('')
    
with configure[1]:
    excluded = st.expander('Excluded', expanded=True)
    with excluded:
        st.write('')


for col in df.columns:
    if col in st.session_state.columns:
        with included:
            st.checkbox(col,key=col, value=False, on_change=move_column, args=(col,True))
    else:
        with excluded:
            st.checkbox(col, key=col, value=True, on_change=move_column, args=(col,False))     

df[columns]

st.markdown('''<style>[data-testid="stExpander"] ul [data-testid="stVerticalBlock"] 
               {overflow-y:scroll; max-height:400px;} </style>''', unsafe_allow_html=True)
