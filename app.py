
import streamlit as st
import streamlit.components.v1 as components
import json

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Trading Dashboard Pro",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>
    .stApp {
        background-color: #0b1120;
        color: white;
    }

    header[data-testid="stHeader"] {
        background-color: #0b1120;
    }

    section[data-testid="stSidebar"] {
        background-color: #111827;
    }

    h1, h2, h3 {
        color: #ffffff;
    }

    div[data-testid="stMetric"] {
        background-color: #111827;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #263247;
    }

    .main-title {
        font-size: 30px;
        font-weight: bold;
        color: #38bdf8;
    }
</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================

st.sidebar.title("⚙️ Dashboard Settings")

st.sidebar.markdown("---")

st.sidebar.subheader("Chart Settings")

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
st.sidebar.subheader("Trading Pairs")

symbol1 = st.sidebar.text_input(
    "Chart 1",
    "BINANCE:BTCUSDT"
)

symbol2 = st.sidebar.text_input(
    "Chart 2",
    "BINANCE:ETHUSDT"
)

symbol3 = st.sidebar.text_input(
    "Chart 3",
    "OANDA:EURUSD"
)

symbol4 = st.sidebar.text_input(
    "Chart 4",
    "OANDA:XAUUSD"
)

st.sidebar.markdown("---")

st.sidebar.info(
    "Gunakan format EXCHANGE:SYMBOL. "
    "Contoh: BINANCE:BTCUSDT"
)

# =========================
# HEADER
# =========================

st.markdown(
    '<div class="main-title">📈 TRADING DASHBOARD PRO</div>',
    unsafe_allow_html=True
)

st.caption(
    "Multi Chart TradingView | Market Analysis Dashboard"
)

st.markdown("---")

# =========================
# MARKET OVERVIEW
# =========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("CHARTS", "04")

with col2:
    st.metric("TIMEFRAME", timeframe)

with col3:
    st.metric("THEME", theme.upper())

with col4:
    st.metric("STATUS", "READY")

st.markdown("---")

# =========================
# TRADINGVIEW CHART FUNCTION
# =========================

def tradingview_chart(symbol, timeframe, theme, height=480):

    config = {
        "autosize": True,
        "symbol": symbol,
        "interval": timeframe,
        "timezone": "Asia/Jakarta",
        "theme": theme,
        "style": "1",
        "locale": "en",
        "allow_symbol_change": True,
        "calendar": False,
        "support_host": "https://www.tradingview.com",
        "details": True,
        "hotlist": True,
        "withdateranges": True,
        "hide_side_toolbar": False,
        "watchlist": [],
        "studies": [
            "STD;SMA"
        ],
        "show_popup_button": True,
        "popup_width": "1000",
        "popup_height": "650"
    }

    config_json = json.dumps(config)

    html_code = f"""
    <div class="tradingview-widget-container"
         style="height:100%;width:100%">

        <div class="tradingview-widget-container__widget"
             style="height:100%;width:100%">
        </div>

        <script
            type="text/javascript"
            src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js"
            async>
            {config_json}
        </script>

    </div>
    """

    components.html(
        html_code,
        height=height,
        scrolling=False
    )


# =========================
# 4 CHART LAYOUT
# =========================

st.subheader("📊 Market Charts")

# ROW 1

col1, col2 = st.columns(2, gap="medium")

with col1:
    st.markdown(f"### 🟠 {symbol1}")
    tradingview_chart(
        symbol1,
        timeframe,
        theme
    )

with col2:
    st.markdown(f"### 🔵 {symbol2}")
    tradingview_chart(
        symbol2,
        timeframe,
        theme
    )

st.markdown("---")

# ROW 2

col3, col4 = st.columns(2, gap="medium")

with col3:
    st.markdown(f"### 💱 {symbol3}")
    tradingview_chart(
        symbol3,
        timeframe,
        theme
    )

with col4:
    st.markdown(f"### 🟡 {symbol4}")
    tradingview_chart(
        symbol4,
        timeframe,
        theme
    )

# =========================
# FOOTER
# =========================

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:#64748b; padding:15px">
        TRADING DASHBOARD PRO<br>
        Powered by TradingView Widgets
    </div>
    """,
    unsafe_allow_html=True
)
