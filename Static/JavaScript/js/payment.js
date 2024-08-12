document.getElementById('payment-form').addEventListener('submit', (event) => {
    event.preventDefault();

    const firstName = document.getElementById('first-name').value.trim();
    const lastName = document.getElementById('last-name').value.trim();
    const cardName = document.getElementById('card-name').value;
    const cardNumber = document.getElementById('card-number').value;
    const expiryDate = document.getElementById('expiry-date').value;
    const cvv = document.getElementById('cvv').value;
    const address = document.getElementById('address').value;

    const paymentDetails = {
        firstName,
        lastName,
        cardName,
        cardNumber,
        expiryDate,
        cvv,
        address
    };
    if (!firstName || !lastName) {
        alert
        alert('Veuillez remplir tous les champs requis.');
        
        retu
       return;
    }
    alert('Formulaire soumis avec succès !');
    this.submit(); 
});
    console.log('Payment details:', paymentDetails);

    alert('Paiement réussi !');

    window.location.href = 'confirmation.html';
