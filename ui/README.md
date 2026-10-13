# User Interface (UI) Module

## Kế hoạch tích hợp
- UI giao tiếp trực tiếp với hàm `reply(query: str)` từ module `src.assistant.rules`.
- Khi người dùng gửi câu hỏi, giao diện truyền chuỗi truy vấn vào backend và hiển thị kết quả phản hồi cùng nguồn trích dẫn.

## Thiết kế khung giao diện (Placeholder)
- File `ui/app.py` là trang giao diện placeholder khởi tạo khung chat và ô nhập tin nhắn văn bản.
