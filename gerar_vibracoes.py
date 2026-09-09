import os
import pyvista as pv

# --- CONFIGURAÇÃO ---
ARQUIVO_ENTRADA = "FEMMeshGmsh.frd"  # <--- Certifique-se de manter o nome do seu arquivo real aqui!
CAMPO_DE_RESULTADO = "DISP" 
# --------------------

def criar_modelo_vibracoes():
    if not os.path.exists(ARQUIVO_ENTRADA):
        print(f"❌ ERRO: O arquivo '{ARQUIVO_ENTRADA}' não foi encontrado.")
        return

    print("⏳ Carregando a estrutura para análise de frequências...")
    mesh = pv.read(ARQUIVO_ENTRADA)
    
    pl = pv.Plotter()
    pl.background_color = "#fdfdfd"
    
    print("🎨 Gerando mapa de calor de energia cinética (Modo 1 - 1.25 Hz)...")
    pl.add_mesh(
        mesh, 
        scalars=CAMPO_DE_RESULTADO, 
        cmap="plasma",            # Mapa térmico: destaca as zonas de vibração máxima
        show_edges=True, 
        edge_color="#111111",     # Mudado para cinza claro para dar contraste no roxo/rosa
        line_width=0.4,           # Linhas bem finas e nítidas  
        opacity=0.95,		  # Quase totalmente sólido para a cor ficar viva

# AJUSTE CIRURGICO DE ILUMINAÇÃO: Dá volume, sombra e brilho realista nas curvas 

        ambient=0.45,             # Aumenta a claridade interna das cores escuras    
        diffuse=0.65,                
        specular=0.25,
	specular_power=20,
               
        scalar_bar_args={
            "title": "Zonas Críticas (Modo 1 - 1.25 Hz)",
            "color": "black",
            "shadow": True,
            "position_x": 0.85,     
            "position_y": 0.1
        }
    )
    
    pl.show_axes()
    pl.enable_trackball_style()
    
    # SALVA COM O NOME EXATO QUE O NOVO SITE VAI PROCURAR!
    nome_site = "catedral_vibracoes_3d.html"
    print(f"💾 Exportando modelo dinâmico para: {nome_site}...")
    pl.export_html(nome_site)
    print("✅ CONCLUÍDO! Arquivo de vibrações gerado com sucesso!")

if __name__ == "__main__":
    criar_modelo_vibracoes()