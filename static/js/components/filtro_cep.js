document.addEventListener('DOMContentLoaded', function () {
    var cepInput = document.getElementById('cep');

    // Impedir a digitação de caracteres que não sejam números
    cepInput.addEventListener('keypress', function (e) {
        // Verifica se o caractere digitado é um número (dígitos de 0 a 9)
        if (!e.key.match(/[0-9]/)) {
            // Previne a ação padrão (não adiciona o caractere ao campo)
            e.preventDefault();
        }
    });

    // Função que é chamada quando o campo CEP perde o foco
    cepInput.addEventListener('blur', function (e) {
        var cep = e.target.value.replace(/\D/g, ''); // Remove caracteres não numéricos
        if (cep.length === 8) {
            var url = `https://viacep.com.br/ws/${cep}/json/`;

            fetch(url)
                .then(response => response.json())
                .then(data => {
                    if (!data.erro) {
                        document.getElementById('rua').value = data.logradouro;
                        document.getElementById('bairro').value = data.bairro;
                    } else {
                        alert('CEP não encontrado.');
                    }
                })
                .catch(err => {
                    alert('Não foi possível buscar o CEP.');
                });
        }
    });
});
