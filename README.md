## Nomade Data

##### Sobre o projeto
Criamos um SCORE de RISCO DE CRÉDITO para MEIOS DE HOSPEDAGEM, analisando métricas específica do mercado de turismo.

Para isso, criamos metodos se capturar informações externas como booking, tripadvisor, serasa, reclame aqui, pagerank (google), etc.

O foco do projeto é oferecer mais segurança para financeiras realizar empréstimos para um mercado que está com dificuldades de aprovação de crédito.

Para isso foi identificado alguns sistemas facilitadores que auxiliaram no preenchimento, reduzindo assim o input manual dos dados. Sao eles:
* 1 - Extrair e armazenar Dados cadastrais na API da Receita Federal
* 2 - Busca informações específica do setor (Booking, TripAdvisor)
* 2 - Busca informações sobre avaliações de quartos (Booking, TripAdvisor)
* 3 - Informações finananceiras do Serasa
* 4 - Analise de sentimento dos clientes nas redes sociais (nao desenvolvido)
* 5 - geração do score (não integrado com o google functions)

Todos os códigos foram clonados no Google Cloud, e estão aberta ao público.

![Arq](/arq.jpg)

##### APIs e comunicação (POST)

https://us-central1-hackgetnet-team56.cloudfunctions.net/add_serasa_score

https://us-central1-hackgetnet-team56.cloudfunctions.net/business_info

https://us-central1-hackgetnet-team56.cloudfunctions.net/crawler_booking 

https://us-central1-hackgetnet-team56.cloudfunctions.net/nomade_score 

https://us-central1-hackgetnet-team56.cloudfunctions.net/save_booking_score 


##### Tecnologias utilizadas
* [Google Cloud Plataform] - Microserviços
* [Python 3.8] - Backend
* [NodeJS 12] - Backend


##### Links
Vídeo demo: https://github.com/Nomade-Data/gcp-microservices.git

Vídeo pitch: https://www.youtube.com/watch?v=I2QXmjBn4Yc

PPT: 


##### Grupo
| Nome | GitHub | Email
|---|---|---|
| Eduardo Dias |  @eduardodiasm | carloseduardodiasm@gmail.com |
| Gustavo Franco  | @gfrancodev  | guatvojorgee2511@gmail.com |
| Igor Lima | @igor17400 | igorlima1740@gmail.com |
| Thales Gibbon | @thalesgibbon | thales.gibbon@gmail.com |
| Nicolle | @  | @ |
