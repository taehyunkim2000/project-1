class Product:
  def __init__(self, product_id, name, category, price, quantity_in_stock):
      self.product_id = product_id
      self.name = name
      self.category = category
      self.price = price
      self.quantity_in_stock = quantity_in_stock

class Inventory:
  def __init__(self):
      self.products = []

  def add_product(self, product):
      self.products.append(product)

  def update_stock(self, product_id, quantity):
      for product in self.products:
          if product.product_id == product_id:
              product.quantity_in_stock += quantity
              return

  def get_product_info(self, product_id):
      for product in self.products:
          if product.product_id == product_id:
              return product
      return None

class Transaction:
  def __init__(self, transaction_id, products_sold, total_amount):
      self.transaction_id = transaction_id
      self.products_sold = products_sold
      self.total_amount = total_amount

class Report:
  def generate_stock_report(self, inventory):
      for product in inventory.products:
          print(f"Product: {product.name}, Category: {product.category}, Stock: {product.quantity_in_stock}")

  def generate_sales_report(self, transactions):
      for transaction in transactions:
          print(f"Transaction ID: {transaction.transaction_id}, Total Amount: {transaction.total_amount}")

if __name__ == "__main__":
  inventory = Inventory()
  transactions = []
  report = Report()

  while True:
      print("\nOptions:")
      print("1. Add Product")
      print("2. Update Stock")
      print("3. Record Sale")
      print("4. Generate Stock Report")
      print("5. Generate Sales Report")
      print("6. Exit")

      choice = input("Enter your choice: ")

      if choice == "1":
          product_id = int(input("Enter Product ID: "))
          name = input("Enter Product Name: ")
          category = input("Enter Product Category: ")
          price = float(input("Enter Product Price: "))
          quantity = int(input("Enter Quantity in Stock: "))
          product = Product(product_id, name, category, price, quantity)
          inventory.add_product(product)
          print("Product added successfully.")

      elif choice == "2":
          product_id = int(input("Enter Product ID: "))
          quantity = int(input("Enter Quantity to Update: "))
          inventory.update_stock(product_id, quantity)
          print("Stock updated successfully.")

      elif choice == "3":
          transaction_id = len(transactions) + 1
          products_sold = []
          total_amount = 0

          while True:
              product_id = int(input("Enter Product ID (0 to stop): "))

              if product_id == 0:
                  break

              product = inventory.get_product_info(product_id)

              if product:
                  quantity = int(input(f"Enter Quantity of {product.name} Sold: "))
                  products_sold.append((product, quantity))
                  total_amount += product.price * quantity
              else:
                  print("Product not found.")

          transaction = Transaction(transaction_id, products_sold, total_amount)
          transactions.append(transaction)
          print(f"Sale recorded with Transaction ID: {transaction_id}")

      elif choice == "4":
          report.generate_stock_report(inventory)

      elif choice == "5":
          report.generate_sales_report(transactions)

      elif choice == "6":
          break
