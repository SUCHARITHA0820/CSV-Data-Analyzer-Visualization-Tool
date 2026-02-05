# CSV-Data-Analyzer-Visualization-Tool
Features
CSV File Loading: Easily browse and import local CSV files.

Data Preview: View your dataset in an interactive QTableWidget.

Statistical Summary: Automatically calculates total rows, columns, missing values, and descriptive statistics (mean, std, min, max, etc.).

Mean Data Visualization: Generates a dynamic bar chart representing the mean values of all numeric columns using QtChart.

Responsive Interface: Clean layout with error handling for non-numeric data.

🛠️ Built With
Python 3.x

PyQt5: For the graphical user interface.

Pandas: For high-performance data manipulation and analysis.

QtChart: For rendering high-quality statistical graphs.

📋 Prerequisites
Ensure you have the following Python libraries installed:

Bash
pip install pandas PyQt5 PyQtChart
💻 How to Run
Clone this repository or download the source code.

Navigate to the project directory.

Run the application using:

Bash
python your_filename.py
📖 Usage
Load Data: Click the "Load CSV File" button and select a .csv file from your computer.

Analyze: The application will display a summary of the data (missing values, numeric columns) and populate the table.

Visualize: Click "Show Mean Chart" to open a new window displaying a bar series of the average values for your numeric data.
