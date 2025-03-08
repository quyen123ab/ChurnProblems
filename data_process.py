import pandas as pd

df = pd.read_csv(r"C:\Users\ADMIN\Downloads\WA_Fn-UseC_-Telco-Customer-Churn.csv") 

print(df.head()) # đầu tiên có thể df.head() để xem khái quát về dữ liệu
print(df.shape) # Xem các đặc trựng (features) và số dữ liệu có trong mỗi đặc trưng
print(df.isnull().sum()) # để kiểm tra xem có dữ liệu nào bị thiếu không nếu có vẽ bản đồ và kiểm tra số dữ liệu thiếu từng cột. Nếu không bắt đầu fit model. Ở đây không thiếu dữ liệu mọi người có thể thử lại nếu muốn

