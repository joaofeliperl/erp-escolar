$(document).ready(function () {
    // Armazena os estilos de exibição originais
    var originalDisplayStyles = [];

    function storeOriginalDisplayStyles() {
        var table = document.getElementsByTagName("table")[0];
        var tr = table.getElementsByTagName("tr");

        for (var i = 0; i < tr.length; i++) {
            originalDisplayStyles[i] = tr[i].style.display || "";
        }
    }

    // Função para realizar a filtragem
    function filterTable() {
        var inputName, inputCpf, filterName, filterCpf, table, tr, tdName, tdCpf, i, txtValueName, txtValueCpf;
        inputName = document.getElementById("filterInput");
        inputCpf = document.getElementById("filterInputCpf");
        filterName = inputName.value.toUpperCase();
        filterCpf = inputCpf.value.replace(/[^\d]/g, ''); // Remove caracteres não numéricos
        table = document.getElementsByTagName("table")[0];
        tr = table.getElementsByTagName("tr");

        for (i = 0; i < tr.length; i++) {
            tdCpf = tr[i].getElementsByTagName("td")[0]; // Coluna de CPF
            tdName = tr[i].getElementsByTagName("td")[1]; // Coluna de Nome

            if (tdCpf && tdName) {
                txtValueCpf = tdCpf.textContent || tdCpf.innerText;
                txtValueName = tdName.textContent || tdName.innerText;

                // Aplica filtros
                var cpfFilterPass = txtValueCpf.replace(/[^\d]/g, '').indexOf(filterCpf) > -1;
                var nameFilterPass = txtValueName.toUpperCase().indexOf(filterName) > -1;

                if (nameFilterPass && cpfFilterPass) {
                    tr[i].style.display = "";
                } else {
                    tr[i].style.display = "none";
                }
            }
        }
    }

    // Restaura os estilos de exibição originais
    function restoreOriginalDisplayStyles() {
        var table = document.getElementsByTagName("table")[0];
        var tr = table.getElementsByTagName("tr");

        for (var i = 0; i < tr.length; i++) {
            tr[i].style.display = originalDisplayStyles[i];
        }
    }

    // Aplique a filtragem ao clicar no botão
    $("#filterBtn").click(function () {
        filterTable();
    });

    // Aplique a filtragem ao pressionar Enter nos campos de entrada
    $("#filterInput, #filterInputCpf").keyup(function (event) {
        if (event.keyCode === 13) {
            filterTable();
        }
    });

    // Limpa o filtro e restaura a tabela original
    $("#filterInput, #filterInputCpf").on("input", function () {
        if ($(this).val() === "") {
            restoreOriginalDisplayStyles();
        }
    });

    // Armazena os estilos de exibição originais quando a página carrega
    storeOriginalDisplayStyles();
});