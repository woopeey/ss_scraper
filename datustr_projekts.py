import requests
from bs4 import BeautifulSoup

brand = input("marka: ").strip().lower()
model = input("modelis (raksti 0, ja nav svarīgi): ").strip().lower()
kartsana = input("kārtot pēc cenas (asc/desc): ").strip().lower()

if kartsana not in ["asc", "desc"]:
    print("jāievada 'asc' vai 'desc'.")
    exit()

HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36", 
           "accept": "*/*"}

if model == "0":
    BASE_URL = f"https://www.ss.com/lv/transport/cars/{brand}/"
else:
    BASE_URL = f"https://www.ss.com/lv/transport/cars/{brand}/{model}"

URL = BASE_URL + "page1.html"

try:
    response = requests.get(URL, headers=HEADERS)
    response.raise_for_status()
except Exception as e:
    print(f"Neizdevās ielādēt lapu: {e}")
    exit()

soup = BeautifulSoup(response.text, "lxml")

try:
    rows = soup.find("form").find("table", {"align": "center"}).find_all("tr")[1:-1]
except AttributeError:
    print("Lapas struktūra nav atrasta.")
    exit()

sludinajumi = []
for row in rows:
    try:
        cols = row.find_all("td")
        title = cols[2].text.strip()
        modelis = cols[3].text.strip()
        year = cols[4].text.strip()
        tilp = cols[5].text.strip()
        run = cols[6].text.strip()
        price = cols[7].text.strip()

        sludinajumi.append({
            "title": title,
            "modelis": modelis,
            "gads": year,
            "mottilpums": tilp,
            "nobraukums": run,
            "cena": price
        })
    except Exception:
        continue

def parse_cena(cena_str):
    try:
        return int(cena_str.replace("€", "").replace(" ", "").replace(",", "").strip())
    except:
        return float("inf")

def filtret(dati, model):
    rezultati = []
    for ieraksts in dati:
        if model != "0" and model not in ieraksts["modelis"].lower():
            continue
        rezultati.append(ieraksts)
    return rezultati

def izdave(dati):
    if not dati:
        print("nav atrasti rezultāti")
        return

    dati.sort(key=lambda x: parse_cena(x["cena"]), reverse=(kartsana == "desc"))

    for i, ieraksts in enumerate(dati, 1):
        print(f"\n--- Sludinājums #{i} ---")
        for k, v in ieraksts.items():
            print(f"{k.capitalize()}: {v}")

    print("\n modeļu vidējā cena:")
    cenas = {}
    skaits = {}

    for ieraksts in dati:
        model = ieraksts['modelis']
        cena = parse_cena(ieraksts['cena'])
        if cena == float("inf"):
            continue
        cenas[model] = cenas.get(model, 0) + cena
        skaits[model] = skaits.get(model, 0) + 1

    videjas = {model: cenas[model] / skaits[model] for model in cenas}
    for model, vid_cena in sorted(videjas.items(), key=lambda x: x[1], reverse=True):
        print(f"{model}: {int(vid_cena):,} € ({skaits[model]} sludinājumi)".replace(",", " "))

filtrētie = filtret(sludinajumi, model)
izdave(filtrētie)