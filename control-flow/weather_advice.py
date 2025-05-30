# Weather advice app

# Creating the weather variable that prompts the user
weather = input("What's the weather like today ?(sunny/rainy/cold): ")

# using the if to check what the user input
if weather.lower() == 'sunny':
    print('Wear a t-shirt and sunglasses.')
elif weather.lower() == 'rainy':
    print("Don't forget your umbrella and a raincoat.")
elif weather.lower() == 'cold':
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")