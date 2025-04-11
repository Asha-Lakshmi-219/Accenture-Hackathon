from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class RecommendationAgent:
    def __init__(self):
        self.similarity_threshold = 0.7
    
    def generate_recommendations(self, customer_profile, product_catalog, purchase_history):
        if customer_profile['segment'] == 'new_visitor':
            return self._recommend_for_new_visitor(product_catalog)
        else:
            return self._recommend_for_existing_customer(
                customer_profile, 
                product_catalog, 
                purchase_history
            )
    
    def _recommend_for_new_visitor(self, product_catalog):
        # Recommend popular products
        sorted_products = sorted(
            product_catalog, 
            key=lambda x: x['rating'] * x['total_sales'],
            reverse=True
        )
        return sorted_products[:5]
    
    def _recommend_for_existing_customer(self, customer_profile, product_catalog, purchase_history):
        # Get customer's preferred categories
        purchased_categories = set(
            purchase['category'] for purchase in purchase_history
        )
        
        # Find similar products
        recommendations = []
        for product in product_catalog:
            if product['category'] in purchased_categories:
                similarity_score = self._calculate_similarity(
                    customer_profile,
                    product,
                    purchase_history
                )
                if similarity_score > self.similarity_threshold:
                    recommendations.append({
                        'product': product,
                        'score': similarity_score
                    })
        
        # Sort by similarity score
        recommendations.sort(key=lambda x: x['score'], reverse=True)
        return [r['product'] for r in recommendations[:5]]
    
    def _calculate_similarity(self, customer_profile, product, purchase_history):
        # Calculate similarity based on various factors
        category_match = product['category'] in set(
            p['category'] for p in purchase_history
        )
        price_range_match = self._is_in_price_range(
            product['price'],
            purchase_history
        )
        
        similarity = (
            0.4 * category_match +
            0.3 * price_range_match +
            0.3 * (product['rating'] / 5.0)
        )
        
        return similarity
    
    def _is_in_price_range(self, price, purchase_history):
        if not purchase_history:
            return True
        avg_purchase = sum(p['amount'] for p in purchase_history) / len(purchase_history)
        return 0.5 <= price / avg_purchase <= 1.5