import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np

# AI CODE 
def show():
    st.title("⏬ Countersink Depth Calculator")
    
    if st.button("← Back to Dashboard"):
        st.session_state.current_page = 'dashboard'
        st.rerun()
    st.markdown("---")

    col_input, col_plot = st.columns([1, 2])

    with col_input:
        st.subheader("Tool & Hole Params")
        
        # Inputs
        tool_angle = st.selectbox("Tool Angle (Included)", [90, 82, 60, 100, 120])
        hole_dia = st.number_input("Existing Hole Diameter (mm)", value=10.0, min_value=0.0)
        target_dia = st.number_input("Target Chamfer Diameter (mm)", value=12.0, min_value=0.0)
        
        # Logic
        # 1. Calc the radius difference (one side)
        rad_diff = (target_dia - hole_dia) / 2
        
        # 2. Calc Depth
        # Tan(theta) = Opp / Adj
        # We know Opposite (Rad Diff) and Angle (Half of included)
        # Depth (Adj) = Opposite / Tan(theta)
        
        half_angle_rad = math.radians(tool_angle / 2)
        
        if target_dia > hole_dia:
            depth = rad_diff / math.tan(half_angle_rad)
            valid = True
        else:
            depth = 0.0
            valid = False
            st.error("Target Diameter must be larger than Hole Diameter")

    # Outputs
    with col_input:
        if valid:
            st.markdown("### 🏁 Result")
            st.success(f"**Z-Depth:** {depth:.3f} mm")
            st.info(f"**From Surface:** Z -{depth:.3f}")
            st.caption("Assuming Z0.0 is the top surface")

    # Visualizer
    with col_plot:
        if valid:
            fig, ax = plt.subplots()
            
            # 1. Draw the Material (Gray blocks)
            # Left Block
            ax.fill_between([-20, -hole_dia/2], [0, 0], [-20, -20], color='gray', alpha=0.5)
            # Right Block
            ax.fill_between([hole_dia/2, 20], [0, 0], [-20, -20], color='gray', alpha=0.5)
            
            # 2. Draw the Tool Profile (Red Dashed)
            # We calculate the triangle points based on depth and angle
            # Tip is at (0, -depth + offset). Let's put Z0 at the top surface.
            
            # We want the tool to touch the "Target Diameter" at Z=0
            # So the tip is actually BELOW Z0 by the amount we calculated.
            tip_z = -depth
            
            # Draw arbitrary tool width (large enough to see)
            tool_w = target_dia + 10
            tool_h = (tool_w / 2) / math.tan(half_angle_rad)
            
            # Tool coordinates (V shape)
            tool_x = [-tool_w/2, 0, tool_w/2]
            tool_y = [tip_z + tool_h, tip_z, tip_z + tool_h]
            
            ax.plot(tool_x, tool_y, 'r--', linewidth=2, label=f"{tool_angle}° Tool")
            ax.plot([0], [tip_z], 'rx', markersize=10, label="Tool Tip")
            
            # Draw Centerline
            ax.axvline(0, color='k', linestyle='-.', alpha=0.3)
            
            # Labels
            ax.annotate(f"Z -{depth:.3f}", xy=(0.5, tip_z), xytext=(5, 0), 
                        textcoords="offset points", color='red', fontweight='bold')
            
            ax.set_aspect('equal')
            ax.set_ylim(tip_z - 5, 5)
            ax.set_xlim(-target_dia, target_dia)
            ax.legend(loc='upper right')
            ax.grid(True, alpha=0.3)
            ax.set_title("Cross Section View")
            
            st.pyplot(fig)