import gradio as gr


def greet(name, age):
    return "hello" + name + str(age)

with gr.Blocks() as demo:
    name = gr.Text(label="input your name")
    age = gr.Number(label="age")
    output = gr.Text(label="output")

    btn = gr.Button("greet")

    btn.click(
        fn=greet,
        inputs=[name, age],
        outputs=output
    )

    # 给个example，且需要绑定至相应的位置
    examples = gr.Examples(
        examples=[
            ['a', 1],
            ['b', 3]
        ],
        inputs=[name, age]
    )




if __name__ == "__main__":
    demo.launch()