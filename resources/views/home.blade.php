<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Gerador de Contratos</title>
    <link rel="stylesheet"  href= "{{ asset('css/home.css') }}"/>
</head>
<body>
    <div class="card">
        <h2 class="text">Faça login</h2>
        <form action="POST">
            @csrf
            <div>
                <label for="email">E-mail</label><br>
                <input type="email" id="email" name="email" placeholder="E-mail" class="email">
            </div>
            <br>
            <div>
                <label for="senha">Senha</label><br>
                <input type="password" name="senha" id="senha" placeholder="Senha" class="senha">
            </div>
            <br>
            <div>
                <button type="submit" class="enviar">Entrar</button>
            </div>
            <div>
                <a href="#" class="esqueceu">Esqueceu a senha</a>
            </div>
        </form>
    </div>
</body>
</html>