1. A equipe deverá entregar um relatório no formato pdf

2. Abra o repositório no Codespaces

3. Crie um servidor web em Flask (Python) que exiba veis, ao ser acessado, as seguintes
informações do sistema:
(a) O nome completo dos integrantes da equipe 🟢
(b) O PID (Process ID) do processo que executa o servidor 🟢
(c) A quantidade de memória utilizada pelo processo (em MB) 🟢
(d) O uso de CPU (%) 🟢
(e) O sistema operacional detectado (por exemplo: Linux, Ubuntu, etc.) 🟢
(f) Dica: utilize os módulos os, platform e psutil.
Exemplo de saída:
Nome: Ana Silva e João das Couves
PID: 1423
Memória usada: 25.6 MB
CPU: 3.4%
Sistema Operacional: Linux (Ubuntu)

4. Crie duas rotas: /info e /metricas, onde:
• /info: Mostra o nome dos integrantes da equipe 🟢
• /metricas: Retorna o conteúdo, no formato JSON, as informações solicitadas no
Item 3 🟢

5. Criação do Web Service
Crie um novo Web Service no https://render.com/ e conecte ao repositório do GitHub.
Configure:
• Linguagem: Python 3
• Comando de inicialização: gunicorn app:APP
• Tipo de instância: Free
• Branch: main

6. Seu relatório deverá conter os seguintes itens:

Nome completo dos integrantes

Link para a aplicação hospedada no Render e do repositório
• Se o repositório for privado, adicione o usuário hrchlhck

Descrição resumida dos passos realizados

Printscreens de:
• Saída JSON da rota /info no navegador
• Saída JSON da rota /metricas no navegador
• Configuração no Render

Uma análise final (5 – 8 linhas) respondendo: “Quais aspectos de um sistema opera-
cional ainda são perceptíveis quando se utiliza um serviço PaaS, e o que é completa-
mente abstraído?”