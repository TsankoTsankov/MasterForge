import streamlit as st
from tools import hex, bolt, taps

st.set_page_config(page_title="MasterForge", page_icon="⚙️", layout="wide")

if 'current_page' not in st.session_state:
    st.session_state.current_page = 'dashboard'

def show_dashboard():
    st.title("🏭 Machine Shop Floor")
    st.markdown("### Tool Select")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("⚪ Bolt Circle")
        if st.button("Open Generator", key="btn_bolt"):
            st.session_state.current_page = 'bolt'
            st.rerun()
        st.success("🔩 Tap & Drill Chart")
        if st.button("Open Chart", key="btn_taps"):
            st.session_state.current_page = 'taps'
            st.rerun()

    with col2:
        st.info("⬡ Hexagon Geometry")
        if st.button("Open Hex Tool", key="btn_hex"):
            st.session_state.current_page = 'hex'
            st.rerun()
            
    with col3:
        st.warning("⚡ Feeds & Speeds")
        st.caption("Under Construction")

if st.session_state.current_page == 'dashboard':
    show_dashboard()
elif st.session_state.current_page == 'bolt':
    bolt.show()
elif st.session_state.current_page == 'hex':
    hex.show()
elif st.session_state.current_page == 'taps':
    taps.show()
