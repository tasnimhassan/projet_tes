document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM est bien present');
    const cartItems = [
        { "id": 1, "name": "Robe kaki-Clair", "price": 5000, "image": "file:///C:/Users/enaya/OneDrive/Bureau/sitesoutien/photo1.jpg" },
        { "id": 2, "name": "Robe beige-blanc", "price": 5000, "image": "file:///C:/Users/enaya/OneDrive/Bureau/sitesoutien/photo2.jpg" },
        { "id": 3, "name": "Robe beige-blanc", "price": 5000, "image": "file:///C:/Users/enaya/OneDrive/Bureau/sitesoutien/photo3.jpg" },
        { "id": 4, "name": "Robe beige-blanc", "price": 5000, "image": "file:///C:/Users/enaya/OneDrive/Bureau/sitesoutien/photo4.jpg" },
        { "id": 5, "name": "Robe beige-blanc", "price": 5000, "image": "file:///C:/Users/enaya/OneDrive/Bureau/sitesoutien/photo5.jpg" },
        { "id": 6, "name": "Robe kaki-Beige", "price": 5000, "image": "file:///C:/Users/enaya/OneDrive/Bureau/sitesoutien/photo6.jpg" },
        { "id": 7, "name": "Robe beige-blanc", "price": 5000, "image": "file:///C:/Users/enaya/OneDrive/Bureau/sitesoutien/photo7.jpg" },
        { "id": 8, "name": "Robe beige-blanc", "price": 5000, "image": "file:///C:/Users/enaya/OneDrive/Bureau/sitesoutien/photo8.jpg" },
        { "id": 9, "name": "Robe beige-blanc", "price": 5000, "image": "file:///C:/Users/enaya/OneDrive/Bureau/sitesoutien/photo9.jpg" }
    ];
    let ProductsHTML = document.querySelector('.listProduct');
    function renderCartItems() {
        const cartItemsContainer = document.getElementById('cart-items');
        const cartTotalContainer = document.getElementById('cart-total');

        console.log('Rendering cart items'); // Vérifiez que la fonction renderCartItems est bien appelée

        if (!cartItemsContainer || !cartTotalContainer) {
            console.error("Les éléments du panier ne sont pas trouvés dans le DOM.");
            return;
        }
        const addToCartButtons = document.querySelectorAll('.add-to-cart');
        console.log("Nombre de boutons 'Ajouter au panier' trouvés:", addToCartButtons.length);
        addToCartButtons.forEach(button => {
            button.addEventListener('click', () => {
                const productId = button.getAttribute('data-product-id');
                console.log("Bouton cliqué, ID du produit:", productId);
                addToCart(productId);
            });
        });
        cartItemsContainer.innerHTML = '';
        let total = 0;

        cartItems.forEach(item => {
            total += item.price * item.quantity;

            const itemElement = document.createElement('div');
            itemElement.innerHTML = `
                <div class="cart-item">
                    <img src="${item.image}" alt="${item.name}" class="cart-item-image" />
                    <div class="cart-item-details">
                        <p>${item.name} - ${item.price}fdj</p>
                        <label for="quantity-${item.id}">Quantité: </label>
                        <select id="quantity-${item.id}" onchange="updateQuantity(${item.id}, this.value)">
                            ${Array.from({ length: 10 }, (_, i) => i + 1).map(q => `
                                <option value="${q}" ${q === item.quantity ? 'selected' : ''}>${q}</option>
                            `).join('')}
                        </select>
                        <button onclick="removeItem(${item.id})">Supprimer</button>
                    </div>
                </div>
            `;
            cartItemsContainer.appendChild(itemElement);
        });

        cartTotalContainer.innerHTML = `Votre Total d'achat est: ${total}fdj`;
    }

    window.updateQuantity = function (id, quantity) {
        const item = cartItems.find(item => item.id === id);
        if (item) {
            item.quantity = parseInt(quantity);
            renderCartItems();
        }
    };

    window.removeItem = function (id) {
        const itemIndex = cartItems.findIndex(item => item.id === id);
        if (itemIndex !== -1) {
            cartItems.splice(itemIndex, 1);
            renderCartItems();
        }
    };

    renderCartItems();

    addToCartButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            var productId = button.getAttribute('data-product-id');
            addToCart(productId);
        });
    });

    function addToCart(productId) {
        console.log("Produit ajouté au panier avec l'ID:", productId);
        const product = cartItems.find(item => item.id === parseInt(productId));
        if (product) {
            product.quantity += 1;
        } else {
        }
        renderCartItems();
    }
});
