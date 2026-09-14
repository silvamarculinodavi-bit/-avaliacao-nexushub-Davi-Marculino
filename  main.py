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