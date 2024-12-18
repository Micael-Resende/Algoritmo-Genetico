import pygame
from ag_config import LARGURA, ALTURA, FONT_SIZE, FONT, TITLE_FONT

def gerar_paleta_cores(letters):
    """Gera uma paleta de cores aleatória para as letras."""
    import random
    random.seed(42)
    return {letter: (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)) for letter in letters}

def renderizar_problema_tela(screen, problem, mapping, y_offset=50, fitness=0):
    """
    Renderiza as palavras, mapeamento e operação completa na tela.
    Mostra também se o cálculo está correto (fitness = 0).
    """
    # Criar a paleta de cores para as letras
    all_letters = set("".join("".join(v) for v in problem.values()))
    color_palette = gerar_paleta_cores(all_letters)

    def render_colored_text(text, y_off, x_start, is_number=False):
        """Renderiza o texto caractere a caractere com as cores definidas."""
        spacing = FONT_SIZE + 10
        for char in text:
            if is_number:
                letter_origin = next((k for k, v in mapping.items() if str(v) == char), None)
                color = color_palette.get(letter_origin, (255, 255, 255))
            else:
                color = color_palette.get(char, (255, 255, 255))
            cs = FONT.render(char, True, color)
            screen.blit(cs, (x_start, y_off))
            x_start += spacing

    # Desenhar as palavras do problema
    keys = list(problem.keys())
    max_word_length = max(len(letters) for letters in problem.values())
    letter_spacing = FONT_SIZE + 10
    x_offset_initial = (LARGURA - max_word_length * letter_spacing) // 2

    render_colored_text("".join(problem[keys[0]]), y_offset, x_offset_initial)
    render_colored_text("".join(problem[keys[1]]), y_offset + 40, x_offset_initial)
    render_colored_text("".join(problem[keys[2]]), y_offset + 120, x_offset_initial)

    # Desenhar o sinal de +
    plus_sign_surface = FONT.render("+", True, (255, 255, 255))
    screen.blit(plus_sign_surface, (x_offset_initial - letter_spacing, y_offset + 40))

    # Linha horizontal
    bar_start = x_offset_initial
    bar_end = x_offset_initial + max_word_length * letter_spacing
    pygame.draw.line(screen, (255, 255, 255), (bar_start, y_offset + 80), (bar_end, y_offset + 80), 4)

    # Renderizar números correspondentes
    rendered = {key: "".join(str(mapping.get(letter, "?")) for letter in word) for key, word in problem.items()}
    y_offset_num = y_offset + 200
    render_colored_text(rendered[keys[0]], y_offset_num, x_offset_initial, is_number=True)
    render_colored_text(rendered[keys[1]], y_offset_num + 40, x_offset_initial, is_number=True)
    render_colored_text(rendered[keys[2]], y_offset_num + 120, x_offset_initial, is_number=True)

    # Desenhar linha final
    screen.blit(plus_sign_surface, (x_offset_initial - letter_spacing, y_offset_num + 40))
    pygame.draw.line(screen, (255, 255, 255), (bar_start, y_offset_num + 80), (bar_end, y_offset_num + 80), 4)

    # Mostrar mapeamento das letras
    exibir_mapeamento(screen, mapping, color_palette, y_offset_num + 200)

    # # Exibir status do cálculo (correto/incorreto)
    # if fitness == 0:
    #     status_msg = "Cálculo Correto!"
    #     color = (0, 255, 0)  # Verde
    # else:
    #     status_msg = f"Cálculo Incorreto! Fitness: {fitness}"
    #     color = (255, 0, 0)  # Vermelho

    #status_surface = TITLE_FONT.render(status_msg, True, color)
    #screen.blit(status_surface, ((LARGURA - status_surface.get_width()) // 2, y_offset_num + 280))

def exibir_mapeamento(screen, mapping, color_palette, y_offset):
    """Exibe o mapeamento das letras para os números na tela."""
    text_surface = TITLE_FONT.render("Mapeamento:", True, (255, 255, 255))
    screen.blit(text_surface, ((LARGURA - text_surface.get_width()) // 2, y_offset))
    y_offset += 40

    mapping_items = list(mapping.items())
    chars_per_line = 4
    for i in range(0, len(mapping_items), chars_per_line):
        chunk = mapping_items[i:i + chars_per_line]
        total_width = 0
        parts = []

        for idx, (letter, num) in enumerate(chunk):
            color = color_palette.get(letter, (255, 255, 255))
            letter_surf = FONT.render(letter, True, color)
            eq_surf = FONT.render("=", True, (255, 255, 255))
            num_surf = FONT.render(str(num), True, (255, 255, 255))
            parts.append([letter_surf, eq_surf, num_surf])
            total_width += sum(surf.get_width() for surf in [letter_surf, eq_surf, num_surf])
            if idx < len(chunk) - 1:
                total_width += 20  # Espaçamento entre os pares

        start_x = (LARGURA - total_width) // 2
        for part in parts:
            for surf in part:
                screen.blit(surf, (start_x, y_offset))
                start_x += surf.get_width()
            start_x += 20  # Espaçamento entre pares
        y_offset += 40
