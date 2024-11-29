import tkinter as tk
from tkinter import messagebox
from src.database.operacoes_genericas_banco import OperacoesBanco
from src.models.endereco import Endereco
from src.models.apicultor import Apicultor
from src.database.conexao_banco import ConexaoBanco
from src.models.apiario import Apiario

# realize a importação da classe Apiario que vc criou, que encontr-se no arquivo apiario.py
# Siga o modelo das importações das classes Endereco e Apicultor
class MainWindow:
    def __init__(self, root):
        """
        Inicializa a janela principal.
        :param root: Instância da janela principal do tkinter.
        """
        self.root = root
        self.root.title("Gerenciador de Endereços e Usuários")
        self.root.geometry("500x400")
        # Configuração de conexão ao banco de dados
        self.conexao = ConexaoBanco("localhost", "root", "admin", "ApisCoop")
        self.conexao.conectar()
        self.operacoes = OperacoesBanco(self.conexao)
        # Aba de navegação
        self.tab_control = tk.Frame(self.root)
        self.tab_control.pack(fill=tk.BOTH, expand=True)
        self.menu_inicial()
    def menu_inicial(self):
        """
        Cria o menu inicial com opções para gerenciamento de Endereços e Usuários.
        """
        # Limpa o conteúdo atual
        for widget in self.tab_control.winfo_children():
            widget.destroy()
        tk.Label(self.tab_control, text="Gerenciador de Endereços e Apicultores", font=("Arial", 16)).pack(pady=20)
        tk.Button(self.tab_control, text="Gerenciar Endereços", font=("Arial", 14), command=self.menu_enderecos).pack(pady=10)
        tk.Button(self.tab_control, text="Gerenciar Apicultores", font=("Arial", 14), command=self.menu_apicultores).pack(pady=10)
        tk.Button(self.tab_control, text="Gerenciar Apiários", font=("Arial", 14), command=self.menu_apiarios).pack(pady=10)

        # Crie aqui um Botão para Gerenciar Apiários
    def menu_enderecos(self):
        """
        Menu para gerenciar endereços.
        """
        # Limpa o conteúdo atual
        for widget in self.tab_control.winfo_children():
            widget.destroy()
        tk.Label(self.tab_control, text="Gerenciar Endereços", font=("Arial", 16)).pack(pady=10)
        # Formulário de cadastro de endereço
        tk.Label(self.tab_control, text="Logradouro:").pack()
        logradouro_entry = tk.Entry(self.tab_control)
        logradouro_entry.pack()
        tk.Label(self.tab_control, text="Bairro:").pack()
        bairro_entry = tk.Entry(self.tab_control)
        bairro_entry.pack()
        tk.Label(self.tab_control, text="Cidade:").pack()
        cidade_entry = tk.Entry(self.tab_control)
        cidade_entry.pack()
        tk.Label(self.tab_control, text="Estado:").pack()
        estado_entry = tk.Entry(self.tab_control)
        estado_entry.pack()
        tk.Label(self.tab_control, text="CEP:").pack()
        cep_entry = tk.Entry(self.tab_control)
        cep_entry.pack()
        tk.Button(self.tab_control, text="Cadastrar Endereço",
                  command=lambda: self.cadastrar_endereco(
                      logradouro_entry.get(),
                      bairro_entry.get(),
                      cidade_entry.get(),
                      estado_entry.get(),
                      cep_entry.get()
                  )).pack(pady=10)
        tk.Button(self.tab_control, text="Voltar", command=self.menu_inicial).pack(pady=10)
    #Para obter a media 8,0, o aluno deve realizar a cópia de toda a função menu_enderecos e, em seguida, realizar
    # as devidas modificações para que a função sirva para cadastrar um apiario.
    # Para obter a media 10,0, o aluno deve realizar a cópia de toda a função menu_apicultores e, em seguida, realizar
    # as devidas modificações para que a função sirva para cadastrar, excluir, alterar e pesquisar um apiario.
    def menu_apicultores(self):
        """
        Menu para gerenciar usuários.
        """
        # Limpa o conteúdo atual
        for widget in self.tab_control.winfo_children():
            widget.destroy()
        tk.Label(self.tab_control, text="Gerenciar Apicultores", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.tab_control, text="Cadastrar Apicultor", font=("Arial", 12),
                  command=self.formulario_apicultor).pack(pady=5)
        tk.Button(self.tab_control, text="Buscar Apicultor", font=("Arial", 12),
                  command=self.buscar_apicultor).pack(pady=5)
        tk.Button(self.tab_control, text="Atualizar Apicultor", font=("Arial", 12),
                  command=self.atualizar_apicultor).pack(pady=5)
        tk.Button(self.tab_control, text="Excluir Apicultor", font=("Arial", 12),
                  command=self.excluir_apicultor).pack(pady=5)
        tk.Button(self.tab_control, text="Voltar", command=self.menu_inicial).pack(pady=20)
    #A função função Furmulario_apicultor deve ser replicada, após a sua replicação o aluno deve verificar quais são os
    #campus (atributos) que existem na tabela apiario do banco de dados e realizar as devidas modificações.
    def formulario_apicultor(self):
        # Formulário de cadastro de usuário
        for widget in self.tab_control.winfo_children():
            widget.destroy()
        #Por exemplo: Para apiario, o text do tk.Label deve ser substituído para Nome do Apiario
        tk.Label(self.tab_control, text="Nome do Apicultor:").pack()
        nome_entry = tk.Entry(self.tab_control) #nome_entry substituir para nome_apiario_entry
        nome_entry.pack()
        #Para Todos os campos o aluno deve fazer as devidas substituições, ou seja, trocar E-mail por Localização
        tk.Label(self.tab_control, text="E-mail:").pack()
        email_entry = tk.Entry(self.tab_control)#email_entry substituir para localização_entry
        email_entry.pack()
        # o Aluno deve replicar as trêslinhas a seguir e fazer as devidas modificações para receber a informação tamanho
        tk.Label(self.tab_control, text="ID do Endereço:").pack()
        endereco_id_entry = tk.Entry(self.tab_control)
        endereco_id_entry.pack()
        # o Aluno deve criar mais um campo tk.Label, tk.Entry e entry.pack() para trabalhar com a chave estrangeira
        #id_apicultor
        tk.Button(self.tab_control, text="Cadastrar Apicultor",
                  command=lambda: self.cadastrar_apicultor(
                      nome_entry.get(),
                      email_entry.get(),
                      endereco_id_entry.get()
                  )).pack(pady=10)
        tk.Button(self.tab_control, text="Voltar", command=self.menu_inicial).pack(pady=10)
    #A função formulario_apicultor deve replicada para uma nova função chamada formulario_apiario. O aluno deve realizar
    #as devidas modificações para que a função consiga mostrar os devidos campos
    # Para não se confundir, o aluno pode realizar as modificações na função cadastrar_endereco, ou seja, substituir para
    # cadastrar_apiario
    def cadastrar_endereco(self, logradouro, bairro, cidade, estado, cep): # os parametros devem ser os do apiario
        """
        Cadastra um novo endereço no banco de dados.
        """
        if not logradouro or not bairro or not cidade or not estado or not cep:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return
        #onde aparecer endereco substitua para apiario e os parametros devem ser do apiario
        endereco = Endereco(logradouro, bairro, cidade, estado, cep)
        self.operacoes.inserir("endereco", ["logradouro", "bairro", "cidade", "estado", "cep"],
                               [logradouro, bairro, cidade, estado, cep])
        messagebox.showinfo("Sucesso", "Endereço cadastrado com sucesso!")
    # Para não se confundir, o aluno pode realizar as modificações na função buscar_endereco, ou seja, substituir para
    # buscar_apiario
    def buscar_endereco(self):
        """
        Abre um formulário para buscar um endereço pelo ID.
        """
        for widget in self.tab_control.winfo_children():
            widget.destroy()
        #adaptar o text do tk.Label para Buscar Apiario
        tk.Label(self.tab_control, text="Buscar Endereço", font=("Arial", 16)).pack(pady=10)
        # adaptar o text do tk.Label para ID do Apiário
        tk.Label(self.tab_control, text="ID do Endereço:").pack()
        id_entry = tk.Entry(self.tab_control)
        id_entry.pack()
        # Na função realizar_busca(), o aluno deve modificar para os campos para que eles recebam as informações da tabela
        # apiario. Muito cuidado coms os nomes dos campos, verifique os nomes na tabela apiario do banco de dados.
        def realizar_busca():
            try:
                id_endereco = int(id_entry.get())
                endereco = self.operacoes.buscar_por_id("endereco", "id_endereco", id_endereco)
                if endereco:
                    result_text = f"Logradouro: {endereco['logradouro']}\n" \
                                  f"Bairro: {endereco['bairro']}\n" \
                                  f"Cidade: {endereco['cidade']}\n" \
                                  f"Estado: {endereco['estado']}\n" \
                                  f"CEP: {endereco['cep']}"
                    messagebox.showinfo("Resultado da Busca", result_text)
                else:
                    messagebox.showinfo("Resultado da Busca", "Endereço não encontrado.")
            except ValueError:
                messagebox.showerror("Erro", "O ID deve ser um número.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao buscar endereço: {e}")
        tk.Button(self.tab_control, text="Buscar", command=realizar_busca).pack(pady=10)
        tk.Button(self.tab_control, text="Voltar", command=self.menu_enderecos).pack(pady=10)
    # Na função atualizar_endereco(), o aluno deve modificar a função para que os campos recebam as informações
    # da tabela apiario. Substitua o nome atualizar_endereco() para atualizar_apiario(). Depois faça as modificações para
    # lidar com os campos da tabela apiario.
    def atualizar_endereco(self):
        """
        Abre um formulário para atualizar um endereço.
        """
        for widget in self.tab_control.winfo_children():
            widget.destroy()
        tk.Label(self.tab_control, text="Atualizar Endereço", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.tab_control, text="ID do Endereço:").pack()
        id_entry = tk.Entry(self.tab_control)
        id_entry.pack()
        tk.Label(self.tab_control, text="Novo Logradouro:").pack()
        logradouro_entry = tk.Entry(self.tab_control)
        logradouro_entry.pack()
        tk.Label(self.tab_control, text="Novo Bairro:").pack()
        bairro_entry = tk.Entry(self.tab_control)
        bairro_entry.pack()
        tk.Label(self.tab_control, text="Nova Cidade:").pack()
        cidade_entry = tk.Entry(self.tab_control)
        cidade_entry.pack()
        tk.Label(self.tab_control, text="Novo Estado:").pack()
        estado_entry = tk.Entry(self.tab_control)
        estado_entry.pack()
        tk.Label(self.tab_control, text="Novo CEP:").pack()
        cep_entry = tk.Entry(self.tab_control)
        cep_entry.pack()
        #Na função a seguir adapte os campos para aparecerem as informações do apiario.
        def realizar_atualizacao():
            try:
                id_endereco = int(id_entry.get())
                dados = {
                    "logradouro": logradouro_entry.get() or None,
                    "bairro": bairro_entry.get() or None,
                    "cidade": cidade_entry.get() or None,
                    "estado": estado_entry.get() or None,
                    "cep": cep_entry.get() or None
                }
                # Remove campos vazios
                dados = {key: value for key, value in dados.items() if value is not None}
                if not dados:
                    messagebox.showwarning("Aviso", "Nenhum dado foi fornecido para atualização.")
                    return
                self.operacoes.atualizar("endereco", "id_endereco", id_endereco, dados)
                messagebox.showinfo("Sucesso", "Endereço atualizado com sucesso!")
                self.menu_enderecos()
            except ValueError:
                messagebox.showerror("Erro", "O ID deve ser um número.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao atualizar endereço: {e}")
        tk.Button(self.tab_control, text="Atualizar", command=realizar_atualizacao).pack(pady=10)
        tk.Button(self.tab_control, text="Voltar", command=self.menu_enderecos).pack(pady=10)
    # Na função excluir_endereco(), o aluno deve modificar a função para que os campos recebam as informações
    # da tabela apiario. Substitua o nome excluir_endereco() para excluir_apiario(). Depois faça as modificações para
    # lidar com os campos da tabela apiario.
    def excluir_endereco(self):
        """
        Abre um formulário para excluir um endereço pelo ID.
        """
        for widget in self.tab_control.winfo_children():
            widget.destroy()
        tk.Label(self.tab_control, text="Excluir Endereço", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.tab_control, text="ID do Endereço:").pack()
        id_entry = tk.Entry(self.tab_control)
        id_entry.pack()
        def realizar_exclusao():
            try:
                id_endereco = int(id_entry.get())
                self.operacoes.excluir("endereco", "id_endereco", id_endereco)
                messagebox.showinfo("Sucesso", "Endereço excluído com sucesso!")
                self.menu_enderecos()
            except ValueError:
                messagebox.showerror("Erro", "O ID deve ser um número.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao excluir endereço: {e}")
        tk.Button(self.tab_control, text="Excluir", command=realizar_exclusao).pack(pady=10)
        tk.Button(self.tab_control, text="Voltar", command=self.menu_enderecos).pack(pady=10)
    #Se o aluno fez todas as modificações nas funções anteriores que lidam com endereço, a tarefa foi concluida e o
    #Software deve funcionar. Observação: verifique como estão as funções para o apicultor para que as modificações an-
    #teriores temham sucesso.
    
    def cadastrar_apicultor(self, nome, email, endereco_id):
        """
        Cadastra um novo usuário no banco de dados.
        """
        if not nome or not email or not endereco_id:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return
        try:
            endereco_id = int(endereco_id)
        except ValueError:
            messagebox.showerror("Erro", "O ID do Endereço deve ser um número.")
            return
        apicultor = Apicultor(nome, email, endereco_id)
        self.operacoes.inserir("apicultor", ["nome_apicultor", "email", "endereco"], [nome, email, endereco_id])
        messagebox.showinfo("Sucesso", "Apicultor cadastrado com sucesso!")

    def buscar_apicultor(self):
        """
        Abre um formulário para buscar um usuário pelo ID.
        """
        for widget in self.tab_control.winfo_children():
            widget.destroy()
        tk.Label(self.tab_control, text="Buscar Apicultor", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.tab_control, text="ID do Apicultor:").pack()
        id_entry = tk.Entry(self.tab_control)
        id_entry.pack()
        def realizar_busca():
            try:
                id_apicultor = int(id_entry.get())
                apicultor = self.operacoes.buscar_por_id("apicultor", "id_apicultor", id_apicultor)
                if apicultor:
                    result_text = f"Nome: {apicultor['nome_apicultor']}\n" \
                                  f"E-mail: {apicultor['email']}\n" \
                                  f"ID Endereço: {apicultor['endereco']}"
                    messagebox.showinfo("Resultado da Busca", result_text)
                else:
                    messagebox.showinfo("Resultado da Busca", "Apicultor não encontrado.")
            except ValueError:
                messagebox.showerror("Erro", "O ID deve ser um número.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao buscar apicultor: {e}")
        tk.Button(self.tab_control, text="Buscar", command=realizar_busca).pack(pady=10)
        tk.Button(self.tab_control, text="Voltar", command=self.menu_apicultores).pack(pady=10)
    def atualizar_apicultor(self):
        """
        Abre um formulário para atualizar um apicultor.
        """
        for widget in self.tab_control.winfo_children():
            widget.destroy()
        tk.Label(self.tab_control, text="Atualizar Apicultor", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.tab_control, text="ID do apicultor:").pack()
        id_entry = tk.Entry(self.tab_control)
        id_entry.pack()
        tk.Label(self.tab_control, text="Novo Nome:").pack()
        nome_entry = tk.Entry(self.tab_control)
        nome_entry.pack()
        tk.Label(self.tab_control, text="Novo E-mail:").pack()
        email_entry = tk.Entry(self.tab_control)
        email_entry.pack()
        tk.Label(self.tab_control, text="Novo ID do Endereço:").pack()
        endereco_id_entry = tk.Entry(self.tab_control)
        endereco_id_entry.pack()
        def realizar_atualizacao():
            try:
                id_apicultor = int(id_entry.get())
                dados = {
                    "nome_apicultor": nome_entry.get() or None,
                    "email": email_entry.get() or None,
                    "endereco": endereco_id_entry.get() or None,
                }
                # Remove campos vazios
                dados = {key: value for key, value in dados.items() if value is not None}
                if not dados:
                    messagebox.showwarning("Aviso", "Nenhum dado foi fornecido para atualização.")
                    return
                # Converte endereco para inteiro se fornecido
                if "endereco" in dados:
                    try:
                        dados["endereco"] = int(dados["endereco"])
                    except ValueError:
                        messagebox.showerror("Erro", "O ID do Endereço deve ser um número.")
                        return
                self.operacoes.atualizar("apicultor", "id_apicultor", id_apicultor, dados)
                messagebox.showinfo("Sucesso", "Apicultor atualizado com sucesso!")
                self.menu_apicultores()
            except ValueError:
                messagebox.showerror("Erro", "O ID do Apicultor deve ser um número.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao atualizar apicultor: {e}")
        tk.Button(self.tab_control, text="Atualizar", command=realizar_atualizacao).pack(pady=10)
        tk.Button(self.tab_control, text="Voltar", command=self.menu_apicultores).pack(pady=10)
    def excluir_apicultor(self):
        """
        Abre um formulário para excluir um usuário pelo ID.
        """
        for widget in self.tab_control.winfo_children():
            widget.destroy()
        tk.Label(self.tab_control, text="Excluir Apicultor", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.tab_control, text="ID do Apicultor:").pack()
        id_entry = tk.Entry(self.tab_control)
        id_entry.pack()
        def realizar_exclusao():
            try:
                id_apicultor = int(id_entry.get())
                # Confirmação antes de excluir
                confirmar = messagebox.askyesno("Confirmação",
                                                f"Tem certeza de que deseja excluir o apicultor com ID {id_apicultor}?")
                if not confirmar:
                    return
                self.operacoes.excluir("apicultor", "id_apicultor", id_apicultor)
                messagebox.showinfo("Sucesso", "Apicultor excluído com sucesso!")
                self.menu_apicultores()
            except ValueError:
                messagebox.showerror("Erro", "O ID do Apicultor deve ser um número.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao excluir apicultor: {e}")
        tk.Button(self.tab_control, text="Excluir", command=realizar_exclusao).pack(pady=10)
        tk.Button(self.tab_control, text="Voltar", command=self.menu_apicultores).pack(pady=10)

    def menu_apiarios(self):
        for widget in self.tab_control.winfo_children():
            widget.destroy()
        tk.Label(self.tab_control, text="Gerenciar Apiários", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.tab_control, text="Cadastrar Apiário", font=("Arial", 12),
                  command=self.formulario_apiario).pack(pady=5)
        tk.Button(self.tab_control, text="Buscar Apiário", font=("Arial", 12),
                  command=self.buscar_apiario).pack(pady=5)
        tk.Button(self.tab_control, text="Atualizar Apiário", font=("Arial", 12),
                  command=self.atualizar_apiario).pack(pady=5)
        tk.Button(self.tab_control, text="Excluir Apiário", font=("Arial", 12),
                  command=self.excluir_apiario).pack(pady=5)
        tk.Button(self.tab_control, text="Voltar", command=self.menu_inicial).pack(pady=20)

    def formulario_apiario(self):
        for widget in self.tab_control.winfo_children():
            widget.destroy()

        tk.Label(self.tab_control, text="Nome do Apiário:").pack()
        nome_apiario_entry = tk.Entry(self.tab_control)
        nome_apiario_entry.pack()

        tk.Label(self.tab_control, text="Localização:").pack()
        localizacao_entry = tk.Entry(self.tab_control)
        localizacao_entry.pack()

        tk.Label(self.tab_control, text="ID do Apicultor:").pack()
        apicultor_id_entry = tk.Entry(self.tab_control)
        apicultor_id_entry.pack()

        tk.Label(self.tab_control, text="Tamanho do Apiário:").pack()
        tamanho_entry = tk.Entry(self.tab_control)
        tamanho_entry.pack()

        tk.Button(self.tab_control, text="Cadastrar Apiário",
                  command=lambda: self.cadastrar_apiario(
                      nome_apiario_entry.get(),
                      localizacao_entry.get(),
                      tamanho_entry.get(),
                      apicultor_id_entry.get(),
                  )).pack(pady=10)

        tk.Button(self.tab_control, text="Voltar", command=self.menu_inicial).pack(pady=10)

    def cadastrar_apiario(self, nome_apiario, localizacao, tamanho, id_produtor):
        try:

            print(id_produtor)
            self.operacoes.inserir("apiario", ['nome_apiario', 'localizacao', 'tamanho', 'id_produtor'],
                                   [nome_apiario, localizacao, tamanho, id_produtor]
                                   )

            messagebox.showinfo("Sucesso", "Apiário cadastrado com sucesso!")

            self.menu_inicial()

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar apiário: {e}")

    def buscar_apiario(self):
        for widget in self.tab_control.winfo_children():
            widget.destroy()
        tk.Label(self.tab_control, text="Buscar Apiário", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.tab_control, text="ID do Apiário:").pack()
        id_entry = tk.Entry(self.tab_control)
        id_entry.pack()

        def realizar_busca():
            try:
                id_apiario = int(id_entry.get())
                apiario = self.operacoes.buscar_por_id("apiario", "id_apiario", id_apiario)
                print(id_apiario)
                if apiario:
                    result_text = f"Nome: {apiario['nome_apiario']}\n" \
                                  f"Localização: {apiario['localizacao']}\n" \
                                  f"Apicultor ID: {apiario['id_produtor']}"
                    messagebox.showinfo("Resultado da Busca", result_text)
                else:
                    messagebox.showinfo("Resultado da Busca", "Apiário não encontrado.")
            except ValueError:
                messagebox.showerror("Erro", "O ID deve ser um número.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao buscar apiário: {e}")

        tk.Button(self.tab_control, text="Buscar", command=realizar_busca).pack(pady=10)
        tk.Button(self.tab_control, text="Voltar", command=self.menu_apiarios).pack(pady=10)

    def atualizar_apiario(self):
        for widget in self.tab_control.winfo_children():
            widget.destroy()
        tk.Label(self.tab_control, text="Atualizar Apiário", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.tab_control, text="ID do Apiário:").pack()
        id_entry = tk.Entry(self.tab_control)
        id_entry.pack()

        tk.Label(self.tab_control, text="Novo Nome:").pack()
        nome_entry = tk.Entry(self.tab_control)
        nome_entry.pack()

        tk.Label(self.tab_control, text="Nova Localização:").pack()
        localizacao_entry = tk.Entry(self.tab_control)
        localizacao_entry.pack()

        tk.Label(self.tab_control, text="Novo Tamanho:").pack()
        tamanho_entry = tk.Entry(self.tab_control)
        tamanho_entry.pack()

        def realizar_atualizacao():
            try:
                id_apiario = int(id_entry.get())
                dados = {
                    "nome_apiario": nome_entry.get() or None,
                    "localizacao": localizacao_entry.get() or None,
                    "tamanho": tamanho_entry.get() or None
                }
                dados = {key: value for key, value in dados.items() if value is not None}
                if not dados:
                    messagebox.showwarning("Aviso", "Nenhum dado foi fornecido para atualização.")
                    return
                self.operacoes.atualizar("apiario", "id_apiario", id_apiario, dados)
                messagebox.showinfo("Sucesso", "Apiário atualizado com sucesso!")
                self.menu_apiarios()
            except ValueError:
                messagebox.showerror("Erro", "O ID deve ser um número.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao atualizar apiário: {e}")

        tk.Button(self.tab_control, text="Atualizar", command=realizar_atualizacao).pack(pady=10)
        tk.Button(self.tab_control, text="Voltar", command=self.menu_apiarios).pack(pady=10)

    def excluir_apiario(self):
        for widget in self.tab_control.winfo_children():
            widget.destroy()

        tk.Label(self.tab_control, text="Excluir Apiário", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.tab_control, text="ID do Apiário:").pack()
        id_entry = tk.Entry(self.tab_control)
        id_entry.pack()

        def realizar_exclusao():
            try:
                id_apiario = int(id_entry.get())
                apiario = self.operacoes.buscar_por_id("apiario", "id_apiario", id_apiario)

                if apiario:
                    self.operacoes.excluir("apiario", "id_apiario", id_apiario)
                    messagebox.showinfo("Sucesso", "Apiário excluído com sucesso!")
                    self.menu_inicial()
                else:
                    messagebox.showinfo("Erro", "Apiário não encontrado.")
            except ValueError:
                messagebox.showerror("Erro", "O ID deve ser um número.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao excluir apiário: {e}")

        tk.Button(self.tab_control, text="Excluir", command=realizar_exclusao).pack(pady=10)
        tk.Button(self.tab_control, text="Voltar", command=self.menu_inicial).pack(pady=10)
