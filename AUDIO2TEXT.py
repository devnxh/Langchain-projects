import speech_recognition as sr

def audio_to_text(audio_path, output_file):
    
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load the audio file
    try:
        with sr.AudioFile(audio_path) as source:
            print("Processing audio...")
            audio = recognizer.record(source)  # Read the entire audio file
    except Exception as e:
        print(f"Error loading audio file: {e}")
        return

    # Perform recognition
    try:
        print("Transcribing audio...")
        transcription = recognizer.recognize_google(audio)  # Using Google's Web Speech API
        print("Transcription completed.")

        # Save the transcription to a text file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(transcription)
        print(f"Transcription saved to {output_file}")
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand the audio.")
    except sr.RequestError as e:
        print(f"Error with the SpeechRecognition service: {e}")

# Input: Path to the audio file and output text file
audio_file = "D:/COURSES/INFOSYS/PROJECT/EE.wav"  # Replace with your audio file path
output_file = "D:/COURSES/INFOSYS/PROJECT/EE.txt"  # Replace with desired output file path

audio_to_text(audio_file, output_file)
