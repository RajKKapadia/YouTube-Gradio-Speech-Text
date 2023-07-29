import gradio as gr
from fastapi import FastAPI

from gradio_ui import demo

app = FastAPI()

@app.get('/')
async def home():
    return 'Gradio app is runing at the route /gradio', 200

app = gr.mount_gradio_app(app, demo, path='/gradio')
