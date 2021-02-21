# from menu_manager import MenuManager
import sqlite3 as sl
def load_manager():
    MenuManager()
    return MenuManager
   
def show_user_menu():
    print('    MENU\n (a) Add an Item \n (b) Delete item \n (c) View menu \n (d) Exit ')
    choice=input( ' ' )
    if choice== 'a':
        add_item_to_menu()
        show_user_menu()
    elif choice=='b':
        remove_item_from_menu()
        show_user_menu()
    elif choice=='c':
        show_restuarant_menu()
        show_user_menu()
    elif choice == 'd':
        menu2.save_to_file()
        print(menu2.menu)               

def add_item_to_menu():
    name =input('Name: ')
    price =input('Price: ')
    menu2.add_item(name,price)
    # print (menu2.menu)

def remove_item_from_menu():
    name=input("Name of item : ")
    menu2.remove_item(name)
    # print(menu2.menu)

def show_restuarant_menu():
    for item in menu2.menu['items']:
        print(item['name'] +': $' +str(item['price']))

class MenuItem:
    def __init__(self,item_name,item_price):
        self.item_price=item_price
        self.item_name=item_name

    def run_query(self,query):
        connection=sl.connect("restuarant_menu.db")
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()

    def save_to_db(self):
        query = f"INSERT INTO Restuarant_items (Item, Price) VALUES ('{self.item_name}', {self.item_price})"
        return self.run_query(query)
        
    def delete_from_db(self):
        query=f'DELETE FROM Restuarant_items where Item ="{self.item_name}" '
        return self.run_query(query)
        
    def update_db(self,old_item ):
        query=f"UPDATE Restuarant_items SET Item = '{self.item_name}' WHERE Item = '{old_item}'"
        self.run_query(query)
        query =f"UPDATE Restuarant_items SET Price = {self.item_price} WHERE Item = '{self.item_name}'" 
        self.run_query(query)

    def all_(self):
        query=f'select Item,Price from Restuarant_items'
        connection=sl.connect("restuarant_menu.db")
        cursor = connection.cursor()
        cursor.execute(query)
        results=cursor.fetchall()
        connection.close()
        print(list(results))
        return results
        
    @classmethod
    def get_by_name(cls,name):
        query=f'select Item from Restuarant_items where Item ="{name}" '
        connection=sl.connect("restuarant_menu.db")
        cursor = connection.cursor()
        cursor.execute(query)
        results=cursor.fetchall()
        connection.close()
        if len(results) < 1:
            print('Doesnt exist')
        else:    
            print(list(results))
        
	

# test=MenuItem('oranges',10)
# # changetest=MenuItem('chicken',25)
# # changetest.update_db('chips')
# test.get_by_name('chicken')
MenuItem.get_by_name('chicken')