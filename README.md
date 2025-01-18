# Dashboard Building with Plotly Dash

![Dashboard Preview](https://github.com/vipulc2580/DashBoard-Building-with-Plotly-Dash/blob/main/healthcare%20Dashboard.png)

## Agenda

This project demonstrates how to build interactive and visually appealing dashboards using Plotly Dash. The main focus areas include:

- Creating dynamic visualizations for data analysis.
- Building an intuitive and responsive user interface.
- Integrating multiple plots and charts into a cohesive dashboard.

---

## Describing the Data

The dataset used in this project includes:

- **Columns**:
  - `Date`: Timestamp of the data entry.
  - `Category`: Classification of data points into different groups.
  - `Values`: Numerical data representing metrics for analysis.
  - Additional columns that provide context and support for visualizations.

The data is preprocessed to handle missing values, normalize formats, and ensure compatibility with Plotly Dash components. Derived features such as moving averages and percentage changes are included to enhance the insights provided by the dashboard.

---

## Charts and Filters

The dashboard includes the following charts:

- **Line Chart**:
  - **Purpose**: Visualizes trends over time.
  - **Filters**: Date range, category.

- **Bar Chart**:
  - **Purpose**: Compares values across categories.
  - **Filters**: Category, aggregation type (sum, average).

- **Pie Chart**:
  - **Purpose**: Displays the proportion of categories within the dataset.
  - **Filters**: Category.

- **Histogram Distribution*:
  - **Purpose**: Shows Billing Amount over various range bins
  - **Filters**:Filtered by Gender and we can customize the bill amount to get granularity of distribution over fixed bin size.

- **Histogram Distribution**:
  - **Purpose**: Visualizing the proportion of count over various bin size for specific gender.
  - **Filters**: Filter by Gender.

Each chart is interactive and responds to user inputs from the filters, allowing for tailored insights based on selected criteria.

---

## How to Use It

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/vipulc2580/DashBoard-Building-with-Plotly-Dash.git
   cd DashBoard-Building-with-Plotly-Dash
   ```

2. **Install Dependencies**:
   Ensure you have Python installed, then install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   Start the Dash app by running the following command:
   ```bash
   python app.py
   ```

4. **Access the Dashboard**:
   Open your web browser and navigate to:
   ```
   http://127.0.0.1:8050/
   ```

5. **Interact with the Dashboard**:
   Explore the various features and visualizations.

---

## Libraries Used

The project leverages the following libraries:

- **Plotly Dash**: For building the interactive dashboard.
- **Pandas**: For data manipulation and preprocessing.
- **NumPy**: For numerical computations.
- **Flask**: For serving the web application.
- **Plotly Express**: For creating easy and quick visualizations.

---

Feel free to explore the repository and customize the dashboards to suit your specific data analysis needs!
