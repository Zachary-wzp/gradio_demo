import gradio as gr

with gr.Blocks() as demo:

    gr.Markdown("""
    # h1
    ## h2
    ### h3
    """)

    gr.HTML("""
    <h1>AAAA </h1>
    """)


if __name__ == "__main__":
    demo.launch()