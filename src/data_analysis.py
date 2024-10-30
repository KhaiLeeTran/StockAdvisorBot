import pandas as pd
import matplotlib.pyplot as plt

class DataAnalysis:
    def __init__(self, data_path: str):
        self._df = pd.read_csv(data_path)
    
    def create_df(self):
        # Giả sử cột Date là 'Date' và cột cần vẽ là 'S&P500'
        # Chuyển đổi cột 'Date' thành datetime
        self._df['Date'] = pd.to_datetime(self._df['Date'])

        # Đặt 'Date' làm index
        self._df.set_index('Date', inplace=True)

        return self._df