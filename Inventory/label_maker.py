import labels, barcode,os
from reportlab.graphics import shapes
from reportlab.graphics.barcode import getCodes, getCodeNames, createBarcodeDrawing
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.platypus import SimpleDocTemplate, Image
from reportlab.pdfbase.ttfonts import TTFont

from barcode.writer import ImageWriter
import PIL
font_path = 'fonts'

registerFont(TTFont('3of9', os.path.join(font_path, 'free3of9.ttf')))
# Create an A4 portrait (210mm x 297mm) sheets with 2 columns and 8 rows of
# labels. Each label is 90mm x 25mm with a 2mm rounded corner. The margins are
# automatically calculated.
specs = labels.Specification(210, 297, 2, 7, 101, 34,  top_padding=0, bottom_padding=0, row_gap=0 )

# Create a function to draw each label. This will be given the ReportLab drawing
# object to draw on, the dimensions (NB. these will be in points, the unit
# ReportLab uses) of the label, and the object to render.
def draw_label(label, width, height, obj):
    # Just convert the object to a string and print this at the bottom left of
    # the label.
    # label.add(10,2,shapes.Image(obj[0]))
    label.add(shapes.String(2, 2, str(obj[0]), fontName="Helvetica", fontSize=40))
    label.add(shapes.String(2, 40, str(obj[1]), fontName="Helvetica", fontSize=40))
    # if 'bcode' in str(obj) :
    #     label.add(shapes.String(2, 2, str(obj[5:]), fontName="Helvetica", fontSize=40))
    # else:
    #     label.add(shapes.String(2, 2, str(obj), fontName="Helvetica", fontSize=40))

# Create the sheet.
sheet = labels.Sheet(specs, draw_label, border=True)
# trying to make barcode
ean = barcode.get('ean13', '123456789102', writer=ImageWriter())
filename = ean.save('ean13')


# Add a couple of labels.
sheet.add_label([123,'test'])
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
