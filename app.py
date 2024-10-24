import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = r'C:\Users\HP\Desktop\KALA\Hotel.csv.csv'
df = pd.read_csv(file_path)

# Preprocess the columns if necessary (e.g., filling NaNs, converting data types)
df['lead_time'] = pd.to_numeric(df['lead_time'], errors='coerce')
df['avg_room_price'] = pd.to_numeric(df['avg_room_price'], errors='coerce')
df['week_nights'] = pd.to_numeric(df['week_nights'], errors='coerce')
df['weekend_nights'] = pd.to_numeric(df['weekend_nights'], errors='coerce')
df['year'] = pd.to_numeric(df['year'], errors='coerce')

# Operation 1: Total number of bookings per year
total_bookings_per_year = df.groupby('year').size()

# Operation 2: Average lead time for each room type
avg_lead_time_per_room_type = df.groupby('room_type')['lead_time'].mean()

# Operation 3: Total bookings by market segment
total_bookings_by_market_segment = df.groupby('market_segment').size()

# Operation 4: Revenue generated per month
df['total_revenue'] = (df['avg_room_price'] * (df['week_nights'] + df['weekend_nights'])).fillna(0)
revenue_per_month = df.groupby(['year', 'month'])['total_revenue'].sum()

# Operation 5: Average stay duration by market segment
df['stay_duration'] = df['week_nights'] + df['weekend_nights']
avg_stay_duration_by_market_segment = df.groupby('market_segment')['stay_duration'].mean()

# Creating dataframes for each operation result for output tables
total_bookings_per_year_df = pd.DataFrame(total_bookings_per_year, columns=['Total Bookings']).reset_index()
avg_lead_time_per_room_type_df = pd.DataFrame(avg_lead_time_per_room_type, columns=['Average Lead Time']).reset_index()
total_bookings_by_market_segment_df = pd.DataFrame(total_bookings_by_market_segment, columns=['Total Bookings']).reset_index()
revenue_per_month_df = pd.DataFrame(revenue_per_month, columns=['Total Revenue']).reset_index()
avg_stay_duration_by_market_segment_df = pd.DataFrame(avg_stay_duration_by_market_segment, columns=['Average Stay Duration']).reset_index()

# Plotting the results
fig, axs = plt.subplots(3, 2, figsize=(14, 10))
fig.tight_layout(pad=5.0)

# Plot 1: Total bookings per year
axs[0, 0].bar(total_bookings_per_year.index, total_bookings_per_year.values, color='skyblue')
axs[0, 0].set_title('Total Bookings Per Year')
axs[0, 0].set_xlabel('Year')
axs[0, 0].set_ylabel('Number of Bookings')

# Plot 2: Average lead time per room type
axs[0, 1].bar(avg_lead_time_per_room_type.index, avg_lead_time_per_room_type.values, color='lightgreen')
axs[0, 1].set_title('Average Lead Time Per Room Type')
axs[0, 1].set_xlabel('Room Type')
axs[0, 1].set_ylabel('Average Lead Time (days)')

# Plot 3: Total bookings by market segment
axs[1, 0].bar(total_bookings_by_market_segment.index, total_bookings_by_market_segment.values, color='salmon')
axs[1, 0].set_title('Total Bookings By Market Segment')
axs[1, 0].set_xlabel('Market Segment')
axs[1, 0].set_ylabel('Number of Bookings')

# Plot 4: Revenue generated per month
revenue_per_month_unstacked = revenue_per_month.unstack(level=0)  # Unstack to separate years in bars
revenue_per_month_unstacked.plot(kind='bar', ax=axs[1, 1], colormap='coolwarm', stacked=True)
axs[1, 1].set_title('Revenue Generated Per Month')
axs[1, 1].set_xlabel('Month')
axs[1, 1].set_ylabel('Total Revenue (€)')

# Plot 5: Average stay duration by market segment
axs[2, 0].bar(avg_stay_duration_by_market_segment.index, avg_stay_duration_by_market_segment.values, color='orange')
axs[2, 0].set_title('Average Stay Duration By Market Segment')
axs[2, 0].set_xlabel('Market Segment')
axs[2, 0].set_ylabel('Average Stay Duration (nights)')

# Remove unused subplot
fig.delaxes(axs[2, 1])

# Show the plots
plt.show()

# Displaying the output tables
{
    "Total Bookings Per Year": total_bookings_per_year_df.head(),
    "Total Bookings By Market Segment": total_bookings_by_market_segment_df.head(),
}
# Display the output tables directly to make sure they print correctly

print("Total Bookings Per Year:")
print(total_bookings_per_year_df)

print("\nTotal Bookings By Market Segment:")
print(total_bookings_by_market_segment_df)
