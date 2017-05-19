import labels, barcode,os, PIL, sqlite3
from reportlab.graphics import shapes
from reportlab.graphics.barcode import getCodes, getCodeNames, createBarcodeDrawing
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.platypus import SimpleDocTemplate, Image
from reportlab.pdfbase.ttfonts import TTFont
from barcode.writer import ImageWriter

conn = sqlite3.connect('inventory.db')
cur = conn.cursor()
# nsn, pn, desc, remarks, location, niin, acft
db = cur.execute('select desc, pn, location, niin, nsn, acft from benchstock where acft="apache"').fetchall()

font_path = 'fonts'
big_lablels = (101, 34, 2, 7)
address_labels = (68.675, 26.4, 3, 10)
label_width , label_height, columns, rows = address_labels
# registerFont(TTFont('3of9', os.path.join(font_path, 'free3of9.ttf')))
# Create an A4 portrait (210mm x 297mm) sheets with 2 columns and 8 rows of
# labels. Each label is 90mm x 25mm with a 2mm rounded corner. The margins are
# automatically calculated.
# 215.9 by 279.4 mm
specs = labels.Specification(215,279.4, columns, rows, label_width, label_height, row_gap=0, column_gap=4,top_padding=1,
                             bottom_padding=1, right_padding=1)

# Create a function to draw each label. This will be given the ReportLab drawing
# object to draw on, the dimensions (NB. these will be in points, the unit
# ReportLab uses) of the label, and the object to render.
def draw_label_top_bc(label, width, height, obj):
    # Just convert the object to a string and print this at the bottom left of
    # the label.
    label.add(shapes.String(2, 2, str(obj[0]), fontName="Helvetica", fontSize=12))
    label.add(shapes.String(2, 13, str(obj[1]), fontName="Helvetica", fontSize=12 ))
    label.add(shapes.String(2, 24, str(obj[2]), fontName="Helvetica", fontSize=12))
    label.add(shapes.Image(2, 46, 180, 40, make_barcode(obj[3], obj[5])))
    # label.add(shapes.String(38, 30, str(obj[3]), fontName="3of9", fontSize=30))
    label.add(shapes.String(2, 35, str(obj[4]), fontName="Helvetica", fontSize=12))

# def draw_label_btm_bc(label, width, height, obj):
#     # Just convert the object to a string and print this at the bottom left of
#     # the label.
#     label.add(shapes.String(2, 2, str(obj[0]), fontName="Helvetica", fontSize=14))
#     label.add(shapes.String(2, 16, str(obj[1]), fontName="Helvetica", fontSize=14 ))
#     label.add(shapes.String(2, 28, str(obj[2]), fontName="Helvetica", fontSize=14))
#     label.add(shapes.Image(2, 55, 180, 40, make_barcode(obj[3])))
#     # label.add(shapes.String(38, 30, str(obj[3]), fontName="3of9", fontSize=30))
#     # label.add(shapes.String(2, 55, str(obj[4]), fontName="Helvetica", fontSize=14))


def make_barcode(code, acft):
    leading = '000'
    if acft == 'luh':
        leading = '720'
    elif acft == 'apache':
        leading = '640'
    code = leading + str(code)
    ean = barcode.get('ean13', code, writer=ImageWriter())
    filename = ean.save('barcodes/{}'.format(code))
    return filename
# Create the sheet.
sheet = labels.Sheet(specs, draw_label_top_bc, border=False)
# trying to make barcode
# ean = barcode.get('ean13', '1234121231234', writer=ImageWriter())
# filename = ean.save('ean13')

# sheet.partial_page(1, ((1, 1), (2, 2), (4, 2)))
# Add a couple of labels.
s = '1234121231234'
n = '{}-{}-{}-{}'.format(s[:-9],s[-9:-7],s[-7:-4],s[-4:])
# sheet.add_label([ 'Nomenclature','Part No.', 'Location', '1234121231234',n, ''])
for row in db:
    if row[3] != '':
        nsn = '{}-{}-{}-{}'.format(row[4][:-9],row[4][-9:-7],row[4][-7:-4],row[4][-4:])
        sheet.add_label([row[0],row[1],row[2],row[3],nsn, row[5]])
# sheet.add_label("Hello")
# sheet.add_label("World")

# We can also add each item from an iterable.
# sheet.add_labels(range(3, 22))

# Note that any oversize label is automatically trimmed to prevent it messing up
# other labels.
# sheet.add_label("Oversized label here")

# Save the file and we are done.
sheet.save('basic.pdf')
print("{0:d} label(s) output on {1:d} page(s).".format(sheet.label_count, sheet.page_count))
