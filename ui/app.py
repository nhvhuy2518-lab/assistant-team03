"""Trang giao diện trò chuyện mẫu (Placeholder)."""

def render_chat_page() -> str:
    """Trả về cấu trúc HTML/giao diện khung chat."""
    return """
    <div class="chat-container">
        <div id="messages"></div>
        <input type="text" id="user-input" placeholder="Nhập câu hỏi tại đây..." />
        <button id="send-btn">Gửi</button>
    </div>
    """

if __name__ == "__main__":
    print("Đang khởi động trang UI mẫu...")
    print(render_chat_page())
