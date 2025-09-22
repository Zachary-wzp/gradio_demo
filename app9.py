import gradio as gr


def modify(v: bool):
    return gr.Text(value="modify", visible=v, lines=3)

with gr.Blocks() as demo:
    inp = gr.Checkbox()
    out = gr.Text()

    # Checkbox返回一个True/False，modify会把return里Text的参数返回给out里的Text
    inp.change(modify, inp, out)

if __name__ == "__main__":
    demo.launch()