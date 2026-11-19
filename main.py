from faq import buscar_faq, carregar_faq, normalizar

dados = carregar_faq("FAQPixelHaven/dados/faq.json")

print("=-=-=-=-=-FAQ PIXEL HAVEN =-=-=-=-=-")
while True:
    opc = input("FAQ: ").lower()
    opc_formatada = normalizar(opc)
    resultados = buscar_faq(opc_formatada, dados, limite=3)
    for entrada in resultados:
        print(entrada["resposta"])
    if opc == "sair":
        break
