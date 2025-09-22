import gradio as gr

def say_hi(name):
    return "say hi" + name + "!"

def say_hello(name):
    return "say hello" + name + "!"

hi = gr.Interface(
    fn=say_hi,
    inputs="text",
    outputs="text"
)

hello = gr.Interface(
    fn=say_hello,
    inputs="text",
    outputs="text"
)

# 两个Interface集成到一个界面
demo = gr.TabbedInterface(
    interface_list=[hi, hello],
    tab_names=['hi', 'hello']
)

if __name__ == "__main__":
    demo.launch()