document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    let name = document.getElementById('name').value;
    let email = document.getElementById('email').value;
    let message = document.getElementById('message').value;
    let errors = [];

    if (name.length < 3) {
        errors.push("O nome deve ter pelo menos 3 caracteres.");
    }

    if (message.length < 10) {
        errors.push("A mensagem deve ter pelo menos 10 caracteres.");
    }

    if (errors.length > 0) {
        alert(errors.join("\n"));
    } else {
        alert('Formulário enviado com sucesso!');
        // Aqui você pode adicionar o código para enviar o formulário via AJAX ou similar.
        //Teste
    }
});
