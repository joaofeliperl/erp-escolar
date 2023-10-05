document.getElementById('cpf').addEventListener('input', function (event) {
    var input = event.target;
    input.value = formatarCPF(input.value);
});

document.getElementById('cep').addEventListener('input', function (event) {
    var input = event.target;
    input.value = formatarCEP(input.value);
});

document.getElementById('contato').addEventListener('input', function (event) {
    formatarContato(event.target);
});