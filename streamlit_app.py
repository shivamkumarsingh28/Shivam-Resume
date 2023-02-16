import streamlit as st
from PIL import Image
import smtplib
import requests
import datetime
import base64
from streamlit_player import st_player
import streamlit.components.v1 as components


st.set_page_config(
     page_title="Shivam Resume",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="collapsed",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

#####################




def datafetch(a, b, c):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
    st.markdown(f'<div>{c}</div>',unsafe_allow_html=True)
  with col2:
    st.markdown(b)

def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([2,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(f'<div>{b}</div>',unsafe_allow_html=True)
  with col3:
    st.markdown(f'[Click here]({c})')
    st.components.v1.iframe(c, scrolling=True)

def txt5(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(f'{b}')
  with col3:
   
    st_player(c, height=200, key=b)
    
#####################


with st.sidebar:
  with st.form("my_form", clear_on_submit=True):
            name= st.text_input(label="Name",value="", placeholder="Enter Name Here", type="default", key="name")
            email =st.text_input(label="Email",value="", placeholder="Enter Email Here", type="default", key="email")
            number= st.text_input(label="Number",value="", max_chars=10, placeholder="Enter Number Here", type="default", key="number")
            message= st.text_area(label="Message",value="", max_chars=1000, placeholder="Enter Number Here", key="message")

            submitted = st.form_submit_button("Hire")
          
            
            if submitted:
                conn= smtplib.SMTP('smtp.gmail.com', 587)
                conn.starttls()
                conn.login('startupsaeeam@gmail.com','qckkfvequfvzxrnl')
                sendmsg= ("SaeeAM ----" +name+" "+email+" "+number+" "+message)
                conn.sendmail('startupsaeeam@gmail.com', [email.split(","), 'startupsaeeam@gmail.com'], sendmsg)
                conn.quit()
                st.success('Done')
                st.balloons()

# with open("style.css") as f:
#     st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################

st.write('''
  # SHIVAM KUMAR SINGH, Entrepreneur.
  ##### *Resume* 
  ''')
  
image = Image.open('dp1.jpg')
st.image(image, width=150)
  
st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
  - **Who I AM** `Teacher, Entrepreneur, Sportperson, CEO, Leader, Programmer, Developer, Student, Humble Person, And Honest On Work`.
  - Experienced Educator, Entrepreneur, Youtuber, Mentor, Team Leader, Project Manager and Administrator with almost 5 years of experience in all domain i mention and a passion for delivering best through learning. 
  - Strong verbal and written communication skills as demonstrated by extensive participation as speaker .
  - `CEO` on my business **`SaeeAM`** *Indian collage student startup company* i will work here in all domain through that i learn and improve my self.
  - My hobies `Painting, Writing, Dancing, Reading, Hockey, Running, Kabaddi, Cycling, Gym` that i like to do when i free and when i enjoy my life and when i disturb i do .
  ''')

st.markdown('''
  ## Education
  ''')


txt('**Advance Diploma In Computer** (IBM, Aictc, Nsti, DGT), *Nsti-Bangluru*, Bangluru',
  '2022-2024')
st.markdown('''
  - PERCENTAGE: `Puruing`
  - SUBJECTS `Jave, Cloud Computing, Web Development, IT & Iot, And More...`.
  ''')
  
txt('**Programming, Data Structure And Algorithm With Python** (Aictc, Swayam, IIT-Madras), *Online*, Delhi',
  'OnGoing')
st.markdown('''
  - PERCENTAGE: `Puruing`
  - SUBJECTS `Python, Python OOPS, Data Structure, Algorithms, And More...`.
  - Assignment Marks - Assignment - 1st-`60%`, 2nd- `70%`, 3rd-`70%`, 4th- `100%`, And Upcoming
  - Exam Date - 25-SEP, 2022
  ''')
  
txt('**Google Android Developer- Internship** (Aictc, Google, Intership, ), *Online*, Delhi',
  'OnGoing')
st.markdown('''
- PERCENTAGE: `Puruing`
- SUBJECTS `Kotlin, Android Studio, XML, And More...`.
''')

txt('**Salesforce CRM- Internship** (Aictc, Salesforce, Intership, ), *Online*, Delhi',
'OnGoing')
st.markdown('''
- PERCENTAGE: `Puruing`
- SUBJECTS `Salesforce, Admin, Developer, And More...`.
''')

txt('**Bachelors of Science** (BIOTECHNOLOGY), *JAMIA MILLIA ISLAMIA - STUDY CENTER*, DELHI',
'2019-2022')
st.markdown('''
- GPA: `PURSUING`
- Graduated with First Class Honors.
- SUBJECTS `MATH, BOTANY, ZOOLOGY`.
''')


txt('**INTERMEDIATE 12TH** (SCIENCE - PCM), *SHYAM DARI YAMUNA HIGH SCHOOL*, BIHAR, *BIHAR BOARD*',
'2017-2019')
st.markdown('''
- PERCENTAGE: `62%`
- INTERMEDIATE WITH First Class Honors.
- SUBJECTS `PHYSICS, CHEMISTRY, MATH`.
''')

txt('**MATRICULATION 10TH** (ALL SUBJECT), *SARVODAYA BAL VIDYALAYA NO-1*, DELHI, *CBSE-BOARD*',
'2016-2017')
st.markdown('''
- GPA: `7`
- ALL SUBJECT- `MATH, SCIENCE, ENGLISH, SANSKRIT, SOCIAL-SCIENCE`.
''')


#####################
st.markdown('''
## Work Experience
''')

txt('**BYJU'S Think And Learn PVT.LTD**, BDA-Role, Bangalore-Prestige Tech Park',
'2022')
st.markdown('''
- CTC: `10L Yearly`.
- Work: Comunication with parents/student through call understand any guide and help required for both of them. Guide and help parents and student through zoom counselling session and also provide byju's product solution.`.
''')

txt('**Content Creator**, [SaeeAM Education YouTube Channel](https://www.youtube.com/watch?v=PIKz3R4Nqpc&list=PLF7OcypGGslKsmS8uqCOjLoWJqYPai_Us)',
'2019-Present')
st.markdown('''
- Created `261-Videos` `Math, Science, English, Gk&GS`.
- Level `6th to 12th, ITI-Diploma, Graduation, Compedition Exam` `Math, Science, English, Gk&GS, Reasoning`.
''')

txt('**Content Creator**, [SaeeAM Coding YouTube Channel](https://www.youtube.com/channel/UCUSh5Tyq2G7kBrTTE005prA/playlists)',
'2019-Present')
st.markdown('''
- Created `100-Video` `Python, Streamlit, Django, React, Javascript, Linux, Google Cloud Computing, AWS-Azure, HTML, Css, SQL, Panda, Numpy, Matplot, Heroku, And More ...`.
''')

txt('**Content Writer**, [SaeeAM Blog](https://g.page/r/CR93AGLEpeP_EAE) on Google My Business',
'2019-Present')
st.markdown('''
- Written `Many Blog` Education, Career, Job Fair, Services, And lOts of more...
''')

txt('**Private Institution Teacher**, Faculty of Science(PCM) , Pie Institute, Bihar',
'2017-2019')
txt('**Online Teacher**, SaeeAM Classes, Faculty Of Education, All Over India',
'2020-Present')
txt('**Career Guide**, Faculty Of Career, SaeeAM, All Over India',
'2017-Present')
st.markdown('''
- Provided mentorship and supervision to junior students, school level, 10th./12th./B.Sc. students. 
- Online/Offline Medium To Teach `Zoom, Meet`, `School/Institution/Collage`. 
- Video Notes, Class Notes, Study Notes Prepare For Online/Offline Classes.
- Video Lecture Public On Youtube Channels [SaeeAM Edcation](https://www.youtube.com/channel/UCNfYdNva6gCCqq5mdIKHnTw/playlists)
- Lecture Note Public On Telegram Channels [SaeeAM Classes](https://t.me/+4Wwajk1RorA0OTE9)
- Doubt Session Discuss Through Whats'app Group [SaeeAM Class](https://chat.whatsapp.com/KvqQTGzvYp405hofDsHyuO)
''')

txt('**VODAFONE PVT.LTD**, SALES-TL, DELHI',
'2017')
st.markdown('''
- CTC-IN HAND: `240K Yearly`
- WHAT WE DO `Sales, Pitching, Product-Describe, And More ...`
- WHAT WE LEARN `Sales, Communication-skill, Personality-Development, Customer-handling, Product-Diling And More ...`.
''')

txt('**Film Shooting PVT.LTD**, ALL TYPES WORK, ALL OVER INDIA',
'2018-2020')
st.markdown('''
- CTC-IN HAND: `360K Yearly`
- WHAT WE DO `Sales, Pitching, Product-Describe, And More ...`
- WHAT WE LEARN `Sales, Communication-skill, Personality-Development, Customer-handling, Product-Diling And More ...`.
''')

#####################

st.markdown('''
## Skills
''')
    # disc=edu[15].split(',',1)
txt3("**Programming**","`Python`, `JavaScript`, `Linux`,`Kotlin`, `XML`, `Java`, `Php`")
txt3("**Data processing/wrangling**","`SQL, pandas, numpy`")
txt3("**Data visualization**","`matplotlib`, `seaborn`")
txt3("**Database**","`MySql`, `mongodb`")
txt3("**Machine Learning**","`scikit-learn(**)`, `TensorFlow`")
txt3("**Web development**","`Flask`,`Django`,`Reactjs`,`Nodejs`, `HTML`, `CSS`,`NodeJs`, `Php-Laravel`,`Java-Spring`, `ExpressJs`, `AngularJs`")
txt3("**Model deployment**","`streamlit`, `Heroku`, `AWS`, `Digital Ocean`,`Google Cloud Computing`, `Microsoft Azure`, `AWS-Cloud`, `ngrok`, `Github`, `Pythonanywhere`")
txt3("**App deployment**","`Android Studio`, `Flutter`, `Material Design`,`JavaScript`, `Kivy`, `reactjs`")
txt3("**Other Tools**","`Python-Tkinter`, `Python-opencv`,`d3.js`")
# 
st.markdown('''
## Profile Links
''')


txt3("**Git Hub Link**","[Click Here](https://github.com/shivamkumarsingh28)")
txt3("**LinkedIn Profile**","[Click Here](https://www.linkedin.com/in/shivam-singh-6a7212192/)")
txt3("**SaeeAM Business Profile**","[Click Here](https://business.google.com/n/13598897696179258024/profile?hl=en-GB&fid=18438763562261313311)")

#####################


st.markdown('''
## Project Links
''')

txt5("**Painter/Drawing/Sketch**", "- Created `Painter`.[Click Here]()", "https://youtu.be/0H2CIySbIX4")
txt5("**Consultant Career Guider**", "- Created `Consultant`.[Click Here]()", "https://www.youtube.com/watch?v=3UwQ_dE8RzA")
txt5("**Teaching/ Mentor**", "- Created `Teacher`.[Click Here]()", "https://www.youtube.com/watch?v=QxPMubY19Ak&t=8s")
txt5("**Coding Portal**", "- Created `Coding Portal`.[Click Here]()", "https://youtu.be/bCbMtxfh97I")
txt5("**Kitchen_Garden_Project#1**", "- Created `Kitchen Garden`.[Click Here]()", "https://youtu.be/8eDu0ffscrw")
txt5("**Online_School_Project#2**", "- Created `Online School`.[Click Here]()", "https://www.youtube.com/watch?v=lB-rAgf1vI0")
txt5("**WorkFromHome_Project#3**", "- Created `Workfromhome`.[Click Here]()", "https://youtu.be/I4rE_jWnXbU")
txt5("**Online_Business_Project#4**", "- Created `Online Business`.[Click Here]()", "https://youtu.be/SAFWXAaJLTA")
txt5("**Digital_Resume_Project#5", "- Created `Digital Resume`.[Click Here](https://github.com/shivamkumarsingh28/Shivam-Resume.git)", "https://www.youtube.com/watch?v=vCEE4VhrxeM")
txt5("**Coding_Classes_Batch#3**", "- Created `Coding Classes`.[Click Here]() ", "https://www.youtube.com/watch?v=cLJMWbHLtIM")

