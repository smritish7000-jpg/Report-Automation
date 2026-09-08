import csv 
input_file='project2/sample_orders.csv'
output_file='project2/output.csv'

total_orders=0
total_items=0
total_revenue=0
category_sales={}
city_sales={}
payment_methods={}
product_quantity={}
status_count={}

highest_order=None
highest_order_value=0

rows=[]

with open(input_file, 'r',newline ='',encoding='utf-8') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        order_id=row['OrderID']
        product=row['Product']
        category=row['Category']
        quantity=int(row['Quantity'])
        total_price=float(row['TotalPrice'])   
        city=row['City']
        payment_method=row['PaymentMethod']
        status=row['Status']

        total_orders += 1
        total_items += quantity
        total_revenue += total_price

        if category not in category_sales:
            category_sales[category]=0
        category_sales[category] += total_price

        if city not in city_sales:
            city_sales[city]=0
        city_sales[city] += total_price

        if payment_method not in payment_methods:
            payment_methods[payment_method]=0
        payment_methods[payment_method] += total_price  

        if product not in product_quantity:
            product_quantity[product]=0
        product_quantity[product] += quantity

        if status not in status_count:
            status_count[status]=0
        status_count[status] += 1   

        if total_price > highest_order_value:
            highest_order_value = total_price
            highest_order = {"OrderID": order_id,
                "Product": product,
                "CustomerName": row["CustomerName"],
                "TotalPrice": total_price}

        rows.append(row)

    best_product=max(product_quantity,key=product_quantity.get)
    best_product_quantity=product_quantity[best_product]

    with open(output_file, 'w',newline ='',encoding='utf-8') as file:

        writer = csv.writer(file)
        writer.writerow(['SALES REPORT'])

        writer.writerow([])

        writer.writerow(['Basic Statistics'])
        writer.writerow(['Total Orders',total_orders])
        writer.writerow(['Total Items',total_items])
        writer.writerow(['Total Revenue',f"{total_revenue:.2f}"])
        writer.writerow([])

        writer.writerow(['Best Selling Product', best_product])
        writer.writerow(['Quantity', best_product_quantity])

        writer.writerow([])

        writer.writerow(['Highest Order Value'])
        writer.writerow(['Order ID', 'Product', 'Customer Name', 'Total Price'])
        writer.writerow([highest_order["OrderID"], highest_order["Product"], highest_order["CustomerName"], f"{highest_order['TotalPrice']:.2f}"])  

        writer.writerow([])

        writer.writerow(['Sales by Category'])
        writer.writerow(['Category', 'Total Sales'])
        for category, revenue in category_sales.items():
            writer.writerow([category, f"{revenue:.2f}"])

        writer.writerow([])

        writer.writerow(['Sales by City'])  
        writer.writerow(['City', 'Total Sales'])
        for city,revenue in city_sales.items():
            writer.writerow([city, f"{revenue:.2f}"])

        writer.writerow([])

        writer.writerow(['Sales by Payment Method'])
        writer.writerow(['Payment Method', 'Total Sales'])
        for payment_method,revenue in payment_methods.items():
            writer.writerow([payment_method, f"{revenue:.2f}"])

        writer.writerow([])

        writer.writerow(['Order Status'])
        writer.writerow(['Status', 'Orders'])
        for status,status_count in status_count.items():
            writer.writerow([status, status_count])

        writer.writerow([])




