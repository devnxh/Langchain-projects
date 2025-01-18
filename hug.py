from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torch
import librosa

def audio_to_text_in_chunks(audio_path, output_file, chunk_duration=30):
   
    # Load the processor and model
    processor = WhisperProcessor.from_pretrained("openai/whisper-medium")
    model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-medium")

    # Load the audio
    audio, rate = librosa.load(audio_path, sr=16000)

    # Calculate the number of samples per chunk
    chunk_samples = chunk_duration * rate

    # Split audio into chunks
    transcription = ""
    for start in range(0, len(audio), chunk_samples):
        # Extract chunk
        chunk = audio[start:start + chunk_samples]

        # Process the audio chunk
        inputs = processor(chunk, sampling_rate=rate, return_tensors="pt", padding=True)

        # Pad mel spectrogram features to length 3000 if necessary
        input_features = inputs["input_features"]
        if input_features.shape[-1] < 3000:
            padding = 3000 - input_features.shape[-1]
            input_features = torch.nn.functional.pad(input_features, (0, padding), mode="constant", value=0)

        # Perform inference
        with torch.no_grad():
            predicted_ids = model.generate(input_features)

        # Decode the transcription
        chunk_text = processor.decode(predicted_ids[0], skip_special_tokens=True)
        transcription += chunk_text + " "

    # Save the transcription to a text file
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(transcription.strip())
    
    print(f"Transcription saved to {output_file}")

# Input: Path to the audio file and output text file
audio_file = "D:/COURSES/INFOSYS/PROJECT/EE2.wav"  # Replace with your audio file path
output_file = "D:/COURSES/INFOSYS/PROJECT/transcription.txt"  # Replace with desired output file path

audio_to_text_in_chunks(audio_file, output_file)
