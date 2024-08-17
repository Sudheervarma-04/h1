import datetime

# Data structure to store e-waste items
e_waste_items = []

# Function to add items
def add_item(name, purchase_date, lifespan):
    e_waste_items.append({
        'name': name,
        'purchase_date': purchase_date,
        'lifespan': lifespan,
        'status': 'in use'
    })

# Function to check item status
def check_status():
    today = datetime.date.today()
    for item in e_waste_items:
        purchase_date = datetime.datetime.strptime(item['purchase_date'], "%Y-%m-%d").date()
        if (today - purchase_date).days > item['lifespan']:
            item['status'] = 'ready for recycling'
        else:
            item['status'] = 'in use'

# Function to recycle items
def recycle_item(item_name):
    for item in e_waste_items:
        if item['name'] == item_name and item['status'] == 'ready for recycling':
            item['status'] = 'recycled'
            print(f"Item '{item_name}' has been recycled.")

# Example usage
add_item('Computer', '2018-10-03', 365*2)  # 2 years lifespan
add_item('Bluetooth ', '2019-08-10', 365*1.5)  # 1.5 years lifespan

check_status()

for item in e_waste_items:
    print(f"{item['name']} - Status: {item['status']}")

recycle_item('Computer')