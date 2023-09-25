import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV data
data = pd.read_csv("C:/Users/User/Desktop/AUB Masters/MSBA 325/world-data-2023.csv")

# Streamlit app title
st.title("Data Analysis Dashboard")

# User selects the visualization type
selected_viz = st.selectbox("Select Visualization", ["Total CO2 Emissions by Continent", "Life Expectancy by Continent"])

# Only show "Show Filter Options" checkbox when "Life Expectancy by Continent" is selected
if selected_viz == "Life Expectancy by Continent":
    # Use a checkbox to toggle visibility of filter options
    show_filter_options = st.checkbox("Show Filter Options")

    if show_filter_options:
        # Example of a slider for filtering data
        selected_min_life_expectancy = st.slider("Select Minimum Life Expectancy", min_value=0, max_value=100, value=0)

        # Filter data based on the selected minimum life expectancy
        filtered_data = data[data['Life expectancy'] >= selected_min_life_expectancy]

        # Display a data table with filtered results
        st.subheader("Filtered Data")
        st.write(filtered_data)

if selected_viz == "Total CO2 Emissions by Continent":
    # Clean and convert the "CO2-Emissions" column to numeric (remove commas)
    data["Co2-Emissions"] = data["Co2-Emissions"].str.replace(",", "").astype(float)

    # Calculate CO2 emissions per continent
    co2_emissions_by_continent = data.groupby("Continent")["Co2-Emissions"].sum().reset_index()

    # Create a bar chart to display total CO2 emissions by continent
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(co2_emissions_by_continent["Continent"], co2_emissions_by_continent["Co2-Emissions"])
    ax.set_xlabel("Continent")
    ax.set_ylabel("Total CO2 Emissions")
    ax.set_title("Total CO2 Emissions by Continent")

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Display the bar chart
    st.pyplot(fig)

elif selected_viz == "Life Expectancy by Continent":
    # Create a scatter plot to display life expectancy by continent
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = {'Africa': 'red', 'Asia': 'blue', 'Europe': 'green', 'North America': 'purple', 'Oceania': 'orange', 'South America': 'brown'}

    for continent, color in colors.items():
        subset = data[data['Continent'] == continent]
        ax.scatter(subset['Life expectancy'], subset['Continent'], label=continent, color=color, alpha=0.7, s=100)

    ax.set_xlabel("Life Expectancy")
    ax.set_ylabel("Continent")
    ax.set_title("Life Expectancy by Continent")
    ax.legend()

    # Display the scatter plot
    st.pyplot(fig)