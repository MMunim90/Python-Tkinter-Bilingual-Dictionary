# Munim's Dictionary

A desktop English–Bengali dictionary built with Python and Tkinter. Search English words, view their Bengali meanings, and listen to pronunciations using text-to-speech.

## Features

- *300 built-in dictionary entries** with English words and Bengali meanings
- **Autocomplete search** with alphabetically sorted suggestions
- **Case-insensitive lookup**
- **English pronunciation** using `pyttsx3` and the Windows SAPI5 speech engine
- **Bengali pronunciation** using `gTTS`
- **Stop Voice** control
- Simple desktop GUI built with Tkinter
- No backend or database required

## Project Structure

```text
munim-dictionary/
├── Python Tkinter Bilingual Dictionary.py
├── dictionary_data.py
└── README.md
```

- `Python Tkinter Bilingual Dictionary.py`: Main application, GUI, search, autocomplete, and voice controls.
- `dictionary_data.py`: Built-in dictionary data containing 300 English words and their Bengali meanings.

Keep both Python files in the same directory so the application can import the dictionary data.

## Requirements

- Python 3.12 or a compatible Python 3 version
- Tkinter (included with most standard Windows Python installations)
- `pyttsx3` for English text-to-speech
- `gTTS` for Bengali text-to-speech
- `pygame` for playing generated Bengali audio

## Installation

Open Command Prompt or a terminal in the project directory and install the required packages:

```bash
python -m pip install pyttsx3 gTTS pygame
```

## Run the Application

```bash
python "Python Tkinter Bilingual Dictionary.py"
```

## How to Use

1. Launch the application.
2. Type an English word in the search box.
3. Choose a word from the autocomplete suggestions, or finish typing it.
4. Click **Show** or press **Enter** to display the Bengali meaning.
5. Click **Speak English** to hear the English word.
6. Click **Speak Bangla** to hear the Bengali meaning.
7. Click **Stop Voice** to request that current speech stop.

If a word is not in the built-in dictionary, the app displays a “Meaning not found” message.

## Text-to-Speech Notes

### English voice

English speech uses `pyttsx3`, which works offline when a compatible Windows speech voice is installed. The application uses Windows SAPI5.

If English speech does not work, test the library with:

```bash
python -c "import pyttsx3; e=pyttsx3.init('sapi5'); e.say('Hello'); e.runAndWait()"
```

### Bengali voice

Bengali speech uses `gTTS`, which requires an internet connection to generate audio. `pygame` plays the generated audio.

If Bengali speech fails, check your internet connection and audio output.

## Editing the Dictionary

Open `dictionary_data.py` and edit the `DICTIONARY` mapping. Each entry follows this format:

```python
"Apple": "আপেল",
"Beautiful": "সুন্দর",
"Computer": "কম্পিউটার",
```

Use an English word as the key and its Bengali meaning as the value. Keep the two Python files in the same folder. The app sorts words alphabetically for suggestions.

## Troubleshooting

### `ModuleNotFoundError`

Install the dependencies using the same Python interpreter that runs the app:

```bash
python -m pip install pyttsx3 gTTS pygame
```

### English voice says `run loop already started`

Close other running instances of the application and try again. If the issue persists, check that Windows SAPI5 speech works with the standalone test shown above.

### Bengali voice is unavailable

Check your internet connection and confirm that your computer's audio output is working.

## Technologies

- Python
- Tkinter / ttk
- pyttsx3
- gTTS
- pygame

## License

Choose a license before publishing this project publicly. If you want others to use, modify, and distribute the code, consider adding an open-source license such as the MIT License.
