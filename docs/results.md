# Results — Oil Prices & Norwegian Markets

## 1. Indexed Performance

All assets are rebased to 100 at the start of the period (2016). Key observations:

- **EQNR and DNB** have performed significantly best, reaching 500–600 by 2026, reflecting strong growth in the Norwegian energy and banking sectors.
- **Oil** moved sideways from 2016–2020, collapsed during COVID-19, recovered sharply through 2021–2022 and has remained at elevated levels since.
- **NHY** showed moderate growth, but trailed behind EQNR and DNB.
- **NOK/USD** is the weakest performer of the period — the krone has weakened relative to the dollar over time.

---

## 2. Oil Volatility

- The largest volatility spike occurred in **early 2020** during the COVID-19 pandemic, when oil markets experienced extreme uncertainty (Brent crude briefly went negative in April 2020).
- A second spike emerged around **2022**, coinciding with Russia's invasion of Ukraine and disruptions in the energy market.
- A third spike is visible in **early 2026**, suggesting renewed market uncertainty.
- Outside these events, volatility remained relatively stable in the 0.2–0.4 range.

---

## 3. Oil vs NOK/USD (Direct Relationship)

- The scatter plot shows a **weak positive relationship** between daily oil returns and NOK/USD movements.
- The regression line is nearly flat, indicating that **daily oil price movements alone are a poor predictor of daily krone movements**.
- Most data points are tightly clustered around zero, with a few outliers during extreme market events.
- The relationship is more structural and long-term than reactive on a daily basis.

---

## 4. Rolling Correlation

- Correlations between oil and Norwegian stocks are **not stable over time** — they fluctuate significantly.
- **EQNR** consistently shows the highest correlation with oil, which is expected given it is an oil and gas company.
- **DNB and NHY** show moderate and variable correlations, with spikes during market stress (COVID, the Ukraine war).
- **NOK/USD** correlation with oil is generally positive but noisy.
- Correlations tend to **increase during crises**, as global risk sentiment drives all assets in the same direction.

---

## 5. Correlation Matrix

- **EQNR, DNB and NHY** are strongly correlated with each other, reflecting their shared exposure to the Norwegian economy.
- **Oil** has a moderate positive correlation with the Norwegian stocks, strongest with EQNR.
- **NOK/USD** shows the weakest correlation with equity assets and appears more independent in its daily movements.
- No strong negative correlations exist in the dataset.

---

## 6. Descriptive Statistics

| Asset  | Mean Return | Daily Std | Ann. Volatility |
| ------ | ----------- | --------- | --------------- |
| Oil    | 0.06%       | 2.46%     | 39.05%          |
| EQNR   | 0.08%       | 1.85%     | 29.41%          |
| DNB    | 0.07%       | 1.52%     | 23.77%          |
| NHY    | 0.09%       | 2.13%     | 33.88%          |
| NOKUSD | 0.02%       | 1.52%     | 20.59%          |

- **Oil** is the most volatile asset with an annualized volatility of ~39%, reflecting its sensitivity to geopolitical and macroeconomic shocks.
- **NOK/USD** is the least volatile, consistent with it being an exchange rate rather than an equity.
- All assets show positive mean daily returns over the period.

---

## 7. Oil Price Regression

- The linear trend line shows a **long-term upward trajectory** in oil prices from 2016 to 2026.
- The model forecasts continued moderate growth, though the linear assumption becomes less reliable further into the future.
- Notable deviations from the trend include the **2020 COVID crash** and the **2022 price surge** following the Ukraine war.
- The forecast (dotted line) extends ~720 business days (~3 years) and suggests oil prices could trend toward $100–120 if the historical trend holds.

---

## Reflection — Are Norwegian Markets Really That Oil-Dependent?

A surprising finding is that Norwegian markets **are not as strongly affected by oil as one might expect** — and this actually makes sense when you think it through.

**Why the impact is weaker than expected:**

- **DNB and NHY** are not directly oil-dependent — DNB is a bank, NHY works with aluminium. They follow the broader Norwegian market, not oil specifically.
- **EQNR** is the only company with direct oil exposure, and that is also where the strongest correlation is observed.
- **NOK/USD** reacts to many factors beyond oil — interest rate differentials, global risk appetite and inflation.

**When oil actually dominates:**

- During crises like COVID and the Ukraine war, all correlations spike — but it is not oil driving this, rather **global panic** pulling everything down simultaneously.

**Conclusion:**
Norway as an economy is diversified enough that oil is not the sole driver at the stock market level — even though the country remains heavily dependent on oil revenues at the state level through the Government Pension Fund. The daily relationship between oil prices and Norwegian stocks is real, but weaker and more situational than the structural dependency might suggest.

---

## Political Context — What Does the Government Say?

The findings in this analysis align with what Prime Minister Jonas Gahr Støre and LO leader Peggy Hessen Følsvik argued in Dagens Næringsliv (January 2025): **it is work, not oil, that lubricates the Norwegian economy.**

The government points out that the welfare state and the Norwegian model are not the result of oil revenues alone, but of two fundamental factors:

- **The ability to create value** — through high employment and a productive working life.
- **The ability to distribute value fairly** — through the trade union movement, the wage coordination model, and a redistributive tax system.

**How this connects to the analysis:**

- The fact that **DNB and NHY** do not closely track oil prices on a daily basis supports exactly this — these companies are driven by the broader Norwegian business community and labour market, not oil prices directly.
- The fact that **EQNR** has the strongest correlation with oil is logical, but EQNR is one company — not representative of the Norwegian economy as a whole.
- The Government Pension Fund acts as a state-level buffer and long-term savings vehicle, but **the stock market reflects the real economy** — which is far more diversified than the price of a single commodity.

The government's point is that reforms and welfare cannot be solved with oil money alone, but require competence, leadership and work. The data in this analysis supports the same picture: Norwegian markets live their own life, and the oil price is one factor among many.
