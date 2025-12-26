import streamlit as st
from tools import hex, bolt, taps, countersink

st.set_page_config(page_title="MasterForge", page_icon="⚙️", layout="wide")

if 'current_page' not in st.session_state:
    st.session_state.current_page = 'dashboard'

def show_dashboard():
    st.title("🏭 Machine Shop Floor")
    st.markdown("### Tool Select")
    
    # We define 3 columns. We can stack multiple widgets in them.
    col1, col2, col3 = st.columns(3)
    
    # COLUMN 1: Bolt Circle & Taps
    with col1:
        st.info("⚪ Bolt Circle")
        if st.button("Open Generator", key="btn_bolt"):
            st.session_state.current_page = 'bolt'
            st.rerun()
            
        st.markdown("---") # Visual separator
        
        st.success("🔩 Tap & Drill Chart")
        if st.button("Open Chart", key="btn_taps"):
            st.session_state.current_page = 'taps'
            st.rerun()

    # COLUMN 2: Hex Geometry & Countersink
    with col2:
        st.info("⬡ Hexagon Geometry")
        if st.button("Open Hex Tool", key="btn_hex"):
            st.session_state.current_page = 'hex'
            st.rerun()
            
        st.markdown("---") # Visual separator

        st.info("⏬ Countersink Calc")
        if st.button("Open Depth Calc", key="btn_csink"):
            st.session_state.current_page = 'csink'
            st.rerun()
            
    # COLUMN 3: Feeds & Speeds (Placeholder)
    with col3:
        st.warning("⚡ Feeds & Speeds")
        st.caption("Under Construction")

# Navigation Logic
if st.session_state.current_page == 'dashboard':
    show_dashboard()
elif st.session_state.current_page == 'bolt':
    bolt.show()
elif st.session_state.current_page == 'hex':
    hex.show()
elif st.session_state.current_page == 'taps':
    taps.show()
elif st.session_state.current_page == 'csink':
    countersink.show()