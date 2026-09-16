startup = {
"nome": "CyberPulse Tech",
"segmento": "Segurança da Informação",
"ano_adesao": "2026"
}

solucoes_ativas = ["Firewall IA", "Scan de Vulnerabilidades"]

print(f"Nome da startup: {startup['nome']}")
print(f"Segmento: {startup['segmento']}")
print(solucoes_ativas[0])


bancadas = [[1, 0], [0, 1]]

print("--- Mapeamento das Bancadas (1 = Ocupado, 0 = Livre) ---")
print(f"Setor Norte - Bancada N1 [0][0]: {bancadas[0][0]}")
print(f"Setor Norte - Bancada N2 [0][1]: {bancadas[0][1]}")
print(f"Setor Sul - Bancada S1 [1][0]: {bancadas[1][0]}")
print(f"Setor Sul - Bancada S2 [1][1]: {bancadas[1][1]}")

with open("custos_cloud.csv", "r", encoding="utf-8") as arquivo:
	cabecalho = arquivo.readline()
	linha_custo_1 = arquivo.readline()
	linha_custo_2 = arquivo.readline()
	linha_custo_3 = arquivo.readline()
	linha_custo_4 = arquivo.readline()

print(cabecalho, end="")
print(linha_custo_1, end="")
print(linha_custo_2, end="")
print(linha_custo_3, end="")
print(linha_custo_4, end="")

custo_1 = float(linha_custo_1.split(",")[1])
custo_2 = float(linha_custo_2.split(",")[1])
custo_3 = float(linha_custo_3.split(",")[1])
custo_4 = float(linha_custo_4.split(",")[1])
total_custos = custo_1 + custo_2 + custo_3 + custo_4

print("\n--- Painel Final ---")
print(f"Startup: {startup['nome']}")
print("Bancada: Bancada N1")
print(f"Total dos custos: R$ {total_custos:.2f}")