import os
import pyvista as pv

# --- CONFIGURAÇÃO ---
ARQUIVO_ENTRADA = "FEMMeshGmsh.frd"  # <--- Mantenha o nome do seu arquivo!
CAMPO_DE_RESULTADO = "DISP" 
# --------------------

def criar_pagina_3d():
    if not os.path.exists(ARQUIVO_ENTRADA):
        print(f"❌ ERRO: O arquivo '{ARQUIVO_ENTRADA}' não foi encontrado.")
        return

    print("⏳ Carregando a estrutura do CalculiX...")
    mesh = pv.read(ARQUIVO_ENTRADA)
    
    # Criando o visualizador
    pl = pv.Plotter()
    
    # AJUSTE 1: Fundo cinza bem claro para dar contraste sem cansar os olhos
    pl.background_color = "#fdfdfd"
    
    print(f"🎨 Otimizando o visual dinâmico para: {CAMPO_DE_RESULTADO}...")
    
    # AJUSTE 2: Configuração avançada de exibição da malha
    pl.add_mesh(
        mesh, 
        scalars=CAMPO_DE_RESULTADO, 
        cmap="jet", 
        
        # Ajuste definitivo: linhas escuras bem finas com transparência na superfície
        show_edges=True, 
        edge_color="#111111",       # Linhas cinza-escuras para dar contorno
        line_width=0.3,             # Linhas bem finas
	opacity=0.9,		    # Deixa a superfície sólida o suficiente para ver a cor 	
        
        # Mantém as configurações originais de luz 
        ambient=0.3,                
        diffuse=0.7,                
        specular=0.1,               
        
        scalar_bar_args={
            "title": f"Escala: {CAMPO_DE_RESULTADO}",
            "color": "black",
            "shadow": True,
            "position_x": 0.85,     # Ajusta a posição da barra na tela
            "position_y": 0.1
        }
    )
    
    # AJUSTE 3: Adiciona luzes extras nas laterais para eliminar sombras escuras
    pl.add_light(pv.Light(position=(10, 10, 10), intensity=0.8))
    pl.add_light(pv.Light(position=(-10, -10, 10), intensity=0.5))
    
    pl.show_axes()
    pl.enable_trackball_style()
    
    nome_site = "catedral_cristo_rei_3d.html"
    print(f"💾 Salvando o site interativo em: {nome_site}...")
    pl.export_html(nome_site)
    print("✅ PRONTO! O site com visual otimizado foi criado!")

if __name__ == "__main__":
    criar_pagina_3d()
