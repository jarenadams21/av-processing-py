import gradio as gr
import librosa
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

# Signalling function to process audio from input
def signalling(audio):
    print(audio)

    # Process audio input from user
    audio_file = open(audio, "rb")

    # Gather all samples and sample rate to be used in Spectrogram
    samples, sample_rate = librosa.load(audio_file, sr=None)

    # Create a plot
    plt.figure(figsize=(14, 5))
    plt.plot(samples)

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
    fn=signalling,
    inputs=gr.Audio(sources=["microphone"], type="filepath"),
    outputs="image"
)

if __name__ == "__main__":
    ul.launch(show_api=False)
