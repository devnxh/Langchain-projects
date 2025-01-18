import ffmpeg

# Using raw strings for file paths to avoid escape sequence warnings
video_file = r'D:\COURSES\INFOSYS\PROJECT\EE.mp4'
audio_file = r'D:\COURSES\INFOSYS\PROJECT\output.mp3'
output_file = r'D:\COURSES\INFOSYS\PROJECT\EE2.mp4'

# Input the video and audio streams
video_stream = ffmpeg.input(video_file)
audio_stream = ffmpeg.input(audio_file)

# Output the new video with replaced audio
ffmpeg.output(video_stream.video, audio_stream.audio, output_file, vcodec='copy', acodec='aac').run()
