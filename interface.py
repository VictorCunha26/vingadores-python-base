from vingadores import Interface
from vingadores import Vingador

def main():
    Vingador('Homem de Ferro', 'Tony Stark', 'Humano', ['Inteligência', 'Engenharia', 'Rico'], 'Armadura', ['Arrogância', 'Orgulho'], 2000)
    Vingador('Capitão América', 'Steve Rogers', 'Humano', ['Força', 'Habilidade em Combate', 'Liderança'], 'Escudo', ['Inexperiência no mundo moderno'], 8000)
    Vingador('Thor', 'Thor Odinson', 'Deus', ['Força sobre-humana', 'Controle sobre raios', 'Imortalidade'], 'Mjolnir', ['Desatenção', 'Impulsividade'], 10000)
    Vingador('Hulk', 'Bruce Banner', 'Humano', ['Força sobre-humana', 'Regeneração', 'Durabilidade'], 'Força', ['Raiva', 'Controle mental'], 10000)

    Interface().menu() 

if __name__ == "__main__":
    main()
