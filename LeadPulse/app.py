import streamlit as st

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="LeadPulse", page_icon="🎯")

# --- ŞİFRELEME KATMANI ---
def check_password():
    """Kullanıcı şifreyi doğru girene kadar False döner."""
    def password_entered():
        if st.session_state["password"] == "hazirim1":
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Güvenlik için şifreyi hafızadan sil
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # Şifre henüz girilmediyse giriş ekranını göster
        st.subheader("🔒 Özel Erişim")
        st.text_input(
            "Lütfen giriş şifresini yazın:", 
            type="password", 
            on_change=password_entered, 
            key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Şifre yanlış girildiyse hata mesajı ve giriş ekranını göster
        st.subheader("🔒 Özel Erişim")
        st.text_input(
            "Lütfen giriş şifresini yazın:", 
            type="password", 
            on_change=password_entered, 
            key="password"
        )
        st.error("😕 Hatalı şifre. Lütfen tekrar deneyin.")
        return False
    else:
        # Şifre doğruysa
        return True

# --- UYGULAMA MANTIĞI ---
if check_password():
    # Şifre doğruysa buradaki kodlar çalışmaya başlar
    
    if 'step' not in st.session_state:
        st.session_state.step = 1
    if 'score' not in st.session_state:
        st.session_state.score = 0

    def ilerle():
        st.session_state.step += 1

    def reset():
        st.session_state.step = 1
        st.session_state.score = 0

    st.title("🛡️ LeadPulse: Liderlik Antrenmanı")
    st.write(f"İlerleme: {min(st.session_state.step, 3)} / 3")
    st.write("---")

    if st.session_state.step == 1:
        st.header("Vaka 1: Sessiz Uzman")
        st.info("Ekibin en kıdemli üyesi artık fikir belirtmiyor. Ne yaparsın?")
        secim = st.radio("Kararın:", ["Sorumluluk artırırım", "Birebir görüşürüm", "Uyarırım"], key="v1")
        
        if st.button("Onayla ve Devam Et"):
            if secim == "Birebir görüşürüm":
                st.session_state.score += 1
                st.success("Doğru hamle!")
            else:
                st.error("Yanlış hamle!")
            st.button("Sonraki Soru ➡️", on_click=ilerle)

    elif st.session_state.step == 2:
        st.header("Vaka 2: Geri Bildirim")
        st.info("Rapor verileri doğru ama görseli zayıf. Ne dersin?")
        secim = st.radio("Kararın:", ["Sandviç metodu", "Net ve şeffaf geribildirim", "Görmezden gelirim"], key="v2")
        
        if st.button("Onayla ve Devam Et"):
            if secim == "Net ve şeffaf geribildirim":
                st.session_state.score += 1
                st.success("Harika!")
            else:
                st.error("Gereksiz dolambaçlı yol.")
            st.button("Sonraki Soru ➡️", on_click=ilerle)

    elif st.session_state.step == 3:
        st.header("Vaka 3: Z Kuşağı")
        st.info("Mert mesai biter bitmez çıkıyor, ekip tepkili. Ne yaparsın?")
        secim = st.radio("Kararın:", ["Ekibe uymasını söylerim", "Verimliliğe odaklanırım", "Baskı yaparım"], key="v3")
        
        if st.button("Final Kararını Ver"):
            if secim == "Verimliliğe odaklanırım":
                st.session_state.score += 1
                st.success("Mükemmel liderlik!")
            else:
                st.error("Z kuşağını kaybettin.")
            st.button("Sonuçları Gör 🎉", on_click=ilerle)

    else:
        st.balloons()
        st.header("🏆 Antrenman Tamamlandı!")
        st.metric("Skorun", f"{st.session_state.score} / 3")
        st.button("Yeniden Başla", on_click=reset)