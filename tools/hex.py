import streamlit as st
import math
import pandas as pd
import matplotlib.pyplot as plt

def show():
    st.title("⬡ Hexagon: Flats to Points")
    
    if st.button("← Back to Dashboard"):
        st.session_state.current_page = 'dashboard'
        st.rerun() 

    st.markdown("---")
    
    col_input, col_plot = st.columns([1, 2])
    
    with col_input:
        st.subheader("Dimensions")
        cx = st.number_input("Center X", value=0.0, key="hex_cx")
        cy = st.number_input("Center Y", value=0.0, key="hex_cy")
        af = st.number_input("Across Flats (mm)", value=20.0, step=1.0)
        orientation = st.number_input("Orientation (Deg)", value=0.0, step=30.0)

    # Math Engine
    radius = af / math.sqrt(3)
    coords = []
    
    for i in range(7):
        deg = orientation + (i * 60)
        rad = math.radians(deg)
        x = cx + (radius * math.cos(rad))
        y = cy + (radius * math.sin(rad))
        coords.append({"X": x, "Y": y})
        
    df = pd.DataFrame(coords)
    
    # Visualization
    with col_input:
        st.info(f"**Corner Radius:** {radius:.3f} mm")
        st.dataframe(df.iloc[:6], hide_index=True)

    with col_plot:
        fig, ax = plt.subplots()
        ax.plot(df["X"], df["Y"], 'b-o', linewidth=2)
        
        for index, row in df.iloc[:6].iterrows():
             ax.annotate(f"{index+1}", (row['X'], row['Y']), xytext=(10,10), textcoords='offset points')

        circle = plt.Circle((cx, cy), af/2, color='green', fill=False, linestyle='--')
        ax.add_patch(circle)
        
        ax.set_aspect('equal')
        ax.grid(True)
        st.pyplot(fig)