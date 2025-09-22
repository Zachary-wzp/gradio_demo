import gradio as gr

def echo(message, history):
    return f"you typed: {message}"

demo = gr.ChatInterface(
    fn=echo,
    examples=["hello", "hola", "merhaba"],
    title="Echo Bot",
    # 鼠标光标自动锁定到输入框
    autofocus=True,
    description="aaaa"
)

if __name__ == "__main__":
    demo.launch()