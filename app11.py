import gradio as gr

def add_book(b, books):
    books.append(b)
    return books

with gr.Blocks() as demo:
    books = gr.State([]) # 会话状态
    inp = gr.Text()
    out = gr.Text()

    btn = gr.Button()

    btn.click(add_book, [inp, books], out)

if __name__ == "__main__":
    demo.launch()