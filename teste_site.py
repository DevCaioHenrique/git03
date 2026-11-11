  GNU nano 7.2                      teste_site.py                               
 print("Teste 1: Arquivo HTML encontrado!")

# Ler o conteúdo do HTML
 html = arquivo.read_text(encoding="utf-8").lower()

# Teste 2: verificar a tag HTML
 assert "<html" in html, "ERRO: Tag HTML ausente!"
 print("Teste 2: Tag HTML encontrada!")

# Teste 3: verificar o titulo da pagina
 assert "<title>" in html, "ERRO: Titulo ausente!"
 assert "</title>" in html, "ERRO: Fechamento do titulo ausente!"
 print("Teste 3: Titulo encontrado!")

# Teste 4: verificar o fechamento do HTML
 assert "</html>" in html, "ERRO: Fechamento HTML ausente!"
 print("Teste 4: Fechamento HTML encontrado!")

print("SUCESSO: Todos os testes passaram!")

