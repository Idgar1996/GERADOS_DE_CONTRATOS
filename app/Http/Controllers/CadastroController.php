<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Routing\Controller;

class CadastroController extends Controller
{
    public function create()
    {
        return view('cadastro');
    }


    public function store(Request $request)
    {
        dd($request->all());
    }
}