import streamlit as st
from PIL import Image
import smtplib
import requests
import hydralit_components as hc
from streamlit_player import st_player, _SUPPORTED_EVENTS
import datetime
import base64
import streamlit.components.v1 as components
from gsheetsdb import connect

# Define your javascript

#make it look nice from the start
# st.set_page_config(layout='wide',initial_sidebar_state='collapsed')
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

conn= connect()

def SaeeAM_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = "https://docs.google.com/spreadsheets/d/1AUUOpmJuftHrZ3RCjnKHGGZ1mF9GdLQtx3ravbNDYyM"
Database = SaeeAM_query(f'SELECT * FROM "{sheet_url}"')

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


# specify the primary menu definition
menu_data = [
    {'id':'Achieve','icon': "fas fa-archive", 'label':"Achievement"},
    {'id':'Projects','icon':"fas fa-project-diagram",'label':"Projects"},
    {'id':'Past','icon': "fas fa-angle-left", 'label':"Was Do"},#no tooltip message
    {'id':'Present','icon': "fas fa-stop-circle", 'label':"Doing"},
    {'id':'Future','icon': "fas fa-angle-right", 'label':"Will Do"},
]

over_theme = {'txc_inactive': '#FFFFFF'}
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    home_name='Shivam Kumar Singh',
    login_name='Social Media',
    hide_streamlit_markers=True, #will show the st hamburger as well as the navbar now!
    sticky_nav=True, #at the top or not
    sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
)


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

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
if menu_id == "Shivam Kumar Singh":
  
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


# Print results.
  for edu in Database:
    
    if edu[13] != None:
      # disc=edu[15].split(',',1)
      datafetch(edu[13],edu[14], edu[15])
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
  
  txt('**ITI- TECHNICAL TRAINING** (WELDER TRADE), *AKS- ARAB KI SARAI*, DELHI-NIZAMUDDIN',
  '2020-2021')
  st.markdown('''
  - PERCENTAGE: `75%`
  - SUBJECTS `MATH & SCIENCE, TRADE THEORY, WORKSHOP-PRACTICAL, IT & COMMUNICATION SKILL, ENGINEERING DRAWING`.
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
  for work in Database:
    
    if work[16] != None:
      # disc=edu[15].split(',',1)
      txt(work[16],work[17], work[18])
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
  txt('**YAMAHA PVT.LTD**, ITI-WELDER, UP',
  '2022')
  st.markdown('''
  - CTC-IN HAND: `120K Yearly`
  - WHAT WE DO `Engine Mounting, Gauging, Panasonic Robot Operator, Welding Frame, Quality Checking, And More ...`
  - WHAT WE LEARN `Technical Knowledage, Apprentienship`.
  ''')

  txt('**MARUTI SUZUKI PVT.LTD**, ITI-WELDER, DELHI',
  '2022')
  st.markdown('''
  - CTC-IN HAND: `240K Yearly`.
  ''')

  
  
  #####################

  st.markdown('''
  ## Skills
  ''')
  for skill in Database:
    
    if skill[19] != None:
      # disc=edu[15].split(',',1)
      txt3(skill[19],skill[20])
  # 
  st.markdown('''
  ## Profile Links
  ''')
  for skill in Database:
    
    if skill[21] != None:
      # disc=edu[15].split(',',1)
      txt3(skill[21],skill[22])

#####################
if menu_id == "Social Media":
  st.markdown('''
  ## Social Media
  ''')
  for link in Database:
    
    if link[23] != None:
      # disc=edu[15].split(',',1)
      txt3(link[23],link[24])
      st.markdown("***")
  

if menu_id == "Projects":
  for projects in Database:
    if projects[3] != None:
      txt5(projects[3],projects[4], projects[5])
      st.markdown("***")
  
  

if menu_id == "Past":

# Print results.
  for wasdo in Database:
    with st.container():
      if wasdo[10] != None:
        txt3(wasdo[10],wasdo[11])
        st.markdown("***")
    
    
if menu_id == "Present":

# Print results.
  for doing in Database:
    if doing[8] != None:
      txt3(doing[8],doing[9])
      st.markdown("***")
    
if menu_id == "Future":

# Print results.
  for willdo in Database:
    if willdo[6] != None:
      txt3(willdo[6], willdo[7])
      st.markdown("***")
    
    
if menu_id == "Achieve":
  for achieve in Database:
    with st.container():
      if achieve[0] != None:
        txt4(achieve[0], achieve[1], achieve[2])
        st.markdown("***")
    
