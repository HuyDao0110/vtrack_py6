import streamlit as st

# --- CẤU HÌNH TRANG WEB ---
st.set_page_config(page_title="YTrack - Ứng dụng nghe nhạc", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "Home"

# --- 1. THANH ĐIỀU HƯỚNG ---
nav = st.columns([2, 4, 2, 2])

with nav[0]:
    st.image("logo.png", width=130) # Logo góc trái

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

# --- 2. QUẢN LÝ CÁC TRANG ---
if st.session_state.page == "Home":
    st.write("# Nghe gì hôm nay, User?")
    
    # Banner lớn chạy ngang màn hình
    st.image("best_notification.png", use_container_width=True)

    # --- NGHỆ SĨ PHỔ BIẾN ---
    st.write("## Nghệ sĩ phổ biến")
    art_cols = st.columns(5)
    artists = [
        ("Sơn Tùng M-TP", "A01son_tung.png"),
        ("SOOBIN", "A02soobin.png"),
        ("bùi trường linh", "A03buitruonglinh.png"),
        ("Trang Pháp", "A04trang_phap.png"),
        ("Xem thêm", "A05more.png")
    ]
    for i, (name, file_name) in enumerate(artists):
        with art_cols[i]:
            # Đã phóng to ảnh lên width=200 và dùng caption hiển thị tên ngay dưới ảnh gọn gàng
            st.image(file_name, caption=name, width=200)

    # --- ALBUM NỔI BẬT ---
    st.write("## Album nổi bật")
    alb_cols = st.columns(6)
    albums = [
        "B01mtp_mtp.png", "B02ai_cung_phai_bat_dau_tu_dau_do.png", 
        "B03danh_doi.png", "B04bat_no_len.png", 
        "B05tung_ngay_nhu_mai_mai.png", "B06more.png"
    ]
    for i, file_name in enumerate(albums):
        with alb_cols[i]:
            # Phóng to ảnh bìa Album lên width=180
            st.image(file_name, width=180)

    # --- BXH BÀI HÁT NỔI BẬT THÁNG NÀY ---
    st.write("## BXH bài hát nổi bật *Tháng này*")
    bxh_l, bxh_r = st.columns([4, 6])
    with bxh_l:
        st.image("come_my_way.png", width=360) # Ảnh bìa bài hát BXH lớn, rõ nét
            
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
        st.image("A04trang_phap.png", width=400)
    with r:
        st.write("# Trang Pháp và hành trình")
        st.write("▶ Phát tất cả | 7 bài hát")

elif st.session_state.page == "Thư viện":
    st.image("thu_vien_yeu_thich.png", use_container_width=True)
    if st.button("Trở về"): st.session_state.page = "Home"
