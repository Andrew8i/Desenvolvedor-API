📌 Descrição
Esta API RESTful foi desenvolvida utilizando Flask e Flask-RESTful para gerenciar uma lista de desenvolvedores e suas respectivas habilidades. A API permite criar, modificar, buscar e excluir tanto desenvolvedores quanto habilidades.

🚀 Funcionalidades
Gerenciamento de Desenvolvedores:

📌 GET /<int:id>/ - Obtém um desenvolvedor pelo ID.

✏️ PUT /<int:id>/ - Modifica um desenvolvedor existente.

❌ DELETE /<int:id>/ - Remove um desenvolvedor pelo ID.

➕ POST / - Adiciona um novo desenvolvedor se suas habilidades constarem na lista de habilidades disponíveis.

📜 GET / - Retorna a lista de todos os desenvolvedores cadastrados.

Gerenciamento de Habilidades:

📜 GET /habilidades/ - Retorna todas as habilidades disponíveis.

➕ POST /habilidades/ - Adiciona uma nova habilidade à lista.

✏️ PUT /habilidades/<int:id> - Modifica uma habilidade existente pelo ID.

❌ DELETE /habilidades/<int:id> - Remove uma habilidade pelo ID.

🛠 Tecnologias
Python

Flask

Flask-RESTful