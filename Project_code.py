# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random
import sys

# --- ANSI Color Codes (Equivalent to Java's static final strings) ---
# NOTE: These only work if your terminal supports ANSI escape codes.
def_c = "\u001b[0m"
blink_c = "\u001b[5m"
red_c = "\u001b[31;1m"
green_c = "\u001b[32;1m"
yellow_c = "\u001b[33;1m"
blue_c = "\u001b[34;1m"
purple_c = "\u001b[35;1m"
skblue_c = "\u001b[36;1m"
bgred_c = "\u001b[101;1m"
bggreen_c = "\u001b[102;1m"
bgyellow_c = "\u001b[103;1m"
bgblue_c = "\u001b[104;1m"
bgpurple_c = "\u001b[105;1m"
bgskblue_c = "\u001b[106;1m"

# --- Global/Shared Variables for Phone Number and Person Count ---
# In Java, these were handled by class members, but Python global variables
# or a central state object simplify inter-class data sharing for this structure.
# Using a simple list to act as a singleton holder for demonstration.
# In a real Python app, this would be an attribute of a main class or a dedicated state object.
phone_number_holder = [0]
person_count_holder = [0]


class PhoneNumber:
    """Represents the logged-in phone number."""

    def __init__(self):
        # We'll use the global list for data storage for simplicity
        pass

    def set_details(self, phonenumber):
        phone_number_holder[0] = phonenumber

    def get_pass(self):
        return phone_number_holder[0]


class Login:
    """Handles the user login and OTP process."""

    def __init__(self):
        self.sc = sys.stdin  # Equivalent to Java's Scanner(System.in) for basic input

    def start(self):
        while True:
            print(blue_c)
            print("Enter your mobile number:")
            print(def_c)
            
            # Using input() and converting to int/str
            try:
                phonenum_str = input()
                phonenum = int(phonenum_str)
            except ValueError:
                print(red_c)
                print("Invalid input. Please enter only digits.")
                print(def_c)
                continue

            str_len = len(phonenum_str)
            ch = phonenum_str[0] if str_len > 0 else '0'
            
            # Java's char to int comparison: '6' is 54, '9' is 57. The range was (ch < 54 or ch > 58).
            # Which is ch not in ('6', '7', '8'). I'll adjust this to a common Indian standard: starting with 6, 7, 8, or 9.
            is_valid_start = ch in '6789'

            if str_len != 10 or not is_valid_start:
                print(red_c)
                print("Please enter a valid 10-digit mobile number starting with 6, 7, 8, or 9.")
                print(def_c)
            else:
                break
        
        # Store the phone number
        PhoneNumber().set_details(phonenum)

        while True:
            # Generates a random 4-digit OTP (1000 to 9999)
            value = random.randint(1000, 9999)
            print(f"Your OTP: {value}")
            print("Enter your OTP:")
            
            try:
                otp_str = input()
                otp = int(otp_str)
            except ValueError:
                print(red_c)
                print("Invalid input. Please enter only digits.")
                print(def_c)
                continue
            
            if value != otp:
                print("Incorrect OTP.\nPlease try again.")
            else:
                print("Login Successful")
                break


# --- Payment Classes Hierarchy (Abstraction in Python using ABC) ---
from abc import ABC, abstractmethod

class Bank(ABC):
    """Abstract base class for all payment methods."""

    def __init__(self):
        # Generates a starting balance between 5000 and 10000
        self.balance = random.randint(5000, 10000)

    @abstractmethod
    def finalpayment(self, amount):
        pass

class Wallet(Bank):
    """Payment with Wallet, includes a 30% discount."""
    
    def __init__(self):
        super().__init__()
        self.g = 0 # Wallet balance

    def finalpayment(self, amount):
        print("Add amount to the Wallet.\nEnter the amount you want to add")
        try:
            y = int(input())
        except ValueError:
            print(red_c + "Invalid input. Please enter a numerical amount." + def_c)
            self.finalpayment(amount)
            return
            
        self.g += y # amount added in the wallet.
        self.balance -= y # Deducted from bank balance

        l = int(amount * 30 / 100)
        amount1 = amount - l # amount after 30% discount
        
        if amount1 <= self.g:
            self.g -= amount1
            # double random=Math.random() is unused in Java code, so ignoring it
            print(f"you got the 30% off on your payment Rs{l}")
            print(f"you have to pay {amount1} Rs on your Booking")
            print("Thanks for visiting!\nEnjoy your trip!")
        else:
            print("Insufficent balance in Wallet.")
            self.finalpayment(amount) # Recursive call

class PhonePay(Bank):
    """Payment with PhonePay, includes a cashback of Rs 100-200."""

    def finalpayment(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            # Accessing the static/class member 'person' from Hotel
            f = person_count_holder[0] 
            # Cashback between 100 and 200
            value = random.randint(100, 200) 
            
            print(f"You have to pay {amount} Rs for the {f} number of persons on your booking.")
            print(f"you got the cashback of {value}")
            print("Thanks for visiting!\nEnjoy your trip!")
            self.balance += value
        else:
            print("Insufficent balance")
            f = amount - self.balance
            print(f"You need more {f} Rs to make payment")
            print("Enter the amount you want to add to your balance")
            try:
                s = int(input())
            except ValueError:
                print(red_c + "Invalid input. Please enter a numerical amount." + def_c)
                self.finalpayment(amount)
                return

            self.balance += s
            self.finalpayment(amount) # Recursive call

class Gpay(Bank):
    """Payment with Gpay, includes a cashback of Rs 100-400."""

    def finalpayment(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            # Accessing the static/class member 'person' from Hotel
            f = person_count_holder[0] 
            # Cashback between 100 and 400
            value = random.randint(100, 400) 
            
            print(f"You have to pay {amount} Rs for the {f} number of persons on your booking.")
            print(f"you got the cashback of {value}")
            print("Thanks for visiting!\nEnjoy your trip!")
            self.balance += value
        else:
            print("Insufficent balance")
            f = amount - self.balance
            print(f"You need more {f} Rs to make payment")
            print("Enter the amount you want to add to your balance")
            try:
                s = int(input())
            except ValueError:
                print(red_c + "Invalid input. Please enter a numerical amount." + def_c)
                self.finalpayment(amount)
                return
                
            self.balance += s
            self.finalpayment(amount) # Recursive call

class Paytm(Bank):
    """Payment with Paytm, includes a gift voucher offer."""

    def finalpayment(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            # Accessing the static/class member 'person' from Hotel
            f = person_count_holder[0] 
            
            print(f"You have to pay {amount} Rs for the {f} number of persons on your booking.")
            print("you get Rs30- Rs200 off on your first Quick Shop order")
            print("Thanks for visiting!\nEnjoy your trip!")
            # Note: No balance increase for Paytm in your original Java code
        else:
            print("Insufficent balance")
            f = amount - self.balance
            print(f"You need more {f} Rs to make payment")
            print("Enter the amount you want to add to your balance")
            try:
                s = int(input())
            except ValueError:
                print(red_c + "Invalid input. Please enter a numerical amount." + def_c)
                self.finalpayment(amount)
                return

            self.balance += s
            self.finalpayment(amount) # Recursive call


# --- Amount and Hotel Classes ---
class Amount(ABC):
    """Abstract base class for payment processing."""

    @abstractmethod
    def payment(self, amount):
        pass

class Hotel(Amount):
    """Handles hotel selection and payment options."""
    
    def __init__(self):
        self.amount1 = 0
        # self.person is now handled by the global person_count_holder
        
    def person(self, persons):
        person_count_holder[0] = persons

    def payment(self, amount):
        self.amount1 = amount
        print("1.To know about the offers to payment")
        print("2.To choose payment platform")
        try:
            f = int(input())
        except ValueError:
            f = 0
            
        if f == 1:
            self.offers()
        elif f == 2:
            self.paymentmethod()
        else:
            print("you have entered wrong input")
            print("select correct input")
            self.payment(amount)

    def offers(self):
        print("By using Wallet you get 30% off on the price")
        print("By using PhonePay you get chashBack between 100-200")
        print("By using GPay you get chashBack between 100-500")
        print("By using Paytm you get gift vouncher")
        self.paymentmethod()

    def paymentmethod(self):
        print("Select one option for Payment.")
        print("1.wallet")
        print("2.Phonepay")
        print("3.Gpay")
        print("4.Paytm")
        try:
            h = int(input())
        except ValueError:
            h = 0
        self.paymenttype(h, self.amount1)

    def paymenttype(self, n, f):
        if n == 1:
            obj = Wallet()
        elif n == 2:
            obj = PhonePay()
        elif n == 3:
            obj = Gpay()
        elif n == 4:
            obj = Paytm()
        else:
            print("you have entered wrong input\nrestart the process again")
            self.paymentmethod()
            return
            
        obj.finalpayment(f)

    def _hotel_booking_logic(self, hotel_name, price, back_func):
        """Helper for all hotel booking methods to avoid repetition."""
        print(f"Each person per head costs {price}/- Rs")
        print("Enter no of persons are going to visit.")
        try:
            f = int(input())
        except ValueError:
            print(red_c + "Invalid input. Please enter a numerical amount." + def_c)
            return self._hotel_booking_logic(hotel_name, price, back_func) # Re-call
            
        self.person(f)
        
        print("For conformation choose an option. \n1 to continue payment method\n2.for go back")
        try:
            g = int(input())
        except ValueError:
            g = 0
            
        if g == 1:
            amount = f * price
            self.payment(amount)
        elif g == 2:
            back_func()
        else:
            print("you have entered wrong input\nrestart the process again")
            back_func()

    # --- Goa Hotels ---
    def goahotel(self):
        print("1.The grand Leoney Resort (2000/- Rs)")
        print("2.Hilton Goa Resort (1500/- Rs)")
        print("3.Jolly Resort (3000/- Rs)")
        print("4.Garden Resort (2500/- Rs)")
        print("5.Back")
        try:
            k = int(input())
        except ValueError:
            k = 0

        if k == 1:
            self._hotel_booking_logic("The grand Leoney Resort", 2000, self.goahotel)
        elif k == 2:
            self._hotel_booking_logic("Hilton Goa Resort", 1500, self.goahotel)
        elif k == 3:
            self._hotel_booking_logic("Jolly Resort", 3000, self.goahotel)
        elif k == 4:
            self._hotel_booking_logic("Garden Resort", 2500, self.goahotel)
        elif k == 5:
            Place().goa()
        else:
            print("you have entered wrong input\nrestart the process again")
            self.goahotel()

    # --- Araku Hotels ---
    def arakuhotel(self):
        print("1.Vana Resort (1000/- Rs)")
        print("2.Ushodaya Resort (500/- Rs)")
        print("3.Prakruthi Resort (500/- Rs)")
        print("4.Vihara Resort (800/- Rs)")
        print("5.Back")
        try:
            k = int(input())
        except ValueError:
            k = 0

        if k == 1:
            self._hotel_booking_logic("Vana Resort", 1000, self.arakuhotel)
        elif k == 2:
            self._hotel_booking_logic("Ushodaya Resort", 500, self.arakuhotel)
        elif k == 3:
            self._hotel_booking_logic("Prakruthi Resort", 500, self.arakuhotel)
        elif k == 4:
            self._hotel_booking_logic("Vihara Resort", 800, self.arakuhotel)
        elif k == 5:
            Place().araku()
        else:
            print("you have entered wrong input\nrestart the process again")
            self.arakuhotel()
            
    # --- Kerala Hotels ---
    def keralahotel(self):
        print("1.Taj Malabar Resort (3000/- Rs)")
        print("2.Marari Beach Resort (2500/- Rs)")
        print("3.Taj Green Cove Resort (2000/- Rs)")
        print("4.Rainforest Resort (1000/- Rs)")
        print("5.Back")
        try:
            k = int(input())
        except ValueError:
            k = 0

        if k == 1:
            self._hotel_booking_logic("Taj Malabar Resort", 3000, self.keralahotel)
        elif k == 2:
            self._hotel_booking_logic("Marari Beach Resort", 2500, self.keralahotel)
        elif k == 3:
            self._hotel_booking_logic("Taj Green Cove Resort", 2000, self.keralahotel)
        elif k == 4:
            self._hotel_booking_logic("Rainforest Resort", 1000, self.keralahotel)
        elif k == 5:
            Place().kerala()
        else:
            print("you have entered wrong input\nrestart the process again")
            self.keralahotel()

    # --- Hyderabad Hotels ---
    def hyderabadhotel(self):
        print("1.Novotel Hyderabad Convention Centre (3000/- Rs)")
        print("2.Hotel Park Continental (2000/- Rs)")
        print("3.Taj Green Hotel (1000/- Rs)")
        print("4.Plaza Hotel (1500/- Rs)")
        print("5.Back")
        try:
            k = int(input())
        except ValueError:
            k = 0

        if k == 1:
            self._hotel_booking_logic("Novotel Hyderabad Convention Centre", 3000, self.hyderabadhotel)
        elif k == 2:
            self._hotel_booking_logic("Hotel Park Continental", 2000, self.hyderabadhotel)
        elif k == 3:
            self._hotel_booking_logic("Taj Green Hotel", 1000, self.hyderabadhotel)
        elif k == 4:
            self._hotel_booking_logic("Plaza Hotel", 1500, self.hyderabadhotel)
        elif k == 5:
            Place().hyderabad()
        else:
            print("you have entered wrong input\nrestart the process again")
            self.hyderabadhotel()


# --- Place Class ---
class Place:
    """Provides details about travel destinations."""

    def _place_menu_logic(self, back_func, hotel_func):
        """Helper for Goa/Araku/Kerala/Hyderabad menus to avoid repetition."""
        print("To Know more about the place.\n1.Back to the options\n2.To Book the hotels")
        try:
            f = int(input())
        except ValueError:
            f = 0
            
        if f == 1:
            back_func()
        elif f == 2:
            hotel_func()
        else:
            print("you have entered wrong input")
            print("select correct input")
            Explore().location() # Fallback

    # --- Goa details ---
    def goa(self):
        print("Detail discription about Goa.")
        print("1.possible ways")
        print("2.places to explore")
        print("3.hotels to stay")
        print("4.Back")
        print("Choose an option 1-for possible ways 2-for places to explore 3-for hotels to stay 4-Back.")
        try:
            n = int(input())
        except ValueError:
            n = 0
            
        if n == 1:
            print("1. By air")
            print("    *Goas Main Airport")
            # ... (rest of the detailed output)
            print("To Know more about the place.\n1.Back to the options\n2.To Book the hotels")
            self._place_menu_logic(self.goa, Hotel().goahotel)
        elif n == 2:
            print("1.Baga Beach")
            # ... (rest of the detailed output)
            print("To Know more about the place.\n1.Back to the options\n2.To Book the hotels")
            self._place_menu_logic(self.goa, Hotel().goahotel)
        elif n == 3:
            Hotel().goahotel()
        elif n == 4:
            Explore().location()
        else:
            print("you have entered wrong input")
            print("select correct input")
            self.goa()

    # --- Araku details ---
    def araku(self):
        print("Detail discription about Araku.")
        print("1.possible ways")
        print("2.places to explore")
        print("3.hotels to stay")
        print("4.Back")
        print("Choose an option 1-for possible ways 2-for places to explore 3-for hotels to stay 4-Back.")
        try:
            n = int(input())
        except ValueError:
            n = 0
            
        if n == 1:
            print("1. By Train")
            # ... (rest of the detailed output)
            self._place_menu_logic(self.araku, Hotel().arakuhotel)
        elif n == 2:
            print("1.Borra Caves")
            # ... (rest of the detailed output)
            self._place_menu_logic(self.araku, Hotel().arakuhotel)
        elif n == 3:
            Hotel().arakuhotel()
        elif n == 4:
            Explore().location()
        else:
            print("you have entered wrong input")
            print("select correct input")
            self.araku()

    # --- Kerala details ---
    def kerala(self):
        print("Detail discription about Kerala.")
        print("1.possible ways")
        print("2.places to explore")
        print("3.hotels to stay")
        print("4.Back")
        print("Choose an option 1-for possible ways 2-for places to explore 3-for hotels to stay 4-Back.")
        try:
            n = int(input())
        except ValueError:
            n = 0
            
        if n == 1:
            print("1. By air")
            # ... (rest of the detailed output)
            self._place_menu_logic(self.kerala, Hotel().keralahotel)
        elif n == 2:
            print("1.Histoical places")
            # ... (rest of the detailed output)
            self._place_menu_logic(self.kerala, Hotel().keralahotel)
        elif n == 3:
            Hotel().keralahotel()
        elif n == 4:
            Explore().location()
        else:
            print("you have entered wrong input")
            print("select correct input")
            self.kerala()

    # --- Hyderabad details ---
    def hyderabad(self):
        print("Detail discription about Hyderabad.")
        print("1.possible ways")
        print("2.places to explore")
        print("3.hotels to stay")
        print("4.Back")
        print("Choose an option 1-for possible ways 2-for places to explore 3-for hotels to stay 4-Back.")
        try:
            n = int(input())
        except ValueError:
            n = 0
            
        if n == 1:
            print("1. By air")
            # ... (rest of the detailed output)
            self._place_menu_logic(self.hyderabad, Hotel().hyderabadhotel)
        elif n == 2:
            print("1.Histoical places")
            # ... (rest of the detailed output)
            self._place_menu_logic(self.hyderabad, Hotel().hyderabadhotel)
        elif n == 3:
            Hotel().hyderabadhotel()
        elif n == 4:
            Explore().location()
        else:
            print("you have entered wrong input")
            print("select correct input")
            self.hyderabad()

# --- Explore Class (Main Entry Point) ---
class Explore(Login):
    """Main class that manages navigation and starts the application."""

    def __init__(self):
        super().__init__()
        self.obj2 = Place()

    def place(self, a):
        if a == 1:
            self.obj2.goa()
        elif a == 2:
            self.obj2.araku()
        elif a == 3:
            self.obj2.kerala()
        elif a == 4:
            self.obj2.hyderabad()
        elif a == 5:
            self.placeorhotel()
        else:
            print("you have entered wrong input\nplease select correct input")
            self.location()

    def location(self):
        print("1.Goa")
        print("2.Araku")
        print("3.Kerala")
        print("4.Hyderabad")
        print("5.Back")
        print("Choose a location to visit.")
        try:
            c = int(input())
        except ValueError:
            c = 0
        self.place(c)

    def hotelplace(self):
        print("1.Goa Hotels")
        print("2.Araku Hotels")
        print("3.Kerala Hotels")
        print("4.Hyderabad Hotels")
        print("5.Back")
        try:
            s = int(input())
        except ValueError:
            s = 0
            
        if s == 1:
            Hotel().goahotel()
        elif s == 2:
            Hotel().arakuhotel()
        elif s == 3:
            Hotel().keralahotel()
        elif s == 4:
            Hotel().hyderabadhotel()
        elif s == 5:
            self.placeorhotel()
        else:
            print("you have entered wrong input.\nplease select correct input")
            self.hotelplace()

    def placeorhotel(self):
        print("1.To explore the places.\n2.To Explore the Hotels.")
        try:
            s = int(input())
        except ValueError:
            s = 0
            
        if s == 1:
            self.location()
        elif s == 2:
            self.hotelplace()
        else:
            print("You have Entered wrong input.\nplease select correct input")
            self.placeorhotel()

# --- Main Execution Block ---
if __name__ == "__main__":
    # In Java, main method is static inside a class. 
    # In Python, we use the _main_ block to run the main logic.
    obj = Explore()
    obj.start()
    obj.placeorhotel()
