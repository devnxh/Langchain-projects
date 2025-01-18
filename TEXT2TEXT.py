from googletrans import Translator, LANGUAGES

def translate_file(file_path, target_language):
    try:
        # Open and read the content of the text file
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Initialize the translator
        translator = Translator()

        # Translate the text
        translated = translator.translate(text, dest=target_language)

        # Print the translated text
        print("\nTranslated Text:")
        print(translated.text)

        # Save the translated text to a new file
        output_file = f"translated_{target_language}.txt"
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(translated.text)

        print(f"\nThe translated text has been saved to {output_file}")

    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Available languages:")
    for lang_code, lang_name in LANGUAGES.items():
        print(f"{lang_name.title()} ({lang_code})")

    # Get the file path and target language from the user
    file_path = input("\nEnter the path to the text file: ")
    target_language = input("Enter the target language code (e.g., 'fr' for French, 'es' for Spanish): ")

    # Call the function to translate the file
    translate_file(file_path, target_language)
