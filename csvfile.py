import sys
import pandas as pd
from PyQt5.QtGui import QPainter

from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QVBoxLayout, QFileDialog, QTableWidget, QTableWidgetItem
)

from PyQt5.QtChart import (
    QChart, QChartView, QBarSet,
    QBarSeries, QBarCategoryAxis
)

from PyQt5.QtCore import Qt


class CSVAnalyzer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CSV Data Analyzer (PyQt5 Only)")
        self.setGeometry(200, 200, 900, 600)

        self.load_btn = QPushButton("Load CSV File")
        self.load_btn.clicked.connect(self.load_csv)

        self.chart_btn = QPushButton("Show Mean Chart")
        self.chart_btn.clicked.connect(self.show_chart)
        self.chart_btn.setEnabled(False)

        self.info_label = QLabel("Upload a CSV file to start analysis")
        self.info_label.setWordWrap(True)

        self.table = QTableWidget()
        self.df = None

        layout = QVBoxLayout()
        layout.addWidget(self.load_btn)
        layout.addWidget(self.chart_btn)
        layout.addWidget(self.info_label)
        layout.addWidget(self.table)

        self.setLayout(layout)

    def load_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open CSV File", "", "CSV Files (*.csv)"
        )

        if not file_path:
            return

        self.df = pd.read_csv(file_path)

        rows, cols = self.df.shape
        missing = self.df.isnull().sum().sum()

        numeric_cols = self.df.select_dtypes(include="number").columns.tolist()
        summary = self.df.describe()

        self.info_label.setText(
            f"Rows: {rows} | Columns: {cols} | Missing Values: {missing}\n\n"
            f"Numeric Columns ({len(numeric_cols)}):\n"
            f"{', '.join(numeric_cols) if numeric_cols else 'None'}\n\n"
            f"Summary Statistics:\n{summary.to_string()}"
        )

        self.table.setRowCount(rows)
        self.table.setColumnCount(cols)
        self.table.setHorizontalHeaderLabels(self.df.columns)

        for i in range(rows):
            for j in range(cols):
                self.table.setItem(
                    i, j, QTableWidgetItem(str(self.df.iat[i, j]))
                )

        self.chart_btn.setEnabled(True)

    def show_chart(self):
        numeric_df = self.df.select_dtypes(include="number")

        if numeric_df.empty:
            self.info_label.setText("No numeric columns available for visualization.")
            return

        means = numeric_df.mean()

        bar_set = QBarSet("Mean Values")
        for value in means:
            bar_set.append(value)

        series = QBarSeries()
        series.append(bar_set)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Mean of Numeric Columns")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        axis_x = QBarCategoryAxis()
        axis_x.append(means.index.tolist())
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)


        # chart_view = QChartView(chart)
        # chart_view.setRenderHint(chart_view.renderHints())

        chart_window = QWidget()
        chart_layout = QVBoxLayout()
        chart_layout.addWidget(chart_view)
        chart_window.setLayout(chart_layout)
        chart_window.setWindowTitle("Data Visualization")
        chart_window.resize(600, 400)
        chart_window.show()

        self.chart_window = chart_window  # prevent garbage collection


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CSVAnalyzer()
    window.show()
    sys.exit(app.exec_())
