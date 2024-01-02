import gradio as gr
import librosa
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import numpy as np

# Signalling function to process audio from input
def mel_spectrogram(audio):
    print(audio)

    # Process audio input from user
    audio_file = open(audio, "rb")

    # Gather all samples and sample rate to be used in Spectrogram
    samples, sample_rate = librosa.load(audio_file, sr=None)

    # Create a plot
    ## Calculate time values in seconds
    start_sample = 0  # Start at the beginning
    end_sample = int(30 * sample_rate)  # End at 30 seconds
    segment_samples = samples[start_sample:end_sample]

    # Create a plot
    # Calculate time values in seconds for the segment
    time = np.linspace(0, len(segment_samples) / sample_rate, num=len(segment_samples))

    # Create a Mel scale spectrogram for the segment
    sgram = librosa.stft(segment_samples)
    sgram_mag, _ = librosa.magphase(sgram)
    mel_scale_sgram = librosa.feature.melspectrogram(S=sgram_mag, sr=sample_rate)
    mel_sgram = librosa.amplitude_to_db(mel_scale_sgram, ref=np.min)

    # Display the Mel spectrogram
    librosa.display.specshow(mel_sgram, sr=sample_rate, x_axis='time', y_axis='mel')
    plt.colorbar(format='%+2.0f dB')
    plt.show()


    # Save the plot to a buffer
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    # Convert buffer to PIL image
    image = Image.open(buf)

    # Close the figure
    plt.close()

    return image

# Create a Gradio interface
ul = gr.Interface(
    fn=mel_spectrogram,
    inputs=gr.Audio(sources=["microphone"], type="filepath"),
    outputs="image"
)

if __name__ == "__main__":
    ul.launch(show_api=False)
