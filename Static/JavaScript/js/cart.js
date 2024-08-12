document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM est bien présent');

    let cartItems = [];
    const cartItemsFromStorage = localStorage.getItem('cartItems');

    if (cartItemsFromStorage) {
        try {
            cartItems = JSON.parse(cartItemsFromStorage);
        } catch (error) {
            console.error("Erreur lors de la désérialisation des données du localStorage :", error);
            localStorage.setItem('cartItems', JSON.stringify(cartItems));
        }
    }

    function renderCartItems() {
        const cartItemsContainer = document.getElementById('cart-items');
        const cartTotalContainer = document.getElementById('cart-total');

        console.log('Rendering cart items');

        if (!cartItemsContainer || !cartTotalContainer) {
            console.error("Les éléments du panier ne sont pas trouvés dans le DOM.");
            return;
        }

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

        cartTotalContainer.innerHTML = `Votre total d'achat est: ${total}fdj`;
    }

    window.updateQuantity = function(id, quantity) {
        const item = cartItems.find(item => item.id === id);
        if (item) {
            item.quantity = parseInt(quantity);
            localStorage.setItem('cartItems', JSON.stringify(cartItems));
            renderCartItems();
        }
    };

    window.removeItem = function(id) {
        const itemIndex = cartItems.findIndex(item => item.id === id);
        if (itemIndex !== -1) {
            cartItems.splice(itemIndex, 1);
            localStorage.setItem('cartItems', JSON.stringify(cartItems));
            renderCartItems();
        }
    };

    function addToCart(productId) {
        console.log("Produit ajouté au panier avec l'ID:", productId);
        const productElement = document.querySelector(`.add-to-cart[data-product-id="${productId}"]`).closest('.row');
        const productName = productElement.querySelector('.product-text h5').innerText;
        const productPrice = parseInt(productElement.querySelector('.price p').innerText.replace('franc', ''));
        const productImage = productElement.querySelector('img').src;
    
        let product = cartItems.find(item => item.id === parseInt(productId));
        if (product) {
            product.quantity += 1;
        } else {
            const newProduct = {
                id: parseInt(productId),
                name: productName,
                price: productPrice,
                image: productImage,
                quantity: 1
            };
            cartItems.push(newProduct);
        }
        localStorage.setItem('cartItems', JSON.stringify(cartItems));
        renderCartItems();

        window.location.href = 'panier.html';
    }
    

    renderCartItems();
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    console.log("Nombre de boutons 'Ajouter au panier' trouvés:", addToCartButtons.length);
    addToCartButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            const productId = button.getAttribute('data-product-id');
            console.log("Bouton cliqué, ID du produit:", productId);
            addToCart(productId);
        });
    });
});