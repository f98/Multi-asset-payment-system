class Customer:
    def __init__(self, name, dollar_holdings, euro_holdings,euro_percentage,dollar_percentage):
  
        self.name = name
        self.dollar_holdings = dollar_holdings
        self.euro_holdings = euro_holdings
        self.euor_percentage=euro_percentage
        self.dollar_percentage=dollar_percentage

# Create an instance of the Customer class
Alice = Customer("alice", 1000, 800, 0.15 , 0.85)
Bob=Customer('bob,',5000,1500, 0.25 , 0.75)
Ali=Customer('ali',2500,1500, 0.10 , 0.90)
Asma=Customer('asma',2500,3000, 0.35 , 0.65)
# Sample customer data (replace with actual data from your Customer objects)
customers_data = {
    'Alice': Customer('Alice', dollar_holdings=1000, euro_holdings=800, euro_percentage=0.15,dollar_percentage=0.85),
    'Bob': Customer('Bob', dollar_holdings=5000, euro_holdings=5000,euro_percentage=0.25,dollar_percentage=0.75),
    'Ali': Customer('Ali', dollar_holdings=2500, euro_holdings=1500, euro_percentage=0.10,dollar_percentage=0.90),
    'Asma': Customer('Asma', dollar_holdings=2500, euro_holdings=3000, euro_percentage=0.35,dollar_percentage=0.65)
}


