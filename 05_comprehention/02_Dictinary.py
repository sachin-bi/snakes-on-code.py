

chai_price_inr = {
    "masala chai": 81,
    "lemon chai": 120,
    "black chai": 200,
}

chai_price_usd = { key:val/80 for key, val in chai_price_inr.items()}

print(f"result dict.: {chai_price_usd}")
