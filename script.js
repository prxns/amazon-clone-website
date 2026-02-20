fetch ("/products")
.then(response => response.json())
.then(products => {
    const shop = document.querySelector(".shop");
    shop.innerHTML = "";

    products.forEach(product => {
        const productHTML = `
        <div class = "box1">
        <h2>${product.name}</h2>
          <img src="/images/${product.image}" class="box1-img"/>
          <p>₹${product.price}</p>
        </div>
        `;
        shop.innerHTML += productHTML;
    });
});