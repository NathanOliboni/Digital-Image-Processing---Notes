def gamma_correct(c):
    if c <= 0.04045:
        return c / 12.92
    else:
        return ((c + 0.055) / 1.055) ** 2.4
    
def rgb_to_xyz(rgb):
    r = gamma_correct(rgb[0])
    g = gamma_correct(rgb[1])
    b = gamma_correct(rgb[2])
    
    '''
            Matriz sRGB D65
    | 0.4124564  0.3575761  0.1804375 |
    | 0.2126729  0.7151522  0.0721750 |
    | 0.0193339  0.1191920  0.9503041 |
    '''

    x = r * 0.4124564 + g * 0.3575761 + b * 0.1804375
    y = r * 0.2126729 + g * 0.7151522 + b * 0.0721750
    z = r * 0.0193339 + g * 0.1191920 + b * 0.9503041

    return [x, y, z]

def inverse_gamma(c):
    if c <= 0.0031308:
        return c * 12.92
    else:
        return 1.055 * (c ** (1 / 2.4)) - 0.055
    
def xyz_to_rgb(xyz):
    '''
            Matriz inversa
    | 3.2404542 -1.5371385 -0.4985314  |
    | -0.9692660  1.8760108  0.0415560 |
    | 0.0556434 -0.2040259  1.0572252  |    
    '''
    r = xyz[0] * 3.2404542 + xyz[1] * -1.5371385 + xyz[2] * -0.4985314
    g = xyz[0] * -0.9692660 + xyz[1] * 1.8760108 + xyz[2] * 0.0415560
    b = xyz[0] * 0.0556434 + xyz[1] * -0.2040259 + xyz[2] * 1.0572252

    r = inverse_gamma(r)
    g = inverse_gamma(g)
    b = inverse_gamma(b)

    return [r, g, b]

def rgb_to_cmy(rgb):
    c = 1 - rgb[0]
    m = 1 - rgb[1]
    y = 1 - rgb[2]
    return [c, m, y]

def cmy_to_rgb(cmy):
    r = 1 - cmy[0]
    g = 1 - cmy[1]
    b = 1 - cmy[2]
    return [r, g, b]

def rgb_to_yuv(rgb):
    '''
        Matriz RGB para YUV
    | 0.299  0.587  0.114     |
    | -0.14713 -0.28886 0.436 |
    | 0.615 -0.51499 -0.10001 |
    '''
    y = 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]
    u = -0.14713 * rgb[0] - 0.28886 * rgb[1] + 0.436 * rgb[2]
    v = 0.615 * rgb[0] - 0.51499 * rgb[1] - 0.10001 * rgb[2]
    return [y, u, v]

def yuv_to_rgb(yuv):
    r = yuv[0] + 1.13983 * yuv[2]
    g = yuv[0] - 0.39465 * yuv[1] - 0.58060 * yuv[2]
    b = yuv[0] + 2.03211 * yuv[1]
    return [r, g, b]

def main():
    rgb = []
    for color in ['Red', 'Green', 'Blue']:
        value = int(input(f"Informe o valor para {color} (0-255): "))
        while value < 0 or value > 255:
            print("O valor deve estar entre 0 e 255.")
            value = int(input(f"Informe o valor para {color} (0-255): "))
        rgb.append(value)
    
    for _ in range(len(rgb)):
        rgb[_] = rgb[_] / 255
        
    while True:
        print("\nEscolha a conversão desejada:")
        print("1. RGB para XYZ")
        print("2. RGB para CMY")
        print("3. RGB para YUV")
        print("4. XYZ para RGB")
        print("5. CMY para RGB")
        print("6. YUV para RGB")
        print("7. Alterar valores RGB")
        print("8. Sair")
        
        choice = int(input("Digite sua escolha: "))
        
        if choice == 1:
            xyz = rgb_to_xyz(rgb)
            print(f"XYZ: {xyz}")
        elif choice == 2:
            cmy = rgb_to_cmy(rgb)
            print(f"CMY: {cmy}")
        elif choice == 3:
            yuv = rgb_to_yuv(rgb)
            print(f"YUV: {yuv}")
        elif choice == 4:
            rgb_converted = xyz_to_rgb(rgb)
            print(f"RGB: {rgb_converted}")
        elif choice == 5:
            rgb_converted = cmy_to_rgb(rgb)
            print(f"RGB: {rgb_converted}")
        elif choice == 6:
            rgb_converted = yuv_to_rgb(rgb)
            print(f"RGB: {rgb_converted}")
        elif choice == 7:
            rgb = []
            for color in ['Red', 'Green', 'Blue']:
                value = int(input(f"Informe o valor para {color} (0-255): "))
                while value < 0 or value > 255:
                    print("O valor deve estar entre 0 e 255.")
                    value = int(input(f"Informe o valor para {color} (0-255): "))
                rgb.append(value)
            
            for _ in range(len(rgb)):
                rgb[_] = rgb[_] / 255
        elif choice == 8:
            break
        else:
            print("Escolha inválida.")
    
if __name__ == "__main__":
    main()