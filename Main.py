# Date: January 2022 (17/01/22)
# Name: Andrew Matysiak
# Description: VENDING_MACHINE v0.1 --- CURRENT WIP

# NOTES:
# todo: MAINTENANCE mode create a KEY == ie len(product_list +1) etc for adding new unlisted items
# todo: all def functions into a class???
# todo: auto Alert Message when enter maintenance mode if ANY supply == 0
# todo: write statistics etc to File.
# todo: ['17-01-2023', '17-01-2023', 200, 200, 200, 200, 'Coffee', 'Cola', 'Cola', 200, 5, 5, 5, 5, 10, 50, 50, 50, 50, 200, 'Cola', 'Coffee']
#       above output after two cycles of vending...FIX

from datetime import datetime


class Machine:
    # VARIABLES:
    # =========
    product_list = {1: ["Coffee", 200, 10, "no", 5, ""],
                    2: ["Tea", 150, 8, "no", 4, ""],
                    3: ["Cola", 250, 3, "n/a", 1, ""],
                    4: ["Juice", 400, 0, "n/a", 2, ""]}

    supply_list = {1: ["Sugar", 100],
                   2: ["Coffee Beans", 100]}

    current_date = datetime.now().strftime("%d-%m-20%y")

    valid_coins = [5, 10, 20, 50, 100, 200]

    paper_money = [500, 1000, 2000, 5000, 10000]

    coin_reserve = {5: 100, 10: 100, 20: 100, 50: 100, 100: 100, 200: 100}

    current_user_transaction_record = []

    user_total_cost = 0

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
        return "{}\nPrice: ${:.2f}\nCount: {}\nOption to add sugar: {}\nTime to Prepare/Dispense: {} mins\nStirring option: '{}'\n".format(
            self.name, self.price / 100, self.count, self.sugar, self.time, self.stir)

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

    # CLASS METHODS:
    # =============
    def select(self):
        pass


# FUNCTIONS:
# =========
def display_transactions_summary(data):  # todo: create an instance of USER containing (objects, total)??
    print("*" * 66)
    print("CURRENT SELECTION(S):")

    if len(data) == 0:
        print("No current selections...")

    else:
        for i in range(len(data)):
            #user_total_cost += data[i].price
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











#  coin_reserve = {5: 100, 10: 100, 20: 100, 50: 100, 100: 100, 200: 100}

def adjust_coin_reserve(data, machine_coins, change_dispensed):          #[Date, coins, items], [machine coins (coin_reserve)], [change given (value)]]

    change_counter = []

    for i in data:
        if type(i) == int:
            machine_coins[i] += 1       # adds coins to machine reserve

    # todo: add  ... 'AND' coin_reserve[50] > 0 etc
    if change_dispensed > 0:

        if change_dispensed >= 100 and Machine.coin_reserve[100] > 0:
            change_counter.append(100)
            Machine.coin_reserve[100] -= 1
            b = change_dispensed - 100
        else:
            b = change_dispensed
#TODO add a modulus setup here for 50c
        if b >= 50 and change_dispensed >= 150 and Machine.coin_reserve[50] > 0:
            change_counter.append(50)
            Machine.coin_reserve[50] -= 1
            c = b - 50
        elif b >= 50:
            change_counter.append(50)
            Machine.coin_reserve[50] -= 1
            c = change_dispensed - 50
        else:
            c = b

        if c >= 20 and change_dispensed >= 170 and Machine.coin_reserve[20] > 0:
            d = change_dispensed - 170
            x = c // 20

            if c % 20 == 0:
                for i in range(x):
                    if Machine.coin_reserve[20] > 0:
                        change_counter.append(20)
                        Machine.coin_reserve[20] -= 1
                    d = 0
            else:
                for i in range(x):
                    if Machine.coin_reserve[20] > 0:
                        change_counter.append(20)
                        Machine.coin_reserve[20] -= 1
                d = c - (x * 20)
        elif c >= 20 and Machine.coin_reserve[20] > 0:
            x = c // 20
            for i in range(x):
                change_counter.append(20)
                Machine.coin_reserve[20] -= 1
            d = c - (x * 20)
        else:
            d = c



# TODO: continue adjusting here onwards
        if d >= 10 and change_dispensed >= 180:
            e = change_dispensed - 180
            y = d // 10

            if d % 10 == 0:
                for i in range(y):
                    change_counter.append(10)
                    e = 0
            else:
                for i in range(y):
                    change_counter.append(10)
                e = d - (y * 10)
        elif d >= 10:
            y = d // 10
            for i in range(y):
                change_counter.append(10)
            e = d - (y * 10)
        else:
            e = d

        if e >= 5:
            change_counter.append(5)
    #todo add a no coins available clause
    return change_counter


# todo: working on this function here: === 1/1 =========================================================================
def insert_coins(transactions_total):
    print("")
                                                        # TODO: do S-007 here...
    total_coins_entered = 0
    total_coin_list = []

    while total_coins_entered < transactions_total:
        print("TOTAL owing: ${:.2f}".format(Machine.user_total_cost / 100))
        print("TOTAL entered: ${:.2f}".format(total_coins_entered / 100))

        try:

            inserted_coin = input("INSERT COINS or 'R' to REFUND coins and exit PAYMENT: ").strip().lower()
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






    if total_coins_entered > transactions_total:
        change = total_coins_entered - transactions_total
        print("CHANGE GIVEN: ${:.2f}, ITEM(S) DISPENSED:".format(change / 100))

    else:
        print("CHANGE GIVEN: $0.00, ITEM(S) DISPENSED:")

    for i in Machine.current_user_transaction_record:
        print(i.name)                                       # display items after >= correct coins inserted

    for i in Machine.current_user_transaction_record:
        Machine.transaction_history.append(i.name)

    Machine.statistics.append(Machine.transaction_history.insert(0, Machine.current_date))      # create statistics transaction history



    Machine.user_total_cost = 0
    Machine.current_user_transaction_record = []




    # todo working here:



    # todo : update vending machine 'coin_reserve' ((+)inserted coins data & (-)if change is given)
    # todo : VendingMachine.transaction_history should be = [date, user_choice, items, coins_inserted]




    # todo: for testing only below
    print("TESTING ONLY...")
    print(Machine.transaction_history)                               # [Date, coins, items]
    print("data sent to coin calculator...TESTING")

    print(adjust_coin_reserve(Machine.transaction_history, Machine.coin_reserve, change))    #[Date, coins, items], [machine coins], [change given]]
    goodbye_message() #keep and un-comment later

    #todo: remove PRINT above 'print(adjust_coin_reserve(Machine.transac.....)' etc
    #exit()





# todo: working above=== insert_coin() function =======================================================================











def refund_coins(coins):
    print("Coins refunded: ")
    for i in coins:
        print("${:.2f}".format(i / 100), end=" ")   # 'end' allows horizontal printing
    if len(coins) == 0:
        print("No coins refunded as none were inserted...")
    Machine.transaction_history = []    # reset coin history

    #exit()  # delete this later







# todo ============================= working above 'insert-coins()'=====================================================


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










    # TODO: CODE BELOW ... (DISPLAYS STOCK SUPPLY) PUT this in MAINTENANCE/ADMIN display
    print()
    for i in Machine.supply_list:
        print("-) Item: {}, Count: {}".format(Machine.supply_list[i][0], Machine.supply_list[i][1]))
    # TODO: =============================================================================================












def main_menu():
    while True:
        print("")
        menu_choice = input("Please select from the following MAIN MENU (a, b, c or d):\n"
                            "a) List Products\n"
                            "b) Choose Product(s)\n"
                            "c) Transaction Records\Statistics\n"
                            "d) Customer Maintenance mode\n"
                            "> ").strip().lower()
        print("")
        if is_valid(menu_choice, ['a', 'b', 'c', 'd']):
            break

    if menu_choice == 'a':
        list_products()
        main_menu()

    elif menu_choice == 'b':
        display_transactions_summary(Machine.current_user_transaction_record)
        select_product()








    elif menu_choice == 'c':
        pass










    else:
        # menu_choice == 'd'
        pass

# TODO: Working Above =======b, c + d options=========================================================================


def select_product_menu():
    for i in Machine.product_list:
        print("{}) {}".format(i, Machine.product_list[i][0]))


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
            print("")

            if selection == 'm':
                main_menu()

            else:
                if Machine.product_list[int(selection)][2] == 0:  # Count == 0 thus NO Object of class Item will be created
                    print("Unfortunately there is 0", Machine.product_list[int(selection)][0], "remaining.\n")
                    post_selection_options(Machine.current_user_transaction_record)

                elif int(selection) == 1 and Machine.supply_list[2][1] == 0:    # if 'Coffee' chosen and 0 coffee beans...
                    print("Unfortunately there are no more COFFEE BEANS for coffee...\n")
                    continue

                elif Machine.product_list[int(selection)][2] > 0:   # create an OBJECT of class ITEM.. IF selection > 0 count value
                    Machine.product_list[int(selection)][2] -= 1    # subtracts item from product_list

                    if int(selection) == 1:                        # if choose coffee subtract coffee beans also
                        Machine.supply_list[2][1] -= 1

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

                        if (sugar_option == 'y' or sugar_option == 'yes') and Machine.supply_list[1][1] > 0:
                            current_user_item.sugar = "yes"  # adds sugar to item ie "yes"
                            Machine.supply_list[1][1] -= 1  # subtracts sugar from SUPPLY LIST

                            while True:
                                stir = input("MANUAL or AUTO stirring sugar? ").strip().lower()

                                if is_valid(stir, ['a', 'm', 'auto', 'manual']):
                                    break

                            if stir == 'a' or stir == 'auto':
                                print("Your sugar addition to", current_user_item.name, "will be AUTOMATICALLY stirred.")
                                current_user_item.stir = "AUTO"

                            else:
                                current_user_item.stir = "MANUAL"

                        elif (sugar_option == 'y' or sugar_option == 'yes') and Machine.supply_list[1][1] == 0:
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
                        Machine.supply_list[1][1] += 1

                    if data[i].name == "Coffee":           # restock Coffee Beans
                        Machine.supply_list[2][1] += 1

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
                Machine.supply_list[1][1] += 1
                Machine.supply_list[2][1] += 1
                Machine.product_list[int(last_item_selected_key)][3] = "no"


            elif int(data[-1].key_value) == 2 and data[-1].sugar == "yes":   # restocks sugar (tea)
                Machine.supply_list[1][1] += 1
                Machine.product_list[int(last_item_selected_key)][3] = "no"

            del data[-1]

        display_transactions_summary(data)
        post_selection_options(Machine.current_user_transaction_record)


def running_total_owing():
    Machine.user_total_cost = 0

    for i in range(len(Machine.current_user_transaction_record)):
        Machine.user_total_cost += Machine.current_user_transaction_record[i].price
    return Machine.user_total_cost


def restart():
    main_menu()


def turn_on():
    machine_mode = "*WORKING*"
    welcome_message(machine_mode)
    main_menu()


def wait_time():
    pass    #TODO: calc after full payment...



def welcome_message(machine_state):
    print("")
    print("=" * 61)
    print("*" * 5 + " WELCOME!!! PYTHON VENDING MACHINE: " + machine_state + " mode " + "*" * 5)
    print("=" * 61 + "\t", Machine.current_date)
# TODO: variable for: WORKING/MAINTENANCE mode

#================================================================


class Maintenance:



    def status(self, current_status):
        if current_status:
            Maintenance.state = "* MAINTENANCE *"
            Maintenance.machine_status = False
        else:
            Maintenance.state = "* WORKING *"
            Maintenance.machine_status = True



def maintenance():

    while True:
        print("*" * 44)
        print("*** Welcome to CUSTOMER MAINTENANCE mode ***")
        print("Current machine status:", Maintenance.state)
        print("Please choose from the following:")
        print("1) Change Vending Machine STATUS to WORKING/MAINTENANCE mode")
        print("2) Add Inventory")

        customer = input("> ")

        if int(customer) == 1:

            Maintenance.status(Maintenance.machine_status)

        elif int(customer) == 2:
            try:
                items = []
                #vendor = VendingMachine()
                name = input("Enter item: ")
                price = int(input("Enter price (in cents): "))
                count = int(input("Enter count of item: "))
                ingredients = input("Sugar available?: ")
                items.append(name)
                items.append(price)
                items.append(count)
                items.append(ingredients)
                print(items)

            except ValueError:
                print("please enter a valid number...")
        else:
            continue


maintenance()




# =============================================== MAIN BODY BELOW =====================================================

turn_on()

