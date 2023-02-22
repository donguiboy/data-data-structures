# pylint: disable=missing-docstring

# TODO: add some currency rates
RATES = {
    "USDEUR": 0.85,
    "GBPEUR": 1.13,
    "CHFEUR": 0.86,
    "EURGBP": 0.885
    }

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string

    amount = (100,"EUR")
    currency = ("EURGBP")
                    convert(100, "EURGBP")
                        100 * EURGBP => 88,5
    """
   # values = amount[0]
   # change = amount[1]+currency
    #RATES.get(change, None)
    for key, value in RATES.items():
        if amount[1] == key[0:3] and currency == "EUR":
            return round(value * amount[0])
        if amount[1] == key[0:3] and currency == "GBP":
            return round(value * amount[0])
    return None
