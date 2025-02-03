import sys
import time
import re

def read_words(file_path):
    """Lee palabras de un archivo ignorando puntuación y errores."""
    words = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                words.extend(re.findall(r'\b\w+\b', line.lower()))  # Extrae palabras sin signos
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{file_path}'.")
        return []
    return words

def count_words(words):
    """Cuenta la frecuencia de cada palabra en el archivo."""
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def save_results(word_count, file_name, elapsed_time):
    """Guarda los resultados en un archivo de salida."""
    output_file = f"WordCountResults_{file_name}.txt"
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            for word, count in sorted(word_count.items()):
                file.write(f"{word}: {count}\n")
            file.write(f"Tiempo de ejecución: {elapsed_time:.4f} segundos\n")
        
        print(f"✅ Resultados guardados en '{output_file}'")
    except IOError:
        print(f"❌ Error: No se pudo escribir en '{output_file}'.")

def main():
    """Ejecuta el programa con múltiples archivos."""
    if len(sys.argv) < 2:
        print("\n❌ Error: Debes proporcionar al menos un archivo de texto.")
        print("📌 Uso correcto: python wordCount.py TC1.txt TC2.txt TC3.txt TC4.txt TC5.txt")
        sys.exit(1)

    for file_path in sys.argv[1:]:
        start_time = time.time()
        words = read_words(file_path)
        word_count = count_words(words)
        elapsed_time = time.time() - start_time

        if word_count:
            save_results(word_count, file_path.split('.')[0], elapsed_time)

if __name__ == "__main__":
    main()
