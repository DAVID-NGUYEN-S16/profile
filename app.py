import streamlit as st
import requests 
from streamlit_lottie import  st_lottie
from PIL import Image
# Find icon from https://www.webfx.com/tools/emoji-cheat-sheet/

st.set_page_config(page_title='My Webpage', page_icon=':grinning_face:', layout='wide')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_css("style/style.css")
# ---- LOAD ASSETS -----
lottie_coding = load_lottieurl('https://lottie.host/9ef09e1b-12f5-4a92-b89e-6b645d61a447/T6ShFNr3Cd.json')
img_contact_form = Image.open('image/294273449_1444844159364205_1532145779273968602_n.jpg')
# ---- HEADER SECTION ---- 
with st.container():
    st.subheader('Hi, I am David :wave:')
    st.title('AI Engineer From Viet Nam')
    st.write('nice ><')
    st.write("[Learn More >](https://www.webfx.com/tools/emoji-cheat-sheet/)")
    
# WHAT I DO 
with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column : 
        st.header('What I do ')
        st.write('###')
        st.write(
            '''
            I will sorry
            '''
        )
        st.write("[Facebook>](https://www.facebook.com/nam14056969/)")
    with right_column:
        st_lottie(lottie_coding, height=300, key='Coding')
# ---- PROJECTS ----
with st.container():
    st.write('---')
    st.write("My Projects")
    st.write('##')
    
    image_column, text_column = st.columns((1, 2))
    with image_column:
        # insert image
        st.image(img_contact_form)
    with text_column :
        st.subheader('Integrate Lottie Animations Inside Your Streamlit App')
        st.write(
            '''
            Learn how to use Lottie Files in Streamlit!
            '''
        )
        st.markdown("[Watching Video...](https://youtube.com)")
# ---- CONTACT ------
with st.container():
    st.write('---')
    st.header('Get In touch With Me')
    st.write('##')
    # Documentation: https://formsubmit.co/
    contact_form = '''
    <form action="https://formsubmit.co/nguyenvannam14052003@gmail.com" method="POST">
        <input type="text" name="name" placeholder='Your name' required>
        <input type="email" name="email" placeholder='Your email' required>
        <button type="submit">Send</button>
    </form>
    '''
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()