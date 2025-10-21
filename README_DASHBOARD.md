# 📊 Dashboard Analisi Tecnica Bitcoin

## 🎯 Cosa ho creato

Una **dashboard web interattiva** completa per l'analisi tecnica di Bitcoin con:

- ✅ 15+ indicatori tecnici calcolati
- 📈 4 grafici interattivi (Chart.js)
- 📊 Statistiche in tempo reale
- 📋 Tabella dati ultimi 20 valori
- 🎨 Design moderno e responsive

---

## 📁 File Creati

### 1. `analisi_completa.py`
Script Python che:
- Carica dati Bitcoin da CSV
- Calcola tutti gli indicatori tecnici
- Esporta risultati in JSON

**Indicatori calcolati:**
- **Momentum**: RSI, Stochastic, Williams %R
- **Trend**: SMA, EMA, MACD, ADX
- **Volatilità**: Bollinger Bands, ATR
- **Volume**: OBV, MFI, CMF

### 2. `dashboard.html`
Pagina web con:
- Grafici interattivi (puoi zoomare, nascondere linee, ecc.)
- Cards con statistiche principali
- Tabella dati
- Design professionale

### 3. `analisi_bitcoin.json`
Dati esportati in formato JSON per il web

---

## 🚀 Come Usare

### Visualizzare la Dashboard

**Opzione 1: Aprire direttamente** (se il browser lo permette)
```bash
# Linux/Mac
open dashboard.html

# Windows
start dashboard.html
```

**Opzione 2: Server locale** (raccomandato)
```bash
python -m http.server 8000
```
Poi apri nel browser: `http://localhost:8000/dashboard.html`

---

## 🔄 Usare Dati Freschi

### Metodo 1: Cambiare la fonte dati

Modifica `analisi_completa.py` alla riga 17:

```python
# CAMBIA QUESTA RIGA:
input_file = 'test/data/datas.csv'  # Vecchi dati 2011-2017

# IN:
input_file = 'dati_freschi.csv'  # I tuoi dati freschi!
```

### Metodo 2: Formato CSV richiesto

Il file CSV deve avere queste colonne:
```csv
Timestamp,Open,High,Low,Close,Volume_BTC,Volume_Currency,Weighted_Price
1503403200,3896.18,3951.83,3885.09,3934.21,350.96,1376127.00,3918.46
...
```

### Metodo 3: Scaricare da fonti online

Puoi scaricare dati freschi da:
- **Kaggle**: https://www.kaggle.com/datasets (cerca "bitcoin historical data")
- **CryptoDataDownload**: https://www.cryptodatadownload.com/data/binance/
- **Yahoo Finance**: Manualmente dal sito web
- **TradingView**: Esporta CSV

### Metodo 4: Script di download (quando funziona)

```bash
# Prova lo script (se non bloccato dalla rete)
python scarica_dati_reali.py
```

---

## 🎨 Caratteristiche Dashboard

### Grafici

1. **Prezzo + Bollinger Bands**
   - Linea prezzo
   - Bande superiore, media, inferiore
   - Area colorata sotto il prezzo

2. **RSI (Relative Strength Index)**
   - Linee a 70 (ipercomprato) e 30 (ipervenduto)
   - Valori 0-100

3. **MACD**
   - Linea MACD
   - Linea Signal
   - Histogram (differenza)

4. **Volume & MFI**
   - Barre volume (asse sinistro)
   - Linea MFI (asse destro)

### Statistiche Cards

- Prezzo attuale
- Variazione percentuale (colorata)
- Min/Max periodo
- RSI con badge segnale (Ipercomprato/Neutrale/Ipervenduto)
- MACD
- MFI

---

## 🛠️ Rigenerare l'Analisi

Ogni volta che cambi i dati:

```bash
# 1. Ricalcola indicatori
python analisi_completa.py

# 2. Ricarica la pagina web (F5)
```

---

## 📊 Interpretazione Indicatori

### RSI (Relative Strength Index)
- **> 70**: Ipercomprato (possibile vendita)
- **30-70**: Neutrale
- **< 30**: Ipervenduto (possibile acquisto)

### MACD
- **MACD > Signal**: Segnale rialzista
- **MACD < Signal**: Segnale ribassista
- **Histogram positivo**: Momentum crescente

### Bollinger Bands
- **Prezzo > BB Superior**: Possibile ipercomprato
- **Prezzo < BB Inferior**: Possibile ipervenduto
- **BB strette**: Bassa volatilità (possibile breakout)

### MFI (Money Flow Index)
- **> 80**: Pressione di acquisto forte
- **< 20**: Pressione di vendita forte

---

## 🎯 Personalizzazione

### Cambiare periodo analisi

In `analisi_completa.py`, modifica:

```python
# Riga 21:
df = df.tail(30 * 24)  # 30 giorni

# Cambia in:
df = df.tail(90 * 24)  # 90 giorni
# oppure
df = df.tail(7 * 24)   # 7 giorni
```

### Aggiungere altri indicatori

Consulta la documentazione TA:
https://technical-analysis-library-in-python.readthedocs.io/

Esempio:
```python
df['cci'] = ta.trend.cci(df['High'], df['Low'], df['Close'], window=20)
```

---

## 🐛 Troubleshooting

**Dashboard non mostra grafici:**
- Controlla console browser (F12)
- Verifica che `analisi_bitcoin.json` esista
- Prova con server locale (non aprire direttamente il file)

**Errore "No module named 'ta'":**
```bash
pip install ta
```

**Dati non aggiornati:**
```bash
# Rigenera JSON
python analisi_completa.py
```

---

## 📚 Risorse

- **Libreria TA**: https://github.com/bukosabino/ta
- **Chart.js**: https://www.chartjs.org/
- **Documentazione TA**: https://technical-analysis-library-in-python.readthedocs.io/

---

## 🎉 Fatto!

Ora hai una dashboard professionale per analizzare Bitcoin!

**Per dati freschi**: sostituisci il CSV e riesegui `analisi_completa.py`

**Made with ❤️ usando la libreria TA Python**
