# Class to structure data to be used in SMS to send
class FlightData:

    def __init__(self, price, origin, destination, airport_origin, airport_destination, depart_from, return_date):
        self.price = price
        self.origin = origin
        self.destination = destination
        self.airport_origin = airport_origin
        self.airport_destination = airport_destination
        self.depart_from = depart_from
        self.return_date = return_date
