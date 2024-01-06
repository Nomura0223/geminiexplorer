# ライブラリのインポート -------------------
import streamlit as st
import google.generativeai as genai
from PIL import Image

# APIキーの設定 -----------------------
genai.configure(api_key="AIzaSyDKS9IwFZSqnon9UXzRE6yWokgrwe-2cmQ")
model = genai.GenerativeModel('gemini-pro')

# サイド画面 ----------------------------------

st.sidebar.title('設定', anchor='sidebar')
st.sidebar.subheader('', divider="rainbow")

language = st.sidebar.selectbox('言語:',
                list(["日本語", "英語"]))

formarity = st.sidebar.selectbox('シーン:', 
             list(["ビジネス", "プライベート"]))

perpose = st.sidebar.selectbox('目的:', 
             list(["打合せの日程調整", "その他"]))

if perpose == "その他":
    perpose = st.sidebar.text_input('その他:')

length = st.sidebar.slider('文字数:', 100, 500, 300)

st.sidebar.subheader('', divider="rainbow")

reply = st.sidebar.toggle('返信')
if reply:
    receivemail = st.sidebar.text_area('受信メール:', height=400)

st.sidebar.subheader('', divider="rainbow")

# メイン画面 -------------------

st.title('メール作成アシスタント', anchor='top')


image = Image.open('robot_wide.png')
st.image(image, use_column_width=True)

# ボタンの設定
col1, col2, col3 = st.columns(3)
with col2:
    button = st.button('作成', use_container_width=True)

st.subheader('', divider="rainbow")

user_input = ""
user_input += f"言語は{language}で文章を作成してください。{length}文字程度の{formarity}シーンでのメールの文章作成してください。メールの目的は{perpose}です。"

if reply:
    user_input += f"文章は次の受信メールに対する返信として作成下さい。\n\n{receivemail}"

# ボタンが押されたら
if button:
    user_text = st.chat_message("user")
    user_text.write(user_input)
    with st.spinner('文章を作成中...'):
        response = model.generate_content(user_input)
    message = st.chat_message("ai")
    message.write(response.text)
    st.subheader('', divider="rainbow")

