import requests
import sqlite3
from datetime import datetime, timedelta
from pymongo import MongoClient
import pandas as pd

client = MongoClient('mongodb://localhost:27017/')
db_mongo = client['sunat_db']
collection = db_mongo['sunat_info']

conn = sqlite3.connect('base.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS sunat_info (
    date TEXT PRIMARY KEY,
    compra REAL,
    venta REAL
)
''')
conn.commit()

def obtener_tipo_cambio(fecha):
    url = f"https://apis.net.pe/tipo-cambio-sunat/{fecha}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        compra = data.get('valorCompra')
        venta = data.get('valorVenta')
        return compra, venta
    else:
        return None, None

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

delta = timedelta(days=1)

while start_date <= end_date:
    fecha_str = start_date.strftime('%Y-%m-%d')
    compra, venta = obtener_tipo_cambio(fecha_str)
    
    if compra is not None and venta is not None:
        cursor.execute('''
            INSERT OR REPLACE INTO sunat_info (date, compra, venta)
            VALUES (?, ?, ?)
        ''', (fecha_str, compra, venta))
        conn.commit()
        
        collection.update_one(
            {'date': fecha_str},
            {'$set': {'compra': compra, 'venta': venta}},
            upsert=True
        )
        
        print(f"Fecha: {fecha_str} - Compra: {compra} - Venta: {venta}")
    else:
        print(f"No se pudo obtener datos para la fecha: {fecha_str}")
    
    start_date += delta

df = pd.read_sql_query("SELECT * FROM sunat_info", conn)
print("\nContenido de la tabla sunat_info:")
print(df)

conn.close()
client.close()
