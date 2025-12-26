import streamlit as st
import pandas as pd

def show():
    st.title("🔩 Tap & Drill Chart")
    
    # Navigation
    if st.button("← Back to Dashboard"):
        st.session_state.current_page = 'dashboard'
        st.rerun()
    
    st.markdown("---")

    # 1. The Database (Dictionary)
    # Format: "Name": [Pitch/TPI, Cut Drill, Form Drill, Clearance]
    # Metric: Dimensions in mm
    # Imperial: Dimensions in inches (converted to mm for display usually, but machinists stick to drill charts)
    
    data_metric = {
        "M3 x 0.5":   {"p": 0.5,  "cut": 2.5,  "form": 2.8,  "clear": 3.4},
        "M4 x 0.7":   {"p": 0.7,  "cut": 3.3,  "form": 3.7,  "clear": 4.5},
        "M5 x 0.8":   {"p": 0.8,  "cut": 4.2,  "form": 4.6,  "clear": 5.5},
        "M6 x 1.0":   {"p": 1.0,  "cut": 5.0,  "form": 5.5,  "clear": 6.6},
        "M8 x 1.25":  {"p": 1.25, "cut": 6.8,  "form": 7.4,  "clear": 9.0},
        "M10 x 1.5":  {"p": 1.5,  "cut": 8.5,  "form": 9.3,  "clear": 11.0},
        "M12 x 1.75": {"p": 1.75, "cut": 10.2, "form": 11.2, "clear": 13.5},
        "M16 x 2.0":  {"p": 2.0,  "cut": 14.0, "form": 15.1, "clear": 17.5},
        "M20 x 2.5":  {"p": 2.5,  "cut": 17.5, "form": 18.9, "clear": 22.0},
    }

    # 2. The Selector
    st.subheader("Select Thread Size")
    
    # We use a selectbox for speed
    target = st.selectbox("Thread", options=data_metric.keys())
    
    # 3. Fetch Data
    info = data_metric[target]
    
    # 4. The Display (Big Cards)
    st.markdown("### 🎯 Drill Sizes (mm)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Standard Cutting Tap (Making chips)
        st.info("🔪 **CUT TAP** (Standard)")
        st.metric(label="Drill Diameter", value=f"{info['cut']} mm")
        st.caption(f"Pitch: {info['p']} mm")
        
    with col2:
        # Form/Roll Tap (Pushing material, no chips)
        st.success("🔨 **FORM TAP** (Roll)")
        st.metric(label="Drill Diameter", value=f"{info['form']} mm")
        st.caption("Requires specific Roll Tap")

    st.markdown("---")
    st.markdown("### 📐 Clearance Hole")
    st.metric(label="Through Hole (Loose Fit)", value=f"{info['clear']} mm")