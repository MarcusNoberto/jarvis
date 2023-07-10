from django.shortcuts import render
from django.shortcuts import redirect, render,  get_object_or_404
from django.contrib import messages
from .models import User
from django.db.models import Q

def createUserView(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        ativo = request.POST.get('ativo', False)
        data_de_saida = request.POST['data_de_saida']
        cpf = request.POST['cpf']
        telefone = request.POST['telefone']
        email_lsd = request.POST['email_lsd']
        email_pessoal = request.POST['email_pessoal']
        lattes = request.POST['lattes']
        sala = request.POST['sala']
        chave = request.POST.get('chave', False)

        # Criação de instância do usuário
        usuario = User(nome=nome, ativo=ativo, data_de_saida=data_de_saida, cpf=cpf,
                       telefone=telefone, email_lsd=email_lsd, email_pessoal=email_pessoal,
                       lattes=lattes, sala=sala, chave=chave)
        usuario.save()

        messages.success(request, 'Usuário adicionado com sucesso.')
        return redirect('sucess_user_add.html')  # Substitua 'nome_da_url' pela URL correta para redirecionamento após a adição do usuário
    else:
        messages.error(request, 'Erro ao adicionar o usuário.')
        return redirect('nome_da_url.html')  # Substitua 'nome_da_url' pela URL correta para redirecionamento em caso de erro
    

def dashboardView(request):
    usuarios_ativos = User.objects.filter(ativo=True).order_by(-id) 
    usuarios_inativos = User.objects.filter(ativo=False).order_by(-id)
    qt_usuarios_ativos =  User.objects.filter(ativo=True).count()
    qt_usuarios_inativos = User.objects.filter(ativo=False).count()

    my_dict = {
        'usuarios_ativos' : usuarios_ativos,
        'usuarios_inativos' : usuarios_inativos,
        'qt_usuarios_ativos' : qt_usuarios_ativos,
        'qt_usuarios_inativos' : qt_usuarios_inativos
    }

    return render(request, 'dashboard.html', context=my_dict)



def alterar_status_usuarios(request):
    if request.method == 'POST':
        cpf = request.POST['cpf']
        usuario = get_object_or_404(User, cpf=cpf)

        # Verifica se a caixa de seleção foi marcada
        if 'check_inativo' in request.POST:
            usuario.ativo = False
        else:
            usuario.ativo = True
        
        usuario.save()

        messages.success(request, 'Status dos usuários atualizado com sucesso.')
        return redirect('nome_da_url')  # Substitua 'nome_da_url' pela URL correta para redirecionamento após a alteração do status
    else:
        messages.error(request, 'Erro ao atualizar o status dos usuários.')
        return redirect('nome_da_url')  # Substitua 'nome_da_url' pela URL correta para redirecionamento em caso de erro
    

def editar_usuario(request, cpf):
    usuario = get_object_or_404(User, cpf=cpf)

    if request.method == 'POST':
        nome = request.POST['nome']
        ativo = request.POST.get('ativo', False)
        data_de_saida = request.POST['data_de_saida']
        telefone = request.POST['telefone']
        email_lsd = request.POST['email_lsd']
        email_pessoal = request.POST['email_pessoal']
        lattes = request.POST['lattes']
        sala = request.POST['sala']
        chave = request.POST.get('chave', False)

        # Atualiza os dados do usuário
        usuario.nome = nome
        usuario.ativo = ativo
        usuario.data_de_saida = data_de_saida
        usuario.telefone = telefone
        usuario.email_lsd = email_lsd
        usuario.email_pessoal = email_pessoal
        usuario.lattes = lattes
        usuario.sala = sala
        usuario.chave = chave
        usuario.save()

        messages.success(request, 'Usuário atualizado com sucesso.')
        return redirect('nome_da_url')  # Substitua 'nome_da_url' pela URL correta para redirecionamento após a edição do usuário

    return render(request, 'editar_usuario.html', {'usuario': usuario})
    # Substitua 'editar_usuario.html' pelo nome do seu template para editar os dados do usuário


@login_required
def pesquisar_usuarios(request):
    query = request.GET.get('q')
    usuarios = []

    if query:
        usuarios = User.objects.filter(
            Q(nome__icontains=query) | Q(cpf__icontains=query)
        )

    return render(request, 'pesquisar_usuarios.html', {'usuarios': usuarios})
    

