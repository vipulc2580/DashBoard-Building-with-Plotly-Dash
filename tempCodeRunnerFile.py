# print('I will learning plotly dash today excited to learn it')
import dash
import dash_bootstrap_components as dbc
from dash import dcc,Input,Output,html
import plotly.express as px
import pandas as pd
import numpy as np

#loading data
def load_data():
    df=pd.read_csv(r'G:\Python\geekssforgeeksPython\JupyterProjects\Dash_Plotly_Application\assets\healthcare.csv')
    df['Billing Amount']=pd.to_numeric(df['Billing Amount'],errors='coerce')
    df['Date Of Admission']=pd.to_datetime(df['Date of Admission'])
    df['YearMonth']=df['Date Of Admission'].dt.to_period('M')
    return df


df=load_data()
total_records=len(df)
average_billing=round(df['Billing Amount'].mean(),2)


#Creating an webapp
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        #Title of The WebPage
           dbc.Row(
            [
                dbc.Col(
                    html.H1('HealthCare Dashboard'),
                    width=15,
                    className='text-center my-5'
                )
            ]
        ),
        #KPI Total Patient Records, Average billing Amount
            dbc.Row(
            [
                dbc.Col(
                    html.Div(f"Total Patient Records: {total_records}"),
                    className="text-center my-3 top-text",
                    width=5
                ),
                dbc.Col(
                    html.Div(f"Average Billing Amount: ${average_billing}"),
                    className="text-center my-3 top-text",
                    width=5
                )
            ],
            className='mb-5'
        ),
        #Patient Demographics and Medical Condition
            dbc.Row(
            [
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody(
                            [
                                html.H4('Patient Demographics',className='card-title'),
                                dcc.Dropdown(
                                    id='gender-filter',
                                    options=[
                                        {'label':gender,'value':gender} for gender in df['Gender'].unique()
                                    ],
                                    value=None,
                                    placeholder='Select a Gender'
                                ),
                                dcc.Graph(id='age-distribution')
                            ]
                        )]
                    )
                ],width=6),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody(
                            [
                                html.H4('Medical Condition Distribution',className='card-title'),
                                dcc.Graph(id='condition-distribution')
                            ]
                        )]
                    )
                ],width=6)
            ]
        ),
        #Isurance Provider Comparsion
            dbc.Row([
            dbc.Col([
                dbc.Card([
                        dbc.CardBody(
                            [
                                html.H4('Isurance Provider Comparsion',className='card-title'),
                                dcc.Graph(id='insurance-comparsion')
                            ]
                        )]
                    )
                ],width=12)
            ]),
            #Billing Distribution
            dbc.Row([
                dbc.Col([
                    dbc.CardBody(
                        [
                            html.H4('Billing Amount Distribution',className='card-title'),
                            dcc.Slider(
                                id="billing-slider",
                                min=df['Billing Amount'].min(),
                                max=df['Billing Amount'].max(),
                                value=df['Billing Amount'].median(),
                                marks={
                                    int(value):f"${int(value)}"
                                    for value in df['Billing Amount'].quantile([0,0.25,0.5,0.75,1]).values
                                },
                                step=100
                            ),
                            dcc.Graph(id="billing-distribution")
                        ]
                    )
                ],width=12)
            ]),
            #Trends in Admission
            dbc.Row([
                dbc.Col([
                    dbc.CardBody(
                        [
                            html.H4('Trends in Admission',className='card-title'),
                            dcc.RadioItems(
                                id="chart-type",
                                options=[
                                    {'label':'Line Chart','value':'line'},
                                    {'label':'Bar Chart','value':'bar'},
                                ],
                                value='line',
                                inline=True,
                                className='mb-4'
                            ),
                            dcc.Dropdown(
                                id="condition-filter",
                                 options=[
                                        {'label':condition,'value':condition} for condition in df['Medical Condition'].unique()
                                    ],
                                    value=None,
                                    placeholder='Select a Medical Condition'
                                ),
                            dcc.Graph(
                                id='admission-trends'
                            )
                        ]
                    )
                ],width=12)
            ])
    ],
    fluid=True  # Ensures responsive layout
)


#callbacks
@app.callback(
    Output('age-distribution','figure'),
    Input('gender-filter','value'))
def update_Patient_Distribution_Plot(selected_gender):
    colorseq=['#4A90E2',"#D81B60"]
    if selected_gender:
        if(selected_gender=='Male'):
            colorseq=colorseq[0:1]
        else:
            colorseq=colorseq[-1:]
        filtered_df=df[df['Gender']==selected_gender]
    else:
        filtered_df=df
    print(len(filtered_df))
    if filtered_df.empty:
        return {}
    fig=px.histogram(filtered_df,
                     x='Age',
                     nbins=10,
                     color="Gender",
                     title='Age Distribution by Gender',
                     color_discrete_sequence=colorseq
                     )
    return fig

#Medical Condition Distribution
@app.callback(
    Output('condition-distribution','figure'),
    Input('gender-filter','value')
)
def update_Medical_Condtion_Gender_Plot(seleted_gender):
    if seleted_gender:
        filtered_df=df[df['Gender']==seleted_gender]
    else:
        filtered_df=df
    fig=px.pie(filtered_df,
               names='Medical Condition',
               title='Medical Condition Distribution by Gender'
               )
    return fig

#Isurance Provider Grouping Based On Gender
@app.callback(
    Output('insurance-comparsion','figure'),
    Input('gender-filter','value')
)
def update_Isurance_provider(selected_gender):
    filtered_data = df[df['Gender'] == selected_gender] if selected_gender else df
    fig = px.bar(
    filtered_data,
    x='Insurance Provider',
    y='Billing Amount',
    color='Medical Condition',
    barmode='group',
    title='Insurance Provider Price Comparison',
    color_discrete_sequence=px.colors.qualitative.Plotly  # Vibrant color palette
    )

    # Update layout for better visuals
    fig.update_layout(
    plot_bgcolor='white',  # White background
    paper_bgcolor='white',  # White chart area
    font=dict(
        family="Arial",
        size=14,
        color="black"
    ),
    title=dict(
        font=dict(size=20, color="black"),
        x=0.5,  # Center-align title
    ),
    xaxis=dict(
        gridcolor='lightgray',  # Light gridlines
        tickangle=0,  # Keep x-axis labels horizontal
        title=dict(font=dict(size=16, color="black")),
    ),
    yaxis=dict(
        gridcolor='lightgray',
        title=dict(font=dict(size=16, color="black")),
    ),
    legend=dict(
        title=dict(font=dict(size=14)),
        font=dict(size=12),
    )
    )

    # Display the updated figure
    return fig


#Billing Distribution Based On Gender
@app.callback(
    Output('billing-distribution','figure'),
    [
        Input('gender-filter','value'),
        Input('billing-slider','value')
    ]
)
def update_billing_distribution_based_Range(selected_gender,amount):
    filtered_data=(df[df['Gender']==selected_gender] if selected_gender!=None else df)
    filtered_data=filtered_data[filtered_data['Billing Amount']<=amount]
    fig=px.histogram(filtered_data,
                     x='Billing Amount',
                     nbins=10,
                     title='Billing Amount Distribution')
    return fig


#Trends in Admission
@app.callback(
    Output('admission-trends','figure'),
    [
        Input('gender-filter','value'),
        Input('chart-type','value'),
        Input('condition-filter','value')
    ]
)
def update_admission_trend_Plot(selected_gender,chart_type,condition):
    filtered_df=(df[df['Gender']==selected_gender] if selected_gender!=None else df)
    filtered_df=(filtered_df[filtered_df['Medical Condition']==condition] if condition!=None else filtered_df)
    trend_df=filtered_df.groupby('YearMonth').size().reset_index(name='Count')
    trend_df['YearMonth']=trend_df['YearMonth'].astype(str)

    if(chart_type=='line'):
        fig=px.line(trend_df,x='YearMonth',y='Count',title='Admission Trend Over Time')
        return fig
    else:
        fig=px.bar(trend_df,x='YearMonth',y='Count',title='Admission Trend Over Time')
        return fig

if __name__ == "__main__":
    app.run_server(debug=True)
