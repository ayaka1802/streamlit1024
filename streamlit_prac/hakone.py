import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('箱根旅行')

tab1, tab2   = st.tabs(["1日目 10/20(金)", "2日目 10/21(土)"])

with tab1:
    st.header("1日目 10/20(金)")
    '''
    女子で新宿のカフェ ピース 14:30~
    '''
    img=Image.open('/Users/ayaka_py/Desktop/streamlit_1024/streamlit_prac/media/cafe.jpeg')
    st.image(img,caption='ピース',use_column_width=True)

    '''
    みかん食べてitoして 16:00~
    '''
    img=Image.open('/Users/ayaka_py/Desktop/streamlit_1024/streamlit_prac/media/mikan.JPG')
    st.image(img,caption='みかん',use_column_width=True)
    '''
    ホテルはこのへん
    '''
    df_map = pd.DataFrame(
    data=[[35.232, 139.104]],
    index=["湯本富士屋ホテル",],
    columns=['lat','lon']
)
    st.map(df_map)
    '''
    蛇さんこわい 21:00~
    '''
    img=Image.open('/Users/ayaka_py/Desktop/streamlit_1024/streamlit_prac/media/hebi.jpeg')
    st.image(img,caption='へび！',use_column_width=True)

with tab2:
    st.header("2日目 10/21(土)")
    '''
    川とかお散歩
    '''
    img=Image.open('/Users/ayaka_py/Desktop/streamlit_1024/streamlit_prac/media/kawa.jpeg')
    st.image(img,caption='かわ！',use_column_width=True)
    img=Image.open('/Users/ayaka_py/Desktop/streamlit_1024/streamlit_prac/media/hasi.JPG')
    st.image(img,caption='はし かわいい',use_column_width=True)

    '''
    お昼
    '''
    img=Image.open('/Users/ayaka_py/Desktop/streamlit_1024/streamlit_prac/media/mesi.JPG')
    st.image(img,caption='おいしそ',use_column_width=True)

    '''
    大涌谷
    '''
    img=Image.open('/Users/ayaka_py/Desktop/streamlit_1024/streamlit_prac/media/oowaku.JPG')
    st.image(img,caption='みづきちゃん合成せねば',use_column_width=True)

    video_file = open('/Users/ayaka_py/Desktop/streamlit_1024/streamlit_prac/media/oowaku.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

