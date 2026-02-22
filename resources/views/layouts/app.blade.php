<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>@yield('title', 'Sistema')</title>
    <link rel="stylesheet" href="{{ asset('css/home.css') }}">
</head>
<body class="tela">

    <main>
        <div class="theme-toggle">
            <button id="lightBtn">☀️</button>
            <button id="darkBtn">🌙</button>
        </div>

        @yield('content')
    </main>

    <script src="{{ asset('js/tema.js') }}"></script>
</body>
</html>