import streamlit as st

def menu_page():
    st.set_page_config(page_title="Portofolio")

    st.sidebar.title('Homepage')
    page = st.sidebar.radio('Pilih halaman:', ['Home', 'Projek', 'Tentang Saya'])

    if page == 'Home':
        st.markdown("<h1 style='text-align: center;'> Welcome to My Portfolio</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: #6c757d;'>🚀 Data Science Enthusiast | Storytelling with Data</h2>", unsafe_allow_html=True)

        st.markdown("---")
        
        st.markdown("""
        <div style='text-align: center; font-size: 20px; font-style: italic; color: #555555;'>
            "Without data, you're just another person with an opinion." – W. Edwards Deming
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        st.markdown("""
        <div style='text-align: justify; font-size: 16px;'>
            Welcome to my interactive data portfolio! I'm passionate about turning raw data into valuable insights. 
            Through this platform, you can explore my work in <b>customer segmentation</b>, <b>A/B testing</b>, 
            <b>dashboard building</b>, and more. Whether you're here to learn, collaborate, or get inspired, 
            I'm excited to share my journey and projects with you.
        </div>
        """, unsafe_allow_html=True)

    elif page == 'Projek':
        # Panggil fungsi project dari module lain
        from main import main
        main()

    elif page == 'Tentang Saya':
        from kontak import link
        link()


# Jika ingin menjalankan langsung menu.py (opsional)
if __name__ == "__main__":
    menu_page()
