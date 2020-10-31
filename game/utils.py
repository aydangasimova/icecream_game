import random

def get_weather():
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

class Game(object):

    def __init__(self,
                 starting_budget,
                 purchase_price_ice,
                 purchase_price_cone,
                 operating_cost):
        """
        Initializes a game with the values provided from the config
        """
        self.starting_budget = starting_budget
        self.purchase_price_ice = purchase_price_ice
        self.purchase_price_cone = purchase_price_cone
        self.operating_cost = operating_cost

        self.game_round = 1
        self.game_continues = "Y"
        self.stock_ice_cream = 0
        self.stock_cones = 0

    def get_max_ice_cream_sales(self):
        """Formula for maximum sales of ice cream during a day"""
        return 1000 * get_weather() * (10 - price)

    def get_actual_ice_cream_sales(max_ice_cream_sales: float, stock_ice_cream: int, stock_cones: int) -> float:
        """Formula for maximum sales of ice cream during a day"""
        return min(max_ice_cream_sales, stock_ice_cream, stock_cones)

    def get_current_budget(self):

    def get_max_ice_cream_purchase(self):
        return (self.starting_budget - self.operating_cost)/(self.purchase_price_ice+self.purchase_price_cone)

class GameRound(Game):
    """
    A Position represents a location in a two-dimensional room.
    """

    def ask_num_ice_to_buy(self):
        current_balance = self.starting_budget

        print("The current weather today is", get_weather(), "degrees celsius \n",
              "Your current balance is ", current_balance)

        print("Stock up your Ice ($", self.purchase_price_ice, "), don't forget to keep some money for the cones (max:",
              self.get_max_ice_cream_purchase(), ")")
        num_ice_bought = int(input())

        return num_ice_bought

    def ask_num_cones_to_buy(self):
        print("Stock up your Ice Cones ($", self.purchase_price_cone,
              "), don't forget to keep some money for the cones (max:",
              self.purchase_price_cone, self.get_max_ice_cream_purchase(),")")
        num_cones_bought = int(input())

        return num_cones_bought

    def ask_selling_price(self):
        print("Set the selling price for your delicious ice creams $(x.xx)")
        selling_price = float(input())
        return selling_price

    def get_ice_creams_sold(self):
        ice_creams_sold = self.get_actual_ice_cream_sales(get_weather(),
                                                     self.stock_ice_cream + self.ask_num_ice_to_buy(),
                                                     self.stock_cones + self.ask_num_cones_to_buy())
        print("You sell", ice_creams_sold)

        return ice_creams_sold

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


def play_game():
    start_game()
