

## 🌟 1. Project Overview: CLI Booking System

This project is a Command-Line Interface (CLI) application designed to simulate a simple *travel and hotel booking system. It demonstrates fundamental **Object-Oriented Programming (OOP)* concepts, including inheritance, abstraction, polymorphism, and user input validation, specifically within the context of a robust class structure.

The user can log in via an OTP process, explore various destinations (Goa, Araku, Kerala, Hyderabad), check hotel prices, and complete payments using different virtual banking/wallet methods, each offering unique incentives (discounts, cashback, vouchers).

### Key Features

  * *Secure Login:* OTP generation and validation.
  * *Destination & Hotel Exploration:* Detailed information on places and specific hotel listings with pricing.
  * *Polymorphic Payment System:* An abstract Bank class implemented by Wallet, PhonePay, Gpay, and Paytm to handle different transaction logics and offers.
  * *Offer Integration:* Payments automatically calculate offers (e.g., 30% wallet discount, variable cashback).
  * *Input Validation:* Checks for 10-digit mobile numbers and handles invalid menu choices.

-----

## 🚀 2. Technology Stack & Prerequisites

| Technology | Purpose |
| :--- | :--- |
| *Primary Language* | Java (Original) / *Python 3* (Converted) |
| *Libraries* | *None* (Pure Python Standard Library) |
| *OOP Concepts* | Inheritance, Abstraction (Bank, Amount), Polymorphism |
| *I/O & UX* | input(), print(), random, and *ANSI Color Codes* for enhanced terminal output. |

### Installation and Running the Project

Since this project uses only the Python Standard Library, there are no special dependencies to install.

1.  *Clone the repository:*
    bash
    git clone [Your-Repo-URL]
    cd simple-booking-system
    
2.  *Run the application:*
    bash
    python booking_system.py
    

-----

## 💡 3. OOP & Code Explanation

The project is structured around several classes that model the real-world components of a booking system.

| Class | Description | OOP Role |
| :--- | :--- | :--- |
| Login | Handles user authentication via mobile number validation and a 4-digit OTP challenge. | Input Handling |
| Bank | *Abstract Base Class* (ABC) defining the required finalpayment() method. It holds the generic balance attribute. | Abstraction / Inheritance |
| Wallet, PhonePay, Gpay, Paytm | *Concrete classes* extending Bank. Each implements a unique finalpayment() method to apply specific logic (discounts, various cashbacks) to demonstrate *Polymorphism*. | Polymorphism / Business Logic |
| Amount | *Abstract Base Class* defining the payment() method. | Abstraction |
| Hotel | Extends Amount. Manages hotel listing, person count, cost calculation, and initiates the payment flow by calling payment(). | Logic / Data Management |
| Place | Provides descriptive details (ways to reach, places to explore) for each destination. | Information Retrieval |
| Explore | The main driver class. Initializes the application and guides the user between exploring places and hotels. | Application Controller |

### Code Details

  * *Global State Management:* Instead of complex dependency injection, key data like the logged-in phone number and the number of persons booked (person_count_holder) are managed using a global list, simulating shared static variables from the original Java structure.
  * *UX (ANSI Colors):* Color codes are defined at the top and used liberally (red_c, blue_c) to improve the terminal user experience and highlight prompts, errors, and success messages.

-----

## 🚧 4. Challenges Faced & Solutions

This project, especially during the conversion from Java to Python, presented several challenges:

### 1\. Java Static vs. Python State

  * *Challenge:* The original Java code heavily relied on static variables (e.g., the person count in the Hotel class) and static imports for utilities. Python's equivalent often requires careful management of global or class-level attributes.
  * *Solution:* Global list variables (phone_number_holder, person_count_holder) were used to mimic the shared, accessible nature of Java's static fields without violating encapsulation too severely.

### 2\. Recursive Function Calls for Flow Control

  * *Challenge:* The original Java code used heavy recursion (e.g., in Login.start() or Bank.finalpayment()) to handle loops and retry logic (e.g., "Insufficient balance, please add funds"). This can quickly lead to a *Stack Overflow Error* in Python if user input is repeatedly invalid.
  * *Solution:* Where practical, the logic was refactored to use standard Python while loops (e.g., in Login.start()) instead of deep recursion, making the program more stable and memory-safe.

### 3\. Syntax Migration Errors

  * *Challenge:* Transcribing code from one language to another inevitably introduces syntax errors.
      * *Apostrophe in Strings:* Single quotes inside double-quoted strings (e.g., Goa's) caused Python's SyntaxError: unterminated string literal.
      * *Main Block Typo:* The Java main method concept was mistranslated as if name == "main": instead of the required **if __name__ == "__main__":**, leading to a NameError.
  * *Solution:* Applying precise corrections (Goa\\'s and __name__) ensures correct program execution and adherence to Python standards.

-----

## 🤝 5. Contribution

Feel free to fork this repository and submit pull requests. Future improvements could include:

  * Adding more destinations and hotels.
  * Implementing proper database or file storage for user/hotel data instead of in-memory state.
  * Using a library like colorama for cross-platform ANSI color support.
  * Introducing a base User class for better state management.


  That's a great request! To make your project more detailed and user-friendly, expanding the "routes and travels" information in the Place class is essential.

I'll provide additional, detailed content for the *Goa, **Araku, **Kerala, and **Hyderabad* sections, focusing on more specific routes, travel options, and local transport.

***

## ✈ Goa: Routes and Travels Details

| Sub-Option | Description |
| :--- | :--- |
| *By Air* | *Goa International Airport (Dabolim - GOI):* Located 30 km from the state capital, Panaji. The main hub for flights to major Indian cities (Delhi, Mumbai, Bengaluru, Chennai) and international charters. *Mopa Airport (New Goa Airport - GOX):* Officially Manohar International Airport, located in North Goa (Pernem). It now handles most domestic traffic, especially budget airlines. |
| *Post-Flight Transport* | *Prepaid Taxis:* Available at both airports. Prices are fixed but can be high. *Goa Miles/Other Ride-Sharing:* App-based taxis are available but may have higher fares during peak season. *KTC Bus Service:* Budget-friendly buses run from Dabolim to nearby Vasco da Gama and Panaji, but less convenient from Mopa. |
| *By Train* | *Major Stations:* *Madgaon (MAO)* in South Goa (closest to popular beaches like Palolem) and *Thivim (THVM)* in North Goa (convenient for Baga, Calangute). Both are on the Konkan Railway route. |
| *By Road (Bus/Car)* | *Bus Operators:* Goa has excellent connectivity via NH 66. Operators like KSRTC, MSRTC, and private companies run regular sleeper and AC services from Mumbai, Pune, and Bengaluru. |
| *Local Transport* | *Rented Scooters/Motorbikes:* The most popular and cost-effective way to explore, available for ₹300–₹500 per day. *Pilot Service:* Motorcycle taxis, identifiable by yellow fenders, are common for short distances. |

***

## ⛰ Araku Valley: Routes and Travels Details

| Sub-Option | Description |
| :--- | :--- |
| *By Train* | *The Rail Journey:* The most scenic route. The *Visakhapatnam – Kirandul Passenger* (often running with a Vistadome coach) passes through over 50 tunnels and 80 bridges. You typically book to *Araku (ARK)* station. |
| *By Road (Bus/Car)* | *Scenic Route:* The 120 km drive from Visakhapatnam takes about 3 hours, offering winding roads and panoramic views of the Eastern Ghats. *APSRTC Buses:* Frequent buses are available from the Visakhapatnam bus station (Dwaraka Nagar). |
| *By Air* | *Nearest Airport:* *Visakhapatnam Airport (VTZ)*, approximately 106 km away. From the airport, one must hire a taxi or take a bus to reach Araku. |
| *Local Transport* | *Hired Taxis:* Taxis can be hired in Araku for day trips to sites like Borra Caves and the tribal museum. *Auto-Rickshaws:* Available for short distances within the main valley town. |

***

## 🌴 Kerala: Routes and Travels Details

| Sub-Option | Description |
| :--- | :--- |
| *By Air* | *Major Airports:* *Cochin International Airport (COK), **Trivandrum International Airport (TRV), **Calicut International Airport (CCJ), and **Kannur International Airport (KIAL)*. Cochin is the busiest and best connected. |
| *By Train* | *Major Stations:* *Thiruvananthapuram Central (TVC), **Ernakulam Junction (ERS/South), and **Kozhikode (CLT)*. Kerala is well-connected to all major Indian metros via the extensive Southern Railway network. |
| *By Road (Bus/Car)* | *National Highways:* NH 66 runs the entire length of Kerala (north-south). *KSRTC:* The state-run corporation offers inter-state (e.g., to Bengaluru, Chennai) and intra-state services, including budget-friendly Superfast and premium Volvo/Scania buses. |
| *Local Transport* | *Auto-Rickshaws and Taxis:* Widely available. *Cochin Metro:* Available in Kochi/Ernakulam for efficient city travel. *Ferry/Boat Service:* Essential for exploring the backwaters of Alappuzha (Alleppey) and Kumarakom, including public ferries and private houseboats. |

***

## 🏛 Hyderabad: Routes and Travels Details

| Sub-Option | Description |
| :--- | :--- |
| *By Air* | *Rajiv Gandhi International Airport (RGIA - HYD):* Located at Shamshabad. A major hub with excellent connectivity across India and globally. |
| *Airport Transport* | *Pushpak Airport Liner:* A reliable, air-conditioned bus service connecting RGIA to key city locations like Secunderabad, Hi-Tech City, and LB Nagar. *Prepaid and App Taxis:* Available 24/7. |
| *By Train* | *Major Stations:* *Secunderabad Junction (SC)* (the main hub), *Hyderabad Deccan (Nampally - HYB), and **Kachiguda (KCG)*. Connected to all major cities in India. |
| *By Road (Bus/Car)* | *TSRTC Buses:* Telangana State Road Transport Corporation runs city buses, inter-city, and inter-state services (e.g., to Bengaluru, Mumbai). |
| *Local Transport* | *Hyderabad Metro Rail:* A rapidly expanding network covering the city's main corridors, including LB Nagar, Miyapur, and Raidurg (Hi-Tech City). *MMTS:* Multi-Modal Transport System (local train) for suburban travel. *Auto-Rickshaws/Cabs:* App-based services (Ola/Uber) and traditional transport are abundant. |
