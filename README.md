# Planilha de Conta - API



# Autenticação

  Autenticação para acesso a lista de contas e formulário de cadastro.
  
  **POST**: /autenticacao
  
  **HEADER**
  
    { "Content-Type": "application/json" }
    
  **BODY**
  
    { "username": "usuario", "password": "123456" }
  
  
  **Sucesso 200 Ok**
  
    { "key": "91e9f8beb6c9e544f349b545161a811607b88310" }
  
      
# Lista

  **GET**: /lista
  
  **HEADER**
  
    { "Authorization": "token 91e9f8beb6c9e544f349b545161a811607b88310" }
  
  
  **Sucesso 200 Ok**
  
    [
      {
          "nome": "Job",
          "valor": "1555.99"
      },
      {
          "nome": "Pagamento",
          "valor": "-545.89"
      }
    ]


# Formulário

  **POST**: /formulario
  
  **HEADER**
    { "Authorization": "token 91e9f8beb6c9e544f349b545161a811607b88310" }
  
  **BODY**
  
    { "nome": "Job", "valor": 1555.99, "tipo":"Entrada" }
      
  Obs.: No campo tipo deverá ser informado: **Entrada** ou **Saída**
    
  **Sucesso 201 Created**
  
    { "nome": "Job", "valor": 1555.99 }
  
  
  
# Acesso pelo browser

A API pode ser acessada pelo browser para testes utilizando as mesmas URLs.
