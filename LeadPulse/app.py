import streamlit as st

# --- DURUM YÖNETİMİ ---
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

# --- AKIŞ ---

if st.session_state.step == 1:
    st.header("Vaka 1: Sessiz Uzman")
    st.info("Ekibin en kıdemli üyesi artık fikir belirtmiyor. Ne yaparsın?")
    secim = st.radio("Kararın:", ["Sorumluluk artırırım", "Birebir görüşürüm", "Uyarırım"])
    
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
    secim = st.radio("Kararın:", ["Sandviç metodu", "Net ve şeffaf geribildirim", "Görmezden gelirim"])
    
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
    secim = st.radio("Kararın:", ["Ekibe uymasını söylerim", "Verimliliğe odaklanırım", "Baskı yaparım"])
    
    if st.button("Final Kararını Ver"):
        if secim == "Verimliliğe odaklanırım":
            st.session_state.score += 1
            st.success("Mükemmel liderlik!")
        else:
            st.error("Z kuşağını kaybettin.")
        st.button("Sonuçları Gör 🎉", on_click=ilerle)

else:
    st.balloons()
    st.header("🏆 Bitti!")
    st.metric("Skorun", f"{st.session_state.score} / 3")
    st.button("Yeniden Başla", on_click=reset)