import streamlit as st

def calculate_strategy_metrics(price, rental_data):
    results = {}
    for strategy, values in rental_data.items():
        annual_income = values["monthly_income"] * 12
        noi = annual_income - values["annual_expenses"]
        cap_rate = round((noi / price) * 100, 2)
        results[strategy] = {
            "monthly_income": values["monthly_income"],
            "annual_income": annual_income,
            "annual_expenses": values["annual_expenses"],
            "NOI": noi,
            "Cap Rate (%)": cap_rate
        }
    return results

def rental_strategy_app():
    st.title("📈 Folio: Real Estate Rental Strategy Builder")
    st.write("Paste a listing URL and see rental strategies based on short-, mid-, and long-term models.")

    url = st.text_input("Paste Realtor.com or other property listing URL")

    if url:
        st.success("✔️ Link received! Using simulated property data for now.")

        property_data = {
            "address": "210 Summit Avenue, Jersey City, NJ 07304",
            "price": 535600,
            "bedrooms": 3,
            "bathrooms": 2,
            "square_feet": 1904,
            "property_taxes": 7360
        }

        st.subheader("📍 Property Overview")
        st.write(f"**Address:** {property_data['address']}")
        st.write(f"**Price:** ${property_data['price']:,}")
        st.write(f"**Bedrooms/Bathrooms:** {property_data['bedrooms']} / {property_data['bathrooms']}")
        st.write(f"**Square Feet:** {property_data['square_feet']} sqft")
        st.write(f"**Annual Taxes:** ${property_data['property_taxes']:,}")

        st.sidebar.header("Adjust Rental Income & Expenses")
        rental_assumptions = {
            "short_term": {
                "monthly_income": st.sidebar.number_input("Short-term Monthly Income", value=4800),
                "annual_expenses": st.sidebar.number_input("Short-term Annual Expenses", value=24000),
            },
            "mid_term": {
                "monthly_income": st.sidebar.number_input("Mid-term Monthly Income", value=3500),
                "annual_expenses": st.sidebar.number_input("Mid-term Annual Expenses", value=15000),
            },
            "long_term": {
                "monthly_income": st.sidebar.number_input("Long-term Monthly Income", value=2800),
                "annual_expenses": st.sidebar.number_input("Long-term Annual Expenses", value=12000),
            },
        }

        strategy_report = calculate_strategy_metrics(property_data["price"], rental_assumptions)
        st.subheader("📊 Rental Strategy Report")

        for strategy, data in strategy_report.items():
            with st.expander(f"{strategy.replace('_', ' ').title()}"):
                st.write(f"- Monthly Income: ${data['monthly_income']:,}")
                st.write(f"- Annual Income: ${data['annual_income']:,}")
                st.write(f"- Annual Expenses: ${data['annual_expenses']:,}")
                st.write(f"- NOI: ${data['NOI']:,}")
                st.write(f"- Cap Rate: {data['Cap Rate (%)']}%")

rental_strategy_app()
