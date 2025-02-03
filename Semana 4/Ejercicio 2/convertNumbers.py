import sys
import time

def to_binary(n):
    """Convierte un número a binario sin usar bin()."""
    return bin(n)[2:]

def to_hexadecimal(n):
    """Convierte un número a hexadecimal sin usar hex()."""
    hex_digits = "0123456789ABCDEF"
    hex_value = ""
    while n > 0:
        hex_value = hex_digits[n % 16] + hex_value
        n //= 16
    return hex_value if hex_value else "0"

def read_numbers(file_path):
    """Lee números del archivo y los convierte."""
    conversions = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    num = int(line.strip())
                    conversions.append((num, to_binary(num), to_hexadecimal(num)))
                except ValueError:
                    print(f"⚠️ [{file_path}] Dato inválido ignorado: {line.strip()}")
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{file_path}'.")
        return []
    return conversions

def save_results(conversions, file_name, elapsed_time):
    """Guarda los resultados en un archivo."""
    output_file = f"ConversionResults_{file_name}.txt"
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            for num, binary, hexa in conversions:
                file.write(f"Número: {num} -> Binario: {binary} -> Hexadecimal: {hexa}\n")
            file.write(f"Tiempo de ejecución: {elapsed_time:.4f} segundos\n")

        print(f"✅ Resultados guardados en '{output_file}'")
    except IOError:
        print(f"❌ Error: No se pudo escribir en '{output_file}'.")

def main():
    """Ejecuta el programa con múltiples archivos."""
    if len(sys.argv) < 2:
        print("\n❌ Error: Debes proporcionar al menos un archivo de datos.")
        print("📌 Uso correcto: python convertNumbers.py TC1.txt TC2.txt TC3.txt TC4.txt")
        sys.exit(1)

    for file_path in sys.argv[1:]:
        start_time = time.time()
        conversions = read_numbers(file_path)
        elapsed_time = time.time() - start_time

        if conversions:
            save_results(conversions, file_path.split('.')[0], elapsed_time)

if __name__ == "__main__":
    main()
