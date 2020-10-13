## Nomade Data

##### Sobre o projeto
Criamos um SCORE de RISCO DE CRÉDITO para MEIOS DE HOSPEDAGEM, analisando métricas específicas do mercado de turismo.

Para isso, criamos métodos de capturar informações externas como booking, tripadvisor, serasa, reclame aqui, pagerank (google), etc.

O foco do projeto é oferecer mais segurança para financeiras realizarem empréstimos para um mercado que está com dificuldades de aprovação de crédito.

Para isso, foram identificado alguns sistemas facilitadores que auxiliaram no preenchimento, reduzindo assim o input manual dos dados. São eles:
* 1 - Extrair e armazenar dados cadastrais na API da Receita Federal.
* 2 - Buscar informações específica do setor (Booking, TripAdvisor).
* 3 - Buscar informações sobre avaliações de quartos (Booking, TripAdvisor).
* 4 - Extrair informações finananceiras do Serasa.

Todos os códigos foram clonados no Google Cloud, e estão abertos ao público.

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
Microserviços: https://github.com/Nomade-Data/gcp-microservices.git

Vídeo demo: https://www.youtube.com/watch?v=I2QXmjBn4Yc

PPT: 


##### Grupo
| Nome | GitHub | Email
|---|---|---|
| Eduardo Dias |  @eduardodiasm | carloseduardodiasm@gmail.com |
| Gustavo Franco  | @gfrancodev  | guatvojorgee2511@gmail.com |
| Igor Lima | @igor17400 | igorlima1740@gmail.com |
| Thales Gibbon | @thalesgibbon | thales.gibbon@gmail.com |
| Nicolle | @  | @ |
