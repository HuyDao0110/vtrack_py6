import streamlit as st

# --- 1. CẤU HÌNH ĐƯỜNG DẪN GITHUB (Chỉ khai báo 1 lần duy nhất ở đầu) ---
GITHUB_BASE = "https://raw.githubusercontent.com/huy15102004/Ytrack_image/main/"

# Hàm rút gọn để "chỉ đích danh" tên file
def get_img(file_name):
    return GITHUB_BASE + file_name


# --- CẤU HÌNH TRANG WEB ---
st.set_page_config(page_title="YTrack - Nghe Nhạc Việt", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "Home"

# --- 2. THANH ĐIỀU HƯỚNG ---
nav = st.columns([2, 4, 2, 2])

with nav[0]:
    # Chỉ đích danh 'logo.png' thông qua hàm get_img
    st.image(get_img("logo.png"), width=110)

with nav[1]:
    st.text_input("Tìm kiếm...", label_visibility="collapsed")

with nav[2]:
    c1, c2 = st.columns(2)
    if c1.button("🏠 Home", use_container_width=True): st.session_state.page = "Home"
    if c2.button("📚 Thư viện", use_container_width=True): st.session_state.page = "Thư viện"

with nav[3]:
    c3, c4 = st.columns(2)
    if c3.button("Đăng nhập", use_container_width=True): st.session_state.page = "Đăng nhập"
    if c4.button("Đăng ký", use_container_width=True): st.session_state.page = "Đăng ký"

st.write("---")

# --- 3. QUẢN LÝ TRANG ---
if st.session_state.page == "Home":
    st.write("# Nghe gì hôm nay, User?")
    
    # Chỉ đích danh 'best_notification.png'
    st.image(get_img("best_notification.png"), use_container_width=True)

    # --- NGHỆ SĨ PHỔ BIẾN ---
    st.write("## Nghệ sĩ phổ biến")
    art_cols = st.columns(5)
    artists = [
        ("Sơn Tùng M-TP", "A01son_tung.jpg"),
        ("SOOBIN", "A02soobin.jpg"),
        ("bùi trường linh", "A03buitruonglinh.png"),
        ("Trang Pháp", "A04trang_phap.jpg"),
        ("Xem thêm", "A05more.png")
    ]
    for i, (name, file) in enumerate(artists):
        with art_cols[i]:
            # Gọi trực tiếp tên file lấy từ danh sách
            st.image(get_img(file), width=140)
            if st.button(name, key=f"art_{i}", use_container_width=True):
                if name == "Trang Pháp": st.session_state.page = "Nghệ sĩ"

    # --- ALBUM NỔI BẬT ---
    st.write("## Album nổi bật")
    alb_cols = st.columns(6)
    albums = [
        "B01mtp_mtp.jpg", "B02ai_cung_phai_bat_dau_tu_dau_do.jpg", 
        "B03danh_doi.jpg", "B04bat_no_len.jpg", 
        "B05tung_ngay_nhu_mai_mai.jpg", "B06more.png"
    ]
    for i, file in enumerate(albums):
        with alb_cols[i]:
            # Chỉ đích danh file album
            st.image(get_img(file), width=130)

    # --- BXH BÀI HÁT NỔI BẬT ---
    st.write("## BXH bài hát nổi bật *Tháng này*")
    bxh_l, bxh_r = st.columns([4, 6])
    with bxh_l:
        # Chỉ đích danh 'come_my_way.jpg'
        st.image(get_img("come_my_way.jpg"), width=320)
            
    with bxh_r:
        songs = [
            {"rank": "2", "title": "Em", "artist": "Binz"},
            {"rank": "3", "title": "Nếu như ta chẳng còn", "artist": "RPT MCK"},
            {"rank": "4", "title": "IDK", "artist": "RPT MCK"},
            {"rank": "5", "title": "Nguyễn Văn Mười", "artist": "RPT MCK"}
        ]
        for s in songs:
            sl, sr = st.columns([8, 2])
            sl.write(f"{s['rank']}. {s['title']}")
            sr.write(f"**{s['artist']}**")

elif st.session_state.page == "Nghệ sĩ":
    if st.button("⬅ Quay lại"): st.session_state.page = "Home"
    st.write("---")
    l, r = st.columns([4, 6])
    with l:
        # Chỉ đích danh 'trang_phap.jpg' ở trang chi tiết
        st.image(get_img("trang_phap.jpg"), width=350)
    with r:
        st.write("# Trang Pháp và hành trình")
        st.write("▶ Phát tất cả | 7 bài hát")
