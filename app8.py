import gradio as gr

def say_hi(name):
    return "hi:" + name

with gr.Blocks() as demo:
    inp = gr.Text()
    out = gr.Text()

    btn = gr.Button()

    btn.click(say_hi, inp, out)
    # 输入完回车直接触发事件
    inp.submit(say_hi, inp, out)


if __name__ == "__main__":
    demo.launch()