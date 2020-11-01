import random
from game_files.game_config import (STARTING_BUDGET,
                                    PURCHASE_PRICE_ICE,
                                    PURCHASE_PRICE_CONE,
                                    OPERATING_COST)


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
                 starting_budget=STARTING_BUDGET,
                 purchase_price_ice=PURCHASE_PRICE_ICE,
                 purchase_price_cone=PURCHASE_PRICE_CONE,
                 operating_cost=OPERATING_COST):
        """
        Initializes a game with the values provided from the config
        """
        self.starting_budget = starting_budget
        self.purchase_price_ice = purchase_price_ice
        self.purchase_price_cone = purchase_price_cone
        self.operating_cost = operating_cost


class GameRound(Game):
    """
    A Position represents a location in a two-dimensional room.
    """

    def __init__(self):
        super().__init__()
        self.temperature = None
        self.stock_ice_cream = None
        self.stock_cones = None

    def get_weather(self):
        """Weather Is randomly generated integer between -10 and 40"""
        self.temperature = random.randint(-10, 40)
        return self.temperature

    def get_current_balance(self, current_balance):  # not sure
        self.current_balance = current_balance

    def ask_num_ice_to_buy(self, current_balance):

        print("The current weather today is", get_weather(), "degrees celsius \n",
              "Your current balance is ", current_balance)

        print("Stock up your Ice ($", self.purchase_price_ice, "), don't forget to keep some money for the cones (max:",
              self.get_max_ice_cream_purchase(), ")")

        num_ice_bought = int(input())

        return num_ice_bought

    def ask_num_cones_to_buy(self):
        print("Stock up your Ice Cones ($", self.purchase_price_cone,
              "), don't forget to keep some money for the cones (max:",
              self.purchase_price_cone, self.get_max_ice_cream_purchase(), ")")

        num_cones_bought = int(input())

        return num_cones_bought

    @staticmethod
    def ask_selling_price():
        print("Set the selling price for your delicious ice creams $(x.xx)")
        selling_price = float(input())
        return selling_price

    def get_max_ice_cream_sales(self):
        """Formula for maximum sales of ice cream during a day"""
        return 1000 * get_weather() * (10 - self.ask_selling_price())

    def get_current_ice_stock(self, current_balance):
        self.stock_ice_cream + self.ask_num_ice_to_buy(current_balance)

    def get_current_cone_stock(self):
        self.stock_cones + self.ask_num_cones_to_buy()

    def get_max_ice_cream_purchase(self):
        return (self.starting_budget - self.operating_cost) / (self.purchase_price_ice + self.purchase_price_cone)

    def get_actual_ice_cream_sales(self):
        """Formula for maximum sales of ice cream during a day"""
        return min(self.get_max_ice_cream_purchase, self.get_current_ice_stock(), self.get_current_cone_stock())

    def prepare_financial_report(self):
        ice_expenses = self.purchase_price_ice * self.ask_num_ice_to_buy()
        cone_expenses = self.purchase_price_cone * self.ask_num_cones_to_buy()
        income = self.ask_selling_price() * self.get_actual_ice_cream_sales()
        total = self.get_current_balance() - self.operating_cost - ice_expenses - cone_expenses + income

        print("==============================================\n",
              "=============Finances Round", self.game_round, "===============\n",
              "=============================================\n",
              "Starting Money", self.get_current_balance(), "\n",
              "Operating Cost", self.operating_cost, "\n",
              "Ice Cream Expenses", ice_expenses, "\n",
              "Cone Expenses", cone_expenses, "\n",
              "Income", income, "\n",
              "=============================================\n",
              "Total", total, "\n")

        return total

    def game_continues(self):
        print("Do you want to continue (Y/N)?")
        game_continues = input(str())
        return game_continues


def play_game(starting_budget):
    print("Welcome to 'You Cone Do It!' "
          "where you run an ice cream empire and either become a billionaire or homeless. \n "
          "You run your ice cream empire, also known as the ice cream cart, round by round. "
          "Every round you get a chance to grow your stash of cash by buying stock (Ice Cream and Cones) "
          "and setting the price for which you want to sell your ice cream. After your input the sales "
          "are simulated resulting in a financial report detailing your stats. \n"
          "Each round costs $75 dollars for your standard expenses")

    game = Game()
    game_round = GameRound()
    current_balance = game.starting_budget
    game_round_num = 1
    game_continues = "Y"
    stock_ice_cream = 0
    stock_cones = 0

    while (game_round.get_current_balance >= game_round.operating_cost) & (game_round.game_continues == "Y"):
        print("The current weather today is", game_round.get_weather(), "degrees celsius \n",
              "Your current balance is ", current_balance)

        game_round.ask_num_ice_to_buy()

        game_round.ask_num_cones_to_buy()

        game_round.ask_selling_price()

        print("You sell", game_round.get_actual_ice_cream_sales())

        game_round.prepare_financial_report()

        current_balance = game_round.prepare_financial_report()

        print("Do you want to continue (Y/N)?")
        game_continues = input(str())

        game_round_num += 1
        stock_ice_cream = 0


if __name__ == "__main__":
    play_game()
