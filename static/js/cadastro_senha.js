document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const senhaInput = document.querySelector('input[name="password"]');
    const confirmarSenhaInput = document.querySelector('input[name="confirm_password"]');
    const errorLabel = document.querySelector('#error-label');

    form.addEventListener('submit', function (e) {
        // Verifica se as senhas coincidem
        if (senhaInput.value !== confirmarSenhaInput.value) {
            e.preventDefault(); // Impede o envio do formulário

            // Exibe uma mensagem de erro
            errorLabel.textContent = 'As senhas não coincidem';
        }
    });

    // Limpa a mensagem de erro quando os campos de senha são alterados
    senhaInput.addEventListener('input', function () {
        errorLabel.textContent = '';
    });

    confirmarSenhaInput.addEventListener('input', function () {
        errorLabel.textContent = '';
    });
});