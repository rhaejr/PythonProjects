from functools import reduce

def calculate_checksum(ean):
    """Calculates the checksum for EAN13-Code.

    :returns: The checksum for `self.ean`.
    :rtype: Integer
    """
    sum_ = lambda x, y: int(x) + int(y)
    evensum = reduce(sum_, ean[::2])
    oddsum = reduce(sum_, ean[1::2])
    return (10 - ((evensum + oddsum * 3) % 10)) % 10

