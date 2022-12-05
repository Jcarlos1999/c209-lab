# **Background Substraction**
  
  ## O que é preciso para utilizar esse código
  
  *  instalar o OpenCV `pip install opencv-python`
  *  Precisará de algum video, no repositorio ja existe um, caso queira usa-lo
  *  Depois de concluir é só dar o comando `python .\backgroundSubtraction.py`
  
  ## O que é background Substraction
   São tecnicas de computação gráfica que permite detectar a(s) diferença(s) entre duas imagens ou em uma sequencia de imagens, muito usada para fazer dectação de movimento.
   
Essa é a equação do background substraction

![equation](https://user-images.githubusercontent.com/52891219/205524459-063093c3-3baa-4337-b941-a4003bf8814d.png)

A imagem a baixo mostra como é o processo de background Substractor

![IMG](https://user-images.githubusercontent.com/52891219/205521911-f0c03073-a928-4505-bb13-9e21e4234a51.PNG)

Na imagem temos duas fotos, uma do frame ***atual(currentFrame)*** e uma do modelo de ***background(background model)***. Fazendo uma subtração pixel a pixel da imagem e depois verificando se o resultado é maior que um 
***limiar(threshold)*** aquele pixel é setado como branco, caso não for é setado como preto, assim formando uma imagem binaria e nos gerando uma foreground mask.

A partir dessa foreground mask é possivel identificar movimentos a partir da comparação entre os frames de um video por exemplo.

![IMG2](https://user-images.githubusercontent.com/52891219/205522185-d2f428c9-8f51-48b9-b039-f42d42b7d1df.PNG)

Acima vemos a diferença entre diferente valroes de threshold, quanto maior menor será a quantidade de pixels detectados(pixels brancos), então é sempre bom achar um meio termo, mas sempre irá depender dos frames no qual está avaliando.

### Links

Nesse código usei a biblioteca do OpenCV que já trás uma abstração grande dos algoritmos para fazer as detecções, mas vou deixar dois links que explicam sobre os algoritmo

  * [KNN](https://www.analyticsvidhya.com/blog/2021/04/simple-understanding-and-implementation-of-knn-algorithm/)
  * [MOG](https://www.sciencedirect.com/topics/engineering/background-subtraction)
  * [What is background substraction](https://www.youtube.com/watch?v=fn07iwCrvqQ)


### João Carlos Rodrigues Franco
