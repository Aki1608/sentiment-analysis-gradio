import gradio as gr
from model_logic import get_prediction

demo = gr.Interface(fn=get_prediction, inputs="text", output="text")

demo.launch()