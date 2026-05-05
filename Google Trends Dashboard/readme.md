# Google Trends Dashboard 📈

A comprehensive Power BI solution designed to track, visualize, and analyze keyword performance and search interest globally. This dashboard provides actionable insights into rising and top-performing keywords across various industries, specifically focusing on roles like Data Analyst, Software Developer, AI Engineer, and more.

<img width="1394" height="776" alt="Screenshot 2026-04-20 082938" src="https://github.com/user-attachments/assets/175c42ff-f60d-4a4e-a350-eae064c434ba" />


## 🚀 Key Features

1. **Global Search Map:** Interactive world map visualization showcasing regional interest and keyword density.

2. **Time-Series Analysis:** Historical tracking of keyword performance from 2004 to 2026, enabling long-term trend discovery.

<img width="1387" height="781" alt="Screenshot 2026-04-20 083036" src="https://github.com/user-attachments/assets/8fcab632-5936-4024-b560-4127e7304ff6" />


3. **Rising vs. Top Keywords:** Distinct modules to identify "breakout" search terms (Rising) versus established high-volume terms (Top).

<img width="1388" height="797" alt="Screenshot 2026-04-20 083049" src="https://github.com/user-attachments/assets/fce93d8a-4da2-434b-9dd3-c0aeaa644196" />


4. **Industry Deep Dives:** Dedicated analysis for technical roles including Data Engineering, AI, and Business Consultancy.

<img width="1385" height="782" alt="Screenshot 2026-04-20 083103" src="https://github.com/user-attachments/assets/c12ba076-94fe-4516-910e-5baf1f9343b0" />


5. **7-Day Performance Tracking:** Waterfall charts and metrics focusing on short-term keyword volatility and growth.

6. **Dynamic Navigation:** Seamless page transitions for an intuitive user experience across overview and detail pages.


## 🛠️ Tech Stack

1. Visualization: Power BI Desktop.

2. Data Processing: Power Query (M) for robust data cleaning and transformation.

3. Data Modeling: Optimized Star Schema to handle multi-year time-series data.

4. Design: Custom UI/UX layout with a clean, modern aesthetic for readability.


## 📊 Dashboard Pages
1. Global Overview
The central hub featuring a world map, top rising keywords (e.g., Nvidia), and a distribution breakdown of keyword categories.

Focus: High-level search intensity and geographic interest.

2. Historical Performance
A detailed timeline view using area charts to track keyword searches by Year, Quarter, and Month.

Focus: Identifying seasonal patterns and long-term growth (2004–2026).

3. Keyword Insights
A deep dive into specific search terms with detailed tables providing types, categories, search values, and direct links to Google Trends.

Focus: Granular metrics and classification of search topics.

4. Performance Tracking
Utilizes waterfall charts to display keyword search increases and decreases over the past 7 days.

Focus: Short-term search volatility and total search accumulation.

## 📐 Data Modeling & Methodology
The project implements advanced data modeling techniques to ensure report performance and accuracy:

Medallion Architecture: Data is processed through layers of cleaning in Power Query before being loaded into the model.

Time Intelligence: DAX measures implemented to calculate YoY growth and quarterly shifts.

Keyword Categorization: Automatic grouping of searches into topics like Career, Topic, Field of Study, and Organization Type.

## 📂 Repository Structure

```text
Google Trends Dashboard/
├── Datasets/                 # Source data files and historical trends
├── Screenshots/              # UI/UX visual references
├── Google_Trends_Report.pbix # Main Power BI Report file
└── README.md                 # Project Documentation
```
## 🛡️ License
This project is licensed under the MIT License.

## ☕ Support & Attribution
Developed with a focus on delivering real-time market intelligence using modern BI techniques.
Data Source: Google Trends (Historical and Real-time data).
