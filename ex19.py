#temos um sile de venda, queremos filtrar nossos usuarios para receberem os anuncios corretos, comforme a tabela
#menor de 15 anos. oferecer artigos infantis
#entre 15 a 21 feminino. oferecer maquiagem e moda
#entre 15 e 32 e atleta masculino. oferecer artigo  esportivos
#entre 15 e 21 não atleta masculino. oferecer videogames
#entre 21 e 32 masculino. oferecer livros, jardinagem e eletrodomesticos
#entre 22 a 35 feminino. oferecer artigos esportivos e itens de casa

idade = int(input("insira sua idade:"))

if idade < 15:
    print("oferecer artigos infantis")
elif idade >= 15 and idade <= 21 and "feminino":
    print("oferecer maquiagem e moda")
elif idade >= 15 and idade <= 32 and "masculino":
    print("oferecer artigos esportivos")
elif idade >= 15 and idade <= 21 and "masculino":
    print("oferecer videogames")
elif idade >= 21 and idade <= 32 and "masculino":
    print("oferecer livros, jardinagem e eletrodomesticos")
elif idade >= 22 and idade <= 35 and "feminino":
    print("oferecer artigos esportivos e itens de casa")
