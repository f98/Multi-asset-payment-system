import streamlit as st  # import streamlit as st 
st.write('Welcome to M.A.P.S simulator !') # write method i used to write


import streamlit as st


# Set the title of the page
st.title('Expected Gains !')
st.write("This simulator presents the outcome of an interaction between three different agents representing three parties: a buyer, a seller, and MAPS. The buyer allocates their income across different asset classes, while the seller has a given time preference. The multi-asset payment system (MAPS) is required to provide optimal value transfer and collect its commission. This simulation provides clear insights into what will happen when the three agents representing the three parties (MAPS, the seller, the buyer) reach a Nash equilibrium for a given increase in currency depreciation or a given increase in securities value.")


# 

# Create three columns for input fields
col1, col2, col3, col4, col5, col6, col7,col8 = st.columns(8)

# Input field for time preference
#transaction_date = col1.date_input('Transaction date')

# Input filed for cashing out
#exit_position = col2.date_input('Exit Position')
# expected exchnage rate 
#e_rate=""

# Input your customer profile
# Input your customer profile
class Customer:
    def __init__(self, name, dollar_holdings, euro_holdings,euro_percentage,dollar_percentage,name_of_asset,acquisation_price,number_of_shares):
  
        self.name = name
        self.dollar_holdings = dollar_holdings
        self.euro_holdings = euro_holdings
        self.euro_percentage=euro_percentage
        self.dollar_percentage=dollar_percentage
        self.name_of_asset=name_of_asset  
        self.acquisation_price=acquisation_price 
        self.number_of_shares= number_of_shares

# Create an instance of the Customer class
Alice = Customer("Alice", 10000, 8000,15/100 ,85/100,"Apple",170.0,10)
Bob=Customer('Bob',50000,15000,0.35,0.65,'Meta',300.0,10)
Ali=Customer('Ali',25000,15000,0.10 ,0.90,'Nike',98.0,20)


# Get the list of customer names
customer_options = [Alice.name, Bob.name, Ali.name]
# column
col1,col2,col3,col4,col5,col6,col7,col8=st.columns(8)
# Select a customer
selected_customer_name = col1.selectbox('Customer', customer_options)

# Get the selected customer object
def get_customer(name):
    if name == "Alice":
        return Alice
    elif name == "Bob":
        return Bob
    elif name == "Ali":
        return Ali
   
selected_customer = get_customer(selected_customer_name)



current_exchange_rate = col3.slider('current exchange rate', min_value=0.89, max_value=0.96, step=0.001)
dollar_depreciation_rate=col5.slider('dollar depreciation rate', min_value=0.000, max_value=0.1, step=0.001)
final_exchange_rate=current_exchange_rate-dollar_depreciation_rate
# Result
value_sold = st.slider('Value sold',min_value=0,max_value=8000,step=10)


def outcome(value_sold, selected_customer, final_exchange_rate):
    
    total_monetary_value = (selected_customer.dollar_percentage*value_sold) + (selected_customer.euro_percentage * value_sold * (1/final_exchange_rate))
    return total_monetary_value 





# average competitor
value_received_with_avg_competitor=(value_sold*0.98)-0.30
# cost with average competitor
cost_with_avg_competitor=(value_sold*0.02) +0.3
# increase in securities value :
increase_in_securities_value=st.slider('increase_in_securities_value',min_value=0.01,max_value=0.07,step=0.001)
securities_sold = (selected_customer.acquisation_price  * (1 + increase_in_securities_value)) * selected_customer.number_of_shares
st.write('test',securities_sold)
rest = value_sold - securities_sold
st.write('test2', rest)
def package(rest, selected_customer, final_exchange_rate,securities_sold):
    
    
    currencies_sold = (selected_customer.dollar_percentage * rest) + (selected_customer.euro_percentage * rest * (1 / final_exchange_rate))
    total_monetary_value = securities_sold + currencies_sold
    return total_monetary_value


# fees
competitor_fees=value_sold-cost_with_avg_competitor





if st.button("Apply") :
    
    if value_sold<=3500:
     final_amount_sold = outcome(value_sold,selected_customer,final_exchange_rate)
     st.write("total monetary value generated by the transaction using MAPS:", final_amount_sold,'$')
     my_gain=((final_amount_sold-value_sold)*0.2)+(value_sold*0.01)
     st.write('Maps gain is' ,my_gain)
     Money_i_will_recieve_as_merchant =final_amount_sold-my_gain
     merchant_excess_money=Money_i_will_recieve_as_merchant-value_sold
     st.write('the monetary value you will receive if you use a payment provider that averages a 2 percent fee plus a fixed fee',value_sold-cost_with_avg_competitor)
     st.write('Money I will receive as merchant ', Money_i_will_recieve_as_merchant)
     st.write('the excess money I will make  as a merchant ',merchant_excess_money)
    else:
     final_amount_sold = package(value_sold,selected_customer,final_exchange_rate,increase_in_securities_value)
     st.write("total monetary value generated by the transaction using MAPS:", final_amount_sold,'$')
     my_gain=((final_amount_sold-value_sold)*0.2)+(value_sold*0.01)
     st.write('Maps gain is' ,my_gain)
     Money_i_will_recieve_as_merchant =final_amount_sold-my_gain
     merchant_excess_money=Money_i_will_recieve_as_merchant-value_sold
     st.write('the monetary value you will receive if you use a payment provider that averages a 2 percent fee plus a fixed fee',value_sold-cost_with_avg_competitor)
     st.write('Money I will receive as merchant ', Money_i_will_recieve_as_merchant)
     st.write('the excess money I will make  as a merchant ',merchant_excess_money)
   

