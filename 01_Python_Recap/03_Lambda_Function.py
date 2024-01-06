"""     Lambda function     """
# lambda / in-line function
dis_price_lambda = lambda discount : 900 - (900 * (discount/100))

# call the function with discount = 10%
print(dis_price_lambda(10))
