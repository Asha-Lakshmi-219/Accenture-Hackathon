from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class ProductAgent:
    def __init__(self):
        self.categories = {}
        self.product_vectors = {}
    
    def analyze_product(self, product_data, purchase_history):
        category = product_data['category']
        if category not in self.categories:
            self.categories[category] = []
        
        # Calculate product metrics
        total_sales = sum(1 for purchase in purchase_history 
                         if purchase['product_id'] == product_data['id'])
        avg_rating = product_data['rating']
        
        # Create product vector
        product_vector = np.array([
            product_data['price'],
            avg_rating,
            total_sales
        ])
        
        self.product_vectors[product_data['id']] = product_vector
        
        return {
            'product_id': product_data['id'],
            'popularity_score': total_sales * avg_rating,
            'category_rank': self._calculate_category_rank(product_data, total_sales)
        }
    
    def _calculate_category_rank(self, product_data, total_sales):
        category_products = self.categories[product_data['category']]
        return sorted(category_products, key=lambda x: x['total_sales']).index(total_sales) + 1