Hotel Booking Analysis

This project performs data analysis on hotel booking data using Python. It includes operations such as calculating the total number of bookings per year, average lead time for each room type, and more. Visualizations are generated using Matplotlib to help interpret the data.

Table of Contents :

Installation

Usage

Operations Performed

Visualization

Output Tables

Installation

To run this project, ensure you have Python 3 and the following libraries installed :

pandas

matplotlib

Install the dependencies using pip:

pip install pandas matplotlib

Usage

cd hotel-booking-analysis

Place your Dataset : Place your CSV file (e.g., Hotel.csv) in the root directory or specify the path to your data file in the script.

Run the Script : You can run the Python script with the following command :

python hotel_analysis.py

Operations Performed

This project includes the following operations:

Total Bookings Per Year: The total number of bookings for each year.

Average Lead Time for Each Room Type: The average number of days between booking and arrival for each room type.

Total Bookings by Market Segment: The total number of bookings for each market segment (e.g., Online, Offline, Corporate).

Revenue Generated per Month: The total revenue generated per month, calculated from the room prices and stay duration.

Average Stay Duration by Market Segment: The average number of nights booked by customers in each market segment.

Visualization :

The script generates the following visualizations:

Bar graph of Total Bookings Per Year

Bar graph of Average Lead Time by Room Type

Bar graph of Total Bookings by Market Segment

Stacked Bar graph of Revenue Generated Per Month

Bar graph of Average Stay Duration by Market Segment

These visualizations are saved as .png files or displayed using Matplotlib.

Output Tables

The script also outputs tables summarizing each operation:

Total bookings per year

Total bookings by market segment
