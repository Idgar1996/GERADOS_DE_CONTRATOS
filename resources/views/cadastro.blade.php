@extends('layouts.app')

@section('title', 'Cadstro')

@section('content')
    <section class="card">
        <h1 class="titulo">Cadastro</h1>
        <p class="intro">Crie sua conta</p>

        <form method="POST" action="{{ route('cadastro.store') }}" class="formulario">
            @csrf

            <!-- Nome -->
            <div class="form-group">
                <label>Nome completo</label>
                <input type="text" name="nome" class="form-input-email" required>
            </div>

            <!-- Documento -->
            <div class="form-group">
                <label>Documento</label>
                <div style="display:flex; gap:10px;">
                    <label>
                        <input type="radio" name="tipo_documento" value="cpf" checked> CPF
                    </label>
                    <label>
                        <input type="radio" name="tipo_documento" value="cnpj"> CNPJ
                    </label>
                </div>
                <input type="text" name="documento" class="form-input-email" required>
            </div>

            <!-- Telefone -->
            <div class="form-group">
                <label>Telefone</label>
                <input type="text" name="telefone" class="form-input-email" required>
            </div>

            <!-- Email -->
            <div class="form-group">
                <label>E-mail</label>
                <input type="email" name="email" class="form-input-email" required>
            </div>

            <!-- Senha -->
            <div class="form-group">
                <label>Senha</label>
                <input type="password" name="senha" class="form-input-senha" required>
            </div>

            <div class="form-group">
                <label>Confirmar senha</label>
                <input type="password" name="senha_confirmation" class="form-input-senha" required>
            </div>

            <!-- Endereço -->
            <div class="form-group">
                <label>CEP</label>
                <input type="text" name="cep" class="form-input-email">
            </div>

            <div class="form-group">
                <label>Estado</label>
                <input type="text" name="estado" class="form-input-email">
            </div>

            <div class="form-group">
                <label>Cidade</label>
                <input type="text" name="cidade" class="form-input-email">
            </div>

            <div class="form-group">
                <label>Rua</label>
                <input type="text" name="rua" class="form-input-email">
            </div>

            <div class="form-group">
                <label>Número</label>
                <input type="text" name="numero" class="form-input-email">
            </div>

            <div class="form-group">
                <label>Complemento</label>
                <input type="text" name="complemento" class="form-input-email">
            </div>

            <div class="form-group">
                <label>Bairro</label>
                <input type="text" name="bairro" class="form-input-email">
            </div>

            <!-- Ramo -->
            <div class="form-group">
                <label>Ramo de atuação</label>
                <select name="ramo" class="form-input-email" required>
                    <option value="">Selecione</option>
                    <option value="imobiliario">Imobiliário</option>
                    <option value="veicular">Veicular</option>
                    <option value="servicos">Prestação de serviços</option>
                    <option value="outros">Outros</option>
                </select>
            </div>

            <button type="submit" class="form-button">Cadastrar</button>

            <nav class="links">
                <a href="{{ route('home') }}" class="esqueceu">Já tenho conta</a>
            </nav>

        </form>
    </section>
@endsection