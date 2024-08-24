import requests
import concurrent.futures
import time

def get_definitions(word):
    url = f"https://jisho.org/api/v1/search/words?keyword={word}"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return None
        
        data = response.json()
        
        if not data['data']:
            return None
        
        # Iterating over all possible entries
        for entry in data['data']:
            reading = entry['japanese'][0].get('reading', None)
            japanese_word = entry['japanese'][0].get('word', reading)
            
            definitions = []
            for sense in entry['senses']:
                definitions.extend(sense['english_definitions'])
                if len(definitions) >= 3:
                    break
            
            flattened_definitions = definitions[:3]
            
            if japanese_word and reading and flattened_definitions:
                return japanese_word, reading, flattened_definitions
        
        return None
    except Exception as e:
        print(f"Error processing word '{word}': {e}")
        return None

def process_word(word):
    result = get_definitions(word)
    time.sleep(0.1)  # Small delay to prevent API rate limiting issues
    return result

def process_file(input_filename, output_filename, progress_callback, update_checking_label, clear_checking_label):
    not_found_words = []

    with open(input_filename, 'r', encoding='utf-8') as infile:
        words = [word.strip() for line in infile for word in line.replace('、', ',').replace(' ', ',').split(',') if word.strip()]
    
    total_words = len(words)
    words_checked = 0

    with open(output_filename, 'w', encoding='utf-8') as outfile:
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = {executor.submit(process_word, word): word for word in words}

            for future in concurrent.futures.as_completed(futures):
                word = futures[future]
                update_checking_label(word)
                
                result = future.result()
                if result:
                    japanese_word, reading, definitions = result
                    if japanese_word == reading:
                        outfile.write(f"{reading};{', '.join(definitions)};\n")
                    else:
                        outfile.write(f"{japanese_word}[{reading}];{', '.join(definitions)};\n")
                else:
                    not_found_words.append(word)

                words_checked += 1
                progress = words_checked / total_words
                progress_callback(progress)
        
        if not_found_words:
            outfile.write("\nDefinition Not Found for:\n")
            for word in not_found_words:
                outfile.write(f"{word}[];;\n")
    
    clear_checking_label()
