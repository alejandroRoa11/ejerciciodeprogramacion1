import sys
import time

def main():
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        start = time.time()
        with open(filename, 'r') as file:
            archivo = file.read()
        word_frequencies = {}
        output2 = "Distinct words and their frequencies:\n"
        current_word = ''
        for char in archivo:
            if char.isalnum():
                current_word += char.lower()
            else:
                if current_word != '':
                    if current_word in word_frequencies:
                        word_frequencies[current_word] += 1
                    else:
                        word_frequencies[current_word] = 1
                    current_word = ''
        
        if current_word != '':
            if current_word in word_frequencies:
                word_frequencies[current_word] += 1
            else:
                word_frequencies[current_word] = 1

        print("Distinct words and their frequencies:")
        for word, frequency in word_frequencies.items():
            print(f"{word}: {frequency}")

            output = str(word)+": "+str(frequency)
            output2 = output2 + output+"\n"
        end = time.time()
        length = end - start
        tiempo = "\ntomó "+str(length)+" segundos"
        print(tiempo)
        with open('/Users/alejandro/Desktop/statsFour/wordCountResults.txt', 'w') as file:
            file.write(output2+tiempo)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

#python3 /Users/alejandro/Desktop/statsFour/wordCount.py /Users/alejandro/Desktop/statsFour/archivo.txt

#python3 /Users/alejandro/Desktop/statsFour/wordCount.py /Users/alejandro/Desktop/codigoQualitySoftware/ArchivosDeApoyo/P3/TC1.txt
#python3 /Users/alejandro/Desktop/statsFour/wordCount.py /Users/alejandro/Desktop/codigoQualitySoftware/ArchivosDeApoyo/P3/TC2.txt
#python3 /Users/alejandro/Desktop/statsFour/wordCount.py /Users/alejandro/Desktop/codigoQualitySoftware/ArchivosDeApoyo/P3/TC3.txt
#python3 /Users/alejandro/Desktop/statsFour/wordCount.py /Users/alejandro/Desktop/codigoQualitySoftware/ArchivosDeApoyo/P3/TC4.txt
#python3 /Users/alejandro/Desktop/statsFour/wordCount.py /Users/alejandro/Desktop/codigoQualitySoftware/ArchivosDeApoyo/P3/TC5.txt