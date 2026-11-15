
import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(
    page_title="Trading Dashboard Pro",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.stApp {
    background: #080d18;
    color: white;
}
header[data-testid="stHeader"] {
    background: #080d18;
}
section[data-testid="stSidebar"] {
    background: #111827;
}
.main-title {
    color: #38bdf8;
    font-size: 32px;
    font-weight: 800;
}
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.title("⚙️ Settings")

timeframe = st.sidebar.selectbox(
    "Timeframe",
    ["1", "5", "15", "30", "60", "240", "D", "W", "M"],
    index=2
)

theme = st.sidebar.selectbox(
    "Chart Theme",
    ["dark", "light"],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.caption(
    "Untuk mengganti pair, klik ikon pencarian "
    "di bagian atas masing-masing chart."
)

# HEADER
st.markdown(
    '<div class="main-title">📈 TRADING DASHBOARD PRO</div>',
    unsafe_allow_html=True
)

st.caption("MULTI CHART • TRADINGVIEW • MARKET ANALYSIS")

st.markdown("---")

# MARKET INFO
a, b, c, d = st.columns(4)

a.metric("TOTAL CHART", "04")
b.metric("TIMEFRAME", timeframe)
c.metric("THEME", theme.upper())
d.metric("PLATFORM", "TRADINGVIEW")

st.markdown("---")
st.subheader("📊 LIVE MARKET CHARTS")

# TRADINGVIEW FUNCTION
def show_chart(symbol, timeframe, theme):

    config = {
        "autosize": True,
        "symbol": symbol,
        "interval": timeframe,
        "timezone": "Asia/Jakarta",
        "theme": theme,
        "style": "1",
        "locale": "en",
        "enable_publishing": False,
        "allow_symbol_change": True,
        "hide_side_toolbar": False,
        "withdateranges": True,
        "details": True,
        "calendar": False,
        "support_host": "https://www.tradingview.com"
    }

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            html, body {{
                margin: 0;
                padding: 0;
                width: 100%;
                height: 100%;
                background: #080d18;
                overflow: hidden;
            }}
            .tradingview-widget-container {{
                width: 100%;
                height: 620px;
            }}
            .tradingview-widget-container__widget {{
                width: 100%;
                height: 620px;
            }}
        </style>
    </head>
    <body>
        <div class="tradingview-widget-container">
            <div class="tradingview-widget-container__widget"></div>
            <script
                type="text/javascript"
                src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js"
                async>
                {json.dumps(config)}
            </script>
        </div>
    </body>
    </html>
    """

    components.html(
        html,
        height=635,
        scrolling=False
    )

# CHART 1 & 2
col1, col2 = st.columns(2, gap="medium")

with col1:
    st.markdown("### 🟠 BTC / USDT")
    show_chart("BINANCE:BTCUSDT", timeframe, theme)

with col2:
    st.markdown("### 🔵 ETH / USDT")
    show_chart("BINANCE:ETHUSDT", timeframe, theme)

st.markdown("---")

# CHART 3 & 4
col3, col4 = st.columns(2, gap="medium")

with col3:
    st.markdown("### 💱 EUR / USD")
    show_chart("OANDA:EURUSD", timeframe, theme)

with col4:
    st.markdown("### 🟡 GOLD / USD")
    show_chart("OANDA:XAUUSD", timeframe, theme)

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:#64748b;
                padding:20px;">
        TRADING DASHBOARD PRO V2<br>
        Powered by TradingView
    </div>
    """,
    unsafe_allow_html=True
)
