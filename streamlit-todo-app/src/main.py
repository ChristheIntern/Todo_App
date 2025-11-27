import sys
from pathlib import Path

# Add src directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

import streamlit as st
from components.todo_input import render_todo_input
from components.todo_display import render_todo_display
from components.todo_completed import render_completed_todos
from components.analytics import render_analytics

# Initialize the Streamlit app
st.set_page_config(page_title="To-Do List", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for better styling
st.markdown("""
    <style>
        .main-title {
            text-align: center;
            color: #2E86AB;
            font-size: 2.5em;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .todo-card {
            background-color: #F0F4F8;
            padding: 15px;
            border-radius: 10px;
            border-left: 5px solid #2E86AB;
            margin: 10px 0;
        }
        .todo-completed {
            background-color: #E8F5E9;
            border-left-color: #4CAF50;
        }
        .priority-high {
            color: #D32F2F;
            font-weight: bold;
        }
        .priority-medium {
            color: #F57C00;
            font-weight: bold;
        }
        .priority-low {
            color: #388E3C;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📝 To-Do List Application</div>', unsafe_allow_html=True)

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["➕ Add To-Do", "📋 Active To-Dos", "✅ Completed To-Dos", "📊 Analytics"])

with tab1:
    render_todo_input()

with tab2:
    render_todo_display()

with tab3:
    render_completed_todos()

with tab4:
    render_analytics()