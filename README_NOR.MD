# Olje sitt påvirkning innenfor det Norske Markedet

Et interaktivt dashboard som analyserer hvordan endringer i oljeprisen påvirker norske aksjer (EQNR, DNB, NHY) og valutakursen NOK/USD.

---

## Innholdsfortegnelse

- [Beskrivelse av datasettet](#beskrivelse-av-datasettet)
- [Analysevalg](#analysevalg)
- [Prosjektstruktur](#prosjektstruktur)
- [Kjøreveiledning](#kjøreveiledning)
- [Krav](#krav)

---

## Beskrivelse av datasettet

### Kilder

All data hentes via **yfinance**, som gir historiske markedsdata fra Yahoo Finance med 15 minutters forsinkelse.

| Aktivum     | Ticker     | Beskrivelse                  |
| ----------- | ---------- | ---------------------------- |
| Olje        | `BZ=F`     | Brent råolje futures-pris    |
| Equinor     | `EQNR.OL`  | Oslo Børs: Equinor ASA       |
| DNB         | `DNB.OL`   | Oslo Børs: DNB Bank ASA      |
| Norsk Hydro | `NHY.OL`   | Oslo Børs: Norsk Hydro ASA   |
| NOK/USD     | `NOKUSD=X` | Norsk krone / US dollar-kurs |

### Innhold

- **Periode:** 10 år med daglige sluttkurser
- **Prosesserte data:** daglige avkastninger, indeksert kursutvikling (basis 100), rullerende korrelasjoner, volatilitet og deskriptiv statistikk

### Begrensninger

- Data er forsinket med 15 minutter — ikke egnet for live handel
- yfinance-data kan ha enkeltdagers hull på norske helligdager; disse fylles inn med siste kjente verdi (forward-fill)
- Lineær regresjon forutsetter et lineært forhold mellom tid og oljepris, noe som er en forenkling av virkeligheten
- Korrelasjon innebærer ikke kausalitet

---

## Analysevalg

### 1. Indeksert kursutvikling

Prisene rebaseres til 100 ved starten av valgt periode, slik at relativ utvikling kan sammenlignes direkte på tvers av aktivum med ulike prisnivåer.

### 2. Oljevolatilitet

Rullerende 30-dagers standardavvik for oljeav kastning, brukt som mål på markedsusikkerhet. Høyere verdi indikerer mer turbulente oljemarkeder.

### 3. Olje vs NOK/USD (Direkte sammenheng)

Et spredningsplott med en OLS-regresjonslinje som viser det samtidige forholdet mellom daglige oljeavkastninger og NOK/USD-avkastninger. Norges oljeøkonomi gjør at disse tenderer til å bevege seg i takt.

### 4. Rullerende korrelasjon

60-dagers rullerende Pearson-korrelasjon mellom oljeavkastninger og hvert norske aktivum, som viser hvordan sammenhengen utvikler seg over tid. Nøkkelhendelser (f.eks. COVID-19, Ukraina-krigen) er markert med vertikale linjer.

### 5. Korrelasjonsmatrise (Heatmap)

En statisk korrelasjonsmatrise for alle aktivum i valgt periode, som gir en oversikt over parvise sammenhenger.

### 6. Statistikktabell

Deskriptiv statistikk for daglige avkastninger: gjennomsnitt, median, minimum, maksimum, daglig standardavvik og annualisert volatilitet (daglig std × √252).

### 7. Oljeprisregresjon

En enkel lineær regresjon (scikit-learn) tilpasset historiske oljepriser med tid som variabel. Produserer en tilpasset trendlinje og en 252-dagers (1 handelsår) fremoverrettet prognose med 95% konfidensintervall. Modellen er bevisst enkel — målet er å demonstrere metoden, ikke å produsere nøyaktige prisprediksjoner.

---

## Prosjektstruktur

```
oil-impact-on-norwegian-economy/
├── src/
│   ├── dashboard/
│   │   ├── app.py          # Streamlit inngangspunkt
│   │   ├── data.py         # Datasett-bygger
│   │   ├── layout.py       # Diagramlayout-definisjon
│   │   ├── render.py       # Plotly figur-renderer
│   │   └── filter.py       # Sidepanel-kontroller
│   ├── lib/
|   |   ├── dashboard/
|   │   │   ├── core.py        # Plotly dashboard byggere
|   |   ├── pipelines/
|   │   │   ├── fetch.py        # yfinance datahenting
|   │   │   ├── returns.py      # Avkastningsberegninger
|   |   │   ├── transforms.py   # Indeksering, standardisering
|   │   │   ├── features.py     # Volatilitet, rullerende korr.
|   │   │   └── regression.py   # Lineær regresjon + prognose
│   ├── pipelines/
│   │   └── processed.py    # Hoved-datapipeline
|   |   └── stocks.py       # Aksje-datapipeline
│   ├── reports/
│   │   └── images.py
│   ├── theme/
|   |   ├── theme.py        # Farge variabler
│   │   └── dashboard_styling.py # styling av dashboard komponenter
│   ├── utils/
│   │   └── dashboard_utils.py
│   └── visuals/
│       ├── annotations.py  # Nøkkelhendelseslinjer
│       ├── correlation.py
│       ├── direct_relationship.py
│       ├── heatmap.py
│       ├── indexed.py
│       ├── regression.py
│       ├── stats_table.py
│       └── volatility.py
├── docs/
|   └── results.md      # Results of the analysis
|   └── results_nor.md
├── data/
│   ├── raw/
│   ├── processed/
│   └── stats/
├── pyproject.toml
└── README.md
└── README_NOR.md
```

---

## Hurtigstart

```bash
pip install -r requirements.txt
python -m src.pipelines.processed
streamlit run src/dashboard/app.py
```

---

## Kjøreveiledning

### 1. Klon repositoriet

```bash
git clone <repo-url>
cd oil-impact-on-norwegian-economy
```

### 2. Installer avhengigheter

Med pip:

```bash
pip install -r requirements.txt
```

Eller med uv:

```bash
uv sync
```

### 3. Kjør datapipelinen

Dette henter data fra yfinance og genererer alle prosesserte CSV-filer.

Med pip:

```bash
python -m src.pipelines.processed
```

Eller med uv:

```bash
uv run python -m src.pipelines.processed
```

### 4. Start dashboardet

Med pip:

```bash
streamlit run src/dashboard/app.py
```

Eller med uv:

```bash
uv run streamlit run src/dashboard/app.py
```

Dashboardet åpnes på:

```text
http://localhost:8501
```

### 5. Oppdater data

Dashboardet oppdateres automatisk hvert 15. minutt. Du kan også oppdatere det manuelt ved å trykke på **Rerun**-knappen i Streamlit-grensesnittet.

---

## Krav

- Python 3.11+

Valgfritt:

- uv (for brukere som ønsker å installere og kjøre prosjektet med uv)

Viktige avhengigheter:

- streamlit
- plotly
- pandas
- numpy
- scikit-learn
- yfinance

---
