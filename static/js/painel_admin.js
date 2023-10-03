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
