import pandas as pd
import os

# Ruta al archivo Excel
excel_path = "Criticidad.xlsx"   # Si está en la raíz, usa este nombre exacto

# Leer el Excel
df = pd.read_excel(excel_path, sheet_name=0)

print("✅ Archivo leído correctamente")
print(f"Total de zonas: {len(df)}")
print(f"Columnas disponibles: {list(df.columns)}\n")

# Mostrar resumen importante
print(df[['Área/Descripción', 'Criticidad', 'Potencia de diseño (TR)', 'Simultaneidad', 'Potencia Efectiva (TR)', 'Categoría/Zona Hospitalaria', 'EFLH (h/año)']])

# Guardar resumen en CSV para fácil revisión
df.to_csv("results/resumen_zonas.csv", index=False)
print("\nResumen guardado en results/resumen_zonas.csv")
