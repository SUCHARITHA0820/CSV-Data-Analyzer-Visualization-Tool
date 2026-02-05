# CSV-Data-Analyzer-Visualization-Tool
🚀 Key Features
📂 Instant CSV Loading: High-speed parsing of local datasets using a native file explorer.

🧩 Interactive Data Preview: Real-time rendering of datasets in a structured QTableWidget.

📈 Automated Statistical Summary: Instant calculation of row/column counts, null value detection, and descriptive statistics (Mean, SD, Min, Max).

📊 Dynamic Visualization: A dedicated visualization engine that generates QtChart bar graphs for numeric column means.

🛡️ Robust Error Handling: Built-in validation to handle non-numeric data and empty files without crashing.

🛠️ Technical Stack
This project is built using a modern Python-centric architecture:

Language: Python 3.x

GUI Framework: PyQt5 (Professional-grade desktop components)

Data Engine: Pandas (Industry-standard data manipulation)

Charting: QtChart (Hardware-accelerated graphics)

📋 Prerequisites
Before running the tool, ensure your environment has the following Core Dependencies:

Bash
# Install the required framework and libraries
pip install pandas PyQt5 PyQtChart
💻 Installation & Execution
Clone the repository to your local machine.

Navigate into the project folder.

Launch the application using the command below:

Bash
python your_filename.py
📖 How It Works
Step 1: Data Ingestion
Click Load CSV File. The application uses Pandas to read the file and automatically detects data types.

Step 2: Analysis
The interface updates to show a comprehensive summary of your data quality (missing values) and a statistical breakdown of your numeric variables.

Step 3: Visualization
Click Show Mean Chart. A new window appears with a high-definition bar chart, providing an immediate visual comparison of your data's averages.

