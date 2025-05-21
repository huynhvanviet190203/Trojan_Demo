# 🐍 Mô phỏng Trojan bằng Python (Dự án học tập)

> ⚠️ **Cảnh báo:** Dự án này chỉ dành cho mục đích **học tập và nghiên cứu an toàn thông tin**. Tuyệt đối **không sử dụng cho mục đích xấu hoặc thực tế**. Tác giả không chịu trách nhiệm nếu có hành vi sai phạm.

## 📌 Giới thiệu

Dự án mô phỏng cách hoạt động cơ bản của một **trojan/backdoor client-server** viết bằng Python. Mục tiêu là giúp sinh viên ngành An toàn thông tin hiểu rõ về cơ chế kết nối ngược, gửi lệnh từ xa, ghi phím,... trong môi trường kiểm soát như máy ảo.

## 📁 Cấu trúc thư mục


## ⚙️ Hoạt động ra sao?

- **client** đóng vai máy bị nhiễm, chủ động kết nối đến server.
- **server** là nơi điều khiển, có thể gửi các lệnh từ xa, mô phỏng một số tính năng:
  - Gửi lệnh hệ thống từ xa
  - Nhận kết quả đầu ra từ client
  - Mô phỏng keylogger (nếu có)

## 🚀 Cách sử dụng

> 🧪 Chạy thử trong môi trường **máy ảo riêng biệt**, KHÔNG thử trên máy thật!

### 🔧 Yêu cầu

- Python 3.x
- Hệ điều hành: Windows hoặc Linux

### ▶️ Chạy máy chủ (server)

```bash
cd server
python server.py

cd client
python client.py

