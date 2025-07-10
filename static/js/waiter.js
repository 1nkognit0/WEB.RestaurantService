document.addEventListener('DOMContentLoaded', function() {
    // Элементы DOM
    const addItemsBtn = document.getElementById('add-items-btn');
    const itemsContainer = document.getElementById('items-container');
    const itemsFields = document.getElementById('items-fields');
    const itemsCountInput = document.getElementById('items-count');

    // Шаблон для динамического добавления строк (уже подготовлен в HTML)
    const itemRowTemplate = document.getElementById('item-row-template');

    // Обработчик кнопки "Добавить позиции"
    addItemsBtn.addEventListener('click', function() {
        const itemsCount = parseInt(itemsCountInput.value);

        if (itemsCount < 1) {
            alert('Количество позиций должно быть не менее 1');
            return;
        }

        // Очищаем предыдущие поля
        itemsFields.innerHTML = '';
        document.getElementById('item-count-be').value = itemsCount;

        // Создаем нужное количество полей из шаблона
        for (let i = 0; i < itemsCount; i++) {
            const clone = itemRowTemplate.content.cloneNode(true);

            // Добавляем уникальные имена для полей (если нужно)
            const select = clone.querySelector('select');
            const quantityInput = clone.querySelector('input[type="number"]');

            select.name = `item-${i}`;
            quantityInput.name = `quantity-${i}`;

            itemsFields.appendChild(clone);
        }

        // Показываем контейнер с полями
        itemsContainer.classList.remove('hidden');
    });
  })