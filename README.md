# Cod reducere Zooplus — fetch automat de pe shopilo.ro

Modul Python pentru fetch automat de **coduri de reducere Zooplus** de pe [shopilo.ro](https://shopilo.ro/magazin/zooplus.ro). Returneaza **cupoane Zooplus** active in format JSON, gata de integrat intr-un bot Telegram, extensie de browser sau orice alt tool.

**Pagina live:** [shopilo-ro.github.io/cod-reducere-zooplus](https://shopilo-ro.github.io/cod-reducere-zooplus/)

![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue) ![License MIT](https://img.shields.io/badge/license-MIT-green)

## Instalare

```bash
pip install requests beautifulsoup4
git clone https://github.com/shopilo-ro/cod-reducere-zooplus
cd cod-reducere-zooplus
python fetch.py
```

## Output exemplu

```json
[
  {
    "store": "Zooplus",
    "code": "SHOPILO10",
    "discount": "10%",
    "description": "10% reducere la prima comanda",
    "expires": "2026-10-02",
    "source": "https://shopilo.ro/magazin/zooplus.ro"
  }
]
```

## Cupoane Zooplus disponibile

| Reducere | Descriere | Sursa |
|----------|-----------|-------|
| 10% | 10% reducere la prima comanda | [shopilo.ro](https://shopilo.ro/magazin/zooplus.ro) |

Codurile active: **[shopilo.ro/magazin/zooplus.ro](https://shopilo.ro/magazin/zooplus.ro)**

## Intrebari frecvente

### Cum folosesc un cod de reducere Zooplus?
Copiaza codul din tabelul de mai sus sau de pe [shopilo.ro](https://shopilo.ro/magazin/zooplus.ro), adauga produsele in cos pe Zooplus, si introdu codul la checkout in campul dedicat.

### Cat timp sunt valabile cupoanele Zooplus?
Fiecare cupon are data de expirare afisata in coloana "Expira". Scriptul fetch.py returneaza doar cupoanele active la momentul rularii.

### Unde gasesc cele mai noi voucher-uri Zooplus?
Pagina [shopilo.ro/magazin/zooplus.ro](https://shopilo.ro/magazin/zooplus.ro) este actualizata zilnic cu cele mai noi cod reducere Zooplus, voucher Zooplus si cupon promotional Zooplus.

### Codul nu functioneaza. Ce fac?
Verifica data de expirare si conditiile (valoare minima cos, produse eligibile). Unele coduri sunt valabile doar in aplicatia mobila sau pentru prima comanda.

## Despre Zooplus

Zooplus este unul dintre magazinele online populare. Gasesti pe [shopilo.ro](https://shopilo.ro/magazin/zooplus.ro) cele mai bune cod reducere Zooplus, cupoane Zooplus verificate si voucher Zooplus active, actualizate zilnic.

## Instalare npm

```bash
npm install cod-reducere-zooplus
```

```javascript
const { fetchCoupons } = require('cod-reducere-zooplus');
fetchCoupons().then(data => console.log(data));
```

## Licenta

MIT — date sursa de pe [shopilo.ro](https://shopilo.ro)
