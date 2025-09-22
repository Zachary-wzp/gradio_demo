import gradio as gr

# 布局组件简介
# gr.Row: 将组件水平排列（在同一行中）
# gr.Column: 将组件垂直排列（在同一列中）
# gr.Group: 用于对一组组件进行逻辑分组，通常在不显示控制布局时使用，
# gr.Tab: 创建选项卡布局，用于在页面中分隔不同的内容
# gr.Accordion: 创建可折叠的内容块

# with gr.Blocks() as demo:
#     with gr.Accordion("SSSS", open=False):
#         with gr.Tab("AAAA"):
#             with gr.Tab("tab1"):
#                 with gr.Row():
#                     # 纵向排列变为水平排列
#                     gr.Text("aaa", scale=1)
#                     gr.Text(scale=3)
#                     with gr.Column():
#                         gr.Text(scale=0, min_width=100)
#                         gr.Text(scale=0, min_width=100)
#                         gr.Text(scale=0, min_width=100)
#
#             with gr.Tab("tab2"):
#                 with gr.Row():
#                     # 纵向排列变为水平排列
#                     gr.Text()
#                     gr.Text()
#                     with gr.Column():
#                         gr.Text()
#                         gr.Text()
#                         gr.Text()
#
#         with gr.Tab("BBBB"):
#             with gr.Tab("tab1"):
#                 with gr.Row():
#                     # 纵向排列变为水平排列
#                     gr.Text("aaa")
#                     gr.Text()
#                     with gr.Column():
#                         gr.Text()
#                         gr.Text()
#                         gr.Text()
#
#             with gr.Tab("tab2"):
#                 with gr.Row():
#                     # 纵向排列变为水平排列
#                     gr.Text()
#                     gr.Text()
#                     with gr.Column():
#                         gr.Text()
#                         gr.Text()
#                         gr.Text()

with gr.Blocks(fill_height=True, fill_width=True) as demo:

    # with gr.Row(equal_height=True):
    #     gr.Text(lines=10)
    #     gr.Textbox()
    #     gr.TextArea() # 多行的text box相当于Text设置lines
    #     gr.Audio()

    gr.Chatbot(scale=1)
    gr.Text()


if __name__ == "__main__":
    demo.launch()