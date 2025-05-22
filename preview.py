from scraper.scraper import get_market_data, get_tagged_new_listings

# Preview sample tokens
tokens = get_market_data("USDT")[:5]
print("\n🔍 Previewing 5 USDT Tokens:\n")
for t in tokens:
    print(f"{t['symbol']}: ${t['lastPrice']} ({t['priceChangePercent']}%)")

# Preview new listings
new_listings = get_tagged_new_listings()
print(f"\n🆕 {len(new_listings)} New Listings Found:\n")
for t in new_listings[:5]:
    print(f"{t['symbol']} ({t['base']}/{t['quote']}) | Tags: {t['tags']}")
