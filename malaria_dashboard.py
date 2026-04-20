import pandas as pd
import plotly.express as px

# ============================================
# DATA
# ============================================
province_data = pd.DataFrame({
    "Province": ["Eastern", "Southern", "Western", "Northern", "Kigali City"],
    "Cases": [285000, 198000, 89000, 32000, 19000],
    "Percentage": [49.2, 34.2, 15.4, 5.5, 3.3]
})

timeline = pd.DataFrame({
    "Year": [2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030],
    "Cases": [5900000,4200000,3100000,1800000,900000,700000,623000,450000,300000,180000,80000,25000,5000,0]
})

economic_data = pd.DataFrame({
    "Category": ["Healthcare Treatment", "Lost Productivity", "Prevention Programs", "School Absences"],
    "Cost_Billion_RWF": [18.5, 42.0, 15.6, 8.5]
})

# ============================================
# CHARTS
# ============================================
fig1 = px.bar(province_data, x="Province", y="Cases",
              title="Malaria Cases by Province",
              text="Cases")

fig2 = px.line(timeline, x="Year", y="Cases",
               title="Malaria Trend to 2030", markers=True)

fig3 = px.bar(economic_data, x="Category", y="Cost_Billion_RWF",
              title="Economic Burden")

chart1 = fig1.to_html(full_html=False, include_plotlyjs='cdn')
chart2 = fig2.to_html(full_html=False, include_plotlyjs=False)
chart3 = fig3.to_html(full_html=False, include_plotlyjs=False)

# ============================================
# CALCULATIONS
# ============================================
peak = 5900000
current = 623000
reduction = ((peak - current) / peak) * 100

# ============================================
# FULL HTML
# ============================================
html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Rwanda Malaria Dashboard</title>

<style>
body {{
    font-family: 'Segoe UI', Arial;
    background: linear-gradient(135deg, #f5f7fa, #e8edf2);
    padding: 20px;
}}

.kpi-card {{
    background: white;
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    margin: 10px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}}

.section-title {{
    font-size: 22px;
    margin-top: 40px;
    border-left: 5px solid #1f77b4;
    padding-left: 10px;
}}
</style>
</head>

<body>

<h1 style="text-align:center;">🦟 Rwanda Malaria Dashboard</h1>

<div class="section-title">📊 KPIs</div>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:20px;">
    <div class="kpi-card"><h2>285,000</h2>Eastern Province</div>
    <div class="kpi-card"><h2>88%</h2>Reduction</div>
    <div class="kpi-card"><h2>RWF 84.6B</h2>Economic Loss</div>
    <div class="kpi-card"><h2>2030</h2>Target</div>
</div>

<div class="section-title">📍 Province Burden</div>
{chart1}

<div class="section-title">📉 Trend</div>
{chart2}

<div style="margin:20px;padding:15px;background:#e8f4f8;border-radius:10px;">
<strong>Reduction Achieved:</strong> {reduction:.0f}%
</div>

<div class="section-title">💰 Economic Impact</div>
{chart3}

<div style="position:fixed;bottom:20px;right:20px;">
<button onclick="startScroll()" style="padding:10px 20px;">▶ Start</button>
<button onclick="stopScroll()" style="padding:10px 20px;">⏹ Stop</button>
</div>

<script>
var scrollInterval;

function startScroll() {{
    scrollInterval = setInterval(function() {{
        window.scrollBy(0, 30);
    }}, 50);
}}

function stopScroll() {{
    clearInterval(scrollInterval);
}}
</script>

</body>
</html>
"""

# ============================================
# SAVE FILE
# ============================================
with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(html)

print("dashboard.html created successfully!")