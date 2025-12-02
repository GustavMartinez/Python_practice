colleagues = ["Sarah Martinez", "Michale Chen", "Emily Brown"]

# Apply the lambda function to each colleagues name
cleaned = map(lambda x: x.replace(" ", "_").lower(), colleagues)

# Convert map object to list:
cleaned_list = list(cleaned)
print(cleaned_list)