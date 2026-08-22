import pandas as pd
import altair as alt

data = pd.DataFrame({
    "Product": ["Fan", "AC", "TV", "Cooler"],
    "Sales": [50, 80, 40, 65]
})

chart = alt.Chart(data).mark_bar().encode(
    x="Product",
    y="Sales"
)

chart.save('my_chart.png')