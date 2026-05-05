# Market Analysis Dashboard 💹

A high-fidelity, real-time financial tracking solution built in Power BI. This dashboard provides professional-grade technical analysis for multiple asset classes, featuring a modern dual-mode UI designed for traders and financial analysts.

---

## 🚀 Key Features

*   **Multi-Asset Coverage:** Dedicated views for **Crypto**, **Stocks**, and **ETFs** (Exchange Traded Funds).
*   **Dual-Mode Interface:** Fully integrated **Light Mode** and **Dark Mode** toggle buttons for optimal visibility in any environment.
*   **Interactive Candlestick Charts:** High-detail price action visuals for tracking Open, Close, and price volatility.
*   **Dynamic Timeframes:** One-click switching between different time horizons: **1Y, 3M, 5D, 5Y, 6M, and Max**.
*   **Real-Time Price Metrics:** Instant calculation of absolute price change and percentage variance.
*   **Company Branding:** Automated rendering of corporate and cryptocurrency logos via dynamic image URLs.

---

## 🛠️ Tech Stack

*   **Visualization:** Power BI Desktop
*   **Data Modeling:** Star Schema architecture optimized for high-frequency time-series data.
*   **UI/UX:** Advanced use of **Bookmarks** and **Selection Panes** to manage Light/Dark mode transitions and asset switching.
*   **Data Category:** Image URL integration for dynamic rendering of 50+ unique asset logos.

---

## 📊 Dashboard Modules

### 1. Crypto Market View
Track major digital assets like **ETH-USD**, **BTC-USD**, and **SOL-USD**. Designed with a focus on high-volatility tracking and crypto-native aesthetics.
# Market Analysis Dashboard 💹

A high-fidelity, real-time financial tracking solution built in Power BI. This dashboard provides professional-grade technical analysis for multiple asset classes, featuring a modern dual-mode UI designed for traders and financial analysts.

---

## 🚀 Key Features

*   **Multi-Asset Coverage:** Dedicated views for **Crypto**, **Stocks**, and **ETFs** (Exchange Traded Funds).
*   **Dual-Mode Interface:** Fully integrated **Light Mode** and **Dark Mode** toggle buttons for optimal visibility in any environment.
*   **Interactive Candlestick Charts:** High-detail price action visuals for tracking Open, Close, and price volatility.
*   **Dynamic Timeframes:** One-click switching between different time horizons: **1Y, 3M, 5D, 5Y, 6M, and Max**.
*   **Real-Time Price Metrics:** Instant calculation of absolute price change and percentage variance.
*   **Company Branding:** Automated rendering of corporate and cryptocurrency logos via dynamic image URLs.

---

## 🛠️ Tech Stack

*   **Visualization:** Power BI Desktop
*   **Data Modeling:** Star Schema architecture optimized for high-frequency time-series data.
*   **UI/UX:** Advanced use of **Bookmarks** and **Selection Panes** to manage Light/Dark mode transitions and asset switching.
*   **Data Category:** Image URL integration for dynamic rendering of 50+ unique asset logos.

---

## 📊 Dashboard Modules

### 1. Crypto Market View
Track major digital assets like **ETH-USD**, **BTC-USD**, and **SOL-USD**. Designed with a focus on high-volatility tracking and crypto-native aesthetics.
<img width="1280" height="719" alt="Screenshot 2026-05-05 110504" src="https://github.com/user-attachments/assets/2c78a591-49e6-4764-9375-bd6c7fa6b04d" />


### 2. Stock Market View
Deep-dive into blue-chip equities including **AAPL**, **GOOGL**, **MSFT**, and **AMZN**. Features precise price-tracking and historical trend analysis.
<img width="1279" height="719" alt="Screenshot 2026-05-05 110521" src="https://github.com/user-attachments/assets/8aeb07be-56fb-4bff-92ab-21209bddae9f" />


### 3. ETFs Dashboard
Monitor broad market segments and thematic funds such as **SPY**, **QQQ**, and **IWM**. Perfect for analyzing sectoral rotations and macro market health.
<img width="1276" height="716" alt="Screenshot 2026-05-05 110538" src="https://github.com/user-attachments/assets/35c5a77b-ead3-41fb-9f51-72a94eccc124" />


---

## 🌓 Dark Mode vs. Light Mode

The dashboard features a sophisticated UI toggle system:
*   **Dark Mode:** Reduces eye strain for long-period monitoring and highlights high-contrast price movements.
*   **Light Mode:** Provides a clean, professional "paper" feel ideal for presentations and reports.

---

## 📐 Data Modeling & DAX

This project utilizes complex DAX logic to ensure price metrics update instantly when switching between assets.

**Implementation Highlights:**
*   **Switching Logic:** `SELECTEDVALUE` used to drive the dynamic header and logo changes based on slicer selection.
*   **Asset Categorization:** Power Query transformations to group disparate financial data into clean Crypto/Stock/ETF buckets.
*   **Navigation:** Bookmark-driven buttons for a seamless "App-like" feel.

---

## 📂 Repository Structure

```text
Market Dashboard/
├── Datasets/                 # Historical price CSVs and API pull records
├── Screenshots/              # UI references (Dark Mode ETH, Light Mode GOOGL, etc.)
├── Market_Analytics.pbix     # Main Power BI Report file
└── README.md                 # Project Documentation
### 2. Stock Market View
Deep-dive into blue-chip equities including **AAPL**, **GOOGL**, **MSFT**, and **AMZN**. Features precise price-tracking and historical trend analysis.

### 3. ETFs Dashboard
Monitor broad market segments and thematic funds such as **SPY**, **QQQ**, and **IWM**. Perfect for analyzing sectoral rotations and macro market health.

---

## 🌓 Dark Mode vs. Light Mode

The dashboard features a sophisticated UI toggle system:
*   **Dark Mode:** Reduces eye strain for long-period monitoring and highlights high-contrast price movements.
*   **Light Mode:** Provides a clean, professional "paper" feel ideal for presentations and reports.

---

## 📐 Data Modeling & DAX

This project utilizes complex DAX logic to ensure price metrics update instantly when switching between assets.

**Implementation Highlights:**
*   **Switching Logic:** `SELECTEDVALUE` used to drive the dynamic header and logo changes based on slicer selection.
*   **Asset Categorization:** Power Query transformations to group disparate financial data into clean Crypto/Stock/ETF buckets.
*   **Navigation:** Bookmark-driven buttons for a seamless "App-like" feel.

---

## 📂 Repository Structure

```text
Market Dashboard/
├── Datasets/                 # Historical price CSVs and API pull records
├── Screenshots/              # UI references (Dark Mode ETH, Light Mode GOOGL, etc.)
├── Market_Analytics.pbix     # Main Power BI Report file
└── README.md                 # Project Documentation
