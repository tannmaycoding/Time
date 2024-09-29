import streamlit as st

st.title("Time Converter")

units = ["sec", "min", "hrs", "days", "months", "years", "decade"]
col1, col2 = st.columns(2)
from_unit = col1.selectbox("Unit From Which You Want To Convert", options=units)
no_of_units = col2.text_input("No. Of Units You Want To Convert", value="0")
to_unit = col1.selectbox("Unit To Which You Want To Convert", options=units)
to_converted = col2.empty()


# Conversion function
def convert_units():
    conversions = {
        "sec": {"sec": 1, "min": 1/60, "hrs": 1/3600, "days": 1/86400, "months": 1/2.628e+6, "years": 1/3.154e+7, "decade": 1/3.154e+8},
        "min": {"sec": 60, "min": 1, "hrs": 1/60, "days": 1/1440, "months": 1/43800, "years": 1/525600, "decade": 1/5.256e+6},
        "hrs": {"sec": 3600, "min": 60, "hrs": 1, "days": 1/24, "months": 1/730, "years": 1/8760, "decade": 1/87600},
        "days": {"sec": 86400, "min": 1440, "hrs": 24, "days": 1, "months": 1/30.417, "years": 1/365, "decade": 1/3650},
        "months": {"sec": 2.628e+6, "min": 43800, "hrs": 730, "days": 30.417, "months": 1, "years": 1/12, "decade": 1/120},
        "years": {"sec": 3.154e+7, "min": 525600, "hrs": 8760, "days": 365, "months": 12, "years": 1, "decade": 10},
        "decade": {"sec": 3.154e+8, "min": 5.256e+6, "hrs": 87600, "days": 3650, "months": 120, "years": 10, "decade": 1},
    }

    if from_unit in conversions and to_unit in conversions[from_unit]:
        return float(no_of_units) * conversions[from_unit][to_unit]
    else:
        return None


# Convert the units and display
try:
    value = float(no_of_units)
    converted_value = convert_units()
    if converted_value is not None:
        to_converted.markdown(f"### {float(converted_value):.2f}")
    else:
        to_converted.markdown("### Conversion not available")
except Exception as e:
    print(e)
    to_converted.markdown("### Please enter a valid number")
