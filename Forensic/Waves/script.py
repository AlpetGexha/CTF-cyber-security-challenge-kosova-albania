import matplotlib.pyplot as plt
from scipy.io import wavfile
import wave

# Step 1: Generate and Display the Spectrogram
def generate_spectrogram(file_path):
    print("Generating spectrogram...")
    sample_rate, audio_data = wavfile.read(file_path)

    # Check if the audio has multiple channels (e.g., stereo)
    if len(audio_data.shape) > 1:  # If it's a 2D array
        audio_data = audio_data.mean(axis=1)  # Convert to mono by averaging channels

    plt.specgram(audio_data, Fs=sample_rate, cmap='plasma')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.title('Spectrogram')
    plt.colorbar(label='Intensity (dB)')
    plt.show()

# Step 2: Extract Raw Audio Data for Inspection
def inspect_audio_data(file_path):
    print("Inspecting audio data...")
    with wave.open(file_path, 'rb') as audio_file:
        frames = audio_file.readframes(audio_file.getnframes())
        print("First 100 bytes of audio data:", frames[:100])

# Step 3: Decode Data Hidden in Least Significant Bits (LSB)
def decode_lsb(file_path):
    print("Decoding hidden data using LSB...")
    with wave.open(file_path, 'rb') as audio_file:
        frames = list(audio_file.readframes(audio_file.getnframes()))
    
    # Extract LSBs from each byte
    lsb = ''.join([str(frame & 1) for frame in frames])
    
    # Convert binary data to ASCII
    try:
        flag = ''.join([chr(int(lsb[i:i+8], 2)) for i in range(0, len(lsb), 8)])
        print("Hidden message (if any):", flag)
    except ValueError:
        print("No ASCII-encoded message found in LSB.")

# Main Function to Run All Steps
def main():
    file_path = 'Untitled.wav'  # Change to your .wav file path
    generate_spectrogram(file_path)
    inspect_audio_data(file_path)
    decode_lsb(file_path)

if __name__ == "__main__":
    main()
