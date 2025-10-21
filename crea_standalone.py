#!/usr/bin/env python3
"""
Crea una versione standalone della dashboard con i dati incorporati
"""
import json

print("📦 Creazione dashboard standalone...")

# Leggi il JSON
with open('analisi_bitcoin.json', 'r') as f:
    data = json.dumps(json.load(f))

# Leggi il template HTML
with open('dashboard.html', 'r') as f:
    html = f.read()

# Sostituisci la parte di fetch con i dati inline
fetch_code = """fetch('analisi_bitcoin.json')
            .then(response => response.json())
            .then(data => {
                renderStats(data.stats);
                renderCharts(data.chart_data);
                renderTable(data.table_data);
            })
            .catch(error => console.error('Errore caricamento dati:', error));"""

inline_code = f"""// Dati incorporati direttamente
        const data = {data};
        renderStats(data.stats);
        renderCharts(data.chart_data);
        renderTable(data.table_data);"""

html = html.replace(fetch_code, inline_code)

# Salva la versione standalone
with open('dashboard_standalone.html', 'w') as f:
    f.write(html)

print("✅ Creato: dashboard_standalone.html")
print()
print("📁 Dimensione file:", len(html) // 1024, "KB")
print()
print("🎯 COME USARE:")
print("   1. Scarica il file 'dashboard_standalone.html'")
print("   2. Fai doppio click per aprirlo")
print("   3. Si aprirà nel tuo browser!")
print()
print("✅ Funziona senza server, offline, ovunque!")
