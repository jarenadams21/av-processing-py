# Purpose
This repository explores audio and image processing, signalling concepts, and use cases in the context of python.

## Setup (can be abstracted)

1. Create a virtual python environment
- python -m venv tutorial-env
- source tutorial-env/bin/activate

2. Use pip to manage packages (here i am installing Gradio)
- pip install gradio

3. The demo below will appear automatically within the Jupyter Notebook, or pop in a browser on http://localhost:7860 if running from a script

* Target file : signal.py
- using 'gradio signal.py' will run the file with automatic refresh

>> Make sure new files are correctly placed in environment directory


## Random Notes

* The difference between gr.Audio(source='microphone') and gr.Audio(source='microphone', streaming=True), when both are used in gr.Interface(live=True), is that the first Component will automatically submit data and run the Interface function when the user stops recording, whereas the second Component will continuously send data and run the Interface function during recording.


* Example code of streaming images from webcam
```
import gradio as gr
import numpy as np

def flip(im):
    return np.flipud(im)

demo = gr.Interface(
    flip, 
    gr.Image(sources=["webcam"], streaming=True), 
    "image",
    live=True
)
demo.launch()
```