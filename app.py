import streamlit as st
from datetime import datetime

def main():
    # Set up the page configuration
    st.set_page_config(page_title="Kade A. Sanico's Portfolio", page_icon=":mortar_board:", layout="wide")

    # Inject custom CSS for Poppins font
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

        body {
            font-family: 'Poppins', sans-serif;
        }

        .css-1v0mbdj {  /* Text Content */
            font-family: 'Poppins', sans-serif;
        }

        .css-18e3th9 {  /* Title */
            font-family: 'Poppins', sans-serif;
            text-align: center;
        }
        
        .css-1r8wdn2 {  /* Header */
            font-family: 'Poppins', sans-serif;
        }
        
        .css-1b7d572 {  /* Subheader */
            font-family: 'Poppins', sans-serif;
        }
        
        .css-1g8h0d0 {  /* Sidebar */
            font-family: 'Poppins', sans-serif;
        }
        </style>
        """, unsafe_allow_html=True
    )

    # Center the title using HTML
    st.markdown("<h1 style='text-align: center; font-family: \"Poppins\", sans-serif;'>Kade A. Sanico</h1>", unsafe_allow_html=True)

    # Add a sidebar for navigation
    with st.sidebar:
        st.markdown("<h1 style='font-family: \"Poppins\", sans-serif;'>Navigation</h1>", unsafe_allow_html=True)
        st.write("[All About Me](#all-about-me)")
        st.write("[Academic Experience](#academic-experience)")
        st.write("[Responsibilities of the Project](#responsibilities-of-the-project)")
        st.write("[Contact Me](#contact-me)")

    # Autobiography Section
    st.markdown("<h2 style='font-family: \"Poppins\", sans-serif;'>All About Me</h2>", unsafe_allow_html=True)
    st.write("""
    Hello! My name is **Kade A. Sanico**, a dedicated fourth-year Bachelor of Science in Information Technology student at Cebu Institute of Technology-University. 
    I am decent in various programming languages including C++, Java, Python, and SQL. My goal is to continuously learn and develop skills through hands-on experiences. 
    I am eager to find solutions to challenges and make meaningful contributions to the working environment.
    """)

    # Image under "All About Me"
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.write(' ')
    with col2:
        st.image("Me.jpg", caption="Self Portrait", use_column_width=True)
    with col3:
        st.write(' ')

    st.markdown("---")  # Horizontal line for separation

    # Portfolio Section
    st.markdown("<h2 style='font-family: \"Poppins\", sans-serif;'>Academic Experience</h2>", unsafe_allow_html=True)

    # Capstone Project Section
    with st.expander("Capstone Project: SocialSphere"):
        st.write("""
        Collaborated with a team to develop SocialSphere. A comprehensive social media management suite developed for Wildcat Innovations Labs. 
        This project integrates content creation tools with user interaction features into a single platform, aiming to enhance social media management efficiency.
        """)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("login.png", caption="Login Page", use_column_width=True)
        with col2:
            st.image("contentManager.png", caption="Content Manager Page", use_column_width=True)
        with col3:
            st.image("analytics.png", caption="Analytics Page", use_column_width=True)

    st.markdown("---")  # Horizontal line for separation

    st.markdown("<h2 style='font-family: \"Poppins\", sans-serif;'>Technologies Used</h2>", unsafe_allow_html=True)
    st.write("""Utilization of various programming languages and tools to develop the project, 
             including Python, Django, HTML/CSS, JavaScript, and MySQL. 
             """)

    st.markdown("---")  # Horizontal line for separation

    st.markdown("<h2 style='font-family: \"Poppins\", sans-serif;'>Responsibilities of the Project</h2>", unsafe_allow_html=True)
    st.write("""
        Designed and developed user interfaces including the admin dashboard, 
             content creation tools, visitor interaction and its aesthetics. 
             Ensured the UI is intuitive and user friendly to align with user needs. 
             Tasked for fixing and optimizing UI components as needed. 
             Collaborated with other team members to address issues and enhance the user experience.
        """)
    
    st.markdown("---")  # Horizontal line for separation

    # Contact Information
    st.markdown("<h2 style='font-family: \"Poppins\", sans-serif;'>Contact Me</h2>", unsafe_allow_html=True)
    st.write("Feel free to reach out to me via Google Mail at [kadesanico@gmail.com](mailto:kadesanico@gmail.com) or Microsoft Teams at [kade.sanico@cit.edu](mailto:kade.sanico@cit.edu).")

    st.markdown("---")  # Horizontal line for separation

     # Footer with current year
    current_year = datetime.now().year
    st.markdown(f"""
    <div class='footer' style='text-align: center;'>Ako Lang To © {current_year}</div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
