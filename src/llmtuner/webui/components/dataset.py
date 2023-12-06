import os
import json
import gradio as gr
from typing import TYPE_CHECKING, Any, Dict, Tuple
from llmtuner.extras.constants import METHODS, SUPPORTED_MODELS

if TYPE_CHECKING:
    from gradio.components import Component

def create_dataset_box() -> Dict[str, "Component"]:
    available_models = list(SUPPORTED_MODELS.keys()) + ["Custom"]
    with gr.Row():
        lang = gr.Dropdown(choices=["en", "zh"], scale=1)
        model_name = gr.Dropdown(choices=available_models, scale=3)
        model_path = gr.Textbox(scale=3)
    return dict(
        lang=lang,
        model_name=model_name,
        model_path=model_path
    )