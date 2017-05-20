from functools import reduce
import labels, barcode,os, PIL, sqlite3
from reportlab.graphics import shapes
from barcode.writer import ImageWriter


def calculate_checksum(ean):
    """Calculates the checksum for EAN13-Code.

    :returns: The checksum for `self.ean`.
    :rtype: Integer
    """
    sum_ = lambda x, y: int(x) + int(y)
    evensum = reduce(sum_, ean[::2])
    oddsum = reduce(sum_, ean[1::2])
    return (10 - ((evensum + oddsum * 3) % 10)) % 10


def label_maker(acft):
    """ Makes labels for my inventory program"""

    conn = sqlite3.connect('inventory.db')
    cur = conn.cursor()
    # nsn, pn, desc, remarks, location, niin, acft
    db = cur.execute('select desc, pn, location, niin, nsn, acft from benchstock where acft="{}" and label="true"'.format(acft)).fetchall()

    font_path = 'fonts'
    big_lablels = (101, 34, 2, 7)
    address_labels = (68.675, 26.4, 3, 10)
    label_width, label_height, columns, rows = address_labels
    specs = labels.Specification(215, 279.4, columns, rows, label_width, label_height, row_gap=0, column_gap=4,
                                 top_padding=1,
                                 bottom_padding=1, right_padding=1)

    def draw_label_top_bc(label, width, height, obj):
        # Just convert the object to a string and print this at the bottom left of
        # the label.
        label.add(shapes.String(2, 2, str(obj[0]), fontName="Helvetica", fontSize=12))
        label.add(shapes.String(2, 13, str(obj[1]), fontName="Helvetica", fontSize=12))
        label.add(shapes.String(2, 24, str(obj[2]), fontName="Helvetica", fontSize=12))
        label.add(shapes.Image(2, 46, 180, 40, make_barcode(obj[3])))
        # label.add(shapes.String(38, 30, str(obj[3]), fontName="3of9", fontSize=30))
        label.add(shapes.String(2, 35, str(obj[4]), fontName="Helvetica", fontSize=12))

    def make_barcode(code):
        leading = '000'
        if acft == 'luh':
            leading = '720'
        elif acft == 'apache':
            leading = '640'
        code = leading + str(code)
        ean = barcode.get('ean13', code, writer=ImageWriter())
        filename = ean.save('barcodes/{}'.format(code))
        return filename

    sheet = labels.Sheet(specs, draw_label_top_bc, border=False)

    s = '1234121231234'
    n = '{}-{}-{}-{}'.format(s[:-9], s[-9:-7], s[-7:-4], s[-4:])
    # sheet.add_label([ 'Nomenclature','Part No.', 'Location', '1234121231234',n, ''])
    for row in db:
        if row[3] != '':
            nsn = '{}-{}-{}-{}'.format(row[4][:-9], row[4][-9:-7], row[4][-7:-4], row[4][-4:])
            sheet.add_label([row[0], row[1], row[2], row[3], nsn, row[5]])

    sheet.save('basic_new.pdf')
    print("{0:d} label(s) output on {1:d} page(s).".format(sheet.label_count, sheet.page_count))