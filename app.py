import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

# st.write('Display Image')

# if st.checkbox('Show Image', True):
#     img = Image.open('./engineer.png')
#     st.image(img, caption='engineer', use_column_width=True)

# option = st.selectbox('あなたの好きな数字を教えてください。', 
#              list(range(1, 11)))

# 'あなたの好きな数字は、', option, 'です。'

# st.write('Interactive Widgets')
st.write('プレグレスバーの表示')
"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}%')
    bar.progress(i+1)
    time.sleep(0.05)

"Done!!!!"



left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# option = st.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味は、', option, 'です。'

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# "あなたのコンディションは、", condition, "です。"



# df = pd.DataFrame({
#     '1列目': [1,2,3,4],
#     '2列目': [10,20,30,40]
# })

# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

# st.map(df)

# st.line_chart(df)

# st.write(df)
# st.dataframe(df, width=100, height=100)
# st.dataframe(df.style.highlight_max(axis=0))
# st.table(df.style.highlight_max(axis=0))



# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """

