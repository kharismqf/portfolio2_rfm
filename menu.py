import streamlit as st

def menu_page():
    st.set_page_config(page_title="Portofolio")

    st.sidebar.title('Homepage')
    page = st.sidebar.radio('Pilih halaman:', ['Home', 'Project', 'About Me'])

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

    elif page == 'Project':
        # Panggil fungsi project dari module lain
        import main
        main.project()

    elif page == 'About Me':
        import kontak
        kontak.user()

# Jika ingin menjalankan langsung menu.py (opsional)
if __name__ == "__main__":
    menu_page()