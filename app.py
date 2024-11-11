import streamlit as st
import pandas as pd

# 功能1：文件选择
st.title("CSV查询器")
uploaded_file = st.file_uploader("请选择需要解析的CSV文件", type="csv")

if uploaded_file is not None:
    # 读取CSV文件
    df = pd.read_csv(uploaded_file)
    st.write("CSV文件加载成功，数据预览如下：")
    st.dataframe(df)

    # 功能2：展示和查询CSV文件
    # 分数排序
    sort_option = st.selectbox("选择排序列", ["score_aes", "score_flow", "score_pref"])
    sort_order = st.radio("选择排序顺序", ["升序", "降序"])
    sorted_df = df.sort_values(by=sort_option, ascending=(sort_order == "升序"))

    # 分数区间过滤
    min_score, max_score = st.slider("选择分数区间", float(df[sort_option].min()), float(df[sort_option].max()), (float(df[sort_option].min()), float(df[sort_option].max())))
    filtered_df = sorted_df[(sorted_df[sort_option] >= min_score) & (sorted_df[sort_option] <= max_score)]

    st.write("按筛选条件过滤的结果：")
    st.dataframe(filtered_df)

    # 功能3：行数查询
    row_index = st.number_input("输入行号进行查询", min_value=0, max_value=len(df) - 1, step=1)
    if st.button("查询指定行信息"):
        selected_row = df.iloc[int(row_index)]
        st.write("查询结果：")
        st.write(f"path: {selected_row['path']}")
        st.write(f"text: {selected_row['text']}")
        st.write(f"高宽: {selected_row['height']}x{selected_row['width']}")
        st.write(f"fps: {selected_row['fps']}")