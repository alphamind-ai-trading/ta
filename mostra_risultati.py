#!/usr/bin/env python3
"""
Mostra un'anteprima testuale dei risultati dell'analisi
"""
import json
from datetime import datetime

with open('analisi_bitcoin.json') as f:
    data = json.load(f)

stats = data['stats']
chart_data = data['chart_data'][-20:]  # Ultimi 20 punti

print("\n" + "=" * 80)
print("📊 ANALISI TECNICA BITCOIN - RISULTATI".center(80))
print("=" * 80)
print()

# Statistiche principali
prezzo = stats['prezzo']
ind = stats['indicatori_attuali']
periodo = stats['periodo']

print("┌" + "─" * 78 + "┐")
print("│" + " STATISTICHE PRINCIPALI ".center(78) + "│")
print("├" + "─" * 78 + "┤")
print(f"│  💰 Prezzo Attuale:  ${prezzo['attuale']:>15,.2f}" + " " * 39 + "│")
print(f"│  📊 Prezzo Minimo:   ${prezzo['minimo']:>15,.2f}" + " " * 39 + "│")
print(f"│  📈 Prezzo Massimo:  ${prezzo['massimo']:>15,.2f}" + " " * 39 + "│")
print(f"│  📉 Prezzo Medio:    ${prezzo['medio']:>15,.2f}" + " " * 39 + "│")
print("│" + " " * 78 + "│")

var = prezzo['variazione_pct']
var_str = f"{var:+.2f}%"
var_icon = "📈" if var >= 0 else "📉"
print(f"│  {var_icon} Variazione:     {var_str:>15}" + " " * 42 + "│")
print("│" + " " * 78 + "│")
print(f"│  📅 Periodo:         {periodo['inizio']} → {periodo['fine']}" + " " * 17 + "│")
print(f"│  📊 Giorni:          {periodo['giorni']:>3} giorni" + " " * 52 + "│")
print("└" + "─" * 78 + "┘")
print()

# Indicatori
print("┌" + "─" * 78 + "┐")
print("│" + " INDICATORI TECNICI ATTUALI ".center(78) + "│")
print("├" + "─" * 78 + "┤")

# RSI
rsi = ind['rsi']
if rsi > 70:
    rsi_signal = "IPERCOMPRATO 🔴"
elif rsi < 30:
    rsi_signal = "IPERVENDUTO 🟢"
else:
    rsi_signal = "NEUTRALE 🟡"
print(f"│  📊 RSI (14):        {rsi:>7.2f}   [{rsi_signal}]" + " " * (47 - len(rsi_signal)) + "│")

# MACD
macd = ind['macd']
macd_sig = ind['macd_signal']
macd_diff = macd - macd_sig
macd_trend = "Rialzista 📈" if macd > macd_sig else "Ribassista 📉"
print(f"│  📈 MACD:            {macd:>7.2f}   [{macd_trend}]" + " " * (43 - len(macd_trend)) + "│")
print(f"│      Signal:        {macd_sig:>7.2f}" + " " * 48 + "│")
print(f"│      Divergenza:    {macd_diff:>7.2f}" + " " * 48 + "│")

# Altri indicatori
print("│" + " " * 78 + "│")
print(f"│  💹 MFI (14):        {ind['mfi']:>7.2f}" + " " * 48 + "│")
print(f"│  🌊 ATR (14):        {ind['atr']:>7.2f}" + " " * 48 + "│")
print(f"│  💪 ADX (14):        {ind['adx']:>7.2f}" + " " * 48 + "│")
print("└" + "─" * 78 + "┘")
print()

# Mini grafico ASCII del prezzo
print("┌" + "─" * 78 + "┐")
print("│" + " ANDAMENTO PREZZO (Ultimi 20 punti) ".center(78) + "│")
print("├" + "─" * 78 + "┤")

prices = [d['Close'] for d in chart_data]
min_p = min(prices)
max_p = max(prices)
height = 10

for i in range(height, -1, -1):
    threshold = min_p + (max_p - min_p) * i / height
    line = "│ "

    if i == height:
        line += f"${max_p:>8,.0f} │"
    elif i == 0:
        line += f"${min_p:>8,.0f} │"
    else:
        line += " " * 10 + "│"

    for price in prices:
        if price >= threshold:
            line += "█"
        else:
            line += " "

    line += " " * (65 - len(prices)) + "│"
    print(line)

print("│" + " " * 10 + "└" + "─" * 20 + "→ tempo" + " " * 40 + "│")
print("└" + "─" * 78 + "┘")
print()

# Tabella ultimi 5 valori
print("┌" + "─" * 78 + "┐")
print("│" + " ULTIMI 5 VALORI ".center(78) + "│")
print("├" + "─" * 78 + "┤")
print("│ Data/Ora           │   Prezzo │     RSI │    MACD │     MFI │     ATR │")
print("├" + "─" * 78 + "┤")

for d in data['table_data'][-5:]:
    date = d['Date']
    print(f"│ {date:18} │ ${d['Close']:>7,.0f} │ {d['rsi']:>7.2f} │ {d['macd']:>7.2f} │ {d['mfi']:>7.2f} │ {d['atr']:>7.2f} │")

print("└" + "─" * 78 + "┘")
print()

print("=" * 80)
print()
print("📁 File dashboard: /home/user/ta/dashboard_standalone.html")
print("📊 Apri il file nel browser per vedere i grafici interattivi!")
print()
print("=" * 80)
