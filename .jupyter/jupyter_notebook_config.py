# Jupyter Notebook Configuration

c = get_config()

# Configurações de segurança
c.NotebookApp.token = ""
c.NotebookApp.password = ""

# Abre o navegador automaticamente
c.NotebookApp.open_browser = True

# IP e porta padrão
c.NotebookApp.ip = "localhost"
c.NotebookApp.port = 8888

# Permite recarregar extensões sem reiniciar
c.NotebookApp.nbserver_extensions = {}

# Aumenta o tamanho máximo do upload
c.NotebookApp.max_buffer_size = 20971520  # 20MB
