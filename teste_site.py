from pathlib import Path

# Supondo que o arquivo HTML que você está testando se chame "index.html" ou similar:
# Ajuste o nome do arquivo abaixo caso seja diferente no seu projeto.
caminho_arquivo = Path("index.html")

if caminho_arquivo.exists():
    print("Teste 1: Arquivo HTML encontrado!")
    
    # Ler o conteúdo do HTML
    html = caminho_arquivo.read_text(encoding="utf-8").lower()

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
else:
    raise FileNotFoundError(f"O arquivo {caminho_arquivo} não foi encontrado para os testes.")
