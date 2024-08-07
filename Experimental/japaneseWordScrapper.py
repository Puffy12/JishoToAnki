import requests

def get_definitions(word):
    url = f"https://jisho.org/api/v1/search/words?keyword={word}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    
    data = response.json()
    
    if not data['data']:
        return None
    
    entry = data['data'][0]
    reading = entry['japanese'][0]['reading']
    japanese_word = entry['japanese'][0].get('word', reading)  # Use reading if word doesn't exist
    definitions = [sense['english_definitions'] for sense in entry['senses'][:3]]  # Take first 3 senses
    flattened_definitions = [item for sublist in definitions for item in sublist][:3]  # Flatten and limit to 3
    
    return japanese_word, reading, flattened_definitions

def process_file(input_filename, output_filename):
    not_found_words = []
    
    with open(input_filename, 'r', encoding='utf-8') as infile, open(output_filename, 'w', encoding='utf-8') as outfile:
        words_checked = 0
        for line in infile:
            words = line.strip().split(',')
            for word in words:
                words_checked += 1
                if words_checked % 5 == 0:
                    print(f"Checking {word}")
                
                result = get_definitions(word)
                if result:
                    japanese_word, reading, definitions = result
                    if japanese_word == reading:
                        outfile.write(f"{reading};{', '.join(definitions)};\n")
                    else:
                        outfile.write(f"{japanese_word}[{reading}];{', '.join(definitions)};\n")
                else:
                    not_found_words.append(word)
        
        if not_found_words:
            outfile.write("\nDefinition Not Found:\n")
            for word in not_found_words:
                outfile.write(f"{word}\n")

if __name__ == "__main__":
    input_filename = "words.txt"  # Replace with your input file name
    output_filename = "output.txt"  # Replace with your desired output file name
    process_file(input_filename, output_filename)


