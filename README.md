# 📊 Projeto: Algoritmo Genético para Criptoaritmética  

### **Descrição do Projeto**  
Este projeto implementa um **Algoritmo Genético (AG)** para resolver problemas de criptoaritmética. A criptoaritmética consiste em operações aritméticas onde os números são substituídos por letras, e o objetivo é encontrar o valor numérico associado a cada letra que satisfaça a operação.  

### **Objetivos**  
1. Resolver problemas de criptoaritmética, como **SEND + MORE = MONEY**, utilizando algoritmos genéticos.  
2. Avaliar diferentes combinações de métodos e taxas para mutação, crossover e reinserção.  
3. Identificar as 4 melhores configurações de AG com base em:  
   - Taxa de convergência  
   - Tempo médio de execução  
4. Selecionar a **melhor configuração global** ao executar o AG em múltiplos problemas.  
5. Apresentar uma interface gráfica para visualização dos resultados.  

---

## 🚀 **Funcionalidades Principais**  

1. **Execução do Algoritmo Genético**  
   - Tamanho da população: 100  
   - Número de gerações: 50  
   - Taxas de crossover e mutação configuráveis.  
   - Métodos disponíveis: Roleta, Torneio, Crossover PMX, Cíclico, Reinserção com Elitismo.  

2. **Relatório Excel**  
   - Gera um relatório Excel com:  
     - Taxas de convergência  
     - Tempo médio de execução  
     - Média aritmética global de convergência  
     - Justificativas para escolha das melhores configurações.  

3. **Interface Gráfica**  
   - Visualização interativa dos problemas resolvidos.  
   - Mapeamento das letras para os números.  
   - Status do cálculo indicando se o resultado é correto (fitness = 0).  

4. **Execução em Paralelo**  
   - Utiliza a biblioteca **multiprocessing** para acelerar a execução em múltiplas configurações.  

---

## 🧩 **Problemas Resolvidos**  

1. **SEND + MORE = MONEY**  
2. **CROSS + ROADS = DANGER**  
3. **EAT + THAT = APPLE**  
4. **DONALD + GERALD = ROBERT**  
5. **COKE + COLA = OASIS**  

---

## 📂 **Estrutura do Projeto**  

```plaintext
projeto-ag-criptoaritmetica/
│
├── ag_core.py          # Lógica principal do Algoritmo Genético
├── ag_utils.py         # Funções auxiliares, como cálculo de fitness
├── ag_config.py        # Configurações do projeto
├── ag_interface.py     # Interface gráfica com Pygame
├── ag_excel.py         # Geração do relatório Excel
├── ag_problem.py       # Definição dos problemas de criptoaritmética
├── main.py             # Arquivo principal para execução do projeto
├── relatorio_final.xlsx # Relatório gerado pelo programa
├── imagens/            # Imagens do projeto (capturas de tela)
│   ├── exemplo_1.png
│   ├── exemplo_2.png
│   └── exemplo_3.png
└── README.md           # Documentação do projeto
```

---

## 🛠️ **Instalação e Execução**  

1. **Clonar o Repositório**  
   ```bash
   git clone https://github.com/seu-usuario/projeto-ag-criptoaritmetica.git
   cd projeto-ag-criptoaritmetica
   ```

2. **Instalar Dependências**  
   Certifique-se de ter o **Python 3.8+** instalado e execute:  
   ```bash
   pip install pygame pandas openpyxl
   ```

3. **Executar o Projeto**  
   ```bash
   python main.py
   ```

---

## 📸 **Imagens do Projeto**  

### **1. Interface Gráfica (Visualização do Problema)**  
![Interface 1](imagens/exemplo_1.png)

### **2. Relatório Gerado em Excel**  
![Relatório Excel](imagens/exemplo_2.png)

### **3. Terminal - Soluções e Operações**  
![Terminal Output](imagens/exemplo_3.png)

---

## 📊 **Resultados do Projeto**  

- **Média Global de Convergência:** `91.50%`  
- **Configuração Global Selecionada:**  
   - Taxa de Mutação: `5%`  
   - Taxa de Crossover: `80%`  
   - Seleção: `Torneio`  
   - Crossover: `PMX`  
   - Reinserção: `Elitismo`  

---

## 📈 **Possíveis Melhorias**  

- Adicionar novos tipos de problemas e operações matemáticas.  
- Melhorar a interface gráfica para permitir entrada de problemas personalizados.  
- Implementar métodos mais avançados de seleção e crossover para otimização.  

---

## 🧑‍💻 **Desenvolvedor**  

**Nome:** Micael Resende da Silva  
**Email:** micael.silva@estudante.iftm.edu.br
**GitHub:** [https://github.com/seu-usuario](https://github.com/Micael-Resende)  

---

Se tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato! 😊  
