# ライブラリのインポート -------------------
import streamlit as st
import google.generativeai as genai
from PIL import Image

# ページの設定 ----------------------------
st.set_page_config(
    page_title="Gemini Explorer",
    page_icon="🤖",
)

# APIキーの設定 -----------------------
genai.configure(api_key="AIzaSyDKS9IwFZSqnon9UXzRE6yWokgrwe-2cmQ")
model = genai.GenerativeModel('gemini-pro')

# メイン画面 -------------------

st.title('🤖 Welcome to GeminiExplorer 🤖', anchor='top')

image = Image.open('robot_wide.png')
st.image(image, use_column_width=True)


st.sidebar.success("Select the functions above.")

st.markdown(
    """
    Gemini Explorer (ジェミナイエクスプローラー) へようこそ！
    このアプリケーションでは、Gooegleが2023年12月に公開した生成AIモデルGeminiの機能を体験していただけます。\n
    👈 サイドバーからアプリを選択して、Geminiの機能の例を体験下さい！
    """
)
