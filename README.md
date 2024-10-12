# FlappybirdAi
> [!IMPORTANT]
> ### Dependencias :
> - pytorch
> - pygame
> - random

### Descripción :
Este proyecto se trata de un entorno al estilo flappy bird, que utiliza un algoritmo genetico para ir evolucionando una IA.
La IA es un perceptron implementado con pytorch.
Para el algoritmo genetico cada individuo tiene dos genomas :
- los pesos
- el bias

En caso de que al finalizar la ejecución un individuo haya obtenido un score (fitness) de 3600, que es 1 minuto aproximadamente, su IA se guardará en formato ONNX
