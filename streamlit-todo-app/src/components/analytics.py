from typing import List
import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_handler import load_todos

def render_analytics():
    """Render analytics and visualizations."""
    st.header("To-Do Analytics")
    
    todos = load_todos()
    
    if not todos:
        st.info("No to-dos to analyze yet!")
        return
    
    # Metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total To-Dos", len(todos))
    with col2:
        completed = len([t for t in todos if t["completed"]])
        st.metric("Completed", completed)
    with col3:
        st.metric("Remaining", len(todos) - completed)
    
    st.divider()
    
    # Priority distribution
    st.subheader("Priority Distribution")
    priority_data = pd.DataFrame({
        "Priority": [t["priority"] for t in todos],
    })
    priority_counts = priority_data["Priority"].value_counts().reset_index()
    priority_counts.columns = ["Priority", "Count"]
    
    fig_priority = px.bar(priority_counts, x="Priority", y="Count", title="To-Dos by Priority")
    st.plotly_chart(fig_priority, use_container_width=True)
    
    # Category distribution
    st.subheader("Category Distribution")
    categories = [t["category"] for t in todos if t["category"]]
    if categories:
        category_counts = pd.Series(categories).value_counts().reset_index()
        category_counts.columns = ["Category", "Count"]
        fig_category = px.pie(category_counts, values="Count", names="Category", title="To-Dos by Category")
        st.plotly_chart(fig_category, use_container_width=True)
    else:
        st.info("No categories assigned yet!")