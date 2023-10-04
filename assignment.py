import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV data
data = pd.read_csv("world-data-2023.csv")

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

        # Create and display the scatter plot with filtered data
        create_scatter_plot(filtered_data)

        st.write("As seen in the above visualizations, Africa has the lowest life expectancy while Europe has the highest one.")

else:
    if selected_viz == "Total CO2 Emissions by Continent":
        # Create a dropdown to select the continent for CO2 emissions
        selected_continent = st.selectbox("Select Continent for CO2 Emissions", data['Continent'].unique())

        # Filter data based on the selected continent
        filtered_data = data[data['Continent'] == selected_continent]

        # Clean and convert the "CO2-Emissions" column to numeric (remove commas)
        filtered_data["Co2-Emissions"] = filtered_data["Co2-Emissions"].str.replace(",", "").astype(float)

        # Calculate CO2 emissions per country for the selected continent
        co2_emissions_by_country = filtered_data.groupby("Country")["Co2-Emissions"].sum().reset_index()

        # Create a bar chart to display CO2 emissions by country for the selected continent
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(co2_emissions_by_country["Country"], co2_emissions_by_country["Co2-Emissions"])
        ax.set_xlabel("Country")
        ax.set_ylabel("Total CO2 Emissions")
        ax.set_title(f"Total CO2 Emissions for {selected_continent}")
        plt.xticks(rotation=45)

        # Display the bar chart
        st.pyplot(fig)

        st.write(f"{selected_continent} seems to have the following CO2 emissions by country.")
