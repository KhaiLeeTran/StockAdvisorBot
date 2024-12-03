# Giả định rằng các phần cần thiết của Chat đã được triển khai chính xác
from qa_tool import*
from csv_load import*
from data_analysis import*
from summarize_prompt import QA_PROMPT_TEMPLATE
from download_report import create_pdf
import streamlit as st



df = DataAnalysis('D:\project\chatbot_stock\data\dataframe.csv')

csv_ = CSVLoaderCustom(path_file='D:\project\chatbot_stock\data\dataframe.csv')
loader = csv_.split_load()
# Khởi tạo Chat
chat_instance = Chat(
    model_name="llama-3.1-70b-versatile",        # Ví dụ, bạn có thể thay đổi model_name thành bất kỳ mô hình nào bạn sử dụng
    API_KEY="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", # API key thật của bạn
    temperature=0.2,           # Nhiệt độ (temperature) của mô hình
    db_path="D:\project\chatbot_stock\data",  # Đường dẫn cơ sở dữ liệu đã tạo
    loader=loader,     # Loader chứa dữ liệu bạn muốn sử dụng
    prompt=QA_PROMPT_TEMPLATE  # Prompt template
    )



st.title('Stock tips bot')

user_query = st.text_input("Hello! How is the stock market performing today? Please provide me with the latest information on stock indices and notable stocks.")
answer = None
if st.button('Answer'):
    if user_query:
        try:
            answer = chat_instance.qa_bot(user_query)
            st.write("Answer:", answer)
        except Exception as e:
            st.write("An error occurred:", e)
    else:
        st.write("Please enter a question.")


if answer:
    pdf_buffer = create_pdf(answer)
    st.download_button(
        label="Download PDF file",
        data=pdf_buffer,
        file_name="Report.pdf",
        mime="application/pdf"
    )

st.title('S&P 500 Index Value Trends')
# Đường dẫn tới file dữ liệu (có thể cho phép người dùng upload file)
data_file = "D:\project\chatbot_stock\data\sp500_index.csv"

if data_file is not None:
   # Tạo đối tượng DataAnalysis
    analysis = DataAnalysis(data_file)
    
    # Xử lý dữ liệu
    df_processed = analysis.create_df()

    # Hiển thị biểu đồ đường với Streamlit
    st.line_chart(df_processed)