## 1. Xử lý chức năng quên mật khẩu

- Luồng xử lý:
  -> Nhập email
  -> Gửi yêu cầu
  -> Backend kiểm tra email
  -> Gửi link reset (có token)
  -> User mở link
  -> Nhập mật khẩu mới
  -> Xác nhận
  -> Reset thành công
- Lưu ý:

  - không cấu hình email
  - Email không tồn tại(django vẫn báo thành công-> tránh dò user)
  - Token hết hạn

- Nhận xét: chứa biết làm

## 2. Xử lý checkbox 'Quên mật khẩu'

- Luồng xử lý:
  - Tick 'Ghi nhớ đăng nhập'
  - Server biết user muốn nhớ
  - Server kéo dài thời gian session/ token
  - User đóng trình duyệt vẵn còn đăng nhập
- Đảm bảo:
  - Khong lưu mật khẩu
  - Không lưu password trên localStorage
  - Có thể:
    . Xóa session khi logout
    . Rset session khi đổi mật khẩu
    . Giới hàn thời gian ghi nhớ

## 3. Làm sao cho nhiều người dùng đăng nhập cùng 1 lúc

- Gợi ý: mỗi user -> 1 session riêng
  Session là gì? là cơ chế cho phép lưu trữ thông tin người dùng trên máy chủ để duy trì trạng thái giữa các yêu cầu (requests) từ trình duyệt

- Trong settings: "django.contrib.sessions"
- Cu 1 pháp: request.session['key'] = value
- Lưu ý: mỗi trình duyệt là session

## 4. Xử lý trang write_diary.html

Luồng xử lý: Người dùng nhập dữ liệu và nhấn nút "Hoàn thành"(client)-> Gưi dữ liệu (POST) lên server-> server nhận request-> kiem tra dự lệu->lưu csdl-> trả kết quả
