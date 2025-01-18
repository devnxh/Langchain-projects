import subprocess

def extract_audio(video_file_path, output_audio_path):
    
   
    command = [
        "C:\\ffmpeg\\bin\\ffmpeg.exe",
        "-i", video_path,  # Input video file
        "-q:a", "0",           # Highest quality audio
        "-map", "a",           # Extract only the audio stream
        audio_path
    ]
    
    # Run the command
    subprocess.run(command)

if __name__ == "__main__":
    # Example usage
    video_path = "D:\COURSES\INFOSYS\PROJECT\EE.mp4"  # Replace with your video file path
    audio_path = "D:\COURSES\INFOSYS\PROJECT\EE.wav"   # Replace with your desired audio file path
    
    extract_audio(video_path, audio_path)
    print("Extraction completed successfully!")
