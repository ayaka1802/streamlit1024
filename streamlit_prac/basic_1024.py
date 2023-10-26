import streamlit as st
#import numpy as np
#import pandas as pd
#from PIL import Image
import time

st.title('Streamlit 練習 10/24(火)')

#プログレスバー 進捗
st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

'''Done!'''
# st.write('DataFrame')

# df = pd.DataFrame({
#     '1列目':[1,2,3,4],
#     '2列目':[10,20,30,40]
# })

# #st.write(df) 下と同じ結果、縦横は指定できない

# #1.データの表示
# #https://docs.streamlit.io/library/api-reference/data

# #動的なテーブル
#style.highlight_max()ハイライトをつけれる　axis=0は行
#st.dataframe(df.style.highlight_max(axis=0),width=200,height=200)

#静的なテーブル
#st.table(df.style.highlight_max(axis=0))

#2.マジックコマンド マークダウン
#https://docs.streamlit.io/library/api-reference/text


#"""
# 章
## 節
### 項

#```python
#import numpy as np
#import pandas as pd 
#```
#"""

#3.チャート
#https://docs.streamlit.io/library/api-reference/charts

# df2=pd.DataFrame(
#     np.random.rand(20,3),
#     columns=['a','b','c']
# )
# """
# グラフ
# """
#折れ線グラフ
#st.line_chart(df2)

#エリアチャート
#st.area_chart(df2)

#棒グラフ
#st.bar_chart(df2)
#"""
#新宿付近のマップ
#"""
# #マップ
# #新宿付近の緯度経度を作成
# df_map=pd.DataFrame(
#     np.random.rand(100,2) /[50,50] + [35.69,139.70],
#     columns=['lat','lon']
# )
#st.map(df_map)

# """
# ### 箱根の思い出
# みづきちゃんとなっち
# """

#5.インタラクティブなウィジェット
#https://docs.streamlit.io/library/api-reference/widgets

#チェックボックス
st.write('Interactive Widgets')
# if st.checkbox('Show Image'):

#     #4.画像
#     #https://docs.streamlit.io/library/api-reference/media

#     img=Image.open('media/IMG_1671.JPG')
#     #use_column_widthはwebアプリの横幅に合わせる
#     st.image(img,caption='Hakone',use_column_width=True)

# """
# 大涌谷
# """
# if st.checkbox('Show Movie'):
#     #ビデオ
#     video_file = open('media/oowaku.mp4', 'rb')
#     video_bytes = video_file.read()
#     st.video(video_bytes)

# selected=st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1,11))
# )
# 'あなたの好きな数字は、', selected,'です。'

#2カラム表示
left_column, right_column = st.columns(2)
button1=left_column.button('右カラムに文字を表示')
if button1:
    right_column.write('ここは右カラムです')

#エクスパンダー
expander=st.expander('問い合わせ')
expander.write('問い合わせに対する回答')

#st.sidebarつけるとサイドバーに持っていける
#テキスト入力
# text=st.text_input('あなたの趣味を教えてください')
# 'あなたの趣味：', text

# #スライダ
# condition=st.slider('あなたの今の調子は？',0,100,50)
# 'コンディション：',condition

