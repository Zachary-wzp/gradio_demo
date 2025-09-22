import gradio as gr

def say_hi(name):
    return "hi:" + name

with gr.Blocks() as demo:
    inp = gr.Radio(['cat', 'dog', 'fish'])
    out = gr.Text()

    # inp发生时，out直接显示改变后的结果
    inp.change(say_hi, inp, out)

if __name__ == "__main__":
    demo.launch()