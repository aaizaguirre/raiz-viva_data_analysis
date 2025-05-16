import pandas as pd
import numpy as np

# Parameteros
n = 8200  # numero de filas

# Lista de productos con precios (soles)
productos = [
    ("aceite de jojoba 100 ml", 40),
    ("aceite de jojoba 30 ml", 20),
    ("jabón de sangre de grado 120 g", 13),
    ("aceite de copaiba 10 ml", 12),
    ("jabón de copaiba y árbol del te 120 g", 13),
    ("repelente de hierba luisa 75 ml", 16),
    ("aceite de almendras 30 ml", 20),
    ("aceite de almendras 100 ml", 40),
    ("óleo aromático de matico 10 ml", 15),
    ("óleo aromático de árbol del te 10 ml", 20),
    ("óleo aromático de lavanda 10 ml", 20),
    ("óleo aromático de eucalipto 10 ml", 15),
    ("óleo aromático de hierba luisa 10 ml", 15),
    ("óleo aromático de romero 10 ml", 15),
    ("óleo aromático de menta piperita 10 ml", 20),
    ("óleo aromático de palo santo 10 ml", 20),
    ("óleo aromático de molle 10 ml", 15),
    ("óleo aromático de naranja dulce 10 ml", 15),
    ("óleo aromático de palo rosa 10 ml", 25),
    ("óleo aromático de muña 10 ml", 15),
    ("kombucha de maracuyá 1 L", 14),
    ("kombucha de jamaica 1 L", 14),
    ("kombucha de maracuyá 330 ml", 7),
    ("kombucha de kión con espirulina 1 L", 14),
    ("kéfir de agua de manzana 1 L", 14),
    ("kombucha de muña 1 L", 14),
    ("kéfir de agua de manzana 330 ml", 7),
    ("kombucha de kión 1 L", 14),
    ("bálsamo amazónico de noche 20 g", 20),
    ("jabón de aguaje 120 g", 13),
    ("kombucha de jamaica 330 ml", 7),
    ("aceite de aguaje 30 ml", 30),
    ("tónico de romero 50 ml", 15),
    ("agua de rosas 50 ml", 15),
    ("tónico egipcio 50 ml", 20),
    ("aceite de pepita de uva 30 ml", 22),
    ("exfoliante de rostro con arroz amazónico 25 g", 12),
    ("mascarilla de carbón activado 14 g", 10),
    ("aceite de manzanilla 30 ml", 30),
    ("jabón de caléndula 120 g", 13),
    ("jabón saponificado de cacao 90 g", 13),
    ("jabón saponificado de eucalipto 90 g", 13),
    ("jabón de lavanda 120 g", 13),
    ("jabón de arcilla verde 120 g", 13),
    ("jabón saponificado de manzanilla 90 g", 13),
    ("shampoo sólido de sangre de grado 50 g", 28),
    ("pulsera de palo santo", 15),
    ("incienso de palo santo", 12),
    ("3 piezas de madera de palo santo", 8),
    ("sahumerio de plantas medicinales", 10)
]

# Clasificacion de categorias
def clasificacion(prod):
    prod_lower = prod.lower()
    if "óleo aromático" in prod_lower or prod_lower.startswith("aceite") or prod_lower in ["pulsera de palo santo", "incienso de palo santo", "3 piezas de madera de palo santo", "sahumerio de plantas medicinales"]:
        return "aromaterapia"
    if "exfoliante" in prod_lower or "mascarilla" in prod_lower or "tónico" in prod_lower or "agua de rosas" in prod_lower:
        return "rostro"
    if prod_lower.startswith("jabón") or "bálsamo" in prod_lower:
        return "cuidado corporal"
    if "shampoo" in prod_lower:
        return "cabello"
    if "kombucha" in prod_lower or "kéfir" in prod_lower:
        return "probioticos"
    else:
        return "otros"

# Informacion de tienda
tiendas = [
    ("ForestLife", "OUT001", "TIER 1", "PEQUEÑA", "STAND", 2010),
    ("NaturaWood", "OUT002", "TIER 2", "MEDIANA", "TIENDA_INDEPENDIENTE", 2015),
    ("Biossellos", "OUT003", "TIER 1", "GRANDE", "SUPERMERCADO", 2005),
    ("EcoRaíces", "OUT004", "TIER 3", "MEDIANA", "MERCADO", 2018),
    ("VerdeAndino", "OUT005", "TIER 2", "PEQUEÑA", "STAND", 2020)
]

# Generacion de datasets
np.random.seed(42)
rows = []
for i in range(n):
    prod, price = productos[np.random.randint(len(productos))]
    tienda = tiendas[np.random.randint(len(tiendas))]
    conc_activo = round(np.random.uniform(0.5, 5.0), 2)
    article_id = f"FDX{np.random.randint(10000,99999)}"
    visibility = round(np.random.uniform(0.01, 0.1), 8)
    digits = ''.join(filter(str.isdigit, prod))
    weight = int(digits) if digits else np.random.randint(10, 100)
    sales = np.random.randint(0, 500)
    rating = round(np.random.uniform(1.0, 5.0), 1)
    
    rows.append({
        "Concentración ingrediente activo (%)": conc_activo,
        "ID_Articulo": article_id,
        "Tipo_Articulo": clasificacion(prod),
        "Tienda_Local": tienda[0],
        "Año_Establecimiento": tienda[5],
        "ID_Tienda": tienda[1],
        "Ubicación_Tienda": tienda[2],
        "Tamaño_Tienda": tienda[3],
        "Tipo_Tienda": tienda[4],
        "Visibilidad_Articulo": visibility,
        "Peso_articulo": weight,
        "Ventas": sales,
        "Calificacion": rating,
        "Nombre_Producto": prod,
        "Precio_soles": price
    })

df = pd.DataFrame(rows)
csv_path = 'C:/Users/aaiza/Documents/raiz-viva_data_analysis/datos/dataset_raiz-viva.csv'
df.to_csv(csv_path, index=False)

csv_path
