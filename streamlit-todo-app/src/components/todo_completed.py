import streamlit as st
from utils.data_handler import load_todos, save_todos

def render_completed_todos():
    """Render completed to-dos display."""
    st.header("Completed To-Dos")
    
    todos = load_todos()
    completed_todos = [t for t in todos if t["completed"]]
    
    if not completed_todos:
        st.info("📭 No completed to-dos yet. Start completing some tasks!")
        return
    
    # Filter options
    col1, col2 = st.columns(2)
    with col1:
        categories = list(set([t["category"] for t in completed_todos if t["category"]]))
        filter_category = st.multiselect("🏷️ Filter by Category", categories, key="completed_cat")
    with col2:
        filter_priority = st.multiselect("⚡ Filter by Priority", ["Low", "Medium", "High"], key="completed_pri")
    
    # Apply filters
    filtered_todos = completed_todos
    if filter_category:
        filtered_todos = [t for t in filtered_todos if t["category"] in filter_category]
    if filter_priority:
        filtered_todos = [t for t in filtered_todos if t["priority"] in filter_priority]
    
    # Display completed to-dos
    for todo in filtered_todos:
        priority_emoji = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}
        priority_color = {"High": "priority-high", "Medium": "priority-medium", "Low": "priority-low"}
        
        col1, col2, col3 = st.columns([4, 1, 1])
        
        with col1:
            st.markdown(f"""
                <div class="todo-card todo-completed">
                    <s><strong>{todo['title']}</strong></s><br>
                    <small>Category: {todo['category'] or 'Uncategorized'} | 
                    <span class="{priority_color[todo['priority']]}">{priority_emoji[todo['priority']]} {todo['priority']}</span></small>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            if st.button("↩️", key=f"undo_{todo['id']}", help="Mark as incomplete"):
                todo["completed"] = False
                save_todos(todos)
                st.rerun()
        
        with col3:
            if st.button("🗑️", key=f"delete_completed_{todo['id']}", help="Delete"):
                todos.remove(todo)
                save_todos(todos)
                st.rerun()
    
    st.caption(f"✅ {len(filtered_todos)} completed to-dos")