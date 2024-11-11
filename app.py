import streamlit as st
import pandas as pd

# 行数超过指定条目后提示，可能加载过慢
MAX_ROWS_TO_DISPLAY = 10000

st.title("CSV查询器")
uploaded_file = st.file_uploader("选择需要解析的CSV文件", type="csv")

if uploaded_file is not None:
    # 调用系统窗口选择需要读取的CSV文件
    df = pd.read_csv(uploaded_file)
    # 判断文件大小
    if len(df) <= MAX_ROWS_TO_DISPLAY:
        st.write("CSV文件加载成功，数据表预览如下：")
        st.dataframe(df)
    else:
        st.write(f"文件行数超过{MAX_ROWS_TO_DISPLAY}行，加载速度可能变慢")
        st.dataframe(df)

    # 动态生成可用的排序选项
    available_sort_columns = [col for col in ["score_aes", "score_flow", "score_pref"] if col in df.columns]
    if not available_sort_columns:
        st.write("未找到任何可用于排序的列，请检查表格中是否包含aes/flow/pref打分")
    else:
        # 排序方式
        sort_option = st.selectbox("选择排序方式", available_sort_columns)
        sort_order = st.radio("选择排序顺序", ["升序", "降序"])
        sorted_df = df.sort_values(by=sort_option, ascending=(sort_order == "升序"))
        # 分数区间过滤
        min_score, max_score = st.slider("选择分数区间", float(df[sort_option].min()), float(df[sort_option].max()), (float(df[sort_option].min()), float(df[sort_option].max())))
        filtered_df = sorted_df[(sorted_df[sort_option] >= min_score) & (sorted_df[sort_option] <= max_score)]
        st.write(f"过滤结果：已筛选出 {len(filtered_df)} 行")
        st.dataframe(filtered_df)
        #指定行号查询
        with st.container():
            st.write("指定行信息查询")
            row_index = st.number_input("输入行号",min_value=0, max_value=len(df) - 1, step=1)
            # 检查输入
            if row_index < 0 or row_index >= len(df):
                st.warning(f"行号应在 0 到 {len(df) - 1} 之间")
                row_index = None
            query_button = st.button("查询")

            # 查询结果显示
            if query_button:
                selected_row = df.iloc[int(row_index)]
                st.write("查询结果：")
                st.write(f"path: {selected_row['path']}")
                st.write(f"text: {selected_row['text']}")
                st.write(f"宽高: {selected_row['width']}x{selected_row['height']}")
                st.write(f"fps: {selected_row['fps']}")