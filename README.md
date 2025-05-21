# ss_scraper

## Uzdevums  
Šī programma automatizē SS.com portāla datu iegūšanu un filtrēšanu pēc markas, modeļa un cenas, kā arī parāda vidējo cenu katram atrastajam modelim.
  
## Funkcionalitāte  
- Lietotājs ievada:
  - **Marku** (piemēram, `audi`, `bmw`, `volkswagen`)
  - **Modeli** (vai `0`, ja modelis nav svarīgs)
  - **Kārtību pēc cenas**: `asc` (augoši) vai `desc` (dilstoši)
- Tiek iegūti un analizēti SS.com sludinājumi
- Tiek izvadīts:
  - Sludinājumu saraksts ar detaļām (nosaukums, modelis, gads, motora tilpums, nobraukums, cena)
  - Katra modeļa **vidējā cena** un sludinājumu skaits

## Izstrādātājs
- **Annemarija Monska**

## Uzstādīšana  
Instalēt visas nepieciešamās bibliotēkas var ar `requirements.txt` palīdzību, projekta mapē izpildot komandu:   
`pip install -r requirements.txt`

## Lietošana  
Programma tiek palaista terminālī:

```bash
python datustr_projekts.py
```

Piemērs:

```
marka: bmw
modelis (raksti 0, ja nav svarīgi): 530
kārtot pēc cenas (asc/desc): asc
```

Pēc izpildes programma parādīs atrastos sludinājumus un vidējās cenas katram modelim.

## Dokumentācija  

### Izmantotās bibliotēkas  
Bibliotēka | Pielietojums  
:--|:--  
`requests` | Datu ielādei no SS.com  
`beautifulsoup4` | HTML satura parsēšanai  
`lxml` | HTML parsēšanas ātrdarbībai  

### Funkciju pārskats  
Funkcija | Apraksts  
:--|:--  
`parse_cena()` | Pārvērš cenas tekstu par skaitli salīdzināšanai  
`filtret()` | Filtrē rezultātus pēc modeļa  
`izdave()` | Izvada sludinājumus un aprēķina vidējās cenas

## Piezīmes  
- SS.com struktūra var mainīties, kas var izraisīt kļūdas darbībā  
- Nepareizi ievadīti parametri pārtrauks programmas izpildi  
- Cenas tiek attīrītas no simboliem, lai nodrošinātu korektu salīdzinājumu
