# **Background Substraction**

  ## Precisará instalar o Open CV para python
  
  *  `pip install opencv-python`
  *  Precisará de algum video, no repositorio ja existe um, caso queira usa-lo
  *  Depois de concluir é só dar o comando `python .\backgroundSubtraction.py`


A imagem a baixo mostra como é o processo de background Substractor

[IMG](https://www.google.com/url?sa=i&url=https%3A%2F%2Fdocs.opencv.org%2F4.x%2Fd1%2Fdc5%2Ftutorial_background_subtraction.html&psig=AOvVaw2fxHwsIe1KqELADeZUVsl8&ust=1670282059377000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCKjMw9iL4fsCFQAAAAAdAAAAABAE)

Na imagem temos duas fotos, uma do frame **atual(currentFrame)** e uma do modelo de **background(background model)**.Fazendo uma subtração pixel a pixel da imagem e depois verificando se o resultado é maior que um 
**limiar(threshold)** aquele pixel é setado com branco, caso não for é setado como preto, assim formando uma imagem binaria e nos gerando uma foreground mask.

A partir dessa foreground mask é possivel identificar movimentos a partir da comparação
entre os frames de um video por exemplo.
