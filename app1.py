import gradio as gr

def generate_story(a, b, c, d, e, f):
    return f"{a} {b} {c} {d} {e} {f}"

demo = gr.Interface(
    fn=generate_story,
    inputs=[
        # 滑块，value为默认值
        gr.Slider(2, 20, value=4, label='Count', info='Choose between 2 and 20'),
        # 下拉列表（单选）
        gr.Dropdown(
            ['cat', 'dog', 'bird'], label='Animal', info='Animals here'
        ),
        # 多选框
        gr.CheckboxGroup(
            ['usa', 'japan', 'china'], label='Country', info='Choose country'
        ),
        # 单选框
        gr.Radio(
            ['park', 'zoo', 'road']
        ),
        # 下拉列表（多选）
        gr.Dropdown(
            ['ran', 'swam', 'ate', 'slept'], value=['swam', 'slept'], multiselect=True,
        ),
        # 只有一个选项的多选框
        gr.Checkbox(label='Morning', info='Did they do it in the morning?')
    ], # 'text' -> gr.Text()
    outputs="text",
    examples=[
        [2, "cat", ["japan", "Pakistan"], "park", ["ate", "swam"], True],
        [4, "dog", ["japan"], "zoo", ["ate", "swam"], False]
    ],
    title="This is a title",
    description="aaaaaaaaa",
    article="bbbbbbbbb"
)

if __name__ == "__main__":
    demo.launch()