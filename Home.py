from time import sleep
import streamlit as st
from streamlit_option_menu import option_menu as om
from streamlit_lottie import st_lottie , st_lottie_spinner

st.set_page_config(page_icon="Pictures/ajfa.png" , page_title="AJF" , layout="wide" , initial_sidebar_state="collapsed")

st.markdown("""
<style>
        .st-emotion-cache-1waqu2p.ezrtsby2{
            visibility: hidden;
        }
       
        .block-container.st-emotion-cache-1jicfl2.ea3mdgi5{
            margin-top: -110px;
        }       
</style>
""" , unsafe_allow_html=True)


page = om(menu_title=None,
                 options=["Home" , "About" ,"Blog", "Contact"],
                 default_index=0,
                 icons=["house" , "info" , "book", "google"],
                 orientation="horizontal",
                 styles={
                               "container": {"border-radius": "0px"},
                               "nav-link-selected": {"background-color": "#002562"},
                               "icon": {"color": "white", "font-size": "20px"}, 
                               "nav-link": {"font-size": "20px", "margin-right":"40px" ,"--hover-color": "#002562"},
                               
    }
          )



with st.sidebar:
    btn = st.button("🌞")
    
    dark = '''
        <style>
            .stApp {
            background-color: "#1f1f21";
            color: white;
            body {
            color: white;
            }

            h1 {
            color: white;
            }

            div {
              color: white;
            }

                }
            }
        </style>
        '''

    light = '''
        <style>
            .stApp {
            background-color: white;
            color: black;
            body {
            color: black;
            }

            h1 {
            color: blue;
            }

            div {
              color: black;
            }

                }
        </style>'''

    st.markdown(dark, unsafe_allow_html=True)
    # Create a toggle button
    # Use a global variable to store the current theme
    if "theme" not in st.session_state:
        st.session_state.theme = "#1f1f21"
    # Change the theme based on the button state
    if btn:
        if st.session_state.theme == "light":
            st.session_state.theme = "#1f1f21"
        else:
            st.session_state.theme = "light"

    # Apply the theme to the app
    if st.session_state.theme == "#1f1f21":
        st.markdown(dark, unsafe_allow_html=True)
    else:
        st.markdown(light, unsafe_allow_html=True)
    



















st.markdown("""

<style>
        .st-emotion-cache-1z0x1vh.eczjsme6{
            visibility: hidden;
        }           
</style>
""" , unsafe_allow_html=True)


          
if page == "About":
    st.switch_page("pages/About.py")

if page == "Blog":
    st.switch_page("pages/Blog.py")
if page == "Contact":
    st.switch_page("pages/Contact.py") 

st.markdown("""

<style>
        .st-emotion-cache-1laooe4.eczjsme9{
            visibility: hidden;
        }
        .st-emotion-cache-79elbk.eczjsme10{
            margin-top:-85px;
        }
        .st-emotion-cache-j7qwjs.eczjsme7{
            margin-top:-5px;
        }
</style>

""" , unsafe_allow_html=True)



st.markdown("""
<style>
        @media only screen and (max-width: 600px) {
        html{
            font-size: 15px;
        }
}
        .st-emotion-cache-10trblm.e1nzilvr1 {
            font-size: 200px;
            text-align: center;
}
        .st-emotion-cache-ek5jmc.ef3psqc12{
            background-color: #06388a;
            webkit-border-radius: 100px;
            border-radius: 60px;
            border: none;
            color: #06388a;
            cursor: pointer;
            display: inline-block;
            font-family: sans-serif;
            font-size: 20px;
            padding: 5px 15px;
            text-align: center;
            text-decoration: none;

        }
             @keyframes glowing {
        0% {
          background-color: #06388a;
          box-shadow: 0 0 5px #06388a;
        }
        50% {
          background-color: #1957bd;
          box-shadow: 0 0 20px #1957bd;
        }
        100% {
          background-color: 3678e3;
          box-shadow: 0 0 5px 3678e3;
        }
      }
      .st-emotion-cache-ek5jmc.ef3psqc12 {
        animation: glowing 1300ms infinite;
      }
        .st-emotion-cache-ek5jmc.ef3psqc12:hover{
            background-color: blue;
            color: #ffffff
            
        }        
</style>
""" , unsafe_allow_html=True)





st.markdown("""
<style>
        .st-emotion-cache-ek5jmc.ef3psqc12 {
                                        padding:150px;
                                        font-size: 0rem;
  
  
                                            }
        p  {
    margin: 0px 0px 1rem;
    padding: 0px;
    font-size: 20px;
    font-weight: 1;
}        
</style>
""" , unsafe_allow_html=True)


st.markdown("""
                <style>
                            .row-widget.stButton{
                                                                    margin-top: 100px;
                                                                    
                            }    
                              
                </style>
""" , unsafe_allow_html=True)

#st.title("AJF")
c1,c2 = st.columns(2)
with c1:
    with st.container():
      
        if st.button(label="Lets Go" , key="yy"):
            st.switch_page("pages/ED1.py")
with c2:
    
    
    import time
    import requests
    from streamlit_lottie import st_lottie_spinner


    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    lottie_url_download = "https://lottie.host/fa828b57-0ea1-4c81-94ae-028806cd63e2/UPrvPhCd9S.json"
    lottie_download = load_lottieurl(lottie_url_download)


    st_lottie(animation_source=lottie_download ,quality="low" , height=600 , width=600)
    #st_lottie(lottie_hello, key="hello")

 


#lines = ["You have woken up in a mysterious maze",
#         "The building has 5 levels",
#         "Scans show that the floors increase in size as you go down"]
#
## 'Helloworld" text will show up on your screen
#s = "Ali asd kasdhfkj aksdjhf asdhf AJF"
#
#
#def stream_data():
#    for word in s.split(" "):
#        yield word + " "
#        time.sleep(0.15)
#    word.replace("AJF","OK")
#      
#st.write_stream(stream_data)
#
#
#
#
#c1 , c2 = st.columns(2)
#with c1:
#    st.markdown(f""" 
#        <meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no">
#        <h style="font-size:200px;">AJFAI</h>
#        """ , unsafe_allow_html=True)
#with c2:
#    st.image("Pictures/ajf.png")
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>" , unsafe_allow_html=True)
load_css("style/footer_style.css")







st.markdown("""
<style>
            .st-emotion-cache-10trblm.e1nzilvr1 {
                                                    font-size: 22px;
                                                     text-align: center;
                                                }
            .st-emotion-cache-j7qwjs.e11k5jya2{
                                                text-align: center;
            }
</style>
""" , unsafe_allow_html=True)
st.divider()
with st.container():
    c1 , c2 , c3 = st.columns([1,1,1])

    with c1:
        st.header("Mission")
        st.markdown("<h4>The goal of AJF AI is to advance and develop web apps in line with the development of researches in the field of computer engineering.</h4>" , unsafe_allow_html=True)
    with c2:
        st.header("Pages")
        c4,c5,c6 = st.columns([1,0.4,1])
        with c5:
            st.page_link("Home.py" , label="Home")
            st.page_link("pages/About.py" , label="About")
            st.page_link("pages/Blog.py" , label="Blog")
            st.page_link("pages/Contact.py" , label="Contact")
        #st.markdown("<div style='text-align:center;'><a>Home</a></div>" , unsafe_allow_html=True)
        #st.markdown("<div style='text-align:center;'><a>About</a></div>" , unsafe_allow_html=True)
        #st.markdown("<div style='text-align:center;'><a>Blog</a></div>" , unsafe_allow_html=True)
        #st.markdown("<div style='text-align:center;'><a>Contact</a></div>" , unsafe_allow_html=True)
        
        
        
        st.header("Entry Data Sets")
        c7,c8,c9 = st.columns([1,1.2,1])
        with c8:
            st.page_link("pages/ED1.py" , label="Fill out the form")
        #st.markdown("<div style='text-align:center;'><a>Fill out the form</a></div>" , unsafe_allow_html=True)
        
    with c3:
        st.header("Contact Info")
        css_icon="""
        <div style='text-align:center;'>

        <i class="fa-solid fa-envelope"> </i> admin@ajfai.com

        <i class="fa-sharp fa-solid fa-phone"></i> +98 912XXXXXXX

        <i class="fa-solid fa-location-dot"></i> Karaj-Alborz
        </div>
        """
        st.markdown(css_icon , unsafe_allow_html=True)


        st.header("Social Media")
        css_icon1="""
        <div style='text-align:center;'>

        <a style='color:#3480de; text-decoration: none;' href='https://instagram.com'><i class="fa-brands fa-instagram"></i></a>
        <a style='color:#3480de; text-decoration: none;' href='https://twitter.com'><i class="fa-brands fa-x-twitter"></i></a>
        <a style='color:#3480de; text-decoration: none;' href='https://youtube.com'><i class="fa-brands fa-youtube"></i></a>
        <a style='color:#3480de; text-decoration: none;' href='https://linkedin.com'><i class="fa-brands fa-linkedin"></i></a>
        <a style='color:#3480de; text-decoration: none;' href='https://github.com'><i class="fa-brands fa-github"></i></a>
        </div>
        """
        st.markdown(css_icon1 , unsafe_allow_html=True)
        































































#[theme]
#primaryColor="#002562"
#backgroundColor="#1f1f21"
#secondaryBackgroundColor="#3480de" 
#textColor="#ffffff"
#
#[client]
#showSidebarNavigation = true
