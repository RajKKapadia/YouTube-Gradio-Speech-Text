import gradio as gr

from utils import get_transcription

demo = gr.Interface(
    fn=get_transcription,
    inputs=[gr.components.Audio(label='Input', type='filepath'), gr.components.Audio(label='Input', type='filepath', source='microphone')],
    outputs=gr.components.Textbox(label='Transcription'),
    allow_flagging='never'
)
