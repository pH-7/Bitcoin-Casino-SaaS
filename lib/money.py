def dollars_to_cents(dollars):
    """
    Converts dollars to cents.

    :param dollars: Amount in dollars
    :type dollars: float
    :return: int
    """
    return int(dollars * 100)

def cents_to_dollars(cents):
    """
        Converts cents to dollars.
        
        :param cents: Amount in cents
        :type cents: int
        :return: float
        """
    return round(cents / 100.0, 2)
