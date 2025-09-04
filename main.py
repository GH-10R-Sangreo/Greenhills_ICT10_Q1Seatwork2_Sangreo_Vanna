from pyscript import display


print("'La Gueule de Venus")
display("La Geule de Venus", target="insert")

restaurant_name = 'La Gueule de Venus' # string
owner_name = 'Vincent Venus' # string
year_established = 1980 # integer
popular_item_price = 67.5 # float
has_delivery = True # boolean
product_names = ['Champagne','Chocolate Mousse','Ratatouille','Entrecôte','Coquilles Saint-Jacques'] # list
business_hours = 'Weekdays: 9:00 AM - 10:00 PM' # string
business_hours2 = 'Weekends: "8:00 AM - 12:00 AM' # string
tax_rate = 0.16 # float

display(f'Welcome to {restaurant_name}, founded by {owner_name}', target="insert")
display(f'Since {1980}', target="insert")
display(f'{business_hours}', target="insert2")
display(f'{business_hours2}', target="insert2")