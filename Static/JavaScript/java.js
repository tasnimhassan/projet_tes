document.addEventListener("DOMContentLoaded", function() {
    var addToCartButtons = document.querySelectorAll('.add-to-cart');

    // Vérifie que les boutons sont bien sélectionnés
    console.log("Nombre de boutons 'Ajouter au panier' trouvés:", addToCartButtons.length);

    // Boucle à travers chaque bouton et ajoute un écouteur d'événements pour le clic
    addToCartButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var productId = button.getAttribute('data-product-id');
            console.log("Bouton cliqué, ID du produit:", productId);
            addToCart(productId);
        });
    });

    function addToCart(productId) {
        console.log("Produit ajouté au panier avec l'ID:", productId);
        // Logique pour ajouter le produit au panier
    }
    HTMLTableRowElement.addEventListener('click', (event)=>{
        let positionClick = event.target;
        if(positionClick.classList.contains('productID')){
            alert('1');
        }
    })
});
const header = document.querySelector("header");


window.addEventListener("scroll" ,function() {
    header.classList.toggle("sticky",this.window.scrollY > 0);
})