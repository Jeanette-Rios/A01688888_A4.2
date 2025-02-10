"""
Módulo para calcular el
total de ventas basado en registros
y un catálogo de precios.
Cumple con PEP8 y usa
TC1.ProductList.json como catálogo global.
"""
import json
import time
import os


def load_json(file_path):
    """Carga un archivo JSON y maneja errores."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error al cargar {file_path}: {e}")
        return None


def compute_sales(price_catalogue, sales_record):
    """Calcula el total de ventas basado en el catálogo de precios."""
    total_sales = 0.0
    errors = []
    # Convertir lista de productos a diccionario {nombre: precio}
    price_dict = {item['title']: item['price'] for item in price_catalogue}
    for sale in sales_record:
        product = sale.get('Product')  # Asegurar que se accede a 'Product'
        quantity = sale.get('Quantity', 0)
        if not product or product not in price_dict:
            errors.append(f"Producto desconocido: {product}")
            continue
        total_sales += price_dict[product] * quantity
    return total_sales, errors


def find_existing_file(base_name):
    """Verifica si un archivo existe con o sin extensión .json."""
    if os.path.exists(base_name):
        return base_name
    if os.path.exists(base_name + ".json"):
        return base_name + ".json"
    return None


def main():
    """
    Ejecuta el cálculo de ventas usando TC1.ProductList.json.
    Como catálogo global.
    """
    test_cases = ["TC1", "TC2", "TC3"]
    start_time = time.time()
    results = ""
    price_catalogue_file = find_existing_file("TC1.ProductList")
    if price_catalogue_file is None:
        print(
            "Error: No se encontró TC1.ProductList.json para uso global."
        )
        return
    price_catalogue = load_json(price_catalogue_file)
    for case in test_cases:
        sales_record_file = find_existing_file(f"{case}.Sales")
        if sales_record_file is None:
            results += f"Error en la carga de archivos para {case}\n"
            continue
        sales_record = load_json(sales_record_file)
        if sales_record is None:
            results += f"Error en la carga de archivos JSON para {case}\n"
            continue
        total_sales, errors = compute_sales(price_catalogue, sales_record)
        elapsed_time = time.time() - start_time
        results += f"\nResultados para {case}:\n"
        results += (
            f"Total ventas: ${total_sales:.2f}\n"
            f"Tiempo ejecución: {elapsed_time:.4f} s\n"
        )

        if errors:
            results += "\nErrores encontrados:\n" + "\n".join(errors) + "\n"
    print(results)
    with open("SalesResults.txt", "w", encoding="utf-8") as result_file:
        result_file.write(results)


if __name__ == "__main__":
    main()
