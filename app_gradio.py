import gradio as gr
import pandas as pd


# 定义排序和筛选的主函数
def process_csv(file, sort_column, sort_order, min_score, max_score, row_index):
    if file is None:
        return "Please upload a CSV file.", None, None

    # 读取CSV文件
    df = pd.read_csv(file)

    # 检查文件行数，避免显示过大的文件
    if len(df) > 10000:
        message = "The file is too large to display fully. Please use the filtering options below."
    else:
        message = "File loaded successfully. You can sort and filter the data."

    # 检查是否存在排序列
    available_sort_columns = [col for col in ["score_aes", "score_flow", "score_pref"] if col in df.columns]
    if not available_sort_columns:
        return "No sortable columns found in the CSV file.", None, None

    # 进行排序
    if sort_column in available_sort_columns:
        ascending = sort_order == "Ascending"
        df = df.sort_values(by=sort_column, ascending=ascending)

    # 进行分数区间过滤
    df_filtered = df[(df[sort_column] >= min_score) & (df[sort_column] <= max_score)]

    # 提取行号信息
    if 0 <= row_index < len(df):
        selected_row = df.iloc[int(row_index)]
        row_info = {
            "path": selected_row.get("path", "N/A"),
            "text": selected_row.get("text", "N/A"),
            "height": selected_row.get("height", "N/A"),
            "width": selected_row.get("width", "N/A"),
            "fps": selected_row.get("fps", "N/A"),
        }
    else:
        row_info = "Invalid row index."

    return message, df_filtered, row_info


# 定义gradio接口
with gr.Blocks() as demo:
    gr.Markdown("# CSV Detector")

    # 文件上传
    file = gr.File(label="Upload CSV File", type="filepath")

    # 选择排序列
    sort_column = gr.Dropdown(choices=["score_aes", "score_flow", "score_pref"], label="Sort Column", value="score_aes")
    sort_order = gr.Radio(["Ascending", "Descending"], label="Sort Order", value="Ascending")

    # 设置分数过滤范围
    min_score = gr.Number(label="Min Score", value=0)
    max_score = gr.Number(label="Max Score", value=10)

    # 行号查询
    row_index = gr.Number(label="Enter Row Index", value=0)

    # 输出结果
    message = gr.Textbox(label="Status Message", interactive=False)
    display_df = gr.Dataframe(label="Filtered Data")
    row_info = gr.JSON(label="Row Information")

    # 按钮触发处理
    submit_btn = gr.Button("Process CSV")
    submit_btn.click(
        process_csv,
        inputs=[file, sort_column, sort_order, min_score, max_score, row_index],
        outputs=[message, display_df, row_info],
    )

demo.launch()
