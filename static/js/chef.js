document.addEventListener('DOMContentLoaded', function() {
    // Устанавливаем WebSocket-соединение
            const chefSocket = new WebSocket(
            'ws://'
            + window.location.host
            + '/orders/'
        );
    const orderTemplate = document.getElementById('order-template');
    const ordersContainer = document.querySelector('.orders');
    
    // Обработчик входящих сообщений
    chefSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        addNewOrder(data.order);
    };

    // Обработчик ошибок
    chefSocket.onerror = function(error) {
        console.error('WebSocket Error:', error);
        showNotification('Ошибка соединения', 'error');
    };

    // Обработчик закрытия соединения
    chefSocket.onclose = function(e) {
        console.log('WebSocket закрыт...');
    };

    function addNewOrder(order) {
        // Проверяем, нет ли уже такого заказа (на случай дублирования)
        // if (document.querySelector(`.order-card[data-order-id="${order.id}"]`)) {
        //     return;
        // }

        const orderCard = orderTemplate.content.cloneNode(true);
        const cardEl = orderCard.querySelector('.order-card');
        cardEl.dataset.orderId = order.id;

        cardEl.querySelector('.order-id').textContent = order.id;
        cardEl.querySelector('.table-number').textContent = order.table_number;

        const itemsList = cardEl.querySelector('.items-list');
        order.items.forEach(item => {
            const li = document.createElement('li');
            li.textContent = `${item.name} (${item.quantity} шт.)`;
            itemsList.appendChild(li);
        });

        ordersContainer.prepend(cardEl);
    }


});