import gradio as gr

def say_hi(name):
    return "hi:" + name

def say_no(name):
    return "no:" + name

with gr.Blocks() as demo:
    inp = gr.Text()
    out1 = gr.Text()
    out2 = gr.Text()

    btn_hi = gr.Button("say hi")
    btn_no = gr.Button("say no")

    # 一个button可绑定两个事件，也可以分别绑定一个事件
    btn_hi.click(say_hi, inp, out1)
    btn_no.click(say_no, inp, out2)




if __name__ == "__main__":
    demo.launch()