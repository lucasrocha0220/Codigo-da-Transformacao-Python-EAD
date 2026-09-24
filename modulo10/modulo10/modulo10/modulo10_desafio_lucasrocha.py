import requests

GENEROS_TMDB = {
    28: "Ação", 12: "Aventura", 16: "Animação", 35: "Comédia", 80: "Crime",
    99: "Documentário", 18: "Drama", 10751: "Família", 14: "Fantasia",
    36: "História", 27: "Terror", 10402: "Música", 9648: "Mistério",
    10749: "Romance", 878: "Ficção Científica", 10770: "Cinema TV",
    53: "Thriller", 10752: "Guerra", 37: "Faroeste"
}

def buscar_filme():
    nome_filme = input("Digite o nome do filme: ").strip()
    

    chave_api = "5dfc7c8c2095938c6ed4151d7807c523"
    
    url_api = "https://api.themoviedb.org/3/search/movie"
    
    parametros = {
        "api_key": chave_api,
        "query": nome_filme,
        "language": "pt-BR"
    }

    print("\nBuscando dados no TMDB...")

    try:
        resposta = requests.get(url_api, params=parametros, timeout=10)
        

        resposta.raise_for_status()

        dados_filme = resposta.json()
        resultados = dados_filme.get("results", [])

        if not resultados:
            print(f"\n❌ Nenhum filme foi encontrado com o termo '{nome_filme}'.")
            return

        filme = resultados[0]

        titulo_filme = filme.get("title", "Título indisponível")
        sinopse_filme = filme.get("overview", "Sinopse não informada.")
        avaliacao_filme = filme.get("vote_average", "N/A")
        ids_generos = filme.get("genre_ids", [])

        nomes_generos = [GENEROS_TMDB.get(id_genero, "Outro") for id_genero in ids_generos]
        generos_formatados = ", ".join(nomes_generos) if nomes_generos else "Gênero não informado"

        print("\n" + "=" * 50)
        print(f"🎬 Título: {titulo_filme}")
        print(f"🎭 Gênero(s): {generos_formatados}")
        print(f"⭐ Avaliação dos usuários: {avaliacao_filme}/10")
        print("-" * 50)
        print(f"📖 Sinopse:\n{sinopse_filme}")
        print("=" * 50)
    except requests.exceptions.HTTPError as err_http:
        if resposta.status_code == 401:
            print("\n❌ Erro 401: Chave de API não autorizada ou inválida[cite: 1].")
        elif resposta.status_code == 404:
            print("\n❌ Erro 404: Recurso não encontrado no TMDB[cite: 1].")
        else:
            print(f"\n❌ Falha na requisição HTTP: {err_http}")

    except requests.exceptions.ConnectionError:
        print("\n❌ Erro de Conexão: Não foi possível conectar ao servidor do TMDB.")

    except requests.exceptions.Timeout:
        print("\n⏱️ Erro de Tempo Limite: O servidor do TMDB demorou para responder.")

    except requests.exceptions.RequestException as err:
        print(f"\n⚠️ Ocorreu uma falha inesperada na requisição: {err}")

if __name__ == "__main__":
    buscar_filme()