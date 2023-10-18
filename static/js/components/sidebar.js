document.addEventListener("DOMContentLoaded", function () {
    const sidebar = document.getElementById('sidebar');
 
    // Certifique-se de que o sidebar está inicialmente oculto
    sidebar.classList.remove('visible');
 });
 
 document.getElementById('openSidebarButton').addEventListener('click', toggleSidebar);
 
 // Chame a função dropdown no carregamento da página
 dropdown_usuarios();
 dropdown_empresas();
 
 function toggleSidebar() {
    const body = document.body;
    const sidebar = document.getElementById('sidebar');
 
    // Adiciona ou remove a classe 'sidebar-open' no body
    body.classList.toggle('sidebar-open');
 
    // Adiciona ou remove a classe 'translate-x-custom' no body para empurrar o conteúdo para o lado
    body.classList.toggle('translate-x-custom');
 
    // Adiciona ou remove a classe 'overflow-hidden' no body para evitar rolagem quando o menu está aberto
    body.classList.toggle('overflow-hidden');
 
    // Adiciona ou remove a classe 'visible' no sidebar para exibi-lo ou ocultá-lo
    sidebar.classList.toggle('visible');
 }
 
 // Função para fechar o sidebar se o usuário clicar fora dele
 document.addEventListener('click', function (event) {
    const sidebar = document.getElementById('sidebar');
    const body = document.body;
 
    if (!sidebar.contains(event.target)) {
       // Fecha o sidebar se o clique não estiver dentro dele
       body.classList.remove('sidebar-open');
       body.classList.remove('translate-x-custom');
       body.classList.remove('overflow-hidden');
       sidebar.classList.remove('visible');
    }
 });
 