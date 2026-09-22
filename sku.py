#Sku Generator 
from pyscript import document, display 


def sku_generator(e):
    document.getElementById("results").innerHTML = "" #clear

    #get the values from the input field
    category = str(document.getElementById("category").value)  
    products = str(document.getElementById("products").value) 
    stock = str(document.getElementById("stock").value) 

    #Use the first three letters
    category_code = category[0:3].upper()
    products_code = products[0:4].upper()

    #generate the SKU
    FinalSKU = category_code + "-" + products_code + "-" + stock

    #display field 
    display(f'SKU: {FinalSKU}', target="results")


     

