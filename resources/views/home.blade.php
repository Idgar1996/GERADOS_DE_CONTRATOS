<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Gerador de Contratos</title>
    <link rel="stylesheet"  href= "{{ asset('css/home.css') }}"/>
</head>
<body class="tela">
    <div class="card">
        <h2 class="titulo">Faça login</h2>
        <form action="POST" class="formulario">
            @csrf
            <div class="entradas">
                <div class="entryEmail">
                    <label for="email">E-mail</label>
                    <input type="email" id="email" name="email" placeholder="E-mail" class="email">
                </div>
                <div class="entrySenha">
                    <label for="senha">Senha</label>
                    <input type="password" name="senha" id="senha" placeholder="Senha" class="senha">
                </div>
            </div>
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