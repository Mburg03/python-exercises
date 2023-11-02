# Show articles
# Buy an article
# Create a pdf file with the information of the article that the user bought
# Reduce stock article -1

# Procedures:
# First try to do everything that concerns classes and .csv file
# Go and find the code for pdf and replicate it to get a ticket that looks 
# the best possible
import pandas as pd
from fpdf import FPDF

articles_df = pd.read_csv("./resources/articles.csv")

class Article:
    def __init__(self, article_id) -> None:
      self.article_id = article_id
      self.name = articles_df.loc[articles_df["id"] == self.article_id, "name"].squeeze()
      self.price = articles_df.loc[articles_df["id"] == self.article_id, "price"].squeeze()
      self.stock_quantity = articles_df.loc[articles_df["id"] == self.article_id, "in stock"].squeeze()

    def is_in_stock(self):
        article_availability = articles_df.loc[articles_df["id"] == self.article_id, "in stock"].squeeze() != 0  
        if article_availability:
          return True
        else:
          return False
    
    def buy(self) -> None:
        articles_df.loc[articles_df["id"] == self.article_id, "in stock"] -= 1
        articles_df.to_csv("./resources/articles.csv", index=False)
        
    
class Facture:
    def __init__(self, article_object):
      self.article = article_object
            
      
    def create(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        facture_number = article.article_id
        article_name = article.name
        article_price = article.price
        pdf.set_font(family="Times", size=12, style="B")
        pdf.cell(w=0, h=12, txt=f"Receipt no.{facture_number}", align="L", ln=1)
        pdf.cell(w=0, h=12, txt=f"Product name: {article_name}", align="L", ln=1)
        pdf.cell(w=0, h=12, txt=f"Product price: ${article_price}", align="L", ln=1)
        pdf.output(f"./Receipt-{facture_number}.pdf")

        return 'Facture created!'
    
    
print(articles_df)
article_id = int(input("Enter the id of the article you want to buy: "))
article = Article(article_id)

if article.is_in_stock():
    article.buy()
    facture = Facture(article)
    print(facture.create())
else:
    print(f"Item {article_id} not in stock!")
    
