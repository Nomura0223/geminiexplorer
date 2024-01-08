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
                list(["日本語", "English"]))

receiver = st.sidebar.selectbox('受信者:',
                list(["顧客", "上司", "同僚", "その他"]))
if receiver == "その他":
    receiver = st.sidebar.text_input('その他:')

formarity = st.sidebar.selectbox('トーン:', 
             list(["フォーマル", "カジュアル"]))

perpose = st.sidebar.text_input('目的:', placeholder="会議の招待、進捗報告など", value="")

other = st.sidebar.text_input('(任意) その他情報:', placeholder="明日までに返信が欲しい", value="")

# perpose = st.sidebar.selectbox('目的:', 
#              list(["会議の招待", "進捗報告", "その他"]))

# if perpose == "その他":
#     perpose = st.sidebar.text_input('その他:')


attachment = st.sidebar.toggle('添付ファイル')
if attachment:
    attachmentFile = st.sidebar.text_input('ファイルの種類', placeholder="進捗報告資料など", value="")

length = st.sidebar.slider('文字数:', min_value=100, max_value=500,value=300, step=50)

# reply = st.sidebar.toggle('返信')
# if reply:
#     receivemail = st.sidebar.text_area('受信メール:', height=400)

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
user_input += f"回答言語は「{language}」を使用。次の内容を考慮してメールを作成ください。受信者は「{receiver}」、目的は「{perpose}」です。文字数は「{length}」程度で「{formarity}」なトーンでお願いします。"

if other != "":
    user_input += f"メールには「{other}」ことを記載ください。"

if attachment:
    user_input += f"メール末尾には「{attachmentFile}」を添付します。"

# ボタンが押されたら
if button:
    if perpose != "":
        user_text = st.chat_message("user")
        user_text.write(user_input)
        with st.spinner('文章を作成中...'):
            response = model.generate_content(user_input)
        message = st.chat_message("ai")
        message.write(response.text)
        st.subheader('', divider="rainbow")
    else:
        st.error('目的を入力してください。')
    
