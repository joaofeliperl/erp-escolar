const response = await fetch("http://127.0.0.1:5000/painel_admin", {
    method: "GET",
    headers: {
        "Authorization": `Bearer ${token}`,
        "Content-Type": "application/json",
    },
});

if (response.ok) {
    const data = await response.json();
    console.log("Dados recebidos:", data);
} else {
    console.error("Erro na solicitação:", response.statusText);
}
document.addEventListener('DOMContentLoaded', function () {
    const toggleButton = document.getElementById('toggle-sidebar');
    const sidebar = document.getElementById('default-sidebar');

    toggleButton.addEventListener('click', function () {
        sidebar.classList.toggle('-translate-x-full');
    });
});

document.addEventListener('DOMContentLoaded', function () {
    // Obtém referências para o botão e o drawer
    var drawerButton = document.querySelector('[data-drawer-target="drawer-navigation"]');
    var drawer = document.getElementById('drawer-navigation');

    // Adiciona um ouvinte de eventos ao botão para mostrar o drawer
    drawerButton.addEventListener('click', function () {
        drawer.classList.remove('-translate-x-full');
    });

    // Adiciona um ouvinte de eventos ao botão dentro do drawer para esconder o drawer
    drawer.querySelector('[data-drawer-hide="drawer-navigation"]').addEventListener('click', function () {
        drawer.classList.add('-translate-x-full');
    });
});

