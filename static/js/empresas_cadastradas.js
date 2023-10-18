document.addEventListener("DOMContentLoaded", function () {
    const sidebarButton = document.querySelector("[data-drawer-target='sidebar-multi-level-sidebar']");
    const sidebar = document.getElementById("sidebar-multi-level-sidebar");

    sidebarButton.addEventListener("click", function () {
      sidebar.classList.toggle("hidden");
    });

    // Adicione este código se você quiser fechar o sidebar clicando fora dele
    document.addEventListener("click", function (event) {
      if (!sidebar.contains(event.target) && event.target !== sidebarButton) {
        sidebar.classList.add("hidden");
      }
    });
  });

  document.addEventListener("DOMContentLoaded", function () {
    const dropdownButton = document.querySelector("[data-collapse-toggle='dropdown-example']");
    const dropdownList = document.getElementById("dropdown-example");

    dropdownButton.addEventListener("click", function () {
      dropdownList.classList.toggle("hidden");
    });

    // Adicione este código se você quiser fechar o dropdown clicando fora dele
    document.addEventListener("click", function (event) {
      if (!dropdownList.contains(event.target) && event.target !== dropdownButton) {
        dropdownList.classList.add("hidden");
      }
    });
  });