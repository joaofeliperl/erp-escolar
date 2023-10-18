document.addEventListener("DOMContentLoaded", function () {
    const checkboxes = document.querySelectorAll('.toggle-checkbox');

    checkboxes.forEach(function (checkbox) {
        // Verificar o estado inicial ao carregar a página
        const slider = checkbox.parentElement.querySelector('.toggle-slider');
        if (checkbox.checked) {
            slider.style.backgroundColor = '#1D4ED8'; // Cor quando marcado
        } else {
            slider.style.backgroundColor = '#ccc'; // Cor padrão
        }

        // Adicionar evento de alteração
        checkbox.addEventListener('change', function () {
            if (this.checked) {
                slider.style.backgroundColor = '#1D4ED8'; // Cor quando marcado
            } else {
                slider.style.backgroundColor = '#ccc'; // Cor padrão
            }
        });
    });
});
