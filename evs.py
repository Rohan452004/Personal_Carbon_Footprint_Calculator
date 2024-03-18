import streamlit as st

EMISSION_FACTORS = {
    "India": {"Transportation": 0.14, "Electricity": 0.82, "Diet": 1.25, "Waste": 0.1},
    "USA": {"Transportation": 0.11, "Electricity": 0.77, "Diet": 1.23, "Waste": 0.1},
    "Germany": {"Transportation": 0.08, "Electricity": 0.55, "Diet": 1.14, "Waste": 0.1},
    "China": {"Transportation": 0.12, "Electricity": 0.75, "Diet": 1.18, "Waste": 0.09},
    "Brazil": {"Transportation": 0.09, "Electricity": 0.68, "Diet": 1.21, "Waste": 0.12},
    "United Kingdom": {"Transportation": 0.1, "Electricity": 0.6, "Diet": 1.17, "Waste": 0.11},
    "Japan": {"Transportation": 0.09, "Electricity": 0.72, "Diet": 1.15, "Waste": 0.08},
    "France": {"Transportation": 0.07, "Electricity": 0.58, "Diet": 1.13, "Waste": 0.1},
    "Canada": {"Transportation": 0.1, "Electricity": 0.7, "Diet": 1.2, "Waste": 0.1},
    "Australia": {"Transportation": 0.12, "Electricity": 0.75, "Diet": 1.22, "Waste": 0.11},
    "South Africa": {"Transportation": 0.15, "Electricity": 0.9, "Diet": 1.28, "Waste": 0.13},
    "Russia": {"Transportation": 0.13, "Electricity": 0.65, "Diet": 1.19, "Waste": 0.09},
    "Mexico": {"Transportation": 0.1, "Electricity": 0.72, "Diet": 1.25, "Waste": 0.12},
    "South Korea": {"Transportation": 0.11, "Electricity": 0.68, "Diet": 1.14, "Waste": 0.1},
}

def calculate_emissions(country, distance, electricity, waste, meals):
    transportation_emissions = EMISSION_FACTORS[country]["Transportation"] * (distance * 365)
    electricity_emissions = EMISSION_FACTORS[country]["Electricity"] * (electricity * 12)
    diet_emissions = EMISSION_FACTORS[country]["Diet"] * (meals * 365)
    waste_emissions = EMISSION_FACTORS[country]["Waste"] * (waste * 52)

    return (
        round(transportation_emissions / 1000, 2),
        round(electricity_emissions / 1000, 2),
        round(diet_emissions / 1000, 2),
        round(waste_emissions / 1000, 2),
    )
    

def display_results(transportation, electricity, diet, waste, total):
    st.subheader("🌿 Carbon Emissions Breakdown")
    st.write(f"🚗 Transportation: {transportation} tonnes CO2 per year")
    st.write(f"💡 Electricity: {electricity} tonnes CO2 per year")
    st.write(f"🍽 Diet: {diet} tonnes CO2 per year")
    st.write(f"🗑 Waste: {waste} tonnes CO2 per year")

    st.subheader("🌍 Total Carbon Footprint")
    st.success(f"Your total carbon footprint is: {total} tonnes CO2 per year")

    suggest_evaluation(total)

def suggest_evaluation(total_emissions):
    if total_emissions <= 5:
        st.success("🌱 Fantastic! Your carbon emissions are very low. Keep up the sustainable practices!")
    elif 5 < total_emissions <= 10:
        st.warning("⚠️ Good effort! Your carbon emissions are moderate. Consider adopting more sustainable habits.")
        suggest_reduction_strategies()
    else:
        st.error("🔥 Attention! Your carbon emissions are high. Explore ways to reduce your environmental impact.")
        suggest_reduction_strategies()

def suggest_reduction_strategies():
    st.subheader("🌎 Suggestions to Reduce Your Carbon Emissions:")

    st.markdown("1. 🚶 *Transportation:* Consider walking, biking, or using public transportation.")
    st.markdown("2. 💡 *Electricity Consumption:* Turn off lights, unplug chargers, and switch to energy-efficient appliances.")
    st.markdown("3. 🌱 *Diet:* Include more plant-based meals and reduce meat consumption.")
    st.markdown("4. ♻️ *Waste Management:* Recycle, compost, and minimize single-use items.")

def main():
    st.set_page_config(
        layout="wide",
        page_title="Eco-Friendly Carbon Calculator",
        initial_sidebar_state="expanded",
        page_icon="🌍",
    )
    st.title("Personal Carbon Footprint Calculator 🌿")

    st.subheader("🌍 Your Country")
    countries = list(EMISSION_FACTORS.keys())
    country = st.selectbox("Select", countries)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🚗 Daily Commute Distance (km)")
        distance = st.slider("Distance", 0.0, 100.0, key="distance_input")
        custom_distance = st.number_input("Custom Distance (km)", value=distance, key="custom_distance_input")

        st.subheader("💡 Monthly Electricity Consumption (kWh)")
        electricity = st.slider("Electricity", 0.0, 1000.0, key="electricity_input")
        custom_electricity = st.number_input("Custom Electricity (kWh)", value=electricity, key="custom_electricity_input")

    with col2:
        st.subheader("🗑 Waste Generated per Week (kg)")
        waste = st.slider("Waste", 0.0, 100.0, key="waste_input")
        custom_waste = st.number_input("Custom Waste (kg)", value=waste, key="custom_waste_input")

        st.subheader("🍽 Number of Meals per Day")
        meals = st.number_input("Meals", 0, key="meals_input")

    if custom_distance is not None:
        distance = custom_distance
    if custom_electricity is not None:
        electricity = custom_electricity
    if custom_waste is not None:
        waste = custom_waste

    transportation, electricity, diet, waste = calculate_emissions(country, distance, electricity, waste, meals)
    total_emissions = round(transportation + electricity + diet + waste, 2)

    if st.button("Calculate CO2 Emissions"):
        st.header("Results")
        display_results(transportation, electricity, diet, waste, total_emissions)


main()