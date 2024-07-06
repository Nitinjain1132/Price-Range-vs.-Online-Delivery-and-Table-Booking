# Price-Range-vs.-Online-Delivery-and-Table-Booking

Restaurant Data Analysis
This project is a Tkinter-based application for analyzing restaurant data from a CSV file. It explores the relationship between the price range of restaurants and the availability of online delivery and table booking services. The results are displayed both in text format and through graphical visualizations using Matplotlib and Seaborn.

Features
Price Range vs. Online Delivery: Analyzes if higher-priced restaurants are more likely to offer online delivery services.
Price Range vs. Table Booking: Analyzes if higher-priced restaurants are more likely to offer table booking services.
Graphical Visualizations: Provides stacked bar charts to visualize the relationship between price range and the availability of online delivery and table booking services.
Prerequisites
Python 3.x
pandas
tkinter
matplotlib
seaborn
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/restaurant-data-analysis.git
Navigate to the project directory:
bash
Copy code
cd restaurant-data-analysis
Install the required libraries:
bash
Copy code
pip install pandas tkinter matplotlib seaborn
Usage
Make sure your dataset CSV file is properly formatted and placed in the correct directory. Update the file path in the script if necessary.
Run the script:
bash
Copy code
python main.py
Code Overview
Data Loading
The dataset is loaded using pandas.read_csv and processed to analyze the relationship between the price range of restaurants and the availability of online delivery and table booking services.

Tkinter Interface
A Tkinter window is created to display the results. The interface includes buttons to open separate windows for each type of analysis.

Matplotlib and Seaborn Visualizations
Two stacked bar charts are generated using Matplotlib and Seaborn:

One for the relationship between price range and online delivery.
Another for the relationship between price range and table booking.
Dataset
Ensure that your dataset CSV file contains at least the following columns:

Price range: The price range category of the restaurant.
Has Online delivery: Whether the restaurant offers online delivery (Yes/No).
Has Table booking: Whether the restaurant offers table booking (Yes/No).
Example Dataset
Here's a snippet of what your dataset might look like:

csv
Copy code
Price range,Has Online delivery,Has Table booking
3,Yes,Yes
2,No,No
...
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Special thanks to the open-source community for providing the necessary libraries and tools.
Feel free to customize this README file according to your specific needs and additional details about your project.

