document.addEventListener('DOMContentLoaded', function() {

    // fwoeifqnm3ouefnqowufnqouenoqufnqwwww[wwwwwpwwwwwwwfwwwwwwwwwwwwwwwfwfwfwfwfwfwfwfwfwfwfwfwfwfwfwfwfwfwfwfwfwfwfwfwfwfwfwfwfwfwfwfwfwfwfwfwfwfwfww]
    const menuItems = [
        { id: 1, name: 'Брускетта', price: 250 },
        { id: 2, name: 'Сырная тарелка', price: 350 },
        { id: 3, name: 'Стейк Рибай', price: 850 },
        { id: 4, name: 'Паста Карбонара', price: 450 },
        { id: 5, name: 'Салат Цезарь', price: 300 },
        { id: 6, name: 'Тирамису', price: 280 }
    ];
    
    const addItemsBtn = document.getElementById('add-items-btn');
    const itemsContainer = document.getElementById('items-container');
    const itemsFields = document.getElementById('items-fields');
    
    addItemsBtn.addEventListener('click', function() {
        const itemsCount = parseInt(document.getElementById('items-count').value);
        const tableNumber = document.getElementById('table-number').value;
        
        if (!tableNumber) {
            alert('Пожалуйста, выберите номер столика');
            return;
        }
        
        if (itemsCount < 1) {
            alert('Количество позиций должно быть не менее 1');
            return;
        }
        
        // Очищаем предыдущие поля
        itemsFields.innerHTML = '';
        
        // Создаем нужное количество полей
        for (let i = 0; i < itemsCount; i++) {
            const itemRow = document.createElement('div');
            itemRow.className = 'item-row';
            
            // Создаем select для выбора блюда
            const select = document.createElement('select');
            select.required = true;
            select.name = `item-${i}`;
            
            // Добавляем опции в select
            const defaultOption = document.createElement('option');
            defaultOption.value = '';
            defaultOption.textContent = 'Выберите блюдо';
            select.appendChild(defaultOption);
            
            menuItems.forEach(item => {
                const option = document.createElement('option');
                option.value = item.id;
                option.textContent = `${item.name} (${item.price} руб.)`;
                option.dataset.price = item.price;
                select.appendChild(option);
            });
            
            // Создаем input для количества
            const quantityInput = document.createElement('input');
            quantityInput.type = 'number';
            quantityInput.min = '1';
            quantityInput.value = '1';
            quantityInput.required = true;
            quantityInput.name = `quantity-${i}`;
            
            itemRow.appendChild(select);
            itemRow.appendChild(quantityInput);
            
            itemsFields.appendChild(itemRow);
        }
        
        // Показываем контейнер с полями
        itemsContainer.classList.remove('hidden');
    });
    
    // Обработчик отправки заказа                                  alskdfj;alskfj;sladkf;saklfjalfkjs;lfksjd;flkaj;dflksjflkasjflkjlakjlksj
    document.getElementById('submit-order').addEventListener('click', function() {
        alert('Заказ отправлен (в реальном проекте будет отправка на сервер)');
    });
});