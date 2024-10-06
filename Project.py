menu = ['1: View products', '2: Add product', '3: Edit product', '4: Delete product']
products = ["candy", "cake", "fruit", "snacks"]
prices = [200000, 300000, 100000, 500000]

continue_program = 1
while continue_program == 1:
    for option in menu:
        print(option)
    function = int(input('Choose the function you want:'))

    # Function 1: View products
    if (function == 1):
        for i in range(len(prices)):
            print(i + 1, products[i], "", prices[i])

        continue_program = int(input("Do you want to continue? (1 for Yes, 0 for No):"))

    # Function 2: Add product
    if (function == 2):
        new_product = input("Enter the name of the product:")
        new_price = input("Enter the price of the product:")
        products.append(new_product)
        prices.append(new_price)

        continue_program = int(input('Do you want to continue? (1 for Yes, 0 for No):'))

    # Function 3: Edit product
    if (function == 3):
        for i in range(len(prices)):
            print(i + 1, products[i], "", prices[i])

        selected_product = int(input('Choose the product to edit:'))
        new_product_name = input('Enter the new product name:')
        new_price = float(input("Enter the new price:"))
        prices[selected_product - 1] = new_price
        products[selected_product - 1] = new_product_name

        continue_program = int(input("Do you want to continue? (1 for Yes, 0 for No):"))

    # Function 4: Delete product
    if (function == 4):
        for i in range(len(prices)):
            print(i + 1, products[i], "", prices[i])

        selected_product = int(input('Choose the product to delete:'))
        products.pop(selected_product - 1)
        prices.pop(selected_product - 1)

        continue_program = int(input("Do you want to continue? (1 for Yes, 0 for No):"))
