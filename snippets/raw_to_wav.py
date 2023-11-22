import wave

def convert_raw_to_wav(input_file, output_file, sample_rate, num_channels, sample_width):
    # Open the raw audio file for reading
    with open(input_file, 'rb') as raw_file:
        # Create a new WAV file
        with wave.open(output_file, 'wb') as wav_file:
            # Set the WAV file parameters
            wav_file.setnchannels(num_channels)
            wav_file.setsampwidth(sample_width)
            wav_file.setframerate(sample_rate)

            # Read the raw audio data
            raw_data = raw_file.read()

            # Write the raw audio data to the WAV file
            wav_file.writeframes(raw_data)

# Example usage
input_file = 'input.raw'
output_file = 'output.wav'
sample_rate = 8000  # Replace with the actual sample rate of your raw audio
num_channels = 1  # Replace with the actual number of channels of your raw audio
sample_width = 2  # Replace with the actual sample width (in bytes) of your raw audio

convert_raw_to_wav(input_file, output_file, sample_rate, num_channels, sample_width)
