# icecream_game

Python version 3.8 is used.

##Introduction:
This exercise challenges you to write a full game of your own! Simulating an ice cream shop with daily
choices to make. It is the culmination of what you have learnt based on the tutorials and work you have
done in the past.
Don’t forget to add your own flavor to the game, it doesn’t have to be vanilla

### Rules

- You start out with 1,000 euros
- Purchase price of ice cream: 0.30 euros
- Purchase price of cone: 0.15 euros
- Ice cream that is not sold goes bad and cannot be sold the next round, while
cones can be sold the next round
- Formula for maximum sales of ice cream during a day: max_ice_cream_sales =
1000 * temperature * (10 – price) temperature in Celsius, price in dollars.
- Weather Is randomly generated integer between -10 and 40
- Formula for actual sales of ice cream during a day :Actual_ice_cream_sales =
min(max_ice_cream_sales, stock_ice_cream, stock_cones)
- Make sure to always check & validate for correct input.
- If your balance falls below 75 euro’s, the player is broke.