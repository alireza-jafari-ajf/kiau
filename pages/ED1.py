import streamlit as st
import hmac
from time import sleep
from pandas import DataFrame , read_sql_query
from plotly import express as px
from streamlit_option_menu import option_menu as om
from db import create_table , add_data , view_all_data , get_task , view_unique_task , add_data1 , add_data2 , add_data3 , add_data4 , add_data2_app , add_data3_app , add_data4_app , add_data2_both , add_data3_both , edit_task_data 

st.set_page_config(page_icon="Pictures/ajfa.png" , page_title="Entry Data Sets 1" , layout="wide" , initial_sidebar_state="auto")

st.markdown("""
<style>
        .st-emotion-cache-1es31n7.ezrtsby2{
            visibility: hidden;
        }
        .st-emotion-cache-1waqu2p.ezrtsby2{
            visibility: hidden;
        } 
        .block-container.st-emotion-cache-1jicfl2.ea3mdgi5{
            margin-top: -110px;
        }
            img[data-testid="stLogo"] {
            height: 6.5rem;
}                     
</style>
""" , unsafe_allow_html=True)




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

with st.sidebar:
    btn = st.button(":material/emoji_objects:" , use_container_width=True)
    
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
           
            .st-emotion-cache-15eij9r.eqpbllx1:hover{
            background-color: #3480de;
            }
            background-color:#e3e4e8;
            color: black;

            p{
            color: black;
            }
           
            h1 {
            color: black;
            text-align: center;
            font-size: 200px;
            }
            h2 {
            color: black;
            }
            h3 {
            color: black;
            }
            h4 {
            color: black;
            }
            h5 {
            color: black;
            }
            h6 {
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
        if st.session_state.theme == "#e3e4e8":
            st.session_state.theme = "#1f1f21"
        else:
            st.session_state.theme = "#e3e4e8"    # fffffffff

    # Apply the theme to the app
    if st.session_state.theme == "#1f1f21":
        st.markdown(dark, unsafe_allow_html=True)
    else:
        st.markdown(light, unsafe_allow_html=True)
        st.logo("Pictures/icon.ico")



    page1 = om(menu_title="The First Article",
                     options=["Articles", "Entry Data Sets" , "Article 1"],
                     default_index=1,
                     icons=["gear" , "folder", "book"],
                     orientation="horizontal",
                     styles={

                                   "icon": {"color": "white", "font-size": "20px"}, 
                                   "nav-link": {"font-size": "20px", "margin-right":"40px" ,"--hover-color": "#002562"},

        }
              )
    


#----------------------------------------------------------Pages------------------------------------------------------------

st.markdown("""

<style>
        .st-emotion-cache-1z0x1vh.eczjsme6{
            visibility: hidden;
        }           
</style>
""" , unsafe_allow_html=True)



if page1 == "Articles":
    st.switch_page("pages/Blog.py") 

#----------------------------------------------------------Main------------------------------------------------------------

t1 , t2 , t3 = st.tabs(["Entry Form for Data Sets" , "Data Visualition" , "Data Set"])

with t1:
    with st.container(border=True):
        c1 , c2 = st.columns(2)
        create_table()
        with c1:
            fname = st.text_input(label="Q1: Please enter your first name: *" , max_chars=20 , placeholder="Alireza")
            lname = st.text_input(label="Q2: Please enter your last name: *" , max_chars=20 , placeholder="Jafari")
            age = st.number_input(label="Q3: How old are you? *" , min_value=18 , placeholder=22 , max_value=80)
        with c2:
            sex = st.selectbox(label="Q4: What is your gender? *" , options=[None , "Male" , "Female"] , index=0)
            education = st.selectbox(label="Q5: Please select your degree: *" , options=[None ,"Diploma" , "Associate degree" , "Bachelors degree" , "Master degree" , "PHD (Doctorate)" , "Postdoctoral Researcher"] , index=0)
            job = st.text_input(label="Q6: What is field of your study? *" , placeholder="Computer Engineer")
        
        use_academic_ai_tool = st.selectbox(label="Q7: Do you use AI tools for your academic work? *" , options=[None , "Yes" , "No"] , index=0)
        if use_academic_ai_tool == "Yes":
            tool = st.selectbox(label="Q8: Which AI tool do you use to do academic work? *" , options=[None , "ChatGPT" , "Bing AI" , "Gemeni" , "Midjourney(Image Generation)" , "Microsoft Copilot"] , index=0)
            if tool != None:
                app_or_web = st.selectbox("ًًQ9: Do you use AI more in the web browser or do you use its application? *" , options=[None , "Web Browser" , "Application" , "Both"] , index=0)
                if app_or_web != None:
                    if app_or_web == "Web Browser":
                        web_browser = st.selectbox("Q10: In which web browser do you use AI the most? *" , options=[None , "Google Chrome" , "Firefox"] , index=0)
                        if web_browser != None:
                            mainq = st.selectbox(label="Q11: Has AI succeeded in solving your questions and issues? *" , options=[None , "Yes" , "No"] , index=0)
                            if mainq != "No" and mainq != None:
                                why_use = st.selectbox(label="Q12: Why do you use AI? *" , options=[None , "User Friendly" , "High Efficiency" , "Free" , "High Responsibility" , "Other"] , index=0)
                                if why_use == "Other":
                                    another_reason = st.text_input(label="ًQ13: If there is another reason, please share your opinion with us: *" , max_chars=25 , placeholder="Another Reason")
                    
                    if app_or_web == "Application":
                        operating_system = st.selectbox("Q10: Which operating system do you use to use the AI application? *" , options=[None , "Windows" , "Mac OS" , "Linux" , "Android" , "IOS"] , index=0)
                        if operating_system != None:
                            mainq = st.selectbox(label="Q11: Has AI succeeded in solving your questions and issues? *" , options=[None , "Yes" , "No"] , index=0)
                            if mainq != "No" and mainq != None:
                                why_use = st.selectbox(label="Q12: Why do you use AI? *" , options=[None , "User Friendly" , "High Efficiency" , "Free" , "High Responsibility" , "Other"] , index=0)
                                if why_use == "Other":
                                    another_reason = st.text_input(label="ًQ13: If there is another reason, please share your opinion with us: *" , max_chars=25 , placeholder="Another Reason")
                    
                    if app_or_web == "Both":
                        web_browser = st.selectbox("Q10/1: In which web browser do you use AI the most? *" , options=[None , "Google Chrome" , "Firefox"] , index=0)
                        operating_system = st.selectbox("Q10/2: Which operating system do you use to use the AI application? *" , options=[None , "Windows" , "Mac OS" , "Linux" , "Android" , "IOS"] , index=0)
                        if web_browser != None and operating_system != None:
                            mainq = st.selectbox(label="Q11: Has AI succeeded in solving your questions and issues? *" , options=[None , "Yes" , "No"] , index=0)
                            if mainq != "No" and mainq != None:
                                why_use = st.selectbox(label="Q12: Why do you use AI? *" , options=[None , "User Friendly" , "High Efficiency" , "Free" , "High Responsibility" , "Other"] , index=0)
                                if why_use == "Other":
                                    another_reason = st.text_input(label="ًQ13: If there is another reason, please share your opinion with us: *" , max_chars=25 , placeholder="Another Reason")
        sbtn = st.button(label="Submit" , type="primary")
        if sbtn:
           
            #----------------------------------Error-------------------------------------------
            if all(x.isalpha() == False or x.isspace() for x in fname):

                
                st.error("Please enter your First Name (Q1)")
                st.stop()

            if all(x.isalpha() == False or x.isspace() for x in lname):
                st.error("Please enter your Last Name (Q2)")
                st.stop()
            if sex == None:
                st.error("Please Select your (Q4)")
            if education == None:
                st.error("Please Select your (Q5)")
            if all(x.isalpha() == False or x.isspace() for x in job):
                st.error("Please enter your Job (Q6)")
                st.stop()

            
            if age == 30 and education== "Postdoctoral Researcher":
                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                st.stop()
            if age == 29 and education== "Postdoctoral Researcher":
                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                st.stop()
            if age == 28 and education== "Postdoctoral Researcher":
                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                st.stop()
            if age == 27 and education== "Postdoctoral Researcher":
                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                st.stop()
            if age == 26 and education== "PHD (Doctorate)":
                st.error("You can not choose these options based on tradition [PHD (Doctorate)")
                st.stop()
            elif age == 26 and education == "Postdoctoral Researcher":
                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                st.stop()
            elif age ==25 and education == "Postdoctoral Researcher":
                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                st.stop()
            elif age ==25 and education== "PHD (Doctorate)":
                st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                st.stop()
            elif age == 24 and education == "Postdoctoral Researcher":
                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                st.stop()
            elif age == 24 and education== "PHD (Doctorate)":
                st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                st.stop()
            elif age ==23 and education == "Postdoctoral Researcher":
                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                st.stop()
            elif age ==23 and education== "PHD (Doctorate)":
                st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                st.stop()
            elif age ==23 and education== "Master degree":
                st.error("You can not choose these options based on tradition [Master degree]")
                st.stop()
            elif age == 22 and education == "Postdoctoral Researcher":
                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                st.stop()
            if age == 22 and education== "PHD (Doctorate)":
                st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                st.stop()
            elif age == 22 and education== "Master degree":
                st.error("You can not choose these options based on tradition [Master degree]")
                st.stop()
            elif age == 21 and education == "Postdoctoral Researcher":
                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                st.stop()
            elif age == 21 and education== "PHD (Doctorate)":
                st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                st.stop()
            elif age == 21 and education== "Master degree":
                st.error("You can not choose these options based on tradition [Master degree]")
                st.stop()
            elif age == 21 and education == "Bachelors degree":
                st.error("You can not choose these options based on tradition [Bachelors degree]")
                st.stop()
            elif age == 20 and education == "Postdoctoral Researcher":
                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                st.stop()
            elif age == 20 and education== "PHD (Doctorate)":
                st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                st.stop()
            elif age == 20 and education== "Master degree":
                st.error("You can not choose these options based on tradition [Master degree]")
                st.stop()
            elif age == 20 and education == "Bachelors degree":
                st.error("You can not choose these options based on tradition [Bachelors degree]")
                st.stop()
            elif age == 20 and education =="Associate degree":
                st.error("You can not choose these options based on tradition [Associate degree]")
                st.stop()
            elif age == 19 and education == "Postdoctoral Researcher":
                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                st.stop()
            elif age == 19 and education== "PHD (Doctorate)":
                st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                st.stop()
            elif age == 19 and education== "Master degree":
                st.error("You can not choose these options based on tradition [Master degree]")
                st.stop()
            elif age == 19 and education == "Bachelors degree":
                st.error("You can not choose these options based on tradition [Bachelors degree]")
                st.stop()
            elif age == 19 and education =="Associate degree":
                st.error("You can not choose these options based on tradition [Associate degree]")
                st.stop()
            elif age == 18 and education == "Postdoctoral Researcher":
                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                st.stop()
            elif age == 18 and education== "PHD (Doctorate)":
                st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                st.stop()
            elif age == 18 and education== "Master degree":
                st.error("You can not choose these options based on tradition [Master degree]")
                st.stop()
            elif age == 18 and education == "Bachelors degree":
                st.error("You can not choose these options based on tradition [Bachelors degree]")
                st.stop()
            elif age == 18 and education =="Associate degree":
                st.error("You can not choose these options based on tradition [Associate degree]")
                st.stop()
            
            if use_academic_ai_tool == None:
                st.error("Please choose  some options (Q7)")
            if use_academic_ai_tool == "No":
                            add_data1(fname , lname , age , sex , education , job ,  use_academic_ai_tool)
                            st.success("Item Added")
                            st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                            sleep(8)
                            st.switch_page("pages/Home.py")

            if use_academic_ai_tool == "Yes":
                if tool == None:
                    st.error("Please Select your (Q8)")
                    st.stop()
                if app_or_web == None:
                    st.error("Please Select your (Q9)")
                    st.stop()
                if app_or_web == "Web Browser":
                    if web_browser == None:
                        st.error("Please Select your (Q10)")
                        st.stop()
                    if mainq == None:
                        st.error("Please Select your (Q11)")
                        st.stop()
                    if mainq == "No":
                        add_data2(fname , lname , age , sex , education , job ,  use_academic_ai_tool , tool , app_or_web , web_browser , mainq)
                        st.success("Item Added")
                        st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                        sleep(8)
                        st.switch_page("pages/Home.py")
                    if mainq == "Yes":
                        if why_use == None:
                            st.error("Please Select your (Q12)")
                            st.stop()
                        if why_use != "Other":
                            add_data3(fname , lname , age , sex , education , job ,  use_academic_ai_tool , tool , app_or_web , web_browser , why_use , mainq)
                            st.success("Item Added")
                            st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                            sleep(8)
                            st.switch_page("pages/Home.py")
                        if why_use == "Other":
                            if all(x.isalpha() == False or x.isspace() for x in another_reason):
                                st.error("Please Select your (Q13)")
                                st.stop()
                            if another_reason:
                                add_data4(fname , lname , age , sex , education , job ,  use_academic_ai_tool , tool , app_or_web , web_browser , why_use , another_reason , mainq)
                                st.success("Item Added")
                                st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                                sleep(8)
                                st.switch_page("pages/Home.py")
                
                if app_or_web == "Application":
                    if operating_system == None:
                        st.error("Please Select your (Q10)")
                        st.stop()
                    if mainq == None:
                        st.error("Please Select your (Q11)")
                        st.stop()
                    if mainq == "No":
                        add_data2_app(fname , lname , age , sex , education , job ,  use_academic_ai_tool , tool , app_or_web , operating_system , mainq)
                        st.success("Item Added")
                        st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                        sleep(8)
                        st.switch_page("pages/Home.py")
                    if mainq == "Yes":
                        if why_use == None:
                            st.error("Please Select your (Q12)")
                            st.stop()
                        if why_use != "Other":
                            add_data3_app(fname , lname , age , sex , education , job ,  use_academic_ai_tool , tool , app_or_web , operating_system , why_use , mainq)
                            st.success("Item Added")
                            st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                            sleep(8)
                            st.switch_page("pages/Home.py")
                        if why_use == "Other":
                            if all(x.isalpha() == False or x.isspace() for x in another_reason):
                                st.error("Please Select your (Q13)")
                                st.stop()
                            if another_reason:
                                add_data4_app(fname , lname , age , sex , education , job ,  use_academic_ai_tool , tool , app_or_web , operating_system , why_use , another_reason , mainq)
                                st.success("Item Added")
                                st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                                sleep(8)
                                st.switch_page("pages/Home.py")
                
                if app_or_web == "Both":
                    if web_browser == None:
                        st.error("Please Select your (Q10/1)")
                        st.stop()
                    if operating_system == None:
                        st.error("Please Select your (Q10/1)")
                        st.stop()
                    if mainq == None:
                        st.error("Please Select your (Q11)")
                        st.stop()
                    if mainq == "No":
                        add_data2_both(fname , lname , age , sex , education , job ,  use_academic_ai_tool , tool , app_or_web , web_browser ,  operating_system , mainq)
                        st.success("Item Added")
                        st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                        sleep(8)
                        st.switch_page("pages/Home.py")
                    if mainq == "Yes":
                        if why_use == None:
                            st.error("Please Select your (Q12)")
                            st.stop()
                        if why_use != "Other":
                            add_data3_both(fname , lname , age , sex , education , job ,  use_academic_ai_tool , tool , app_or_web , web_browser ,  operating_system , why_use , mainq)
                            st.success("Item Added")
                            st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                            sleep(8)
                            st.switch_page("pages/Home.py")
                        if why_use == "Other":
                            if all(x.isalpha() == False or x.isspace() for x in another_reason):
                                st.error("Please Select your (Q13)")
                                st.stop()
                            if another_reason:
                                add_data(fname , lname , age , sex , education , job ,  use_academic_ai_tool , tool , app_or_web , web_browser ,  operating_system , why_use , another_reason , mainq)
                                st.success("Item Added")
                                st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
                                sleep(8)
                                st.switch_page("pages/Home.py")
    
            #if mainq == None:
            #    st.error("Please Select your (Q10)")
            #    st.stop()
            #add_data(fname , lname , age , sex , education , job ,  use_academic_ai_tool , tool , app_or_web , web_browser , operating_system , why_use , another_reason , mainq)
            #st.success("Item Added")
            #st.info(f"Thank you very much {fname} {lname} for giving your valuable time to our team")
            #sleep(5)
            #st.switch_page("Home.py")
    result = view_all_data()
    df = DataFrame(result , columns=["first_name" , "last_name" , "age" , "gender" , "education" , "job" ,  "use_ai_for_academic_work" , "tool" , "app_or_web" , "web_browser" , "operating_system" , "why_use" , "another_reason" , "ai_ssp"])
    with st.expander("AI_SSP status"):
        tast_df1 = df["ai_ssp"].value_counts().to_frame()
        tast_df1 = tast_df1.reset_index()
        st.dataframe(tast_df1)
        p1 = px.pie(tast_df1 , names="ai_ssp" , values="count")
        st.plotly_chart(p1)
    
    with st.expander("Gender status"):
        tast_df2 = df["gender"].value_counts().to_frame()
        tast_df2 = tast_df2.reset_index()
        st.dataframe(tast_df2)
        p1 = px.pie(tast_df2 , names="gender" , values="count")
        st.plotly_chart(p1)
    
    with st.expander("Age status"):
        tast_df3 = df["age"].value_counts().to_frame()
        tast_df3 = tast_df3.reset_index()
        st.dataframe(tast_df3)
        p1 = px.pie(tast_df3 , names="age" , values="count")
        st.plotly_chart(p1)
    
    with st.expander("Education status"):
        tast_df4 = df["education"].value_counts().to_frame()
        tast_df4 = tast_df4.reset_index()
        st.dataframe(tast_df4)
        p1 = px.pie(tast_df4 , names="education" , values="count")
        st.plotly_chart(p1)
    
    with st.expander("Job status"):
        tast_df5 = df["job"].value_counts().to_frame()
        tast_df5 = tast_df5.reset_index()
        st.dataframe(tast_df5)
        p1 = px.pie(tast_df5 , names="job" , values="count")
        st.plotly_chart(p1)
    
    with st.expander("Tool status"):
        tast_df6 = df["tool"].value_counts().to_frame()
        tast_df6 = tast_df6.reset_index()
        st.dataframe(tast_df6)
        p1 = px.pie(tast_df6 , names="tool" , values="count")
        st.plotly_chart(p1)

    
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>" , unsafe_allow_html=True)
load_css("style/footer_style.css")

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.divider()
with st.container():
    c1 , c2 , c3 = st.columns([1,1,1])

    with c1:
        st.header("Mission")
        st.markdown("<h4>The goal of AJF AI is to advance and develop web apps in line with the development of researches in the field of computer engineering.</h4>" , unsafe_allow_html=True)
    with c2:
        c4,c5,c6 = st.columns([1,1,1])
        with c5:
            st.header("Pages")
            st.page_link("pages/Home.py" , label="Home")
            st.page_link("pages/About.py" , label="About")
            st.page_link("pages/Blog.py" , label="Blog")
            st.page_link("pages/ED1.py" , label="Q&A")
            st.page_link("pages/Contact.py" , label="Contact")
        #st.markdown("<div style='text-align:center;'><a>Home</a></div>" , unsafe_allow_html=True)
        #st.markdown("<div style='text-align:center;'><a>About</a></div>" , unsafe_allow_html=True)
        #st.markdown("<div style='text-align:center;'><a>Blog</a></div>" , unsafe_allow_html=True)
        #st.markdown("<div style='text-align:center;'><a>Contact</a></div>" , unsafe_allow_html=True)
        
        
        
       
    with c3:
        c4,c5,c6 = st.columns([1,2.5,0.4])
        with c5:
            st.header("Contact Info")
        css_icon="""
        <div style='text-align:center;'>

        <i class="fa-solid fa-envelope"> </i> admin@ajfai.com

        <i class="fa-sharp fa-solid fa-phone"></i> +98 9120638732

        <i class="fa-solid fa-location-dot"></i> Karaj-Alborz-Iran
        </div>
        """
        st.markdown(css_icon , unsafe_allow_html=True)

        c4,c5,c6 = st.columns([1,2.5,0.2])
        with c5:
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
         
         
            
                


#---------------------------------------------Tab2---------------------------------------------------------

with t2:
    st.markdown("""
                    <style>
                        h1{
                text-align: center;
                        }
                </style>
                """ , unsafe_allow_html=True)
    st.title("Data Visualization") 
    result = view_all_data()
    df = DataFrame(result , columns=["first_name" , "last_name" , "age" , "gender" , "education" , "Field_of_study" ,  "use_ai_for_academic_work" , "tool" , "app_or_web" , "web_browser" , "operating_system" , "why_use" , "another_reason" , "ai_ssp"])
    tast_df1 = df["age"].value_counts().to_frame()
    tast_df1 = tast_df1.reset_index()
    #st.dataframe(tast_df1)
    tast_df2 = df["gender"].value_counts().to_frame()
    tast_df2 = tast_df2.reset_index()

    tast_df3 = df["education"].value_counts().to_frame()
    tast_df3 = tast_df3.reset_index()

    tast_df4 = df["Field_of_study"].value_counts().to_frame()
    tast_df4 = tast_df4.reset_index()
    
    tast_df5 = df["use_ai_for_academic_work"].value_counts().to_frame()
    tast_df5 = tast_df5.reset_index()
    
    tast_df6 = df["app_or_web"].value_counts().to_frame()
    tast_df6 = tast_df6.reset_index()
    
    tast_df7 = df["web_browser"].value_counts().to_frame()
    tast_df7 = tast_df7.reset_index()
    
    tast_df9 = df["operating_system"].value_counts().to_frame()
    tast_df9 = tast_df9.reset_index()

    tast_df8 = df["why_use"].value_counts().to_frame()
    tast_df8 = tast_df8.reset_index()
    
    tast_df10 = df["tool"].value_counts().to_frame()
    tast_df10 = tast_df10.reset_index()
    
    tast_df11 = df["ai_ssp"].value_counts().to_frame()
    tast_df11 = tast_df11.reset_index()
    

    c1,c2 = st.columns(2) 
    with c1:
        p1 = px.bar(tast_df1 , x="age" , y="count" , color="age" , text_auto=True)
        st.plotly_chart(p1)
    with c2:
        p2 = px.bar(tast_df2 , x="gender" , y="count" , color="gender" , text_auto=True)
        st.plotly_chart(p2)

    c3,c4 = st.columns(2) 
    with c3:
        p3 = px.bar(tast_df3 , x="education" , y="count", color="education" , text_auto=True)
        st.plotly_chart(p3)
    with c4:
        p4 = px.bar(tast_df4 , x="Field_of_study" , y="count", color="Field_of_study" , text_auto=True)
        st.plotly_chart(p4)

    c5,c6 = st.columns(2) 
    with c5:
        p5 = px.bar(tast_df5 , x="use_ai_for_academic_work" , y="count", color="use_ai_for_academic_work" , text_auto=True)
        st.plotly_chart(p5)
    with c6:
        p6 = px.bar(tast_df6 , x="app_or_web" , y="count", color="app_or_web" , text_auto=True)
        st.plotly_chart(p6)
    
    c7,c8 = st.columns(2) 
    with c7:
        p7 = px.bar(tast_df7 , x="web_browser" , y="count", color="web_browser" , text_auto=True)
        st.plotly_chart(p7)
    with c8:
        p8 = px.bar(tast_df9 , x="operating_system" , y="count", color="operating_system" , text_auto=True)
        st.plotly_chart(p8)
   
    c9,c10 = st.columns(2) 
    with c9:
        p9 = px.bar(tast_df8 , x="why_use" , y="count", color="why_use" , text_auto=True)
        st.plotly_chart(p9)
    with c10:
        p10 = px.bar(tast_df10 , x="tool" , y="count", color="tool" , text_auto=True)
        st.plotly_chart(p10)
   
     
  
    
    p11 = px.bar(tast_df11 , x="ai_ssp" , y="count", color="ai_ssp" , text_auto=True)
    st.plotly_chart(p11) 




#---------------------------------------------Tab2---------------------------------------------------------

with t3:
    def check_password():
        """Returns `True` if the user had a correct password."""

        def login_form():
            """Form with widgets to collect user information"""
            with st.form("Credentials"):
                st.text_input("Username", key="username")
                st.text_input("Password", type="password", key="password")
                st.form_submit_button("Log in", on_click=password_entered)

        def password_entered():
            """Checks whether a password entered by the user is correct."""
            if st.session_state["username"] in st.secrets[
                "passwords"
            ] and hmac.compare_digest(
                st.session_state["password"],
                st.secrets.passwords[st.session_state["username"]],
            ):
                st.session_state["password_correct"] = True
                del st.session_state["password"]  # Don't store the username or password.
                del st.session_state["username"]
            else:
                st.session_state["password_correct"] = False

        # Return True if the username + password is validated.
        if st.session_state.get("password_correct", False):
            return True

        # Show inputs for username + password.
        login_form()
        if "password_correct" in st.session_state:
            st.error("😕 User not known or password incorrect")
        return False


    if not check_password():
        st.stop()




    st.title("Welcome To Admin Panel") 
    Admin_Panel = st.selectbox(label="Admin Panel" , options=[None , "Create" , "Read" , "Update" , "Delete" , "About"] , index=0)
    
    if Admin_Panel == "Create":
        st.subheader("Create New Record")
        c1 , c2 = st.columns(2)
        create_table()
        with c1:
            nnfname = st.text_input(label="Q1: Please enter your first name: *" , max_chars=20 , placeholder="Alireza" , key="sadhfsdh")
            nnlname = st.text_input(label="Q2: Please enter your last name: *" , max_chars=20 , placeholder="Jafari", key="sadhfsdfghsdh")
            nnage = st.number_input(label="Q3: How old are you? *" , min_value=18 , placeholder=22 , max_value=80, key="sadhfslksdklvdh")
        with c2:
            nnsex = st.selectbox(label="Q4: What is your gender? *" , options=[None , "Male" , "Female"] , index=0, key="sadhfsdvbcvbdh")
            nneducation = st.selectbox(label="Q5: Please select your degree: *" , options=[None ,"Diploma" , "Associate degree" , "Bachelors degree" , "Master degree" , "PHD (Doctorate)" , "Postdoctoral Researcher"] , index=0, key="sadhfsimdjhdh")
            nnjob = st.text_input(label="Q6: What is your Job? *" , placeholder="Computer Engineer", key="sadhfsFgoiukvdh")
        
        nnuse_academic_ai_tool = st.selectbox(label="Q7: Do you use AI tools for your academic work? *" , options=[None , "Yes" , "No"] , index=0, key="sadhfsddfgvsscbh")
        if nnuse_academic_ai_tool == "Yes":
            nntool = st.selectbox(label="Q8: Which AI tool do you use to do academic work? *" , options=[None , "ChatGPT" , "Bing AI" , "Gemeni" , "Midjourney(Image Generation)" , "Microsoft Copilot"] , index=0, key="sadhfsngdsochdioudh")
            if nntool != None:
                nnapp_or_web = st.selectbox("ًًQ9: Do you use AI more in the web browser or do you use its application? *" , options=[None , "Web Browser" , "Application" , "Both"] , index=0, key="sadhfsdsdfiguksdfkdh")
                if nnapp_or_web != None:
                    if nnapp_or_web == "Web Browser":
                        nnweb_browser = st.selectbox("Q10: In which web browser do you use AI the most? *" , options=[None , "Google Chrome" , "Firefox"] , index=0, key="sadhfsdsfkcmcmcmdh")
                        if nnweb_browser != None:
                            nnmainq = st.selectbox(label="Q11: Has AI succeeded in solving your questions and issues? *" , options=[None , "Yes" , "No"] , index=0, key="sadhfsmsmdfnhdh")
                            if nnmainq != "No" and nnmainq != None:
                                nnwhy_use = st.selectbox(label="Q12: Why do you use AI? *" , options=[None , "User Friendly" , "High Efficiency" , "Free" , "High Responsibility" , "Other"] , index=0, key="sadhfsddifugncvfgdfvh")
                                if nnwhy_use == "Other":
                                    nnanother_reason = st.text_input(label="ًQ13: If there is another reason, please share your opinion with us: *" , max_chars=25 , placeholder="Another Reason", key="sadhfsarfiyhcdfdfjhgdfdh")
                    
                    if nnapp_or_web == "Application":
                        nnoperating_system = st.selectbox("Q10: Which operating system do you use to use the AI application? *" , options=[None , "Windows" , "Mac OS" , "Linux" , "Android" , "IOS"] , index=0, key="sadhfsddffdsfdfgassfvfffh")
                        if nnoperating_system != None:
                            nnmainq = st.selectbox(label="Q11: Has AI succeeded in solving your questions and issues? *" , options=[None , "Yes" , "No"] , index=0, key="sadhfsdhfhfggjggtgh")
                            if nnmainq != "No" and nnmainq != None:
                                nnwhy_use = st.selectbox(label="Q12: Why do you use AI? *" , options=[None , "User Friendly" , "High Efficiency" , "Free" , "High Responsibility" , "Other"] , index=0, key="sadhfsdfghcuuuvdrfgvxcvsdfdh")
                                if nnwhy_use == "Other":
                                    nnanother_reason = st.text_input(label="ًQ13: If there is another reason, please share your opinion with us: *" , max_chars=25 , placeholder="Another Reason", key="sadhfsbvbnmhgvbnvfghgyhbhodh")
                    
                    if nnapp_or_web == "Both":
                        nnweb_browser = st.selectbox("Q10/1: In which web browser do you use AI the most? *" , options=[None , "Google Chrome" , "Firefox"] , index=0, key="sadhfsyhgjqqqwwwedh")
                        nnoperating_system = st.selectbox("Q10/2: Which operating system do you use to use the AI application? *" , options=[None , "Windows" , "Mac OS" , "Linux" , "Android" , "IOS"] , index=0, key="sadhfsfgyufghgufuuuufgyyydh")
                        if nnweb_browser != None and nnoperating_system != None:
                            nnmainq = st.selectbox(label="Q11: Has AI succeeded in solving your questions and issues? *" , options=[None , "Yes" , "No"] , index=0, key="sadhfsdfghdfgsrtgyhyyyyjujjjjdh")
                            if nnmainq != "No" and nnmainq != None:
                                nnwhy_use = st.selectbox(label="Q12: Why do you use AI? *" , options=[None , "User Friendly" , "High Efficiency" , "Free" , "High Responsibility" , "Other"] , index=0, key="sadhfsdkkkjjkjkjhgjghghgfgdfsdsh")
                                if nnwhy_use == "Other":
                                    nnanother_reason = st.text_input(label="ًQ13: If there is another reason, please share your opinion with us: *" , max_chars=25 , placeholder="Another Reason", key="sadhfsjhjhjhgfffddsddrtrdcvrtdh")
        nnsbtn = st.button(label="Submit" , type="primary", key="sadhfjhhfhfujhdkduhflosdh")
        if nnsbtn:
           
            #----------------------------------Error-------------------------------------------
            if all(x.isalpha() == False or x.isspace() for x in nnfname):

                
                st.error("Please enter your First Name (Q1)")
                st.stop()

            if all(x.isalpha() == False or x.isspace() for x in nnlname):
                st.error("Please enter your Last Name (Q2)")
                st.stop()
            if nnsex == None:
                st.error("Please Select your (Q4)")
            if nneducation == None:
                st.error("Please Select your (Q5)")
            if all(x.isalpha() == False or x.isspace() for x in nnjob):
                st.error("Please enter your Job (Q6)")
                st.stop()

            
            if nnage == 30 and nneducation== "Postdoctoral Researcher":
                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                st.stop()
            if nnage == 29 and nneducation== "Postdoctoral Researcher":
                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                st.stop()
            if nnage == 28 and nneducation== "Postdoctoral Researcher":
                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                st.stop()
            if nnage == 27 and nneducation== "Postdoctoral Researcher":
                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                st.stop()
            if nnage == 26 and nneducation== "PHD (Doctorate)":
                st.error("You can not choose these options based on tradition [PHD (Doctorate)")
                st.stop()
            elif nnage == 26 and nneducation == "Postdoctoral Researcher":
                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                st.stop()
            elif nnage ==25 and nneducation == "Postdoctoral Researcher":
                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                st.stop()
            elif nnage ==25 and nneducation== "PHD (Doctorate)":
                st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                st.stop()
            elif nnage == 24 and nneducation == "Postdoctoral Researcher":
                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                st.stop()
            elif nnage == 24 and nneducation== "PHD (Doctorate)":
                st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                st.stop()
            elif nnage ==23 and nneducation == "Postdoctoral Researcher":
                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                st.stop()
            elif nnage ==23 and nneducation== "PHD (Doctorate)":
                st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                st.stop()
            elif nnage ==23 and nneducation== "Master degree":
                st.error("You can not choose these options based on tradition [Master degree]")
                st.stop()
            elif nnage == 22 and nneducation == "Postdoctoral Researcher":
                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                st.stop()
            if nnage == 22 and nneducation== "PHD (Doctorate)":
                st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                st.stop()
            elif nnage == 22 and nneducation== "Master degree":
                st.error("You can not choose these options based on tradition [Master degree]")
                st.stop()
            elif nnage == 21 and nneducation == "Postdoctoral Researcher":
                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                st.stop()
            elif nnage == 21 and nneducation== "PHD (Doctorate)":
                st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                st.stop()
            elif nnage == 21 and nneducation== "Master degree":
                st.error("You can not choose these options based on tradition [Master degree]")
                st.stop()
            elif nnage == 21 and nneducation == "Bachelors degree":
                st.error("You can not choose these options based on tradition [Bachelors degree]")
                st.stop()
            elif nnage == 20 and nneducation == "Postdoctoral Researcher":
                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                st.stop()
            elif nnage == 20 and nneducation== "PHD (Doctorate)":
                st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                st.stop()
            elif nnage == 20 and nneducation== "Master degree":
                st.error("You can not choose these options based on tradition [Master degree]")
                st.stop()
            elif nnage == 20 and nneducation == "Bachelors degree":
                st.error("You can not choose these options based on tradition [Bachelors degree]")
                st.stop()
            elif nnage == 20 and nneducation =="Associate degree":
                st.error("You can not choose these options based on tradition [Associate degree]")
                st.stop()
            elif nnage == 19 and nneducation == "Postdoctoral Researcher":
                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                st.stop()
            elif nnage == 19 and nneducation== "PHD (Doctorate)":
                st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                st.stop()
            elif nnage == 19 and nneducation== "Master degree":
                st.error("You can not choose these options based on tradition [Master degree]")
                st.stop()
            elif nnage == 19 and nneducation == "Bachelors degree":
                st.error("You can not choose these options based on tradition [Bachelors degree]")
                st.stop()
            elif nnage == 19 and nneducation =="Associate degree":
                st.error("You can not choose these options based on tradition [Associate degree]")
                st.stop()
            elif nnage == 18 and nneducation == "Postdoctoral Researcher":
                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
                st.stop()
            elif nnage == 18 and nneducation== "PHD (Doctorate)":
                st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
                st.stop()
            elif nnage == 18 and nneducation== "Master degree":
                st.error("You can not choose these options based on tradition [Master degree]")
                st.stop()
            elif nnage == 18 and nneducation == "Bachelors degree":
                st.error("You can not choose these options based on tradition [Bachelors degree]")
                st.stop()
            elif nnage == 18 and nneducation =="Associate degree":
                st.error("You can not choose these options based on tradition [Associate degree]")
                st.stop()
            
            if nnuse_academic_ai_tool == None:
                st.error("Please choose  some options (Q7)")
            if nnuse_academic_ai_tool == "No":
                            add_data1(nnfname , nnlname , nnage , nnsex , nneducation , nnjob ,  nnuse_academic_ai_tool)
                            st.success("Item Added")
                            st.info(f"Thank you very much {nnfname} {nnlname} for giving your valuable time to our team")
                            sleep(8)
                            st.switch_page("Home.py")

            if nnuse_academic_ai_tool == "Yes":
                if nntool == None:
                    st.error("Please Select your (Q8)")
                    st.stop()
                if nnapp_or_web == None:
                    st.error("Please Select your (Q9)")
                    st.stop()
                if nnapp_or_web == "Web Browser":
                    if nnweb_browser == None:
                        st.error("Please Select your (Q10)")
                        st.stop()
                    if nnmainq == None:
                        st.error("Please Select your (Q11)")
                        st.stop()
                    if nnmainq == "No":
                        add_data2(nnfname , nnlname , nnage , nnsex , nneducation , nnjob ,  nnuse_academic_ai_tool , nntool , nnapp_or_web , nnweb_browser , nnmainq)
                        st.success("Item Added")
                        st.info(f"Thank you very much {nnfname} {nnlname} for giving your valuable time to our team")
                        sleep(8)
                        st.switch_page("Home.py")
                    if nnmainq == "Yes":
                        if nnwhy_use == None:
                            st.error("Please Select your (Q12)")
                            st.stop()
                        if nnwhy_use != "Other":
                            add_data3(nnfname , nnlname , nnage , nnsex , nneducation , nnjob ,  nnuse_academic_ai_tool , nntool , nnapp_or_web , nnweb_browser , nnwhy_use , nnmainq)
                            st.success("Item Added")
                            st.info(f"Thank you very much {nnfname} {nnlname} for giving your valuable time to our team")
                            sleep(8)
                            st.switch_page("Home.py")
                        if nnwhy_use == "Other":
                            if all(x.isalpha() == False or x.isspace() for x in nnanother_reason):
                                st.error("Please Select your (Q13)")
                                st.stop()
                            if nnanother_reason:
                                add_data4(nnfname , nnlname , nnage , nnsex , nneducation , nnjob ,  nnuse_academic_ai_tool , nntool , nnapp_or_web , nnweb_browser , nnwhy_use , nnanother_reason , nnmainq)
                                st.success("Item Added")
                                st.info(f"Thank you very much {nnfname} {nnlname} for giving your valuable time to our team")
                                sleep(8)
                                st.switch_page("Home.py")
                
                if nnapp_or_web == "Application":
                    if nnoperating_system == None:
                        st.error("Please Select your (Q10)")
                        st.stop()
                    if nnmainq == None:
                        st.error("Please Select your (Q11)")
                        st.stop()
                    if nnmainq == "No":
                        add_data2_app(nnfname , nnlname , nnage , nnsex , nneducation , nnjob ,  nnuse_academic_ai_tool , nntool , nnapp_or_web , nnoperating_system , nnmainq)
                        st.success("Item Added")
                        st.info(f"Thank you very much {nnfname} {nnlname} for giving your valuable time to our team")
                        sleep(8)
                        st.switch_page("Home.py")
                    if nnmainq == "Yes":
                        if nnwhy_use == None:
                            st.error("Please Select your (Q12)")
                            st.stop()
                        if nnwhy_use != "Other":
                            add_data3_app(nnfname , nnlname , nnage , nnsex , nneducation , nnjob ,  nnuse_academic_ai_tool , nntool , nnapp_or_web , nnoperating_system , nnwhy_use , nnmainq)
                            st.success("Item Added")
                            st.info(f"Thank you very much {nnfname} {nnlname} for giving your valuable time to our team")
                            sleep(8)
                            st.switch_page("Home.py")
                        if nnwhy_use == "Other":
                            if all(x.isalpha() == False or x.isspace() for x in nnanother_reason):
                                st.error("Please Select your (Q13)")
                                st.stop()
                            if nnanother_reason:
                                add_data4_app(nnfname , nnlname , nnage , nnsex , nneducation , nnjob ,  nnuse_academic_ai_tool , nntool , nnapp_or_web , nnoperating_system , nnwhy_use , nnanother_reason , nnmainq)
                                st.success("Item Added")
                                st.info(f"Thank you very much {nnfname} {nnlname} for giving your valuable time to our team")
                                sleep(8)
                                st.switch_page("Home.py")
                
                if nnapp_or_web == "Both":
                    if nnweb_browser == None:
                        st.error("Please Select your (Q10/1)")
                        st.stop()
                    if nnoperating_system == None:
                        st.error("Please Select your (Q10/1)")
                        st.stop()
                    if nnmainq == None:
                        st.error("Please Select your (Q11)")
                        st.stop()
                    if nnmainq == "No":
                        add_data2_both(nnfname , nnlname , nnage , nnsex , nneducation , nnjob ,  nnuse_academic_ai_tool , nntool , nnapp_or_web , nnweb_browser ,  nnoperating_system , nnmainq)
                        st.success("Item Added")
                        st.info(f"Thank you very much {nnfname} {nnlname} for giving your valuable time to our team")
                        sleep(8)
                        st.switch_page("Home.py")
                    if nnmainq == "Yes":
                        if nnwhy_use == None:
                            st.error("Please Select your (Q12)")
                            st.stop()
                        if nnwhy_use != "Other":
                            add_data3_both(nnfname , nnlname , nnage , nnsex , nneducation , nnjob ,  nnuse_academic_ai_tool , nntool , nnapp_or_web , nnweb_browser ,  nnoperating_system , nnwhy_use , nnmainq)
                            st.success("Item Added")
                            st.info(f"Thank you very much {nnfname} {nnlname} for giving your valuable time to our team")
                            sleep(8)
                            st.switch_page("Home.py")
                        if nnwhy_use == "Other":
                            if all(x.isalpha() == False or x.isspace() for x in nnanother_reason):
                                st.error("Please Select your (Q13)")
                                st.stop()
                            if another_reason:
                                add_data(nnfname , nnlname , nnage , nnsex , nneducation , nnjob ,  nnuse_academic_ai_tool , nntool , nnapp_or_web , nnweb_browser ,  nnoperating_system , nnwhy_use , nnanother_reason , nnmainq)
                                st.success("Item Added")
                                st.info(f"Thank you very much {nnfname} {nnlname} for giving your valuable time to our team")
                                sleep(8)
                                st.switch_page("Home.py")

    if Admin_Panel == "Read":
        st.subheader("View Item")
        result = view_all_data()
        df = DataFrame(result , columns=["first_name" , "last_name" , "age" , "gender" , "education" , "job" ,  "use_ai_for_academic_work" , "tool" , "app_or_web" , "web_browser" , "operating_system" , "why_use" , "another_reason" , "ai_ssp"])
        with st.expander("View all Data"):
            st.dataframe(df)

        with st.expander("AI_SSP status"):
            tast_df1 = df["ai_ssp"].value_counts().to_frame()
            tast_df1 = tast_df1.reset_index()
            st.dataframe(tast_df1)
            p1 = px.pie(tast_df1 , names="ai_ssp" , values="count")
            st.plotly_chart(p1)
        
        with st.expander("Gender status"):
            tast_df2 = df["gender"].value_counts().to_frame()
            tast_df2 = tast_df2.reset_index()
            st.dataframe(tast_df2)
            p1 = px.pie(tast_df2 , names="gender" , values="count")
            st.plotly_chart(p1)
       
        with st.expander("Age status"):
            tast_df3 = df["age"].value_counts().to_frame()
            tast_df3 = tast_df3.reset_index()
            st.dataframe(tast_df3)
            p1 = px.pie(tast_df3 , names="age" , values="count")
            st.plotly_chart(p1)
        
        with st.expander("Education status"):
            tast_df4 = df["education"].value_counts().to_frame()
            tast_df4 = tast_df4.reset_index()
            st.dataframe(tast_df4)
            p1 = px.pie(tast_df4 , names="education" , values="count")
            st.plotly_chart(p1)
        
        with st.expander("Job status"):
            tast_df5 = df["job"].value_counts().to_frame()
            tast_df5 = tast_df5.reset_index()
            st.dataframe(tast_df5)
            p1 = px.pie(tast_df5 , names="job" , values="count")
            st.plotly_chart(p1)
        
        with st.expander("Tool status"):
            tast_df6 = df["tool"].value_counts().to_frame()
            tast_df6 = tast_df6.reset_index()
            st.dataframe(tast_df6)
            p1 = px.pie(tast_df6 , names="tool" , values="count")
            st.plotly_chart(p1)




    if Admin_Panel == "Update":
        st.header("Edit/Update Item")
        st.subheader("View Item")
        result = view_all_data()
        df = DataFrame(result , columns=["first_name" , "last_name" , "age" , "gender" , "education" , "job" ,  "use_ai_for_academic_work" , "tool" , "app_or_web" , "web_browser" , "operating_system" , "why_use" , "another_reason" , "ai_ssp"])
        with st.expander("Current Data"):
            st.dataframe(df)
        a = st.data_editor(df , num_rows="dynamic")
        st.write(a)
#        #st.dataframe(view_unique_task())
#        list_of_task = [i[0] for i in view_unique_task()]
#        select_task = st.selectbox("Task To Edit" , list_of_task)
#        select_result = [get_task(select_task)]
#        st.write(select_result)
#        if select_result:
#            task1 = select_result[0][0]
#            task2 = select_result[0][1]
#            task3 = select_result[0][2]
#            task4 = select_result[0][3]
#            task5 = select_result[0][4]
#            task6 = select_result[0][5]
#            task7 = select_result[0][6]
#            task8 = select_result[0][7]
#            task9 = select_result[0][8]
#            task10 = select_result[0][9]
#            task11 = select_result[0][10]
#            task12 = select_result[0][11]
#            task13 = select_result[0][12]
#            task14 = select_result[0][13]
#
#
#            c1 , c2 = st.columns(2)
#        
#        with c1:
#            nfname = st.text_input(label=str(task1) , max_chars=20 , placeholder="Alireza" , key="fir23stname")
#            nlname = st.text_input(label=str(task2) , max_chars=20 , placeholder="Jafari", key="lastn123ame")
#            nage = st.number_input(label=str(task3) , min_value=18 , placeholder=22 , key="you123rage")
#        with c2:
#            nsex = st.selectbox(label=str(task4) , options=[None , "Male" , "Female"] , index=0 , key="you456456rgender")
#            neducation = st.selectbox(label=str(task5) , options=[None ,"Diploma" , "Associate degree" , "Bachelors degree" , "Master degree" , "PHD (Doctorate)" , "Postdoctoral Researcher"] , index=0 , key="youre456456ducation")
#            njob = st.text_input(label=str(task6) , placeholder="Computer Engineer" , key="you456456rjob")
#        
#        nuse_academic_ai_tool = st.selectbox(label=str(task7) , options=[None , "Yes" , "No"] , index=0 , key="youra45342cademicai")
#        
#        ntool = st.selectbox(label=str(task8) , options=[None , "ChatGPT" , "Bing AI" , "Gemeni" , "Midjourney(Image Generation)" , "Microsoft Copilot"] , index=0 , key="a4564itool")
#           
#        napp_or_web = st.selectbox(str(task9) , options=[None , "Web Browser" , "Application" , "Both"] , index=0 , key="appo4563rweb")
#        nweb_browser = st.selectbox(str(task10) , options=[None , "Google Chrome" , "Firefox"] , index=0 , key="we45623b1")
#        noperating_system = st.selectbox(str(task11) , options=[None , "Windows" , "Mac OS" , "Linux" , "Android" , "IOS"] , index=0 , key="oxfghp1")
#        nwhy_use = st.selectbox(label=str(task12) , options=[None , "User Friendly" , "High Efficiency" , "Free" , "High Responsibility" , "Other"] , index=0 , key="wh342y1")
#        nanother_reason = st.text_input(label=str(task13) , max_chars=25 , placeholder="Another Reason" , key="anot67w3herreason1")
#        nmainq = st.selectbox(label=str(task14) , options=[None , "Yes" , "No"] , index=0 , key="ma745inq1")
#                    
#                    
#        fsbtn = st.button(label="Submit" , type="primary" , key="sbtn2")
#        if fsbtn:
#            if nfname.isalpha() == False:
#                st.error("Please enter your First Name (Q1)")
#                st.stop()
#
#            if nlname.isalpha() == False:
#                st.error("Please enter your Last Name (Q2)")
#                st.stop()
#            if nsex == None:
#                st.error("Please Select your (Q4)")
#            if neducation == None:
#                st.error("Please Select your (Q5)")
#            if job.isalpha == False:
#                st.error("Please enter your Job (Q8)")
#                st.stop()
#
#            
#            if nage == 27 and neducation== "Postdoctoral Researcher" or nage == 28 and neducation== "Postdoctoral Researcher" or nage == 29 and neducation== "Postdoctoral Researcher" or nage == 30 and neducation== "Postdoctoral Researcher":
#                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
#                st.stop()
#            if nage == 26 and neducation== "PHD (Doctorate)":
#                st.error("You can not choose these options based on tradition [PHD (Doctorate)")
#                st.stop()
#            elif nage == 26 and neducation == "Postdoctoral Researcher":
#                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
#                st.stop()
#            elif nage ==25 and neducation == "Postdoctoral Researcher":
#                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
#                st.stop()
#            elif nage ==25 and neducation== "PHD (Doctorate)":
#                st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
#                st.stop()
#            elif nage == 24 and neducation == "Postdoctoral Researcher":
#                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
#                st.stop()
#            elif nage == 24 and neducation== "PHD (Doctorate)":
#                st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
#                st.stop()
#            elif nage ==23 and neducation == "Postdoctoral Researcher":
#                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
#                st.stop()
#            elif nage ==23 and neducation== "PHD (Doctorate)":
#                st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
#                st.stop()
#            elif nage ==23 and neducation== "Master degree":
#                st.error("You can not choose these options based on tradition [Master degree]")
#                st.stop()
#            elif nage == 22 and neducation == "Postdoctoral Researcher":
#                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
#                st.stop()
#            if nage == 22 and neducation== "PHD (Doctorate)":
#                st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
#                st.stop()
#            elif nage == 22 and neducation== "Master degree":
#                st.error("You can not choose these options based on tradition [Master degree]")
#                st.stop()
#            elif nage == 21 and neducation == "Postdoctoral Researcher":
#                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
#                st.stop()
#            elif nage == 21 and neducation== "PHD (Doctorate)":
#                st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
#                st.stop()
#            elif nage == 21 and neducation== "Master degree":
#                st.error("You can not choose these options based on tradition [Master degree]")
#                st.stop()
#            elif nage == 21 and neducation == "Bachelors degree":
#                st.error("You can not choose these options based on tradition [Bachelors degree]")
#                st.stop()
#            elif nage == 20 and neducation == "Postdoctoral Researcher":
#                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
#                st.stop()
#            elif nage == 20 and neducation== "PHD (Doctorate)":
#                st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
#                st.stop()
#            elif nage == 20 and neducation== "Master degree":
#                st.error("You can not choose these options based on tradition [Master degree]")
#                st.stop()
#            elif nage == 20 and neducation == "Bachelors degree":
#                st.error("You can not choose these options based on tradition [Bachelors degree]")
#                st.stop()
#            elif nage == 20 and neducation =="Associate degree":
#                st.error("You can not choose these options based on tradition [Associate degree]")
#                st.stop()
#            elif nage == 19 and neducation == "Postdoctoral Researcher":
#                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
#                st.stop()
#            elif nage == 19 and neducation== "PHD (Doctorate)":
#                st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
#                st.stop()
#            elif nage == 19 and neducation== "Master degree":
#                st.error("You can not choose these options based on tradition [Master degree]")
#                st.stop()
#            elif nage == 19 and neducation == "Bachelors degree":
#                st.error("You can not choose these options based on tradition [Bachelors degree]")
#                st.stop()
#            elif nage == 19 and neducation =="Associate degree":
#                st.error("You can not choose these options based on tradition [Associate degree]")
#                st.stop()
#            elif nage == 18 and neducation == "Postdoctoral Researcher":
#                st.error("You can not choose these options based on tradition [Postdoctoral Researcher]")
#                st.stop()
#            elif nage == 18 and neducation== "PHD (Doctorate)":
#                st.error("You can not choose these options based on tradition [PHD (Doctorate)]")
#                st.stop()
#            elif nage == 18 and neducation== "Master degree":
#                st.error("You can not choose these options based on tradition [Master degree]")
#                st.stop()
#            elif nage == 18 and neducation == "Bachelors degree":
#                st.error("You can not choose these options based on tradition [Bachelors degree]")
#                st.stop()
#            elif nage == 18 and neducation =="Associate degree":
#                st.error("You can not choose these options based on tradition [Associate degree]")
#                st.stop()
#            edit_task_data(nfname , nlname , nage , nsex , neducation , njob ,  nuse_academic_ai_tool , ntool , napp_or_web , nweb_browser , noperating_system , nwhy_use , nanother_reason , nmainq , task1, task2, task3, task4, task5, task6, task7, task8, task9, task10, task11, task12, task13, task14)
#            st.success("Item Updated")
#            st.info(f"Thank you very much {nfname} {nlname} for giving your valuable time to our team")
#            result = view_all_data()
#            df = DataFrame(result , columns=["first_name" , "last_name" , "age" , "gender" , "education" , "job" ,  "use_ai_for_academic_work" , "tool" , "app_or_web" , "web_browser" , "operating_system" , "why_use" , "another_reason" , "ai_ssp"])
#            with st.expander("Updated Data"):
#                st.dataframe(df)






    if Admin_Panel == "Delete":
        st.subheader("Delete Item")

    if Admin_Panel == "About":
        st.subheader("About")


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















