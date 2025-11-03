import requests
import os

# Read API keys from environment; raise if missing.
OPENFDA_KEY = os.getenv("OPENFDA_KEY")
RXNORM_KEY = os.getenv("RXNORM_KEY")
NIH_SUPP_KEY = os.getenv("NIH_SUPP_KEY")


def get_supplement_recommendations(current_supplements):
    """
    Placeholder: Suggest complementary nutrients.
    In a real implementation, you would query NIH/other DBs.
    """
    # Example logic: if user takes magnesium, recommend vitamin B6.
    recommendations = []
    lower_supps = [s.lower() for s in current_supplements]
    if "magnesium" in lower_supps:
        recommendations.append("Vitamin B6")
    # Extend with more rules or API calls
    return recommendations


def get_supplement_interactions(prescriptions, supplements):
    """
    Placeholder: Check for supplement–prescription interactions.
    Replace with calls to openFDA/RxNorm APIs when integrating.
    """
    interactions = []
    presc_lower = [p.lower() for p in prescriptions]
    supp_lower = [s.lower() for s in supplements]
    # Example: St. John's Wort vs SSRIs
    if "ssri" in presc_lower and "st. john's wort" in supp_lower:
        interactions.append("St. John's Wort can interact with SSRIs (risk of serotonin syndrome).")
    # More rules can be coded here until API integration
    return interactions
