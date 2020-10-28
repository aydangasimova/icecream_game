import random
from icecream_game.game.game_config import (STARTING_BUDGET,
                                            PURCHASE_PRICE_ICE,
                                            PURCHASE_PRICE_CONE,
                                            OPERATING_COST)


def get_max_ice_cream_sales(temperature: float, price: float) -> float:
    """Formula for maximum sales of ice cream during a day"""
    return 1000 * temperature * (10 - price)


def get_actual_ice_cream_sales(max_ice_cream_sales: float, stock_ice_cream: int, stock_cones: int) -> float:
    """Formula for maximum sales of ice cream during a day"""
    return min(max_ice_cream_sales, stock_ice_cream, stock_cones)


def get_weather() -> int:
    """Weather Is randomly generated integer between -10 and 40"""
    return random.randint(-10, 40)


def start_game():
    """Starts the game and prints welcome statement """
    print("Welcome to 'You Cone Do It!' "
          "where you run an ice cream empire and either become a billionaire or homeless. \n "
          "You run your ice cream empire, also known as the ice cream cart, round by round. "
          "Every round you get a chance to grow your stash of cash by buying stock (Ice Cream and Cones) "
          "and setting the price for which you want to sell your ice cream. After your input the sales "
          "are simulated resulting in a financial report detailing your stats. \n"
          "Each round costs $75 dollars for your standard expenses")


def prepare_financial_report(game_round,
                             num_ice_bought,
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

    return total


def play_game(starting_balance,
              purchase_price_ice,
              purchase_price_cone,
              operating_cost) -> None:
    """play the game"""

    game_round = 1
    current_balance = starting_balance
    game_continues = "Y"
    stock_ice_cream = 0
    stock_cones = 0

    while (current_balance >= operating_cost) & (game_continues == "Y"):
            print("The current weather today is", get_weather(), "degrees celsius \n",
                  "Your current balance is ", current_balance)

            print("Stock up your Ice ($", purchase_price_ice, "), don't forget to keep some money for the cones (max:",
                  get_max_ice_cream_sales(get_weather(), purchase_price_ice), ")")
            num_ice_bought = int(input())

            print("Stock up your Ice Cones ($", purchase_price_cone,
                  "), don't forget to keep some money for the cones (max:",
                  max_ice_cream_sales, ")")
            num_cones_bought = int(input())

            print("Set the selling price for your delicious ice creams $(x.xx)")
            selling_price = float(input())

            ice_creams_sold = get_actual_ice_cream_sales(get_weather(),
                                                        stock_ice_cream + num_ice_bought,
                                                        stock_cones + num_cones_bought)
            print("You sell", ice_creams_sold)

            current_balance = prepare_financial_report(game_round,
                                                       num_ice_bought,
                                                       purchase_price_ice,
                                                       num_cones_bought,
                                                       purchase_price_cone,
                                                       current_balance,
                                                       operating_cost,
                                                       selling_price,
                                                       ice_creams_sold)


            print("Do you want to continue (Y/N)?")
            game_continues = input(str())
            game_round += 1
            stock_ice_cream = 0

    print("Game over")


if __name__ == "__main__":
    # init(sys.argv[1:])
    start_game()
    play_game(STARTING_BUDGET,
              PURCHASE_PRICE_ICE,
              PURCHASE_PRICE_CONE,
              OPERATING_COST)
