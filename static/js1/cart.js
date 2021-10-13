var updateBtns = document.getElementsByClassName('update-cart');


for (var i = 0; i < updateBtns.length; i++) {
    // i will add an event listener to the button
    updateBtns[i].addEventListener('click', function() {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action:', action)


        // this is to check if the user is authenticated or not
        console.log('USER:', user)
        if (user === 'AnonymousUser') {
            console.log('User is not logged in!!')
        } else {
            updateUserOrder()
        }
    })
}

function updateUserOrder(productId, action) {
    console.log('User is logged in, sending data.......')

    // linking up the function to the url
    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log('data:', data)
    })
}