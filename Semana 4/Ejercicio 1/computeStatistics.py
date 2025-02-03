import sys
import time

def read_numbers_from_file(file_path):
    """Lee números desde un archivo, ignorando datos inválidos."""
    numbers = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    numbers.append(float(line.strip()))
                except ValueError:
                    print(f"⚠️ [{file_path}] Dato inválido ignorado: {line.strip()}")
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{file_path}'.")
        return []
    return numbers

def compute_statistics(numbers):
    """Calcula estadísticas básicas."""
    if not numbers:
        return None

    n = len(numbers)
    mean = sum(numbers) / n
    sorted_numbers = sorted(numbers)
    median = sorted_numbers[n // 2] if n % 2 else (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2

    mode_counts = {}
    for num in numbers:
        mode_counts[num] = mode_counts.get(num, 0) + 1
    mode = max(mode_counts, key=mode_counts.get)

    variance = sum((x - mean) ** 2 for x in numbers) / n
    std_dev = variance ** 0.5

    return mean, median, mode, std_dev, variance

def save_results(results, file_name, elapsed_time):
    """Guarda los resultados en un archivo de salida."""
    output_file = f"StatisticsResults_{file_name}.txt"
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(f"Media: {results[0]:.2f}\n")
            file.write(f"Mediana: {results[1]:.2f}\n")
            file.write(f"Moda: {results[2]:.2f}\n")
            file.write(f"Desviación estándar: {results[3]:.2f}\n")
            file.write(f"Varianza: {results[4]:.2f}\n")
            file.write(f"Tiempo de ejecución: {elapsed_time:.4f} segundos\n")

        print(f"✅ Resultados guardados en '{output_file}'")
    except IOError:
        print(f"❌ Error: No se pudo escribir en '{output_file}'.")

def main():
    """Ejecuta el programa con múltiples archivos."""
    if len(sys.argv) < 2:
        print("\n❌ Error: Debes proporcionar al menos un archivo de datos.")
        print("📌 Uso correcto: python computeStatistics.py TC1.txt TC2.txt ... TC7.txt")
        sys.exit(1)

    for file_path in sys.argv[1:]:
        start_time = time.time()
        numbers = read_numbers_from_file(file_path)
        results = compute_statistics(numbers)
        elapsed_time = time.time() - start_time

        if results:
            save_results(results, file_path.split('.')[0], elapsed_time)

if __name__ == "__main__":
    main()
