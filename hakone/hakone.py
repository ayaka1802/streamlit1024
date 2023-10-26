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
    img=Image.open('https://github.com/ayaka1802/streamlit1024/blob/master/hakone/media/cafe.jpeg?raw=true')
    st.image(img,caption='ピース',use_column_width=True)

    '''
    みかん食べてitoして 16:00~
    '''
    img=Image.open('https://github.com/ayaka1802/streamlit1024/blob/master/hakone/media/mikan.JPG?raw=true')
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
    img=Image.open('https://github.com/ayaka1802/streamlit1024/blob/master/hakone/media/hebi.jpeg?raw=true')
    st.image(img,caption='へび！',use_column_width=True)

with tab2:
    st.header("2日目 10/21(土)")
    '''
    川とかお散歩
    '''
    img=Image.open('https://github.com/ayaka1802/streamlit1024/blob/master/hakone/media/kawa.jpeg?raw=true')
    st.image(img,caption='かわ！',use_column_width=True)
    img=Image.open('https://github.com/ayaka1802/streamlit1024/blob/master/hakone/media/hasi.JPG?raw=true')
    st.image(img,caption='はし かわいい',use_column_width=True)

    '''
    お昼
    '''
    img=Image.open('https://github.com/ayaka1802/streamlit1024/blob/master/hakone/media/mesi.JPG?raw=true')
    st.image(img,caption='おいしそ',use_column_width=True)

    '''
    大涌谷
    '''
    img=Image.open('https://github.com/ayaka1802/streamlit1024/blob/master/hakone/media/oowaku.JPG?raw=true')
    st.image(img,caption='みづきちゃん合成せねば',use_column_width=True)

    video_file = open('https://github.com/ayaka1802/streamlit1024/blob/master/hakone/media/oowaku.mp4?raw=true', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

