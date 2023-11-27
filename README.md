# :ocean: Fluxo máximo

Dado um grafo direcionado e ponderado, o programa consegue calcular o fluxo máximo
que parte de um vértice `s` e atinge um vértice `t`. Também é suportada a 
indicação de um fluxo inicial `f`.

A execução deve ser feita da seguinte forma

```
python3 main.py -s <vertice_s> -t <vertice_t> -f <fluxo_inicial> <arquivo_arestas>
```

> O parâmetro `-f` não é obrigatório. Se não for indicado, receberá o valor 0.
Além disso, o arquivo de arestas deve conter uma lista composta por linhas, 
cada uma representando uma aresta e com a forma `origem destino capacidade`.

Finalizada a execução, é mostrado um único valor: o fluxo máximo.
