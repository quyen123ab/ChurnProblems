import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv(r"C:\Users\ADMIN\Downloads\WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Chuyển cột 'Churn' sang dạng số (nếu chưa)
df['Churn'] = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)

# Chia dữ liệu thành hai nhóm
churned = df[df['Churn'] == 1]   # Nhóm khách hàng rời đi
stayed = df[df['Churn'] == 0]    # Nhóm khách hàng ở lại

# Xem thống kê mô tả
print("Thống kê mô tả khách hàng rời đi:")
print(churned.describe())

print("\nThống kê mô tả khách hàng ở lại:")
print(stayed.describe())

plt.figure(figsize=(8, 6))
sns.histplot(df, x='tenure', hue='Churn', kde=True, bins=30)
plt.title('Phân bố tuổi thọ khách hàng theo trạng thái rời bỏ')
plt.xlabel('Số tháng sử dụng')
plt.ylabel('Số lượng khách hàng')
plt.show()
