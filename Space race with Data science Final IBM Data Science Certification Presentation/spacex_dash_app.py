# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()
launch_site=spacex_df['Launch Site'].unique()
# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
    dcc.Dropdown(
        id='site-dropdown',
        options=[
            {'label': 'All Sites', 'value': 'All Sites'},
            {'label': launch_site[0], 'value': launch_site[0]},
            {'label': launch_site[1], 'value': launch_site[1]},
            {'label': launch_site[2], 'value': launch_site[2]},
            {'label': launch_site[3], 'value': launch_site[3]}
        ],
        value='All Sites',
        searchable=True
    ),
    html.Div(id='Launch_Site-output-container'),
    
    html.Br(),

    # TASK 2: Add a pie chart to show the total successful launches count for all sites
    html.Div(dcc.Graph(id='success-pie-chart')),

    html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id='payload-slider',min=0,max=10000,step=1000,value=(min_payload,max_payload)),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))

def get_pie_chart(entered_site):
    sf=spacex_df.groupby('Launch Site')['class'].mean().reset_index()
    if entered_site == 'All Sites':
        fig = px.pie(sf, values='class', names='Launch Site', hole=.3,
        title='success rate -pie-chart for all sites')
        return fig
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        # Group by 'class' to get the count of success and failures
        filtered_df = filtered_df.groupby('class').size().reset_index(name='counts')
        # Map the 'class' values to 'Failure' and 'Success'
        filtered_df['class'] = filtered_df['class'].map({0: 'Failure', 1: 'Success'})
        fig = px.pie(
            filtered_df, 
            values='counts', 
            names='class', 
            hole=.3,
            title=f'Success Rate for {entered_site}'
        )
        return fig

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='payload-slider', component_property='value'), Input(component_id='site-dropdown', component_property='value')]
)

def update_scatter_chart(payload_range, entered_site):
    low, high = payload_range
    filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)]
    
    if entered_site == 'All Sites':
        fig = px.scatter(
            filtered_df, 
            x='Payload Mass (kg)', 
            y='class', 
            color='Booster Version', 
            title='Scatter plot between Payload Mass and Success Rate for All Sites'
        )
        return fig
    else:
        filtered_df = filtered_df[filtered_df['Launch Site'] == entered_site]
        fig = px.scatter(
            filtered_df, 
            x='Payload Mass (kg)', 
            y='class', 
            color='Booster Version', 
            title=f'Scatter plot between Payload Mass and Success Rate for {entered_site}'
        )
        return fig

# Run the app
if __name__ == '__main__':
    app.run_server()
