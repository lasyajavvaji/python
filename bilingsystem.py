class SupermarketBilling:
    def __init__(self):
        self.items = {}
        self.gst_rate = 0.18  # 18% GST
        self.discount_rate = 0.1  # 10% discount
    
    def add_item(self, name, price, quantity):
        if name in self.items:
            self.items[name]['quantity'] += quantity
        else:
            self.items[name] = {'price': price, 'quantity': quantity}
    
    def calculate_discount(self, total):
        return total * self.discount_rate
    
    def calculate_gst(self, total):
        return total * self.gst_rate
    
    def generate_bill(self):
        total = 0
        print("------ Supermarket Bill ------")
        print(f"{'Item':<20}{'Quantity':<10}{'Price':<10}{'Total':<10}")
        for name, details in self.items.items():
            item_total = details['price'] * details['quantity']
            total += item_total
            print(f"{name:<20}{details['quantity']:<10}{details['price']:<10}{item_total:<10}")
        
        discount = self.calculate_discount(total)
        gst = self.calculate_gst(total - discount)
        final_total = total - discount + gst
        
        print("\n")
        print(f"{'Total':<40}{total:<10}")
        print(f"{'Discount (10%)':<40}{-discount:<10}")
        print(f"{'GST (18%)':<40}{gst:<10}")
        print(f"{'Final Total':<40}{final_total:<10}")
        print("-------------------------------")
    
# Example usage:
billing_system = SupermarketBilling()
billing_system.add_item("Apple", 30, 2)
billing_system.add_item("Banana", 10, 5)
billing_system.add_item("Milk", 25, 1)
billing_system.add_item("Apple", 30, 1)
billing_system.generate_bill()
