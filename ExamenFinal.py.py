import pandas as pd
import matplotlib.pyplot as plt
from ucimlrepo import fetch_ucirepo

#Buscar data de repositorio UC Irvine
data = fetch_ucirepo(id=352).data.features


print(data.head())

# Agregar nueva columna de precio total
data['TotalPrice'] = data['Quantity'] * data['UnitPrice']

# Convertir InvoiceDate a tipo DateTime
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])

# KPI 1: Promedio de ingresos por cliente
# Agrupar por customerid y totalprice
customer_sales = data.groupby('CustomerID')['TotalPrice'].sum()

# Calcular promedio
ARPC = customer_sales.mean()
print(f"Promedio de Ingreso por Cliente: {ARPC:.2f} usd")

# Visualizar top 10 clientes con mayor aporte
top_10_customers = customer_sales.sort_values(ascending=False).head(10)

# Grafico de barras para los top 10
top_10_customers.plot(kind='bar', figsize=(10, 5), color='green')
plt.title('Top 10 Customers by Total Sales')
plt.xlabel('Customer ID')
plt.ylabel('Total Sales (USD)')
plt.xticks(rotation=45)
plt.show()

# KPI 2: Tasa de cancelacion
# Definir transacciones canceladas
canceled_sales = data[data['Quantity'] < 0]

total_transactions = len(data)

canceled_transactions = len(canceled_sales)

# Calcular tasa de transacciones canceladas
cancellation_rate = canceled_transactions / total_transactions
print(f"Tasa de Cancelación de pedidos: {cancellation_rate:.2%}")

# Visualizacion
labels = ['Canceled', 'Non-Canceled']
sizes = [canceled_transactions, total_transactions - canceled_transactions]
plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['red', 'green'])
plt.title('Cancellation Rate')
plt.show()

# KPI 3: Crecimiento ventas mensuales
# Crear columna de mes
data['Month'] = data['InvoiceDate'].dt.to_period('M')

# Agrupar por mes y sumar precio total
monthly_sales = data.groupby('Month')['TotalPrice'].sum()

# Calcular cambio de crecimiento contra mes previo
monthly_growth = monthly_sales.pct_change().fillna(0) * 100
print("Crecimiento de los Ingresos Mensuales:")
print(monthly_growth)

# Visualizar
monthly_growth.plot(kind='line', figsize=(10, 5), marker='o', color='blue')
plt.title('Monthly Revenue Growth')
plt.ylabel('Revenue Growth (%)')
plt.xlabel('Month')
plt.grid(True)
plt.show()
