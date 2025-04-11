import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

class Dashboard:
    def __init__(self):
        st.set_page_config(
            page_title="Smart Shopping AI",
            layout="wide"
        )
    
    def render(self):
        st.title("Smart Shopping AI Dashboard")
        
        # Sidebar for navigation
        self.render_sidebar()
        
        # Main content
        tab1, tab2, tab3 = st.tabs([
            "Product Recommendations",
            "Customer Analytics",
            "Product Analytics"
        ])
        
        with tab1:
            self.render_recommendations()
        
        with tab2:
            self.render_customer_analytics()
            
        with tab3:
            self.render_product_analytics()
    
    def render_sidebar(self):
        st.sidebar.title("Customer Profile")
        customer_id = st.sidebar.selectbox(
            "Select Customer",
            options=["Customer 1", "Customer 2", "Customer 3"]
        )
        
        st.sidebar.divider()
        st.sidebar.subheader("Filters")
        category = st.sidebar.multiselect(
            "Product Categories",
            options=["Electronics", "Clothing", "Books", "Home"]
        )
        price_range = st.sidebar.slider(
            "Price Range",
            min_value=0,
            max_value=1000,
            value=(0, 500)
        )
    
    def render_recommendations(self):
        st.header("Personalized Recommendations")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            self.render_product_card(
                "Product 1",
                "Electronics",
                299.99,
                4.5
            )
        
        with col2:
            self.render_product_card(
                "Product 2",
                "Clothing",
                49.99,
                4.8
            )
            
        with col3:
            self.render_product_card(
                "Product 3",
                "Books",
                19.99,
                4.2
            )
    
    def render_product_card(self, name, category, price, rating):
        st.card(
            f"""
            ### {name}
            **Category:** {category}  
            **Price:** ${price:.2f}  
            **Rating:** {'⭐' * int(rating)} ({rating})
            """
        )
    
    def render_customer_analytics(self):
        st.header("Customer Analytics")
        
        # Customer segments pie chart
        segments_data = pd.DataFrame({
            'Segment': ['New', 'Occasional', 'Frequent', 'VIP'],
            'Count': [100, 250, 150, 50]
        })
        
        fig = px.pie(
            segments_data,
            values='Count',
            names='Segment',
            title='Customer Segments Distribution'
        )
        st.plotly_chart(fig)
    
    def render_product_analytics(self):
        st.header("Product Analytics")
        
        # Product performance chart
        performance_data = pd.DataFrame({
            'Product': ['P1', 'P2', 'P3', 'P4', 'P5'],
            'Sales': [100, 150, 80, 200, 120]
        })
        
        fig = px.bar(
            performance_data,
            x='Product',
            y='Sales',
            title='Product Performance'
        )
        st.plotly_chart(fig)