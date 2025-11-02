
# Set (does not contain dublicates) 


bigMenu = [  "rajma chawal", "biriyani", "rajma chawal", "sweet rajma potato"]

resultSet = { item  for item in bigMenu}
print(f"resultSet: {resultSet}")


receips = {

    "Masala chai": ["ginger", "cardamom", "clove"],
    "Elaichi chai": ["milk", "cardamom", ],
    "Spicy chai": ["ginger", "black paper", "clove"]
}

uniqueSpices = { items for ingredients in receips.values() for items in ingredients}
print(f"unique spices: {uniqueSpices}")


