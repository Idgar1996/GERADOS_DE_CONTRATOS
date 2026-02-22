@extends('layouts.app')

@section('title', 'Gerador de Contratos')

@section('content')
<section class="card">
    <img src="{{ asset('assets/imagens/icone_contrato.png') }}" alt="Icone de documento representando contratos" class="icone">
    <h1 class="titulo">Gerador de contratos</h1>
    <p class="intro">Sistema de criação e gestão contratual</p>
    <br>

    @if(session('erro'))
        <p class="mensagem-erro" role="alert" id="mensagem-erro">
            {{ session("erro") }}
        </p>
    @endif

    <form method="POST" class="formulario">
        @csrf
        <div class="form-group">
            <div class="form-field-email">
                <label for="email">E-mail</label>
                <input type="email" id="email" name="email" placeholder="E-mail" class="form-input-email" required>
            </div>

            <div class="form-field-senha">
                <label for="senha">Senha</label>
                <input type="password" name="senha" id="senha" placeholder="Senha" class="form-input-senha" required>
            </div>
        </div>

        <div>
            <button type="submit" class="form-button">Entrar</button>
        </div>

        <nav class="links">
            <a href="{{ route('cadastro') }}" class="cadastro">Não tem cadastro?</a>
            <a href="#" class="esqueceu">Esqueceu a senha</a>
        </nav>
    </form>
</section>
@endsection