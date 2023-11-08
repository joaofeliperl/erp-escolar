
// Função para formatar o CPF
function formatarCPF(cpf) {
    cpf = cpf.replace(/\D/g, ''); // Remove caracteres não numéricos
    cpf = cpf.replace(/(\d{3})(\d{3})(\d{3})(\d)/, '$1.$2.$3-$4');
    return cpf;
}



// Adiciona um ouvinte de eventos para o campo CPF
document.getElementById('cpf').addEventListener('input', function (event) {
    var input = event.target;
    input.value = formatarCPF(input.value);
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


// Obter referências aos elementos HTML
const empresaLabel = document.getElementById('empresaLabel');
const tooltipEmpresa = document.getElementById('tooltipEmpresa');

// Adicionar um evento de mouseover para mostrar o tooltip
empresaLabel.addEventListener('mouseover', () => {
    tooltipEmpresa.style.display = 'inline';
});

// Adicionar um evento de mouseout para esconder o tooltip
empresaLabel.addEventListener('mouseout', () => {
    tooltipEmpresa.style.display = 'none';
});

