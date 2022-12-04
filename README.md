# **Background Substraction**

  ## Precisará instalar o Open CV para python
  
  *  `pip install opencv-python`
  *  Precisará de algum video, no repositorio ja existe um, caso queira usa-lo
  *  Depois de concluir é só dar o comando `python .\backgroundSubtraction.py`


A imagem a baixo mostra como é o processo de background Substractor

![IMG](https://user-images.githubusercontent.com/52891219/205521911-f0c03073-a928-4505-bb13-9e21e4234a51.PNG)

Na imagem temos duas fotos, uma do frame ***atual(currentFrame)*** e uma do modelo de ***background(background model)***. Fazendo uma subtração pixel a pixel da imagem e depois verificando se o resultado é maior que um 
***limiar(threshold)*** aquele pixel é setado como branco, caso não for é setado como preto, assim formando uma imagem binaria e nos gerando uma foreground mask.

A partir dessa foreground mask é possivel identificar movimentos a partir da comparação entre os frames de um video por exemplo.

![IMG2](https://user-images.githubusercontent.com/52891219/205522185-d2f428c9-8f51-48b9-b039-f42d42b7d1df.PNG)

Acima vemos a diferença entre diferente valroes de threshold, quanto maior menor será a quantidade de pixels detectados(pixels brancos), então é sempre bom achar um meio termo, mas sempre irá depender dos frames no qual está avaliando.

