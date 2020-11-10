import random
from game_files.game_config import (STARTING_BUDGET,
                                    PURCHASE_PRICE_ICE,
                                    PURCHASE_PRICE_CONE,
                                    OPERATING_COST)


def display_instructions() -> None:  # rename to print
    """Starts the game and prints welcome statement """
    print("Welcome to 'You Cone Do It!' "
          "where you run an ice cream empire and either become a billionaire or homeless. \n "
          "You run your ice cream empire, also known as the ice cream cart, round by round. "
          "Every round you get a chance to grow your stash of cash by buying stock (Ice Cream and Cones) "
          "and setting the price for which you want to sell your ice cream. After your input the sales "
          "are simulated resulting in a financial report detailing your stats. \n"
          "Each round costs $75 dollars for your standard expenses")


def get_max_ice_cream_sales(temperature: float, price: float) -> float:
    """Formula for maximum sales of ice cream during a day"""
    return 1000 * temperature * (10 - price)


def get_actual_ice_cream_sales(max_ice_cream_sales: float, stock_ice_cream: int, stock_cones: int) -> float:
    """Formula for maximum sales of ice cream during a day"""
    return min(max_ice_cream_sales, stock_ice_cream, stock_cones)


def get_weather() -> float:
    """Weather Is randomly generated integer between -10 and 40"""
    return random.randint(-10, 40)


def get_total_balance_after_round(num_ice_bought,
                                  purchase_price_ice,
                                  num_cones_bought,
                                  purchase_price_cone,
                                  starting_money,
                                  operating_cost,
                                  selling_price,
                                  icecreams_sold):
    ice_expenses = purchase_price_ice * num_ice_bought
    cone_expenses = purchase_price_cone * num_cones_bought
    income = selling_price * icecreams_sold
    total = starting_money - operating_cost - ice_expenses - cone_expenses + income

    return ice_expenses, cone_expenses, income, total


def display_financial_report(game_round,
                             starting_money,
                             operating_cost,
                             ice_expenses,
                             cone_expenses,
                             income,
                             total):
    print("==============================================\n",
          "=============Finances Round", game_round, "===============\n",
          "=============================================\n",
          "Starting Money", starting_money, "\n",
          "Operating Cost", operating_cost, "\n",
          "Ice Cream Expenses", ice_expenses, "\n",
          "Cone Expenses", cone_expenses, "\n",
          "Income", income, "\n",
          "=============================================\n",
          "Total", total, "\n")


def play_game(starting_balance: int,
              purchase_price_ice: float,
              purchase_price_cone: float,
              operating_cost: float) -> None:
    """play the game"""

    display_instructions()

    game_round = 1
    current_balance = starting_balance
    game_continues = "Y"
    stock_ice_cream = 0
    stock_cones = 0

    while (current_balance >= operating_cost) & (game_continues == "Y"):
        round_weather = get_weather()

        print("The current weather today is", round_weather, "degrees celsius \n",
              "Your current balance is ", current_balance)

        max_ice_cream_purchase = round((current_balance - operating_cost) / (purchase_price_ice + purchase_price_cone))

        print("Stock up your Ice ($", purchase_price_ice, "), don't forget to keep some money for the cones (max:",
              max_ice_cream_purchase, ")")

        while True:
            try:
                num_ice_bought = int(input())
                break
            except ValueError:
                print("Your input is not a valid number/integer! Please try again ...")

        print("Stock up your Ice Cones ($", purchase_price_cone,
              "), (max:", max_ice_cream_purchase, ")")

        while True:
            try:
                num_cones_bought = int(input())
                break
            except ValueError:
                print("Your input is not a valid number/integer! Please try again ...")

        print("Set the selling price for your delicious ice creams $(x.xx)")

        while True:
            try:
                selling_price = float(input())
                break
            except ValueError:
                print("Your input is not a valid number! Please try again ...")

        get_max_ice_cream_sales(round_weather, selling_price)

        ice_creams_sold = get_actual_ice_cream_sales(round_weather,  # not weather but max?
                                                     stock_ice_cream + num_ice_bought,
                                                     stock_cones + num_cones_bought)
        print("You sell", ice_creams_sold)

        round_finances = get_total_balance_after_round(num_ice_bought,
                                                       purchase_price_ice,
                                                       num_cones_bought,
                                                       purchase_price_cone,
                                                       current_balance,
                                                       operating_cost,
                                                       selling_price,
                                                       ice_creams_sold)
        current_balance = round_finances[3]

        display_financial_report(game_round,
                                 current_balance,
                                 operating_cost,
                                 round_finances[0],
                                 round_finances[1],
                                 round_finances[2],
                                 round_finances[3])

        # how do I add multiple checks in here?
        print("Do you want to continue (Y/N)?")
        while True:
            try:
                game_continues = str(input()).upper()
                print(game_continues)
                break
            except ValueError:
                print("Your input must be either Y or N! Please try again ...")

        game_round += 1
        stock_ice_cream = 0

    print("Game over")


if __name__ == "__main__":
    play_game(STARTING_BUDGET,
              PURCHASE_PRICE_ICE,
              PURCHASE_PRICE_CONE,
              OPERATING_COST)
