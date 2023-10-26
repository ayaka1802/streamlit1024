import pandas as pd
import altair as alt
import streamlit as st
import yfinance as yf

st.title('米国株価可視化アプリ')

st.sidebar.write('''
# GAFA株価
こちらは米国株価可視化ツールです。
''')

st.sidebar.write('''
## 表示日数選択
''')

days = st.sidebar.slider('表示日数を指定してください。',1,50,20)

st.write(f'''
## 過去**{days}日間**のGAFA株価
''')

#キャッシュにデータを溜めて2回目以降読み込み速くする
@st.cache_data
def get_data(days, tickers):
    df = pd.DataFrame()
    for company in tickers.keys():
        tkr = yf.Ticker(tickers[company])
        hist = tkr.history(period=f'{days}d')
        hist.index = hist.index.strftime('%d %B %Y')
        hist = hist[['Close']]
        hist.columns = [company]
        hist = hist.T
        hist.index.name = 'Name'
        df = pd.concat([df, hist])
    return df

try:
    st.sidebar.write('''
    ## 株価の範囲指定
    ''')

    ymin, ymax = st.sidebar.slider('範囲を指定してください',0.0,1000.0,(0.0, 1000.0))

    tickers = {
        'apple': 'AAPL',
        'facebook': 'META',
        'google': 'GOOGL',
        'microsoft': 'MSFT',
        'netflix': 'NFLX',
        'amazon': 'AMZN'
    }

    df = get_data(days, tickers)

    companies = st.multiselect(
        '会社名を選択してください',
        list(df.index),
        ['google','amazon','facebook','apple']
    )

    if not companies:
        st.error('少なくとも一社は選んで下さい')
    else:
        data = df.loc[companies]
        #表を描画
        st.write("## 株価（USD）",data.sort_index())

        #表からグラフにするための変換
        data = data.T.reset_index()
        data = pd.melt(data, id_vars=['Date']).rename(
            columns={'value': 'Stock Prices(USD)'}
        )
        #チャート定義
        chart = (
            alt.Chart(data)
            .mark_line(opacity=0.8, clip=True)
            .encode(
                x="Date:T",
                y=alt.Y("Stock Prices(USD):Q", stack=None, scale=alt.Scale(domain=[ymin, ymax])),
                color='Name:N'
            )
        )
        #use_container_width 枠に収まるサイズに勝手に調整
        st.altair_chart(chart,use_container_width=True)
except:
    st.error(
        "エラーが起きました。"
    )