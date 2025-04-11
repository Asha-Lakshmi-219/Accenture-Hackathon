import numpy as np
from sklearn.cluster import KMeans

class CustomerAgent:
    def __init__(self):
        self.segments = ['new_visitor', 'occasional_buyer', 'frequent_buyer', 'vip']
    
    def analyze_customer(self, customer_data, purchase_history):
        # Calculate customer metrics
        total_purchases = len(purchase_history)
        total_spent = sum(purchase['amount'] for purchase in purchase_history)
        avg_purchase = total_spent / total_purchases if total_purchases > 0 else 0
        
        # Determine customer segment
        if total_purchases == 0:
            segment = 'new_visitor'
        elif total_purchases < 5:
            segment = 'occasional_buyer'
        elif total_purchases < 10:
            segment = 'frequent_buyer'
        else:
            segment = 'vip'
            
        return {
            'customer_id': customer_data['id'],
            'segment': segment,
            'total_spent': total_spent,
            'avg_purchase': avg_purchase,
            'purchase_frequency': total_purchases
        }