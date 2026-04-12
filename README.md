# Power BI Analytics Portfolio

Welcome to my Power BI projects repository! These projects serves as a comprehensive portfolio of end-to-end data analytics solutions. Each project showcased here highlights the complete data lifecycle—from **Data Extraction** (API/Web Scraping) and **Data Modeling** (Medallion Architecture) to **Advanced DAX Calculations** and **Interactive Visualizations**.

## 🚀 Projects Overview

### 💰 1. Personal Finance Dashboard
A comprehensive tool for tracking financial health, analyzing spending patterns, and monitoring savings goals.
* **Key Features:** Monthly expense tracking, savings rate analysis, and income vs. expenditure trends.
* **Technical Highlight:** Implemented dynamic "Line Selection" measures and Month-over-Month (MoM) growth calculations using advanced DAX.
<img width="1275" height="718" alt="Screenshot 2026-04-07 113205" src="https://github.com/user-attachments/assets/62fbc6df-b16c-4825-b7d4-26618470e772" />

### 🎥 2. YouTube Creator Dashboard
An automated dashboard for content creators to analyze channel performance.
* **Data Source:** Custom **M-Code** integration with the **YouTube Data API v3**.
* **Insights:** Real-time tracking of Video Views, Likes, Comment counts, and engagement metrics across multiple channel IDs.
<img width="1420" height="785" alt="image" src="https://github.com/user-attachments/assets/bd09a249-5f4d-4ac2-ac79-d415a143988d" />

### 🎵 3. Spotify Top 50 Chart Analysis
Visualizing global music trends based on Spotify's top-charting tracks.
* **Insights:** Artist popularity, song duration distribution, and explicit content analysis.
* **Visuals:** Integrated album art via image URLs and peak position tracking over time.
<img width="1380" height="774" alt="spotify2" src="https://github.com/user-attachments/assets/e121459c-7917-4f44-a146-24ab5eeb642b" />

### 📦 4. Supply Chain Analytics
A business-intelligence approach to logistics and inventory management.
* **Focus:** Tracking order fulfillment, shipping lead times, and inventory turnover.
* **Data Modeling:** Implementation of a Star Schema to optimize report performance and cross-filtering.
<img width="1423" height="800" alt="Screenshot 2026-04-03 170331" src="https://github.com/user-attachments/assets/cbc73354-d884-4cc0-8e89-aacf5fedcfc8" />

### 🏎️ 5. Honda Sales/Service Dashboard
A domain-specific dashboard focused on automotive dealership performance.
* **Focus:** Sales volume trends, regional performance, and service efficiency metrics.
<img width="1423" height="800" alt="Screenshot 2026-03-20 212845" src="https://github.com/user-attachments/assets/e10612bb-7fc4-4115-a7e0-ac1abc8fafdd" />

### 🏅 6. Olympics Historical Analysis
A deep dive into the history of the Olympic Games.
* **Insights:** Medal tallies by country, athlete demographics, and historical trends across different host cities.
<img width="1306" height="727" alt="image" src="https://github.com/user-attachments/assets/81994fca-7c06-4bf1-9a2c-13320237906a" />

---

## 🛠️ Technical Skillset

### Data Engineering & Modeling
* **Medallion Architecture:** Organizing data into Bronze (Raw), Silver (Cleaned), and Gold (Business Ready) layers.
* **Power Query (M-Code):** Expertise in connecting to REST APIs (YouTube API), web scraping, and complex data transformations.
* **Data Modeling:** Proficiency in designing **Star Schemas**, handling granularity mismatches, and managing relationships between disparate data sources.

### DAX & Analytics
* **Advanced DAX:** Time Intelligence (YTD, MoM, YoY), `CALCULATE` logic, `SWITCH` for dynamic visual selections, and `REMOVEFILTERS` for custom granularity handling.
* **Performance Optimization:** Efficient measure writing to ensure fast report rendering in the Power BI Service.

### Data Visualization
* **UI/UX Design:** Creating clean, intuitive layouts with custom navigation buttons, bookmarks, and slicers.
* **Custom Tooltips:** Enhancing user experience with report-page tooltips and conditional formatting.

---

## 📂 Repository Structure

```text
├── Finance Dashboard        # Finance .pbix and data files
├── Honda                    # Automotive sales analysis
├── Olympics Dashboard       # Historical sports data viz
├── Spotify Dashboard        # Music trend analytics
├── Supply Chain Dashboard   # Logistics & Operations
├── Youtube Creator Dashboard # API-integrated channel tracking
└── README.md
