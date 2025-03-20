from fpdf import FPDF
import pandas as pd

df = pd.read_csv(r"G:\PYTHON PROJECTS\PDF Generator\topics.csv")

#create pdf instance using the FPDF class
pdf = FPDF(orientation="P", unit="mm", format="A4") # p for portrait, unit of measuring drawings is mm
pdf.set_auto_page_break(auto=False, margin=0)

#loop over each row in csv file

for index, row in df.iterrows():

    #add pages
    pdf.add_page()

    #adding header
    pdf.set_font(family="Times", style="B", size=26)
    pdf.set_text_color(0, 0, 254)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1)

    # pdf.line(x1,y1, x2,y2) is the template for coordinates of drawing a line on the page
    pdf.line(10,22, 200, 22)

    #adding footer
    pdf.ln(265) #265mm breaklines to go down the page
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(0, 0, 254)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="R")

    #adding horizontal lines on each master page
    for y in range(22, 298, 10):
        pdf.line(10, y, 200, y)

    #adding extra pages for each topic
    for i in range(row['Pages']-1):
        pdf.add_page()
        # adding footer
        pdf.ln(277)  # 265mm breaklines to go down the page
        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(0, 0, 254)
        pdf.cell(w=0, h=12, txt=row['Topic'], align="R")

        # adding horizontal lines on each extra page
        for y in range(22, 298, 10):
            pdf.line(10, y, 200, y)



#generate output pdf file
pdf.output("output.pdf")