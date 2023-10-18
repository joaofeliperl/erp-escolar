        // Adicionando comportamento de dropdown
        document.getElementById('servicesDropdown').addEventListener('click', function () {
            var dropdownContent = document.getElementById('servicesDropdownContent');
            dropdownContent.classList.toggle('hidden');
        });

        // Fechar dropdown ao clicar fora
        window.addEventListener('click', function (event) {
            var dropdownContent = document.getElementById('servicesDropdownContent');
            if (!event.target.matches('#servicesDropdown')) {
                if (!dropdownContent.classList.contains('hidden')) {
                    dropdownContent.classList.add('hidden');
                }
            }
        });