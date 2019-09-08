#!/usr/bin/env python3

from .account import Account
from .util import hash_password, get_price
import views

def run():
    choice = views.welcome_menu()

    if choice == "1": #create account 
        name = views.get_username
        password = views.get_password
        hash_password = hash_password(password)
        balance = views.get_balance
        new_account = Account(username = name, hash_password = hash_password, balance = balance)
        new_account.save()
        main_menu(new_account)

    elif choice == "2": #login
        username = views.get_username()
        password = views.get_password()
        account = Account().login(username, password)

        if not account:
            views.bad_input()
        else:
            main_menu(account)

    elif choice == "3":
        return

    else:
        views.bad_input


def main_menu(account):
    while True:
        choice = views.main_menu()

        if choice == "1": #see balance & positions
            balance = account.balance
            positions = account.get_positions
            views.show_balance(balance)
            views.show_positions(positions)
            
        elif choice == "2": #deposite money
            amount = views.deposit_amount()
            account.deposit(amount)
            account.save()

        elif choice == "3": #look up stock price
            ticker = views.get_ticker()

            try:
                price = get_price(ticker)
                views.stock_price(price)

            except:
                views.bad_stock(ticker)

        elif choice == "4": #buy stock
            ticker = views.get_ticker()
            amount = views.share_tobuy()
            account.buy(ticker, amount)
            account.save()

        elif choice == "5": #sell stock
            ticker = views.get_ticker()
            amount = views.share_tobuy()
            account.sell(ticker, amount)
            account.save()

        elif choice == "6": #trade history
            trades = account.get_trades()
            views.trades(trades)

            
        elif choice == "7" :
            return
        else:
            views.bad_input()