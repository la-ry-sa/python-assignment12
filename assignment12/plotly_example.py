import plotly.express as px
import plotly.data as pldata
df = pldata.wind(return_type='pandas')

print(df.head)
print(df.tail)

df['strength'] = df['strength'].str.replace('[^0-9.]', '', regex=True).astype(float)

fig = px.scatter(
    df,
    x='strength',
    y='frequency',
    color='direction',
    title='Wind Strength vs Frequency'
)

fig.write_html("wind.html", include_plotlyjs='cdn', full_html=True)