
// Função para formatar o CPF
function formatarCPF(cpf) {
    cpf = cpf.replace(/\D/g, ''); // Remove caracteres não numéricos
    cpf = cpf.replace(/(\d{3})(\d{3})(\d{3})(\d)/, '$1.$2.$3-$4');
    return cpf;
}

// Função para formatar o CEP
function formatarCEP(cep) {
    cep = cep.replace(/\D/g, ''); // Remove caracteres não numéricos
    cep = cep.replace(/(\d{5})(\d)/, '$1-$2');
    return cep;
}

// Adiciona um ouvinte de eventos para o campo CPF
document.getElementById('cpf').addEventListener('input', function (event) {
    var input = event.target;
    input.value = formatarCPF(input.value);
});

// Adiciona um ouvinte de eventos para o campo CEP
document.getElementById('cep').addEventListener('input', function (event) {
    var input = event.target;
    input.value = formatarCEP(input.value);
});

function formatarContato(input) {
    // Remove qualquer caractere não numérico
    let rawValue = input.value.replace(/\D/g, '');

    // Aplica a formatação desejada (por exemplo, adicionando parênteses e hífen)
    if (rawValue.length >= 2) {
        rawValue = `(${rawValue.slice(0, 2)}) ${rawValue.slice(2)}`;
    }

    if (rawValue.length >= 10) {
        rawValue = `${rawValue.slice(0, 10)}-${rawValue.slice(10)}`;
    }

    // Atualiza o valor no campo de input
    input.value = rawValue;
}
function validarNumero(input) {
    // Remover caracteres não numéricos usando expressão regular
    input.value = input.value.replace(/\D/g, '');
}