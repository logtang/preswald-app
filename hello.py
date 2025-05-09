# Preswald lib. functions
from preswald import connect, get_df, query, table, text, plotly
# Plotly Express
import plotly.express as px
# NumPy, for regression line 
import numpy as np

connect()  # Initialize connection to preswald.toml data sources
df = get_df("Big5_csv")  # Load data

fig = px.scatter(df, x='c', y='n', title='Conscientousness vs Neuroticism', labels={'c': 'Conscientousness', 'n': 'Neuroticism'})

text('# This is Logan\'s first Preswald app!')
text('The "Big 5" personality traits are a set of five different traits that psychologists might use to track a person\'s peronality.')
text('Here. Let\'s observe the relationship between "conscientousness" and "neuroticism". They\'re meant to track people\'s deliberateness and anxiety, respectively. So you\'d think they negatively correlate.')

plotly(fig) 

text('Now a regression line. Maybe that will help in discerning the trend here.')

x = df['c']
y = df['n']
m, b = np.polyfit(x, y, deg=1)
df['regression'] = m * x + b

# Add regression line to scatter plot
reg_line = px.line(df, x='c', y='regression')
fig.add_traces(reg_line.data)

fig.show()

text(f'With a slope coefficient of {m}, it\'s pretty apparent that there\'s a negative correlation.')
text('And that\'s good! It means the two metrics, self reported conscientiousness and self-reported neuroticism are valid measurements. They\'re supposed to be opposites, and they exhibit this negative trend.')

text('And here, the raw data for reference.')
table(df)

