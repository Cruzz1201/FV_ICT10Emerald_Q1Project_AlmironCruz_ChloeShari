# making a reciept and sku generator

from pyscript import display, document

def compute(e):

    document.getElementById('compute').innerHTML = " " #clears the previous result

    product1 = document.getElementById("option1")
    product2 = document.getElementById("option2")
    product3 = document.getElementById("option3")
    product4 = document.getElementById("option4")
    product5 = document.getElementById("option5")
    product6 = document.getElementById("option6")
    

    subtotal = (
        float(product1.value) * product1.checked +
        float(product2.value) * product2.checked +
        float(product3.value) * product3.checked +
        float(product4.value) * product4.checked +
        float(product5.value) * product5.checked +
        float(product6.value) * product6.checked 
    )
        
    tax = 0.12
    tax_computation = subtotal * tax
    total_price = subtotal + tax_computation
    
    

    display(f'Subtotal: ₱{subtotal:.2f} | VAT : {subtotal * 0.12} | Total :  ₱{total_price}', target='compute')

