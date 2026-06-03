# Resultater — Oljepris & Norske Markeder

## 1. Indeksert Ytelse

Alle assets er rebasert til 100 ved starten av perioden (2016). Viktige observasjoner:

- **EQNR og DNB** har prestert klart best og nådd 500–600 innen 2026, noe som reflekterer sterk vekst i norsk energi- og banksektor.
- **Olje** beveget seg sidelengs fra 2016–2020, kollapset under COVID-19, hentet seg kraftig inn i 2021–2022 og har holdt seg på et høyt nivå siden.
- **NHY** viste moderat vekst, men hengte etter EQNR og DNB.
- **NOK/USD** er den svakeste i perioden — kronen har svekket seg relativt til dollaren over tid.

---

## 2. Oljevolatilitet

- Den største volatilitetsspiket kom i **tidlig 2020** under COVID-19-pandemien, da oljemarkedene opplevde ekstrem usikkerhet (Brent råolje gikk kort negativt i april 2020).
- En ny spike oppsto rundt **2022**, sammenfallende med Russlands invasjon av Ukraina og forstyrrelser i energimarkedet.
- En tredje spike er synlig i **tidlig 2026**, noe som tyder på fornyet markedsusikkerhet.
- Utenfor disse hendelsene holdt volatiliteten seg relativt stabil i området 0.2–0.4.

---

## 3. Olje vs NOK/USD (Direkte Sammenheng)

- Scatter-plottet viser en **svak positiv sammenheng** mellom daglige oljeavkastninger og NOK/USD-bevegelser.
- Regresjonslinjen er nesten flat, noe som indikerer at **daglige oljeprisbevegelser alene er en dårlig prediktor for daglige kronebevegelser**.
- De fleste datapunktene er tett klustret rundt null, med noen få uteliggere under ekstreme markedshendelser.
- Sammenhengen er mer strukturell og langsiktig enn reaktiv på daglig basis.

---

## 4. Rullerende Korrelasjon

- Korrelasjoner mellom olje og norske aksjer er **ikke stabile over tid** — de svinger betydelig.
- **EQNR** viser konsekvent høyest korrelasjon med olje, noe som er forventet siden selskapet er et olje- og gassselskap.
- **DNB og NHY** viser moderate og variable korrelasjoner, med topper under markedsstress (COVID, Ukraina-krigen).
- **NOK/USD**-korrelasjonen med olje er generelt positiv men støyete.
- Korrelasjoner tenderer til å **øke under kriser**, ettersom global risikosentiment driver alle assets i samme retning.

---

## 5. Korrelasjonsmatrise

- **EQNR, DNB og NHY** er sterkt korrelerte med hverandre, noe som reflekterer deres felles eksponering mot norsk økonomi.
- **Olje** har moderat positiv korrelasjon med de norske aksjene, sterkest med EQNR.
- **NOK/USD** viser svakest korrelasjon med aksjeaktiva og fremstår mer uavhengig i daglige bevegelser.
- Ingen sterke negative korrelasjoner eksisterer i datasettet.

---

## 6. Deskriptiv Statistikk

| Asset  | Gj.snitt avkastning | Daglig Std | Ann. Volatilitet |
| ------ | ------------------- | ---------- | ---------------- |
| Oil    | 0.06%               | 2.46%      | 39.05%           |
| EQNR   | 0.08%               | 1.85%      | 29.41%           |
| DNB    | 0.07%               | 1.52%      | 23.77%           |
| NHY    | 0.09%               | 2.13%      | 33.88%           |
| NOKUSD | 0.02%               | 1.52%      | 20.59%           |

- **Olje** er det mest volatile aktivumet med en annualisert volatilitet på ~39%, noe som reflekterer sensitiviteten for geopolitiske og makroøkonomiske sjokk.
- **NOK/USD** er minst volatil, konsistent med at det er en valutakurs og ikke en aksje.
- Alle assets viser positiv gjennomsnittlig daglig avkastning over perioden.

---

## 7. Oljeprisregresjon

- Den lineære trendlinjen viser en **langsiktig oppgående trend** i oljepriser fra 2016 til 2026.
- Modellen predikerer fortsatt moderat vekst, selv om den lineære antakelsen blir mindre pålitelig lengre frem i tid.
- Merkbare avvik fra trenden inkluderer **COVID-krasjet i 2020** og **prissurget i 2022** etter Ukraina-krigen.
- Prognosen (stiplet linje) strekker seg ~720 virkedager (~3 år) frem og antyder at oljepriser kan tende mot $100–120 hvis den historiske trenden holder.

---

## Refleksjon — Er Norske Markeder Egentlig Så Oljeavhengige?

Et overraskende funn er at norske markeder **ikke er like sterkt påvirket av olje som man kanskje skulle forvente** — og det gir faktisk mening når man tenker nærmere over det.

**Hvorfor påvirkningen er svakere enn forventet:**

- **DNB og NHY** er ikke direkte oljeavhengige — DNB er en bank, NHY jobber med aluminium. De følger det norske markedet generelt, ikke olje spesifikt.
- **EQNR** er det eneste selskapet med direkte oljeeksponering, og der ser man også den sterkeste korrelasjonen.
- **NOK/USD** reagerer på mange faktorer utover olje — rentedifferanser, global risikoappetitt og inflasjon.

**Når olje faktisk dominerer:**

- Under kriser som COVID og Ukraina-krigen spiker alle korrelasjoner — men da er det ikke olje som driver, men **global panikk** som drar alt ned samtidig.

**Konklusjon:**
Norge som økonomi er diversifisert nok til at olje ikke er den eneste driveren på børsnivå — selv om landet fortsatt er sterkt avhengig av oljeinntekter på statsnivå gjennom Oljefondet. Den daglige sammenhengen mellom oljepris og norske aksjer er reell, men svakere og mer situasjonsavhengig enn den strukturelle avhengigheten skulle tilsi.

---

## Politisk Kontekst — Hva Sier Regjeringen?

Funnene i denne analysen samsvarer med det statsminister Jonas Gahr Støre og LO-leder Peggy Hessen Følsvik argumenterte for i Dagens Næringsliv (januar 2025): **det er arbeid, ikke olje, som smører norsk økonomi.**

Regjeringen peker på at velferdsstaten og den norske modellen ikke er et resultat av oljeinntekter alene, men av to grunnleggende forhold:

- **Evnen til å skape verdier** — gjennom høy sysselsetting og et produktivt arbeidsliv.
- **Evnen til å dele verdiene rettferdig** — gjennom fagbevegelsen, frontfagsmodellen og et omfordelende skattesystem.

**Hvordan dette kobles til analysen:**

- At **DNB og NHY** ikke følger oljeprisen tett på daglig basis støtter nettopp dette — disse selskapene er drevet av bredere norsk næringsliv og arbeidsliv, ikke oljepris direkte.
- At **EQNR** har sterkest korrelasjon med olje er logisk, men EQNR er ett selskap — ikke representativt for hele norsk økonomi.
- Oljefondet fungerer som en statlig buffer og langsiktig spareordning, men **børsen reflekterer realøkonomien** — som er langt mer diversifisert enn råvareprisen på ett produkt.

Regjeringens poeng er at reformer og velferd ikke kan løses med oljepenger alene, men krever kompetanse, ledelse og arbeid. Dataene i denne analysen underbygger det samme bildet: norske markeder lever sitt eget liv, og oljeprisen er én faktor blant mange.
