def drug_dosage_calculator (weight_kg, strength):
    if weight_kg >= 100 or weight_kg <= 10: # Check if weight is between 100 kg and 200 kg
        raise ValueError("Weight must be between 10 kg and 100 kg.")
    else:
        if strength == "120 mg/5 ml":
            concentration = 120 / 5  
        elif strength == "250 mg/5 ml":
            concentration = 250 / 5  
        else: #ensure the right strength is used
            raise ValueError("Strength must be '120 mg/5 ml' or '250 mg/5 ml'.")

    dose_mg = 15 * weight_kg
    volume_ml = dose_mg / concentration

    return volume_ml

# Example usage:
dose_volume = drug_dosage_calculator(50, "120 mg/5 ml")
print(f"The volume of the drug to be administered is: {dose_volume} ml")
