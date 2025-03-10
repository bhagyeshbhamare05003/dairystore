# import pymongo
# import random

# # MongoDB connection details
# connection_url = "mongodb+srv://mail6164:p5gJG8WFj1oOsfyt@cluster8164.nfco6cq.mongodb.net/dairy_user_info?"
# db_name = "dairy_user_info"

# # Sample product categories
# product_categories = ["milk", "yogurt", "cream", "cheese", "butter"]

# # Function to generate product name with random category
# def generate_product_name():
#     category = random.choice(product_categories)
#     return f"Maple Hill Shelf Stable Whole White {category.capitalize()}"

# # Sample product data
# products_data = [
#     {
#         "_id": 10002007000 + i + 1,  # Generating unique _id values as integers
#         "Product Name": generate_product_name(),
#         # "Product Price": 28.00,  # Updated price as a float
#         "Product Price": "$28.00",
#         "Brand": "Maple Hill",
#         "Flavor": "Whole Milk",
#         "Weight": "6.74 Pounds",
#         "Description": "* MILK YOU CAN FEEL GOOD ABOUT: We are the original 100% grass-fed organic milk brand in America. Maple Hill is committed to sustainable practices and the ethical treatment of animals.\nBETTER FOR THE PLANET: Our FSC certified aseptic milk boxes are 100% recyclable, resealable and don't require the use of plastic straws.\nFARM TO CARTON: Milk, the way nature intended from 100% pasture-raised grass-fed cows from small family-owned farms.\nGREENER PASTURES: We use regenerative agriculture farming methods. We grow our own organic grass and our cows graze from pasture to pasture fertilizing as they go. Our closed loop ecosystem greatly reduces C02."
#     }
#     for i in range(40)
# ]

# # Connect to MongoDB
# client = pymongo.MongoClient(connection_url)
# db = client[db_name]
# collection = db["Product"]

# # Inserting the data into the collection
# collection.insert_many(products_data)

# print("Data inserted successfully.")


# import pymongo

# # MongoDB connection details
# connection_url = "mongodb+srv://mail6164:p5gJG8WFj1oOsfyt@cluster8164.nfco6cq.mongodb.net/dairy_user_info?"
# db_name = "dairy_user_info"

# # Connect to MongoDB
# client = pymongo.MongoClient(connection_url)
# db = client[db_name]
# collection = db["Product"]

# # Iterate through documents in the collection
# for product in collection.find():
#     # Get the existing price value (assuming it's stored as a string)
#     price_str = product.get("Product Price", "")
#     try:
#         # Convert the existing price value from string to float
#         price_float = float(price_str.replace("$", ""))  # Remove "$" sign if present
#         # Update the document with the new float value for "Product Price"
#         collection.update_one({"_id": product["_id"]}, {"$set": {"Product Price": price_float}})
#         print(f"Updated price for product {product['_id']} to {price_float}")
#     except ValueError:
#         print(f"Skipping product {product['_id']}: Invalid price value {price_str}")

# print("Price update completed.")

