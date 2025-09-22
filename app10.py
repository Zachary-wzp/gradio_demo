from xmlrpc.client import escape

import gradio as gr

def plus(i):
    return i + 1

def substract(i):
    return str(i) - 1

def split(i):
    print(i)
    return 1 if i > 0 else -1

with gr.Blocks() as demo:
    n1 = gr.Number(label='n1')
    n2 = gr.Number(label='n2')
    n3 = gr.Number(label='n3')
    n4 = gr.Number(label='n4', value=99)

    btn = gr.Button()
    # 序列事件，且上一步报错不执行下一步
    btn.click(plus, n1, n2).success(substract, n2, n3).success(split, n3, n4)


if __name__ == "__main__":
    demo.launch()