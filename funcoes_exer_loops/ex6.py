def conversor_mh(s):
    print(f"Tempo minutos: {s // 60}:{s % 60}")
    print(f"Tempo horas: {(s / 60) / 60:.2f}")

conversor_mh(5000)