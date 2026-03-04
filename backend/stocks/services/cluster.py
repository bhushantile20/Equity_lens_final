import pandas as pd
from sklearn.cluster import KMeans

def apply_kmeans_clustering(df: pd.DataFrame) -> pd.DataFrame:
    """
    Applies KMeans clustering to the given DataFrame.
    Features: pe_ratio, volatility_ratio, price_range.
    Adds a 'cluster' column to the DataFrame in place.
    """
    if len(df) < 3:
        # Not enough data to cluster into 3 groups reliably, just return 0
        df['cluster'] = 0
        return df
        
    features = ['pe_ratio', 'volatility_ratio', 'price_range']
    
    # Handle missing values by filling with median or 0 before clustering
    X = df[features].copy()
    X.fillna(X.median(), inplace=True)
    X.fillna(0, inplace=True)
    
    kmeans = KMeans(n_clusters=3, random_state=42, n_init='auto')
    try:
        df['cluster'] = kmeans.fit_predict(X)
    except Exception:
        # Fallback if clustering fails
        df['cluster'] = 0
        
    return df
