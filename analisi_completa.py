#!/usr/bin/env python3
"""
Analisi Tecnica Completa di Bitcoin
Genera dati JSON per visualizzazione web
"""
import pandas as pd
import json
from datetime import datetime
import sys
sys.path.insert(0, '/home/user/ta')
import ta

print("=" * 60)
print("📊 ANALISI TECNICA COMPLETA BITCOIN")
print("=" * 60)
print()

# Usa il file CSV disponibile (facile da cambiare!)
input_file = 'test/data/datas.csv'  # <-- CAMBIA QUESTO per usare dati freschi!

print(f"📁 Caricamento dati da: {input_file}")
df = pd.read_csv(input_file)

# Pulisci NaN
df = ta.utils.dropna(df)

# Prendi solo gli ultimi 30 giorni di dati (720 ore) per rendering più veloce
df = df.tail(30 * 24)

print(f"✅ Dati caricati: {len(df):,} candele")
print()

print("🔬 Calcolo indicatori tecnici...")
print()

# ==========  MOMENTUM ==========
print("   📍 Momentum...")
df['rsi'] = ta.momentum.rsi(df['Close'], window=14, fillna=True)
df['stoch'] = ta.momentum.stoch(df['High'], df['Low'], df['Close'], window=14, fillna=True)
df['williams_r'] = ta.momentum.williams_r(df['High'], df['Low'], df['Close'], lbp=14, fillna=True)

# ========== TREND ==========
print("   📍 Trend...")
df['sma_20'] = ta.trend.sma_indicator(df['Close'], window=20, fillna=True)
df['ema_12'] = ta.trend.ema_indicator(df['Close'], window=12, fillna=True)
df['ema_26'] = ta.trend.ema_indicator(df['Close'], window=26, fillna=True)
df['macd'] = ta.trend.macd(df['Close'], fillna=True)
df['macd_signal'] = ta.trend.macd_signal(df['Close'], fillna=True)
df['macd_diff'] = ta.trend.macd_diff(df['Close'], fillna=True)
df['adx'] = ta.trend.adx(df['High'], df['Low'], df['Close'], window=14, fillna=True)

# ========== VOLATILITY ==========
print("   📍 Volatilità...")
df['bb_high'] = ta.volatility.bollinger_hband(df['Close'], window=20, fillna=True)
df['bb_mid'] = ta.volatility.bollinger_mavg(df['Close'], window=20, fillna=True)
df['bb_low'] = ta.volatility.bollinger_lband(df['Close'], window=20, fillna=True)
df['atr'] = ta.volatility.average_true_range(df['High'], df['Low'], df['Close'], window=14, fillna=True)

# ========== VOLUME ==========
print("   📍 Volume...")
df['obv'] = ta.volume.on_balance_volume(df['Close'], df['Volume_BTC'], fillna=True)
df['mfi'] = ta.volume.money_flow_index(df['High'], df['Low'], df['Close'], df['Volume_BTC'], window=14, fillna=True)
df['cmf'] = ta.volume.chaikin_money_flow(df['High'], df['Low'], df['Close'], df['Volume_BTC'], window=20, fillna=True)

print()
print("✅ Indicatori calcolati!")
print()

# Converti Timestamp in formato leggibile
df['Date'] = df['Timestamp'].apply(lambda x: datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M'))

# Prepara dati per JSON
print("📦 Preparazione dati per web...")

# Statistiche generali
stats = {
    'periodo': {
        'inizio': df['Date'].iloc[0],
        'fine': df['Date'].iloc[-1],
        'giorni': len(df) // 24
    },
    'prezzo': {
        'attuale': float(df['Close'].iloc[-1]),
        'minimo': float(df['Close'].min()),
        'massimo': float(df['Close'].max()),
        'medio': float(df['Close'].mean()),
        'variazione_pct': float(((df['Close'].iloc[-1] - df['Close'].iloc[0]) / df['Close'].iloc[0]) * 100)
    },
    'indicatori_attuali': {
        'rsi': float(df['rsi'].iloc[-1]),
        'macd': float(df['macd'].iloc[-1]),
        'macd_signal': float(df['macd_signal'].iloc[-1]),
        'atr': float(df['atr'].iloc[-1]),
        'mfi': float(df['mfi'].iloc[-1]),
        'adx': float(df['adx'].iloc[-1])
    }
}

# Dati per grafici (ultimi 500 punti per performance)
chart_data = df.tail(500)[['Date', 'Open', 'High', 'Low', 'Close', 'Volume_BTC',
                             'rsi', 'macd', 'macd_signal', 'macd_diff',
                             'bb_high', 'bb_mid', 'bb_low',
                             'sma_20', 'ema_12', 'ema_26',
                             'atr', 'obv', 'mfi']].to_dict('records')

# Tabella ultimi 20 valori
table_data = df.tail(20)[['Date', 'Close', 'rsi', 'macd', 'bb_mid', 'atr', 'mfi']].to_dict('records')

# Output JSON
output = {
    'stats': stats,
    'chart_data': chart_data,
    'table_data': table_data,
    'generato': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
}

# Salva JSON
json_file = 'analisi_bitcoin.json'
with open(json_file, 'w') as f:
    json.dump(output, f, indent=2)

print(f"💾 Dati salvati: {json_file}")
print()

# Statistiche finali
print("📊 STATISTICHE ANALISI:")
print(f"   Periodo analizzato: {stats['periodo']['giorni']} giorni")
print(f"   Candele totali: {len(df):,}")
print(f"   Prezzo attuale: ${stats['prezzo']['attuale']:,.2f}")
print(f"   Variazione: {stats['prezzo']['variazione_pct']:+.2f}%")
print()
print(f"   RSI: {stats['indicatori_attuali']['rsi']:.2f}")
print(f"   MACD: {stats['indicatori_attuali']['macd']:.2f}")
print(f"   MFI: {stats['indicatori_attuali']['mfi']:.2f}")
print(f"   ADX: {stats['indicatori_attuali']['adx']:.2f}")
print()

print("=" * 60)
print("✅ ANALISI COMPLETATA!")
print("=" * 60)
