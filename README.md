# Câmeras de São João del-Rei

Para resolver o problema das câmeras, foi usada uma heurística para a solução do problema de cobertura de vértices. Dado o mapa, cada esquina é representada como um vértice, e cada rua, como uma aresta. O objetivo torna-se, assim, determinar o menor número de vértices que formam um conjunto capaz de abranger todas as arestas. 

Para isso, foi utilizada uma heurística gulosa: a cada iteração, o vértice com maior grau é escolhido. As arestas abrangidas por ele são, então, eliminadas. Isso é repetido até que todas as arestas do grafo tenham sido alcançadas.

No final, são mostradas as esquinas e as ruas abrangidas por cada uma delas.

## Execução

```
python3 main.py <arquivo_gml>
```

