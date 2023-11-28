# Interactive Bar Graph with Plotly

This Python script demonstrates how to create an interactive bar graph using the Plotly library. The script allows users to visualize data in a dynamic and interactive way.

## Requirements

- Python 3.x
- Plotly library (`pip install plotly`)

## Usage

1. Install the necessary Python packages:

   ```bash
   pip install plotly
   ```

2. Modify the script by updating the `categories` and `values` lists with your own data:

    ```python
    categories = ['Category A', 'Category B', 'Category C', 'Category D']
    values = [23, 45, 56, 78]
    ```

3. Run the Python script:

    ```bash
    python interactive_bar_graph.py
    ```

4. The script will generate an interactive bar graph using Plotly. The graph will be displayed in your default web browser.

## Customization

- Modify the `categories` and `values` lists to represent your own dataset.
- Adjust colors, titles, axes labels, and other graph properties by modifying the parameters in the script's `update_layout` and `go.Figure` sections.

## Example

Here's a snippet of how to create the bar graph:

```python
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
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details 
