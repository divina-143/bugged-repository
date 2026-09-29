from pyscript import document


def SKU_generator(event):
    category = document.querySelector("#category").value

    product_name = document.querySelector("#product_name").value.strip()

    quantity = document.querySelector("#quantity").value

    if product_name == "":
        document.querySelector("#sku_output").innerHTML = """
            <div class="alert alert-warning">
                Please enter a product name.
            </div>
        """
        return

    if quantity == "":
        document.querySelector("#sku_output").innerHTML = """
            <div class="alert alert-warning">
                Please enter the stock quantity.
            </div>
        """
        return

    category_code = category[:2].upper()

    cleaned_name = product_name.strip()

    product_code = cleaned_name[:3].upper()

    sku = f"{category_code}-{product_code}-{quantity}"

    document.querySelector("#sku_output").innerHTML = f"""
        <div class="result-box">

            <div class="text-muted mb-1">
                Generated SKU
            </div>

            <div class="sku-code">
                {sku}
            </div>

            <hr>

            <small class="text-muted">
                Category: {category}<br>
                Product: {product_name}<br>
                Stock Quantity: {quantity}
            </small>

        </div>


    """

