# Project Link
https://app.powerbi.com/view?r=eyJrIjoiNDZlY2EwNDgtNDJmZS00YWE5LWI0M2MtYzdhZDNhZDRmMTI2IiwidCI6ImE2ZGJkZGRlLTU3OTgtNGViYS1hNWE4LTc4ODA3ZTgyZDllYiJ9&embedImagePlaceholder=true

---


# Olympic Paris 2024 Analytics Dashboard 🏅

An immersive and interactive Power BI dashboard providing a comprehensive analysis of the **Paris 2024 Olympic Games**. This project combines real-time athlete data, historical performance trends, and geographic medal distribution to tell the story of the world's premier sporting event.

---

## 🚀 Key Features

*   **Real-Time Participation Tracking:** Analysis of 11,110+ athletes across 206 participating nations.
*   **Gender Parity Insights:** Visualization of the near-perfect gender balance (5,655 male vs. 5,455 female participants).
*   **Geographic Heatmaps:** Interactive world map showcasing medal density and top-performing regions.
*   **Historical Performance Engine:** A dedicated module to track Olympic progress from 1896 to the present day.
*   **Athlete Demographics:** Breakdown of participants by age categories, gender, and specific sporting disciplines.
*   **Dynamic Navigation:** A custom UI with a sidebar for seamless switching between Home, Overview, Athletes, Country, and Historical views.

---

## 🛠️ Tech Stack

*   **Visualization:** Power BI Desktop
*   **Data Processing:** Power Query (M) for advanced ETL and data transformation
*   **Data Modeling:** Complex Star Schema to link modern results with historical records
*   **Design:** Custom high-fidelity UI/UX with integrated Olympic branding and iconography

---

## 📊 Dashboard Pages

### 1. Home Page
The grand entry point featuring the Paris 2024 branding and a clean navigation menu to access different analytical segments.
<img width="1312" height="735" alt="Screenshot 2026-04-12 215657" src="https://github.com/user-attachments/assets/51f342be-ea3c-4842-a3bf-07f31097bcc0" />



### 2. Tournament Overview
A high-level summary of the games, featuring:
*   **Medal Tally:** Real-time Gold, Silver, and Bronze counts.
*   **Key Highlights:** Text-based summaries of top-performing nations like the USA.
*   **Participation Metrics:** Total nations, teams, and athletes at a glance.
<img width="1306" height="728" alt="Screenshot 2026-04-12 215723" src="https://github.com/user-attachments/assets/920d6ffb-ac96-4a4f-a89a-ff63ce630c2c" />




### 3. Athlete Analytics
A deep dive into the people behind the medals:
*   **Age & Gender:** Bar charts showing the distribution of athletes (e.g., peak participation in the 26-30 age bracket).
*   **Sport Filters:** Sidebar with custom icons to filter data by disciplines like Archery, Gymnastics, and Athletics.
<img width="1307" height="737" alt="Screenshot 2026-04-12 220311" src="https://github.com/user-attachments/assets/1034e148-6f84-4d54-8bff-eccb697e0359" />



### 4. Country Analysis
A geographic-first view allowing users to:
*   Search for specific nations using a custom flag-integrated slicer.
*   View "Key Highlights" and top-performing metrics for selected countries.
<img width="1307" height="734" alt="Screenshot 2026-04-12 220325" src="https://github.com/user-attachments/assets/2796697c-d460-4424-8156-46b91d31c73b" />




### 5. Historical Trends
A comprehensive look back at Olympic history:
*   **Year Slicer:** Select any Olympic year from 1896 to 1928 and beyond.
*   **All-Time Rankings:** Stacked bar charts comparing historical medal counts by superpower nations.
<img width="1308" height="731" alt="Screenshot 2026-04-12 220337" src="https://github.com/user-attachments/assets/00b81eb1-547e-4bf5-9725-ebb727863f4d" />




---

## 📐 Data Modeling & DAX

This project utilizes advanced DAX to calculate participation rates and dynamic medal totals.

**Key Implementation Areas:**
*   **Dynamic Flag Slicers:** Using Image URL data categories to render national flags within filter panes.
*   **Age Binning:** Transforming raw birth dates into meaningful age categories (15-20, 21-25, etc.) for demographic analysis.
*   **Context-Aware KPIs:** Measures that automatically adjust based on selected country or sport.

---

## 📂 Repository Structure

```text
Olympics Dashboard/
├── Datasets/                 # Modern Paris 2024 and Historical Olympic data
├── Screenshots/              # UI references (Overview, Athletes, Country views)
├── Olympics_Dashboard.pbix   # Main Power BI Report file
└── README.md                 # Project Documentation
