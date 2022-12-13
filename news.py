import pandas as pd
import yfinance as yf
import altair as alt
import streamlit as st


st.title('米国株式銘柄直近ニュース検索アプリ')

st.write('検索ボタンを押しても何も表示されない場合、ティッカーが間違っている可能性があります。')

try:
        list = []
        with st.form(key = 'columns_in_form'):
            cols = st.columns(5)
            for i, col in enumerate(cols):
                list.append(col.text_input(f'テッィカー入力',key=i))
              
            submitted = st.form_submit_button("検索")

            if submitted:
                    for i in range(5):
                      tik = list[i]
                      if not tik:
                            st.write('テッィカーが入力されていません。')   
                      else:
                            tik   
                            dtik = yf.Ticker(tik)
                            news = dtik.news
                            if not news:
                               st.write('ティッカーが正しくない可能性があります。')
                            else:
                             df = pd.DataFrame(news)
                             df = df.loc[:, ["title", "publisher","link"]]

                             
                            for i in range(8):
                               title = df.iloc[i-1,0]
                               url = df.iloc[i-1,2]
                               pub = df.iloc[i-1,1]
                               link = '{}({})({})'
                               link = link.format(title,pub,url)
                               st.markdown(link, unsafe_allow_html=True)

                              
                               
                            
                                   

except:
    st.error(
        "エラーが発生しました。ティッカーが正しいか確かめてください。"
    )


