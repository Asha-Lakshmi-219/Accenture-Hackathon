import streamlit as st
from ui.dashboard import Dashboard
from agents.customer_agent import CustomerAgent
from agents.product_agent import ProductAgent
from agents.recommendation_agent import RecommendationAgent

def main():
    # Initialize agents
    customer_agent = CustomerAgent()
    product_agent = ProductAgent()
    recommendation_agent = RecommendationAgent()
    
    # Initialize and render dashboard
    dashboard = Dashboard()
    dashboard.render()

if __name__ == "__main__":
    main()

""" Run application:
pip install streamlit pandas numpy scikit-learn plotly sqlalchemy
streamlit run app.py
"""