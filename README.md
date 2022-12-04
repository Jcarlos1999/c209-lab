# **Background Substraction**

  ## Precisará instalar o Open CV para python
  
  *  `pip install opencv-python`
  *  Precisará de algum video, no repositorio ja existe um, caso queira usa-lo
  *  Depois de concluir é só dar o comando `python .\backgroundSubtraction.py`


A imagem a baixo mostra como é o processo de background Substractor

[IMG](https://drive.google.com/file/d/1K6yFVWecqenOxNTB7hulNLdm2MvyXW8x/view?usp=sharing)

Na imagem temos duas fotos, uma do frame atual(currentFrame) e uma do modelo de background(background model).Fazendo uma subtração pixel a pixel da imagem e depois verificando se o resultado é maior que um limiar(threshold) aquele pixel é setado com branco, caso não for é setado como preto, assim formando uma imagem binaria e nos gerando uma foreground mask.

A partir dessa foreground mask é possivel identificar movimentos a partir da comparação
entre os frames de um video por exemplo.
