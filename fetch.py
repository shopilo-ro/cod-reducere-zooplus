#!/usr/bin/env python3
"""
Fetch coduri de reducere Zooplus de pe shopilo.ro
Sursa: https://shopilo.ro/magazin/zooplus.ro
"""

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

SHOPILO_URL = "https://shopilo.ro/magazin/zooplus.ro"
STORE_NAME = "Zooplus"


def fetch_coupons(url=SHOPILO_URL):
    """Returneaza lista de cupoane active pentru Zooplus de pe shopilo.ro"""
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; coupon-fetcher/1.0; +https://github.com/shopilo-ro/cod-reducere-zooplus)"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Eroare la fetch: {e}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    coupons = []

    for item in soup.select(".coupon-item, [data-coupon], .offer-card"):
        code_el     = item.select_one("[data-code], .coupon-code, .code")
        discount_el = item.select_one(".discount, .percent, .amount")
        desc_el     = item.select_one(".title, .description, h3")
        expires_el  = item.select_one(".expires, .expiry, [data-expires]")

        coupon = {
            "store":      STORE_NAME,
            "code":       code_el.get_text(strip=True)     if code_el     else None,
            "discount":   discount_el.get_text(strip=True) if discount_el else None,
            "description":desc_el.get_text(strip=True)     if desc_el     else None,
            "expires":    expires_el.get_text(strip=True)  if expires_el  else None,
            "source":     SHOPILO_URL,
            "fetched_at": datetime.now().isoformat()
        }

        if coupon["description"]:
            coupons.append(coupon)

    return coupons


if __name__ == "__main__":
    print(f"Fetching coduri reducere {STORE_NAME} de pe shopilo.ro...\n")
    coupons = fetch_coupons()

    if coupons:
        print(json.dumps(coupons, ensure_ascii=False, indent=2))
        print(f"\nTotal: {len(coupons)} cupoane gasite")
    else:
        print(f"Nu s-au gasit cupoane. Vezi lista completa la: {SHOPILO_URL}")
