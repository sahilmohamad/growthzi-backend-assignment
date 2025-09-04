conversion_rates = {
    "US": {"symbol": "$", "rate": 1},      
    "IN": {"symbol": "₹", "rate": 80},     
    "EU": {"symbol": "€", "rate": 0.9},    
    "UK": {"symbol": "£", "rate": 0.8},    
}

def get_price_in_currency(base_price_usd, country_code):
    country_code = country_code.upper()
    if country_code not in conversion_rates:
        country_code = "US"  

    rate = conversion_rates[country_code]["rate"]
    symbol = conversion_rates[country_code]["symbol"]
    local_price = base_price_usd * rate

    return {
        "product": "Pro Plan",
        "price_usd": f"${base_price_usd}",
        "price_local": f"{symbol}{local_price:.2f}",
        "currency": country_code
    }
