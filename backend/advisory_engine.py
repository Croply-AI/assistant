def crop_recommendation(soil_type, rainfall_level):

    if soil_type == "loamy" and rainfall_level == "high":
        return "Maize"

    elif soil_type == "sandy" and rainfall_level == "medium":
        return "Groundnuts"

    elif soil_type == "clay" and rainfall_level == "low":
        return "Cassava"

    else:
        return "Consult advisory system"
