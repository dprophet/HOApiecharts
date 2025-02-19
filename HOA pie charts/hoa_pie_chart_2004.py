import pyecharts.options as opts
from pyecharts.charts import Pie
import webbrowser
import os
from pyecharts.commons.utils import JsCode

# Prepare data for the pie chart
expenses_2004 = {
    "Administrative Expense": 8898,
    "Professional Fees": 5209,
    "Insurance": 59614,
    "Management": 31642,
    "Landscaping, Grounds, and Drainage": 148355,
    "Supplies": 263,
    "Water": 2259,
    "Interest Expense": 11186,
    "Payroll and Related Expenses": 7549,
    "Electrical Repairs": 1100,
    "Plumbing": 489,
    "Exterminator": 2592,
    "Speed Bumps": 3819,
    "Cleaning": 6114,
    "Building Repairs": 2848,
    "Pool Expenses": 7793,
    "Alarm Monitoring": 1399,
    "Utilities": 8133,
    "Telephone": 1398,
    "Licenses": 250,
    "Provision for State Income Taxes": 89
}

# Income and Net Profit (Loss) data
income_data = {
    "Interest Income": 55,
    "Other Income": 300,
    "Common Charges (Note 1)": 331735,
    "Total Revenues": 332090,
    "Total Expenses": 310999,
    "Net Profit (Loss)": 21091
}

# Create a list of tuples for the data
data = list(expenses_2004.items())

# Create a Pie chart with pyecharts
pie_chart = (
    Pie()
    .add(
        "",
        data,
        radius=["40%", "70%"],
        center=["60%", "60%"],  # Move the pie chart down
        label_opts=opts.LabelOpts(
            formatter=JsCode("function(params){return params.name + ': $' + params.value.toLocaleString();}"),
            position="outside"
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Expenses Distribution for 2004",
            subtitle=(
                f"Income:\n"
                f"  Interest Income: ${income_data['Interest Income']:,}\n"
                f"  Other Income: ${income_data['Other Income']:,}\n"
                f"  Common Charges (Note 1): ${income_data['Common Charges (Note 1)']:,}\n"
                f"  Total Revenues: ${income_data['Total Revenues']:,}\n\n"
                f"Total Expenses: ${income_data['Total Expenses']:,}\n"
                f"Net Profit (Loss): ${income_data['Net Profit (Loss)']:,}"
            ),
            title_textstyle_opts=opts.TextStyleOpts(font_size=20, font_weight='bold'),
            subtitle_textstyle_opts=opts.TextStyleOpts(font_size=17, font_weight='bold')  # Increase subtitle size
        ),
        legend_opts=opts.LegendOpts(is_show=False)
    )
)

# Render the chart to a file
file_path = 'expenses_pie_chart_2004.html'
pie_chart.render(file_path)

# Get the absolute file path
absolute_file_path = os.path.abspath(file_path)

# Open the HTML file in the default web browser
webbrowser.open('file://' + absolute_file_path)