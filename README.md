# JishoToAnki

**JishoToAnki** is a tool designed to translate lists of Japanese words from text files using the Jisho API. It formats the translations, including definitions and readings, for easy import into Anki. This application helps you efficiently study and memorize Japanese vocabulary by converting your word lists into a format optimized for flashcard use.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Example](#example)
- [Requirements](#requirements)
- [Troubleshooting](#troubleshooting)
- [Developer Instructions](#developer-instructions)
- [Contributing](#contributing)
- [Contact](#contact)

  
## Features

- Translate Japanese words from text files using the Jisho API.
- Format translations with definitions and readings.
- Create files ready for quick import into Anki.
- Simple and user-friendly graphical interface for easy use.

## Installation

1. **Download the Application:**
   - Download the [latest release](https://github.com/Puffy12/Japanese-Word-Dumper/releases/tag/v1.0.0) of JishoToAnki.

2. **Extract the Files:**
   - Extract the contents of the downloaded archive to a folder named `JishoToAnki`.

3. **Run the Application:**
   - Navigate to the extracted `JishoToAnki` folder.
   - Double-click the `JishoToAnki.exe` file to launch the application.
   - Make sure the icon.ico file is in the same folder or the program will throw an error

## Usage

1. **Input File:**
   - Ensure your input file contains a list of Japanese words separated by commas.
   - Use the "Browse Words File..." button to select your input file.

2. **Output File:**
   - Choose where you want to save the translated output file using the "Browse Output File..." button.

3. **Translate:**
   - Click the "Translate" button to start the translation process. The progress bar will show the status of the translation.

4. **Cancel:**
   - Click the "Close" button to cancel the operation at any time.

## Example

Ensure that your input file (e.g., `Example_Words.txt`) has words separated by commas:


## Requirements

- Windows OS
- Python 3.8 or later (for running the script, if needed)

## Troubleshooting

- **Progress Bar Issue:**
  - If the progress bar starts half full or behaves unexpectedly, ensure the application is up-to-date. Restart the application if needed.

- **Tkinter Issue:**
  - Make sure you have `tcl` and `tk` folders in the proper locations. Check your error logs for their required locations.
  - Move the `tcl8.6` and `tk8.6` (or the version you are using) folders to the correct location as described in [this Stack Overflow article](https://stackoverflow.com/questions/29320039/python-tkinter-throwing-tcl-error).

## Developer Instructions

1. **Activate the Virtual Environment:**
   - Run `.\Scripts\activate` to activate the virtual environment.

2. **Run the Application:**
   - Execute the script with `python ./app.py`.

3. **Deactivate the Virtual Environment:**
   - Run `deactivate` to deactivate the virtual environment after you're done.

Make sure to install all required dependencies listed in `requirements.txt` before running the application.

## Contributing

Feel free to contribute by submitting issues or pull requests on [GitHub](https://github.com/Puffy12/Japanese-Word-Dumper).

## Contact

For any questions or support, please contact me at my website [here](https://michaelmehrdadi.vercel.app/).

---
