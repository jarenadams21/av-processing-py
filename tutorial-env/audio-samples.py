import gradio as gr
import librosa
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import numpy as np

# Signalling function to process audio from input
## Plots Amplitude against Time (Time Domain)
def time_domain(audio):
    print(audio)

    # Process audio input from user
    audio_file = open(audio, "rb")

    # Gather all samples and sample rate to be used in Spectrogram
    samples, sample_rate = librosa.load(audio_file, sr=None)

    # Create a plot
    ## Calculate time values in seconds
    time = np.linspace(0, len(samples) / sample_rate, num=len(samples))

    # Create a plot
    plt.figure(figsize=(14, 5))
    plt.plot(time, samples)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')


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
    fn=time_domain,
    inputs=gr.Audio(sources=["microphone"], type="filepath"),
    outputs="image"
)

if __name__ == "__main__":
    ul.launch(show_api=False)
