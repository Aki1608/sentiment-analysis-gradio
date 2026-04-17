import gradio as gr
from model_logic import ModelLogic

get_prediction = ModelLogic.get_prediction
demo = gr.Interface(fn=get_prediction, inputs="text", outputs="text")

demo.launch()