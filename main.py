import pandas as pd


df = pd.read_csv("files/hotels.csv", dtype={"id": str})
# df headers - id,name,city,capacity,available


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
        self.city = df.loc[df["id"] == self.hotel_id, "city"].squeeze()

    def view_available(self):
        availibility = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availibility == "yes":
            return True
        else:
            return False

    def reserve(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("files/hotels.csv", index=False)


class Confirmation:
    def __init__(self, guest_name, hotel):
        self.guest_name = guest_name
        self.hotel = hotel

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking details:
        Name: {self.guest_name}
        Hotel: {self.hotel.name}
        City: {self.hotel.city}
        Reservation Number: ABC000123456789
        """
        return content


print(df)
hotel_id = input("Enter the id number of the hotel: ")
hotel = Hotel(hotel_id)
if hotel.view_available():
    hotel.reserve()
    guest_name = input("Enter guest name: ")
    confirmation_number = Confirmation(guest_name=guest_name, hotel=hotel)
    print(confirmation_number.generate())
else:
    print("No rooms availalbe in hotel.")
