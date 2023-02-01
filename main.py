import pandas as pd

df = pd.read_csv("files/hotels.csv", dtype={"id": str})
df_cards = pd.read_csv("files/cards.csv", dtype=str).to_dict(orient="records")


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
        Name: {self.guest_name.title()}
        Hotel: {self.hotel.name}
        City: {self.hotel.city}
        Reservation Number: ABC000123456789
        """
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, card_holder, expiration, cvc_code):
        card_data = {"number": self.number,
                     "expiration": expiration,
                     "holder": card_holder,
                     "cvc": cvc_code}
        if card_data in df_cards:
            return True


print(df)
hotel_id = input("Enter the id number of the hotel: ")
hotel = Hotel(hotel_id)
if hotel.view_available():
    credit_card = CreditCard(number="1234567890123456",)
    if credit_card.validate(card_holder="JOHN SMITH",
                            expiration="12/26",
                            cvc_code="123"):
        hotel.reserve()
        guest_name = input("Enter guest name: ")
        confirmation_number = Confirmation(guest_name=guest_name, hotel=hotel)
        print(confirmation_number.generate())
    else:
        print("There was a problem with your payment.")
else:
    print("No rooms availalbe in hotel.")
