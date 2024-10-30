# StockAdvisorBot

StockAdvisorBot is a chatbot that serves as your mentor in the world of stock trading. This chatbot allows users to ask questions about the stock market, receive advice, export answers as PDF files, and display the trend chart of the S&P 500 index.

## Features

### 1. Q&A with the Chatbot
- Users can interact with the chatbot to ask questions about the stock market.
- Receive advice and analysis on suitable stocks based on the current market.

### 2. Download PDF
- After receiving an answer from the chatbot, users can export that answer as a PDF file.
- The PDF file can be saved or shared with others.

### 3. S&P 500 Trend Chart
- Display a chart representing the S&P 500 index over the years.
- Helps users gain a visual understanding of market trends.

## Technologies Used
- **Natural Language Processing**: Utilizes the Llama model API and LangChain to understand and analyze user queries.
- **Vector Database**: Uses Faiss for efficient data storage and querying.
- **PDF Export**: Uses ReportLab to export answers as PDF files.
- **User Interface**: Uses Streamlit to create a user-friendly interface.

## Installation
To install and run this project, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/KhaiLeeTran/StockAdvisorBot.git
   cd StockAdvisorBot/src

2. **Install Required Libraries**
   ```bash
   pip install -r requirements.txt
3. **Run the Application**
    ```bash
    streamlit run app.py
