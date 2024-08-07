import requests

def get_definitions(word):
    """
    Fetches definitions for a given Japanese word from the Jisho API.
    
    Args:
        word (str): The Japanese word to look up.
    
    Returns:
        tuple: A tuple containing:
            - Japanese word (str) or reading if word does not exist
            - Reading of the Japanese word (str)
            - List of up to three English definitions (list of str)
    """
    url = f"https://jisho.org/api/v1/search/words?keyword={word}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    
    data = response.json()
    
    if not data['data']:
        return None
    
    entry = data['data'][0]
    reading = entry['japanese'][0]['reading']
    japanese_word = entry['japanese'][0].get('word', reading)
    definitions = [sense['english_definitions'] for sense in entry['senses'][:3]]
    flattened_definitions = [item for sublist in definitions for item in sublist][:3]
    
    return japanese_word, reading, flattened_definitions

def process_file(input_filename, output_filename, progress_callback):
    """
    Processes the input file and writes the definitions to the output file.
    Updates progress via a callback function.
    
    Args:
        input_filename (str): The path to the input file containing Japanese words.
        output_filename (str): The path to the output file where definitions will be written.
        progress_callback (function): A callback function to update progress (takes float).
    """
    not_found_words = []
    
    # First pass to count the total number of words
    with open(input_filename, 'r', encoding='utf-8') as infile:
        total_words = sum(len(line.strip().split(',')) for line in infile)
    
    words_checked = 0
    
    with open(input_filename, 'r', encoding='utf-8') as infile, open(output_filename, 'w', encoding='utf-8') as outfile:
        for line in infile:
            words = line.strip().split(',')
            for word in words:
            
                result = get_definitions(word)
                if result:
                    japanese_word, reading, definitions = result
                    if japanese_word == reading:
                        outfile.write(f"{reading} -> {', '.join(definitions)}\n")
                    else:
                        outfile.write(f"{japanese_word}[{reading}];{', '.join(definitions)};\n")
                else:
                    not_found_words.append(word)
                    
                    
                words_checked += 1
                if words_checked % 5 == 0:
                    print(f"Checking {word}")
                    
                progress = words_checked / total_words
                progress_callback(progress)
        
        if not_found_words:
            outfile.write("\nDefinition Not Found:\n")
            for word in not_found_words:
                outfile.write(f"{word}\n")
