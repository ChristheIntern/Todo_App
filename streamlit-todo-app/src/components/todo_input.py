import streamlit as st
from utils.data_handler import load_todos, save_todos

def render_todo_input():
    """Render the to-do input form."""
    st.header("Create a New To-Do")
    
    with st.form("todo_form"):
        # Input widgets
        todo_title = st.text_input("📌 To-Do Title", placeholder="Enter a task...")
        
        col1, col2 = st.columns(2)
        with col1:
            todo_priority = st.selectbox("⚡ Priority", ["Low", "Medium", "High"])
        with col2:
            todo_category = st.text_input("🏷️ Category", placeholder="e.g., Work, Personal...")
        
        submitted = st.form_submit_button("➕ Add To-Do", use_container_width=True)
        
        if submitted:
            if todo_title.strip():
                todos = load_todos()
                new_todo = {
                    "id": len(todos) + 1,
                    "title": todo_title,
                    "priority": todo_priority,
                    "category": todo_category,
                    "completed": False
                }
                todos.append(new_todo)
                save_todos(todos)
                st.success("✅ To-Do added successfully!")
                st.rerun()
            else:
                st.error("❌ Please enter a to-do title!")