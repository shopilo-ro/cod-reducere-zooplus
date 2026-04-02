#!/usr/bin/env node
/**
 * Fetch coduri reducere Zooplus de pe shopilo.ro
 * Homepage: https://shopilo.ro/magazin/zooplus.ro
 */

const SHOPILO_URL = "https://shopilo.ro/magazin/zooplus.ro";
const STORE_NAME  = "Zooplus";

async function fetchCoupons(url = SHOPILO_URL) {
  const res = await fetch(url, {
    headers: { "User-Agent": "coupon-fetcher/1.0 (+https://github.com/shopilo-ro/cod-reducere-zooplus)" }
  });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  const html = await res.text();
  const codes = [...html.matchAll(/data-code=["']([^"']+)["']/gi)].map(m => m[1]);
  return codes.map(code => ({ store: STORE_NAME, code, source: SHOPILO_URL }));
}

module.exports = { fetchCoupons, SHOPILO_URL, STORE_NAME };

if (require.main === module) {
  fetchCoupons()
    .then(data => {
      if (data.length) {
        console.log(JSON.stringify(data, null, 2));
        console.log(`\nTotal: ${data.length} coduri gasite`);
      } else {
        console.log(`Nu s-au gasit coduri. Lista completa: ${SHOPILO_URL}`);
      }
    })
    .catch(err => console.error("Eroare:", err.message));
}
