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
