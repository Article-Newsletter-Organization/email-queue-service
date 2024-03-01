# email-queue-consumer

Serviço responsável por enviar e-mails contendo os artigos para os inscritos no newsletter.

# Script story

- Checar a conexão com os serviços, como banco de dados e mensageria
- Observar uma fila na mensageria
- Receber uma mensagem
- Pegar as informações da mensagem, verificar se são válidas e se estão formatada como o esperado
- Verificar se a publicação recebido pela mensagem existe
- Listar todos os inscritos com o e-mail verificado
- Tentar enviar um e-mail com o arquivo PDF do artigo em anexo
- Caso dê algum erro, deve ser usado uma técnica de tracesing para rastrear os motivos pelo log e atualizando a situação 
da publicação no banco de dados
- Caso dê tudo certo, atualizar a situação da publicação