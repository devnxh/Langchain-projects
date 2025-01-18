from gtts import gTTS

# Function to convert text to speech
def text_to_speech_from_file(filename, lang='en'):
    try:
        # Open the file using UTF-8 encoding
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

        # Convert text to speech using gTTS
        tts = gTTS(text=text, lang=lang, slow=False)
        
        # Define output file path
        output_path = r"D:\COURSES\INFOSYS\PROJECT\output.mp3"  # Use a raw string for the file path
        tts.save(output_path)  # Save the speech to a file
        
        print(f"Speech saved successfully to: {output_path}")

    except FileNotFoundError:
        print("Error: The specified file was not found. Please check the file path.")
    except UnicodeDecodeError:
        print("Error: Unable to decode the file. Please ensure it is saved with UTF-8 encoding.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Specify the text file to convert to speech
filename = r"D:\COURSES\INFOSYS\translated_hi.txt"  # Use a raw string for the file path

# Convert the text file to speech
text_to_speech_from_file(filename)
