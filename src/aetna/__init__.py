"""
Diretório base do projeto, onde estão os modulos base:

- cli: módulo responsável por lidar com a interface de linha de comando (CLI) do projeto, 
  permitindo que os usuários interajam com o sistema por meio de comandos no terminal.

- engine: módulo que contém a lógica central do projeto, a engine de orquestração dos agentes, 
  onde estão implementados os principais algoritmos e funcionalidades que fazem o sistema funcionar.

- providers: módulo que contém as integrações com provedores de modelos de linguagem.

- tools: módulo que contém as ferramentas utilizadas pelos agentes.

- main: módulo que contém o ponto de entrada da aplicação, onde a execução do programa começa.
"""

from aetna import (
    cli,
    engine,
    providers,
    tools,
    main
)

__all__ = [
    'cli',
    'engine',
    'providers',
    'tools',
    'main'
]