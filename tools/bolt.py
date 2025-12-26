import streamlit as st
import math
import pandas as pd
import matplotlib.pyplot as plt

def show():
    st.title("⚪ Bolt Circle Generator")
    
    # Navigation
    if st.button("← Back to Dashboard"):
        st.session_state.current_page = 'dashboard'
        st.rerun()
    
    st.markdown("---")
    
    col_input, col_plot = st.columns([1, 2])

    with col_input:
        st.subheader("Dimensions")
        # Unique keys are crucial in Streamlit
        cx = st.number_input("Center X", value=0.0, key="bolt_cx")
        cy = st.number_input("Center Y", value=0.0, key="bolt_cy")
        dia = st.number_input("Circle Diameter", value=100.0)
        num_holes = st.number_input("Hole Count", value=6, min_value=1)
        start_angle = st.number_input("Start Angle (Deg)", value=0.0)

    # Math Engine
    radius = dia / 2.0
    coords = []

    for i in range(int(num_holes)):
        deg = start_angle + (i * (360/num_holes))
        rad = math.radians(deg)
        x = cx + (radius * math.cos(rad))
        y = cy + (radius * math.sin(rad))
        coords.append({"Hole": i+1, "X": x, "Y": y})

    df = pd.DataFrame(coords)

    # Visualization
    with col_input:
        st.dataframe(df, hide_index=True)

    with col_plot:
        fig, ax = plt.subplots()
        ax.scatter(df["X"], df["Y"], color="red", s=80)
        
        # Label holes
        for index, row in df.iterrows():
            ax.annotate(f"{int(row['Hole'])}", (row['X'], row['Y']), xytext=(5,5), textcoords='offset points')

        ref = plt.Circle((cx, cy), radius, color='blue', fill=False, linestyle='--')
        ax.add_patch(ref)
        ax.set_aspect('equal')
        ax.grid(True, linestyle=':')
        st.pyplot(fig)