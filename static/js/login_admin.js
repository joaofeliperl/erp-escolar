document.addEventListener("DOMContentLoaded", async function () {
    const token = "seu_token_aqui"; // Substitua pelo seu token

    if (!token) {
        console.log("Token não encontrado. Redirecionando para /login");
        window.location.href = "/login"; // Redirecione para a página de login, se necessário
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:5000/admin", {
            method: "GET",
            headers: {
                "Authorization": `Bearer ${token}`,
                "Content-Type": "application/json",
            },
        });

        if (!response.ok) {
            console.error("Erro na solicitação:", response.statusText);
        }
    } catch (error) {
        console.error("Erro ao fazer a requisição:", error);
    }
});

document.addEventListener('DOMContentLoaded', function () {
    const passwordInput = document.getElementById('password');
    const showPasswordToggle = document.getElementById('showPasswordToggle');

    showPasswordToggle.addEventListener('click', function () {
        if (passwordInput.type === 'password') {
            passwordInput.type = 'text';
        } else {
            passwordInput.type = 'password';
        }
    });
});

