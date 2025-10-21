#!/usr/bin/env python3
"""
Demo della libreria TA (Technical Analysis)
Mostra vari indicatori tecnici in azione
"""
import pandas as pd
import sys
sys.path.insert(0, '/home/user/ta')
import ta

print("=" * 60)
print("DEMO LIBRERIA TA - ANALISI TECNICA")
print("=" * 60)
print()

# Carica dati di esempio
print("📊 Caricamento dati di esempio...")
df = pd.read_csv("test/data/datas.csv", sep=",")

# Pulisci valori NaN
df = ta.utils.dropna(df)

print(f"✅ Dati caricati: {len(df)} righe")
print()
print("Colonne disponibili:", list(df.columns))
print()

# Mostra le prime righe dei dati originali
print("-" * 60)
print("DATI ORIGINALI (prime 5 righe):")
print("-" * 60)
print(df[['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume_BTC']].head().to_string())
print()

# ========== INDICATORI DI TREND ==========
print("=" * 60)
print("🔵 INDICATORI DI TREND")
print("=" * 60)

# RSI (Relative Strength Index)
print("\n1️⃣  RSI - Relative Strength Index")
df['rsi'] = ta.momentum.rsi(df['Close'], window=14, fillna=True)
print(f"   RSI attuale: {df['rsi'].iloc[-1]:.2f}")
print(f"   RSI medio: {df['rsi'].mean():.2f}")

# MACD (Moving Average Convergence Divergence)
print("\n2️⃣  MACD - Moving Average Convergence Divergence")
df['macd'] = ta.trend.macd(df['Close'], fillna=True)
df['macd_signal'] = ta.trend.macd_signal(df['Close'], fillna=True)
df['macd_diff'] = ta.trend.macd_diff(df['Close'], fillna=True)
print(f"   MACD attuale: {df['macd'].iloc[-1]:.2f}")
print(f"   MACD Signal: {df['macd_signal'].iloc[-1]:.2f}")
print(f"   MACD Diff: {df['macd_diff'].iloc[-1]:.2f}")

# ========== INDICATORI DI VOLATILITÀ ==========
print("\n" + "=" * 60)
print("🟡 INDICATORI DI VOLATILITÀ")
print("=" * 60)

# Bollinger Bands
print("\n3️⃣  Bollinger Bands")
df['bb_high'] = ta.volatility.bollinger_hband(df['Close'], window=20, fillna=True)
df['bb_mid'] = ta.volatility.bollinger_mavg(df['Close'], window=20, fillna=True)
df['bb_low'] = ta.volatility.bollinger_lband(df['Close'], window=20, fillna=True)
print(f"   BB Superior: {df['bb_high'].iloc[-1]:.2f}")
print(f"   BB Media: {df['bb_mid'].iloc[-1]:.2f}")
print(f"   BB Inferior: {df['bb_low'].iloc[-1]:.2f}")
print(f"   Prezzo attuale: {df['Close'].iloc[-1]:.2f}")

# ATR (Average True Range)
print("\n4️⃣  ATR - Average True Range")
df['atr'] = ta.volatility.average_true_range(df['High'], df['Low'], df['Close'], window=14, fillna=True)
print(f"   ATR attuale: {df['atr'].iloc[-1]:.2f}")

# ========== INDICATORI DI VOLUME ==========
print("\n" + "=" * 60)
print("🟢 INDICATORI DI VOLUME")
print("=" * 60)

# OBV (On Balance Volume)
print("\n5️⃣  OBV - On Balance Volume")
df['obv'] = ta.volume.on_balance_volume(df['Close'], df['Volume_BTC'], fillna=True)
print(f"   OBV attuale: {df['obv'].iloc[-1]:.0f}")

# MFI (Money Flow Index)
print("\n6️⃣  MFI - Money Flow Index")
df['mfi'] = ta.volume.money_flow_index(df['High'], df['Low'], df['Close'], df['Volume_BTC'], window=14, fillna=True)
print(f"   MFI attuale: {df['mfi'].iloc[-1]:.2f}")

# ========== RISULTATI FINALI ==========
print("\n" + "=" * 60)
print("📈 TABELLA FINALE CON TUTTI GLI INDICATORI")
print("=" * 60)
print()

# Mostra le ultime 10 righe con gli indicatori selezionati
result_df = df[['Timestamp', 'Close', 'rsi', 'macd', 'bb_mid', 'atr', 'obv', 'mfi']].tail(10)
print(result_df.to_string(index=False))

print("\n" + "=" * 60)
print("✅ DEMO COMPLETATA!")
print("=" * 60)
print()
print("📚 Questa libreria supporta 43 indicatori tecnici diversi!")
print("🔗 Documentazione: https://technical-analysis-library-in-python.readthedocs.io/")
print()
