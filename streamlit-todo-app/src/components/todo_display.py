import streamlit as st
from utils.data_handler import load_todos, save_todos

def render_todo_display():
    """Render active to-do display and management interface."""
    st.header("Active To-Dos")
    
    todos = load_todos()
    active_todos = [t for t in todos if not t["completed"]]
    
    if not active_todos:
        st.info("🎉 No active to-dos! You're all caught up!")
        return
    
    # Filter options
    col1, col2 = st.columns(2)
    with col1:
        categories = list(set([t["category"] for t in active_todos if t["category"]]))
        filter_category = st.multiselect("🏷️ Filter by Category", categories, key="active_cat")
    with col2:
        filter_priority = st.multiselect("⚡ Filter by Priority", ["Low", "Medium", "High"], key="active_pri")
    
    # Apply filters
    filtered_todos = active_todos
    if filter_category:
        filtered_todos = [t for t in filtered_todos if t["category"] in filter_category]
    if filter_priority:
        filtered_todos = [t for t in filtered_todos if t["priority"] in filter_priority]
    
    # Display to-dos
    for todo in filtered_todos:
        priority_emoji = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}
        priority_color = {"High": "priority-high", "Medium": "priority-medium", "Low": "priority-low"}
        
        col1, col2, col3, col4 = st.columns([4, 1, 1, 1])
        
        with col1:
            st.markdown(f"""
                <div class="todo-card">
                    <strong>{todo['title']}</strong><br>
                    <small>Category: {todo['category'] or 'Uncategorized'} | 
                    <span class="{priority_color[todo['priority']]}">{priority_emoji[todo['priority']]} {todo['priority']}</span></small>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            if st.button("✓", key=f"complete_{todo['id']}", help="Mark as complete"):
                todo["completed"] = True
                save_todos(todos)
                st.rerun()
        
        with col3:
            if st.button("✏️", key=f"edit_{todo['id']}", help="Edit"):
                st.info("Edit feature coming soon!")
        
        with col4:
            if st.button("🗑️", key=f"delete_{todo['id']}", help="Delete"):
                todos.remove(todo)
                save_todos(todos)
                st.rerun()
    
    st.caption(f"📌 Showing {len(filtered_todos)} of {len(active_todos)} active to-dos")