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
        var input, filter, table, tr, td, i, txtValue;
        input = document.getElementById("filterInput");
        filter = input.value.toUpperCase();
        table = document.getElementsByTagName("table")[0];
        tr = table.getElementsByTagName("tr");

        for (i = 0; i < tr.length; i++) {
            td = tr[i].getElementsByTagName("td")[1]; // Altere para o índice da coluna pela qual você deseja filtrar

            if (td) {
                txtValue = td.textContent || td.innerText;

                if (txtValue.toUpperCase().indexOf(filter) > -1) {
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

    // Aplique a filtragem ao pressionar Enter no campo de entrada
    $("#filterInput").keyup(function (event) {
        if (event.keyCode === 13) {
            filterTable();
        }
    });

    // Armazena os estilos de exibição originais quando a página carrega
    storeOriginalDisplayStyles();

    // Limpa o filtro e restaura a tabela original
    $("#filterInput").on("input", function () {
        if ($(this).val() === "") {
            restoreOriginalDisplayStyles();
        }
    });
});