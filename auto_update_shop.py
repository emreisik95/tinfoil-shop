#!/usr/bin/env python3
"""
Auto-update Tinfoil Shop
Fetches new games and updates the shop JSON
"""
import json
import requests
from datetime import datetime

def update_shop():
    """Update shop with new games"""
    # Load existing shop
    with open('emre_ultimate_shop.json') as f:
        shop = json.load(f)

    print(f"Current games: {len(shop['files']):,}")

    # Fetch updates from Worldigital
    response = requests.get("https://free.worldigital-brasil.com/free.tfl")
    new_data = response.json()

    # Merge and deduplicate
    existing_urls = {game['url'] for game in shop['files']}

    added = 0
    for game in new_data['files']:
        if game['url'] not in existing_urls:
            shop['files'].append(game)
            added += 1

    print(f"Added {added} new games")

    # Update timestamp
    shop['success'] = f"Emre's Ultimate Game Collection - {len(shop['files']):,} games - Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}"

    # Save
    with open('emre_ultimate_shop.json', 'w') as f:
        json.dump(shop, f, indent=2)

    return added

if __name__ == '__main__':
    update_shop()
