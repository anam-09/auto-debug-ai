
import gradio as gr
from agents.backend_api import analyze_error

def process_input(user_input):
    """
    Sends code/error input to backend API and returns AI suggestions.
    """
    try:
        result = analyze_error(user_input)
        return result
    except Exception as e:
        return f"Error processing input: {str(e)}"

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown(
        """
        # Auto Debug AI
        Enter your code snippet or error message below and get AI suggestions for fixes.
        """
    )
    
    with gr.Row():
        input_box = gr.Textbox(
            lines=5,
            placeholder="Paste your code or error here...",
            label="Input"
        )
        output_box = gr.Textbox(
            lines=10,
            placeholder="Analysis result will appear here...",
            label="Output"
        )
    
    submit_btn = gr.Button("Analyze")
    submit_btn.click(fn=process_input, inputs=input_box, outputs=output_box)

if __name__ == "__main__":
    demo.launch()