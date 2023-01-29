# Date: January 2022 (17/01/22)
# Name: Andrew Matysiak
# Description: VENDING_MACHINE v0.1 --- CURRENT WIP

# NOTES:
# todo: SUPPLY_LIST DICTIONARY IS READ FROM A FILE...
# todo: all def functions into a class???
# todo: if machine in * MAINTENANCE * mode display message must be changed by ADMIN to continue...
# todo: At the beginning of each function, there is a string within triple quotation marks, called a docstring.
#       It is used to explain how the function behaves. Style of the docstring can be found in PEP 257 Docstring
#       Conventions.
# todo: When select to restock items and (item selected to restock) incorrect input, program goes back to 'enter number to restock'
# todo: rename variables in: adjust_coins_reserve function
# todo: check restart() function



from datetime import datetime


class Machine:
    # VARIABLES:
    # =========
    product_list = {1: ["Coffee", 200, 10, "no", 3, ""],
                    2: ["Tea", 150, 8, "no", 2, ""],
                    3: ["Cola", 250, 3, "n/a", 1, ""],
                    4: ["Juice", 400, 0, "n/a", 1, ""]}

    supply_list = {5: ["Sugar", 100],
                   6: ["Coffee Beans", 100]}

    current_date = datetime.now().strftime("%d-%m-20%y")

    valid_coins = [5, 10, 20, 50, 100, 200]

    paper_money = [500, 1000, 2000, 5000, 10000]

    coin_reserve = {5: 10, 10: 10, 20: 10, 50: 10, 100: 10, 200: 10}

    current_user_transaction_record = []

    user_total_cost = 0

    machine_state = "* WORKING *"

    statistics = []

    transaction_history = []


# CLASSES:
# =======
class Item:

    def __init__(self, name, price, count, sugar, time, stir, key_value):
        self.name = name
        self.price = price
        self.count = count
        self.sugar = sugar
        self.time = time
        self.stir = stir
        self.key_value = key_value



    # CLASS CONSTRUCTOR:
    # =================
    # todo: this def __str__ may have to be altered


    def __str__(self):  # print object if 'print(object_name instance of class Item)'
        return "{}\nPrice: ${:.2f}\nCount: {}\nOption to add sugar: {}\nTime to Prepare/Dispense: {}" \
               " mins\nStirring option: '{}'\n".format(self.name, self.price / 100, self.count,
                                                       self.sugar, self.time, self.stir)

    # CLASS METHODS:
    # =============
    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_count(self):
        return self.count

    def get_sugar(self):
        return self.sugar

    def get_time(self):
        return self.time

    def get_stir(self):
        return self.stir

    def get_key(self):
        return self.key_value


class User:

    # CLASS INSTANCE VARIABLES:
    # ==================
    def __init__(self, selections, total_owed):
        self.selections = selections
        self.total_owed = total_owed

    def __str__(self):
        return "{}\nPrice: ${:.2f}\n".format(self.selections, self.total_owed / 100)


# FUNCTIONS:
# =========
def adjust_coin_reserve(data, machine_coins, change_dispensed):          #[Date, coins, items], [machine coins (coin_reserve)], [change given (value)]]

    change_counter = []

    for i in data:
        if type(i) == int:
            machine_coins[i] += 1       # adds coins to machine reserve

    if change_dispensed > 0:
        # 100c
        if change_dispensed >= 100 and Machine.coin_reserve[100] > 0:
            Machine.coin_reserve[100] -= 1
            change_counter.append(100)
            b = change_dispensed - 100
        else:
            b = change_dispensed

        # 50c
        x = b // 50     # x = number of times 50c can go into change remaining (b)
        if b >= 50 and Machine.coin_reserve[50] >= x:    # here have enough 50c for ALL calcs

            for i in range(x):
                Machine.coin_reserve[50] -= 1
                change_counter.append(50)
                b -= 50

        elif b >= 50 and Machine.coin_reserve[50] <= x:     # here DON'T have enough 50c for calcs
            for i in range(Machine.coin_reserve[50]):
                Machine.coin_reserve[50] -= 1
                change_counter.append(50)
                b -= 50

        # 20c
        y = b // 20  # y = number of times 20c can go into change remaining (b)
        if b >= 20 and Machine.coin_reserve[20] >= y:  # here have enough 20c for ALL calcs

            for i in range(y):
                Machine.coin_reserve[20] -= 1
                change_counter.append(20)
                b -= 20

        elif b >= 20 and Machine.coin_reserve[20] <= y:  # here DON'T have enough 20c for calcs
            for i in range(Machine.coin_reserve[20]):
                Machine.coin_reserve[20] -= 1
                change_counter.append(20)
                b -= 20

        # 10c
        z = b // 10  # z = number of times 10c can go into change remaining (b)
        if b >= 10 and Machine.coin_reserve[10] >= z:  # here have enough 10c for ALL calcs

            for i in range(z):
                Machine.coin_reserve[10] -= 1
                change_counter.append(10)
                b -= 10

        elif b >= 10 and Machine.coin_reserve[10] <= z:  # here DON'T have enough 10c for calcs
            for i in range(Machine.coin_reserve[10]):
                Machine.coin_reserve[10] -= 1
                change_counter.append(10)
                b -= 10

        # 5c
        w = b // 5  # w = number of times 5c can go into change remaining (b)
        if b >= 5 and Machine.coin_reserve[5] >= w:  # here have enough 5c for ALL calcs
            for i in range(w):
                Machine.coin_reserve[5] -= 1
                change_counter.append(5)
                b -= 5

        elif b >= 5 and Machine.coin_reserve[5] <= w:
            print("Unfortunately Vending Machine does not contain enough coins to give CORRECT change.. Contact Admin/Maintenance mode to restock...")

            print(Machine.coin_reserve) # todo: for TEST remove (coins returned if not enough change)
            for i in change_counter:
                Machine.coin_reserve[i] += 1        # coins of 'change-bucket' are returned to coin_reserve
            print(Machine.coin_reserve) # todo: for TEST remove (coins returned if not enough change)

            change_counter = ["No change given...<No change available in Vending Machine"] # coin values List is replaced with message

    elif change_dispensed == 0:
        change_counter = ["No change given...<Correct coins were inserted>"]

    return change_counter


def display_coin_reserve():
    print("")
    print("*" * 5 + " Current Coin Reserve " + "*" * 5)
    for i, j in Machine.coin_reserve.items():
        print("${:.2f}:\t\t{}".format(i / 100, j))
    print("")


def display_supply_list():
    print("")
    print("*" * 5 + " Current Ingredient Supply " + "*" * 5)

    for i in Machine.supply_list:
        print("{}) Item: {}, Count: {}".format(i, Machine.supply_list[i][0], Machine.supply_list[i][1]))
    print("")


def display_transactions_summary(data):  # todo: create an instance of USER containing (objects, total)??
    print("*" * 66)
    print("CURRENT SELECTION(S):")

    if len(data) == 0:
        print("No current selections...")

    else:
        for i in range(len(data)):
            # user_total_cost += data[i].price
            if data[i].name == 'Tea':
                print("{}\t\t\t\t\t${:.2f}\t\tadd sugar: {}".format(data[i].name, data[i].price / 100, data[i].sugar))
                # VendingMachine.total_cost += i[2]
            else:
                print("{}\t\t\t\t${:.2f}\t\tadd sugar: {}".format(data[i].name, data[i].price / 100, data[i].sugar))
                # VendingMachine.total_cost += i[2]


def goodbye_message():
    print("")
    print("=" * 61)
    print("*" * 5 + " THANKYOU for using PYTHON VENDING MACHINE... GOODBYE!!! ")
    print("=" * 61)

    turn_on()


def insert_coins(transactions_total):
    print("")
    total_coins_entered = 0
    total_coin_list = []
    change = 0

    while total_coins_entered < transactions_total:
        print("TOTAL owing: ${:.2f}".format(Machine.user_total_cost / 100))
        print("TOTAL entered: ${:.2f}".format(total_coins_entered / 100))

        try:

            inserted_coin = input("INSERT COINS or 'R' to REFUND coins/EXIT payment: ").strip().lower()
            print("")
            if inserted_coin == 'r':
                refund_coins(Machine.transaction_history)   # argument is a list of string numbers
                print("\n")

                display_transactions_summary(Machine.current_user_transaction_record)
                post_selection_options(Machine.current_user_transaction_record)     # this procedure is to go back out of coin insertion mode

            elif Machine.valid_coins.count(int(inserted_coin)) > 0:  # check if valid coin entered
                total_coins_entered += int(inserted_coin)
                Machine.transaction_history.append(int(inserted_coin))
                total_coin_list += str(total_coins_entered)

            elif Machine.paper_money.count(int(inserted_coin)) > 0:
                print("This machine does not accept PAPER MONEY!!!")

            else:
                print("Only coins of the following denomination are accepted: (in cents)")
                for i in Machine.valid_coins:
                    print("${:.2f}".format(i / 100), end=" ")
                print("\n")

        except ValueError:
            print("Please enter a valid coin 'cents value' or press 'R' to refund...")

    print("TOTAL: ${:.2f}".format(total_coins_entered / 100))
    print("")

    if total_coins_entered >= transactions_total:
        change = total_coins_entered - transactions_total
        print("CHANGE OWED: ${:.2f}".format(change / 100))

    print("Wait Time is", wait_time(Machine.current_user_transaction_record), "min(s)...")
    print("ITEM(S) DISPENSED:")

    for i in Machine.current_user_transaction_record:
        print(i.name)                                       # dispense items after >= correct coins inserted

    for i in Machine.current_user_transaction_record:
        Machine.transaction_history.append(i.name)

    Machine.transaction_history.insert(0, Machine.current_date)
    Machine.statistics.append(Machine.transaction_history)

    Machine.user_total_cost = 0                     # reset after dispense
    Machine.current_user_transaction_record = []    # reset after dispense

    if change == 0:
        print("$0.00 change")

    else:
        for i in (adjust_coin_reserve(Machine.transaction_history, Machine.coin_reserve, change)):   #[Date, coins, items], [machine coins], [change given]]
            print("${:.2f}".format(i / 100))

    Machine.transaction_history = []
    goodbye_message()


def is_valid(data, choices):  # choices are in a list
    if data in choices:
        return True
    print("Please enter a valid choice...")
    return False


def list_products():
    print("")
    print("*" * 7 + " CURRENT PRODUCT LIST " + "*" * 7)
    for i in Machine.product_list:
        if Machine.product_list[i][2] > 0:
            print("{}) Item: {}, Count: {}, Price: ${:.2f}".format(i, Machine.product_list[i][0],
                                                                   Machine.product_list[i][2],
                                                                   Machine.product_list[i][1] / 100))
        else:
            print("{}) Item: {}, Count: UNAVAILABLE,  Price: ${:.2f}".format(i, Machine.product_list[i][0],
                                                                             Machine.product_list[i][1] / 100))


def main_menu():
    while True:
        print("")
        menu_choice = input("Please select from the following MAIN MENU (a, b, or c):\n"
                            "a) List Products\n"
                            "b) Choose Product(s)\n"
                            "c) Customer Maintenance mode\n"
                            "> ").strip().lower()
        print("")
        if is_valid(menu_choice, ['a', 'b', 'c']):
            break

    if menu_choice == 'a':
        list_products()
        main_menu()

    elif menu_choice == 'b':
        display_transactions_summary(Machine.current_user_transaction_record)
        select_product()

    else:
        welcome_customer()
        maintenance()


def maintenance():
    while True:
        print("")
        print("Please choose from the following:\n")
        print("a) Add Coins to machine coin reserve")
        print("b) Add Product to inventory")
        print("c) Transaction Statistical Data")
        print("d) Set Machine to WORKING/MAINTENANCE state")
        print("r) RESET Machine")
        print("m) Return to MAIN MENU")

        customer = input("> ").strip().lower()

        if is_valid(customer, ['a', 'b', 'c', 'd', 'm', 'r']):
            break

    if customer == 'a':

        display_coin_reserve()

        while True:
            try:
                restock = input("Enter a valid coin denomination to restock (in cents), 'M' to return to CUSTOMER MENU: ").strip().lower()
                if restock == 'm':
                    maintenance()

                elif int(restock) in Machine.coin_reserve.keys():
                    coin_amount = int(input("Coin found...Enter number of ${:.2f} coins to stock: ".format(int(restock) / 100)))
                    print("RESTOCKING...")
                    Machine.coin_reserve[int(restock)] += coin_amount
                    display_coin_reserve()

                else:
                    print("Please enter a valid coin denomination...(5, 10, 20, 50, 100, 200)")

            except ValueError:
                print("Please enter an integer number...")

    elif customer == 'b':

        while True:
            list_products()
            display_supply_list()
            try:
                restock = input("Enter item number (1-6) to restock, 'M' to return to CUSTOMER/ADMIN MENU: ").strip().lower()
                if restock == 'm':
                    maintenance()

                elif int(restock) in Machine.product_list:
                    print("You have chosen:", Machine.product_list[int(restock)][0])
                    count = int(input("Enter amount of " + Machine.product_list[int(restock)][0] + " to restock: "))
                    Machine.product_list[int(restock)][2] += count
                    print("RESTOCKING...")

                elif int(restock) in Machine.supply_list:
                    print("You have chosen:", Machine.supply_list[int(restock)][0])
                    count = int(input("Enter amount of " + Machine.supply_list[int(restock)][0] + " to restock: "))
                    Machine.supply_list[int(restock)][1] += count
                    print("RESTOCKING...")

            except ValueError:
                print("Please enter an integer number...")

    elif customer == 'c':
        print("")
        print("*" * 24 + " STATISTICS " + "*" * 24)
        print("Writing TRANSACTION HISTORY to file...")     # del this line

        # WRITE:
        file_statistics = open("transactions.txt", "w")
        for i in Machine.statistics:
            file_statistics.writelines(" \n")

            file_statistics.writelines("Date: {}\n".format(i[0]))
            for j in i[1:]:
                if type(j) == str:
                    file_statistics.writelines("Item purchased: {}\n".format(j))
                else:
                    file_statistics.writelines("Coin(s) inserted: ${:.2f}\n".format(j / 100))
        file_statistics.close()

        # READ:
        file_statistics = open("transactions.txt", "r")
        print(file_statistics.read())
        file_statistics.close()

        maintenance()

    elif customer == 'd':
        if Machine.machine_state == "* WORKING *":
            Machine.machine_state = "* MAINTENANCE *"
            welcome_customer()
            maintenance()

        else:
            Machine.machine_state = "* WORKING *"
            welcome_customer()
            maintenance()

    elif customer == 'r':
        Machine.transaction_history.clear()
        Machine.statistics.clear()
        turn_on()

    else:
        main_menu()


def post_selection_options(data):  # data = current_user_transaction_record (List of Item OBJECTS)
    while True:
        choice = input("Select 'P' to PAY, 'C' to CONTINUE BUYING, 'X' to rollback CURRENT transaction ('R' to RESTART all transactions and clear history): ").strip().lower()
        print("")
        if is_valid(choice, ['p', 'c', 'x', 'r']):
            break

    if choice == 'r':
        while True:
            confirmation = input("Do you wish to 'Y' CANCEL all transaction(s) or 'N' continue BUYING...").strip().lower()  # todo: is this S-007??
            if confirmation == 'y':
                for i in range(len(data)):
                    unselect = data[i].key_value
                    Machine.product_list[int(unselect)][2] += 1                 # restock ie unselect all items
                    Machine.product_list[int(unselect)][3] = "no"

                    if data[i].sugar == "yes":                      # restock all sugar if item had sugar selected as 'yes' (from tea + coffee) (HARD RESET OPTION)
                        Machine.supply_list[5][1] += 1

                    if data[i].name == "Coffee":           # restock Coffee Beans
                        Machine.supply_list[6][1] += 1

                Machine.current_user_transaction_record = []        # clear cache -- remove all transaction objects
                restart()

            elif confirmation == 'n':
                display_transactions_summary(Machine.current_user_transaction_record)
                break

    elif choice == 'p':
        running_total_owing()
        display_transactions_summary(data)              # need to add final item in bucket, 'cost' to total owing
        insert_coins(Machine.user_total_cost)

    elif choice == 'c':                     # pressing 'c' LOCKS-IN the price of item in BUCKET
        print("running TOTAL owing: ${:.2f}".format(running_total_owing() / 100))
        select_product()

    else:
        # user has chosen 'X'                                   # this is U-007
        if len(data) == 0:   # only for if 1st choice was not available and try  to 'X' rollback -SOLVED delete??
            print("WARNING: You have no items selected...")

        elif len(data) > 0:  # if there is at least 1 Object item in List....
            last_item_selected_key = data[-1].key_value                     # data = current_user_transaction_record
            Machine.product_list[int(last_item_selected_key)][2] += 1       # restock item

            if int(data[-1].key_value) == 1 and data[-1].sugar == "yes":    # restocks sugar + coffee beans (coffee) and changes productlist back to "no"
                Machine.supply_list[5][1] += 1
                Machine.supply_list[6][1] += 1
                Machine.product_list[int(last_item_selected_key)][3] = "no"

            elif int(data[-1].key_value) == 2 and data[-1].sugar == "yes":   # restocks sugar (tea)
                Machine.supply_list[5][1] += 1
                Machine.product_list[int(last_item_selected_key)][3] = "no"

            del data[-1]

        display_transactions_summary(data)
        post_selection_options(Machine.current_user_transaction_record)


def refund_coins(coins):
    print("Coins refunded: ")
    for i in coins:
        print("${:.2f}".format(i / 100), end=" ")   # 'end' allows horizontal printing
    if len(coins) == 0:
        print("No coins refunded as none were inserted...")
    Machine.transaction_history = []    # reset coin history


def restart():
    main_menu()


def running_total_owing():
    Machine.user_total_cost = 0

    for i in range(len(Machine.current_user_transaction_record)):
        Machine.user_total_cost += Machine.current_user_transaction_record[i].price
    return Machine.user_total_cost


def select_product():
    while True:

        print("")
        print("*" * 23)
        print("*" * 5 + " Select Item " + "*" * 5)
        print("*" * 23)

        select_product_menu()

        try:

            selection = input("Choose an item (1-" + str(len(Machine.product_list)) +
                              "), or ('M' to return to *** MAIN MENU ***): ").strip().lower()

            if selection == 'm':
                main_menu()

            else:
                if Machine.product_list[int(selection)][2] == 0:  # Count == 0 thus NO Object of class Item will be created
                    print("Unfortunately there is 0", Machine.product_list[int(selection)][0], "remaining.\n")
                    post_selection_options(Machine.current_user_transaction_record)

                elif int(selection) == 1 and Machine.supply_list[6][1] == 0:    # if 'Coffee' chosen and 0 coffee beans...
                    print("Unfortunately there are no more COFFEE BEANS for coffee...\n")
                    continue

                elif Machine.product_list[int(selection)][2] > 0:   # create an OBJECT of class ITEM.. IF selection > 0 count value
                    Machine.product_list[int(selection)][2] -= 1    # subtracts item from product_list

                    if int(selection) == 1:                        # if choose coffee subtract coffee beans also
                        Machine.supply_list[6][1] -= 1

                    current_user_item = Item(Machine.product_list[int(selection)][0],
                                             Machine.product_list[int(selection)][1],
                                             Machine.product_list[int(selection)][2],
                                             Machine.product_list[int(selection)][3],
                                             Machine.product_list[int(selection)][4],
                                             Machine.product_list[int(selection)][5],
                                             selection)  # an instance of chosen item

                    # if Tea or Coffee...Sugar is available for this item...
                    if int(selection) == 1 or int(selection) == 2:
                        while True:
                            print("Add sugar to", current_user_item.name, "?")
                            sugar_option = input("(Y/N): ").strip().lower()

                            if is_valid(sugar_option, ['y', 'n', 'yes', 'no']):
                                break

                        if (sugar_option == 'y' or sugar_option == 'yes') and Machine.supply_list[5][1] > 0:
                            current_user_item.sugar = "yes"  # adds sugar to item ie "yes"
                            Machine.supply_list[5][1] -= 1  # subtracts sugar from SUPPLY LIST

                            while True:
                                stir = input("MANUAL or AUTO stirring sugar? ").strip().lower()

                                if is_valid(stir, ['a', 'm', 'auto', 'manual']):
                                    break

                            if stir == 'a' or stir == 'auto':
                                print("Your sugar addition to", current_user_item.name, "will be AUTOMATICALLY stirred.")
                                current_user_item.stir = "AUTO"

                            else:
                                current_user_item.stir = "MANUAL"

                        elif (sugar_option == 'y' or sugar_option == 'yes') and Machine.supply_list[5][1] == 0:
                            print("Unfortunately Vending Machine is OUT OF SUGAR...")

                    Machine.current_user_transaction_record.append(current_user_item)              # this will be a list == [[transaction object 1], [...], [...]]
                    display_transactions_summary(Machine.current_user_transaction_record)

                    print("")
                    post_selection_options(Machine.current_user_transaction_record)

        except KeyError:
            print("Please enter a valid NUMBER within range...")
            select_product()

        except ValueError:
            print("Please enter a valid NUMBER integer...")
            select_product()


def select_product_menu():
    for i in Machine.product_list:
        print("{}) {}".format(i, Machine.product_list[i][0]))


def turn_on():
    welcome_message(Machine.machine_state)
    main_menu()


def wait_time(data):
    wait = 0
    for i in data:
        wait += i.time
    return wait


def welcome_customer():
    print("")
    print("*" * 59)
    print("***** Welcome to CUSTOMER ADMIN:", Machine.machine_state, "mode *****")
    print("*" * 59 + "\t\t", Machine.current_date)
    print("")
    for i in Machine.product_list:
        if Machine.product_list[i][2] == 0:
            print("WARNING!!! Item:", Machine.product_list[i][0], "has 0 stock available...")

    for i in Machine.supply_list:
        if Machine.supply_list[i][1] == 0:
            print("WARNING!!! Ingredient Item:", Machine.supply_list[i][0], "has 0 stock available...")


def welcome_message(machine_state):
    print("")
    print("=" * 63)
    print("*" * 5 + " WELCOME!!! PYTHON VENDING MACHINE: " + machine_state + " mode " + "*" * 5)
    print("=" * 63 + "\t\t", Machine.current_date)






# todo 1/1: The program should have an option for the admin to set the machine mode for example whether the machine is
#  working or under maintenance. The message should be displayed to the user.




# =============================================== MAIN BODY BELOW =====================================================


turn_on()

