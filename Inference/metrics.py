"""
This module contains a function to calculate the metrics for the recommendations
"""

import math

def calculate_metrics(recs, true, k):
    eps = 1e-10
    recommendations = [rec[0] for rec in recs[:k]]
    true_dict = {t[0]: t[1] for t in true}
    
    # calculate precision@k
    precision = len(set(recommendations) & set(true_dict.keys())) / k
    
    # calculate recall@k
    recall = len(set(recommendations) & set(true_dict.keys())) / len(true_dict)
    
    # calculate F1 score
    f1 = 2 * (precision * recall) / ((precision + recall) + eps) # eps to prevent division by zero
    
    # calculate NDCG@k
    dcg = 0
    idcg = 0
    
    # Calculate DCG
    for i, item in enumerate(recommendations):
        if item in true_dict:
            rel = true_dict[item]
            dcg += rel / math.log2(i + 2)
    
    # Calculate IDCG
    sorted_relevances = sorted([t[1] for t in true], reverse=True)
    for i in range(min(k, len(sorted_relevances))):
        idcg += sorted_relevances[i] / math.log2(i + 2)
    
    ndcg = dcg / (idcg + eps)
    
    return precision, recall, f1, ndcg