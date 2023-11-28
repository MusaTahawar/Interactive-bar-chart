import plotly.graph_objects as go

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [23, 45, 56, 78]

# Create a bar graph
fig = go.Figure(data=[go.Bar(
    x=categories,
    y=values,
    marker_color='skyblue'  # Change color as needed
)])

# Update graph layout for better visualization
fig.update_layout(
    title='Interactive Bar Graph',
    xaxis=dict(title='Categories'),
    yaxis=dict(title='Values'),
    hovermode='closest'
)

# Show the interactive graph
fig.show()
