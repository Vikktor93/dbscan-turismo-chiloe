# Genera datos turísticos sintéticos para el análisis espacial de Chiloé
from __future__ import annotations

import argparse
import csv
import random
from datetime import datetime, timedelta
from pathlib import Path


RANGO_LATITUD = (-43.5, -41.8)
RANGO_LONGITUD = (-74.2, -73.4)
TIPOS_TURISTA = ("nacional", "internacional", "excursionista", "residente")
LUGARES = {
    "Castro": (-42.4826, -73.7620),
    "Ancud": (-41.8697, -73.8203),
    "Dalcahue": (-42.3786, -73.6508),
    "Chonchi": (-42.6236, -73.7722),
    "Cucao": (-42.6246, -74.1081),
    "Quellón": (-43.1182, -73.6166),
}
RUTA_SALIDA = Path(__file__).resolve().parents[1] / "data" / "raw" / "turistas_chiloe.csv"
INICIO_PERIODO = datetime(2026, 1, 1)
FIN_PERIODO = datetime(2026, 12, 31, 23, 59, 59)


def limitar(valor: float, limites: tuple[float, float]) -> float:
    # Mantiene un valor dentro de los límites geográficos definidos
    return max(limites[0], min(valor, limites[1]))


def generar_timestamp(aleatorio: random.Random) -> str:
    # Devuelve una fecha y hora aleatoria de 2026 en formato ISO 8601
    segundos = int((FIN_PERIODO - INICIO_PERIODO).total_seconds())
    instante = INICIO_PERIODO + timedelta(seconds=aleatorio.randint(0, segundos))
    return instante.isoformat(sep=" ")


def generar_registros(cantidad: int, semilla: int | None) -> list[dict[str, object]]:
    # Crea registros distribuidos alrededor de las localidades turísticas indicadas
    aleatorio = random.Random(semilla)
    lugares = tuple(LUGARES.items())
    registros: list[dict[str, object]] = []

    for turista_id in range(1, cantidad + 1):
        lugar, (latitud_base, longitud_base) = aleatorio.choice(lugares)
        latitud = limitar(aleatorio.gauss(latitud_base, 0.018), RANGO_LATITUD)
        longitud = limitar(aleatorio.gauss(longitud_base, 0.018), RANGO_LONGITUD)
        registros.append(
            {
                "turista_id": turista_id,
                "latitud": round(latitud, 6),
                "longitud": round(longitud, 6),
                "timestamp": generar_timestamp(aleatorio),
                "tipo_turista": aleatorio.choice(TIPOS_TURISTA),
                "lugar_frecuentado": lugar,
            }
        )

    return registros


def guardar_csv(registros: list[dict[str, object]], ruta_salida: Path) -> None:
    # Crea el directorio de salida y escribe los registros en formato CSV
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    columnas = (
        "turista_id",
        "latitud",
        "longitud",
        "timestamp",
        "tipo_turista",
        "lugar_frecuentado",
    )

    with ruta_salida.open("w", newline="", encoding="utf-8") as archivo_csv:
        escritor = csv.DictWriter(archivo_csv, fieldnames=columnas)
        escritor.writeheader()
        escritor.writerows(registros)


def parsear_argumentos() -> argparse.Namespace:
    # Obtiene los parámetros de ejecución del generador
    analizador = argparse.ArgumentParser(description=__doc__)
    analizador.add_argument(
        "--cantidad",
        type=int,
        default=1_000,
        help="Número de registros a generar (por defecto: 1000).",
    )
    analizador.add_argument(
        "--semilla",
        type=int,
        default=42,
        help="Semilla para generar resultados reproducibles (por defecto: 42).",
    )
    argumentos = analizador.parse_args()
    if argumentos.cantidad <= 0:
        analizador.error("--cantidad debe ser un entero positivo.")
    return argumentos


def main() -> None:
    # Genera y guarda el dataset sintético
    argumentos = parsear_argumentos()
    registros = generar_registros(argumentos.cantidad, argumentos.semilla)
    guardar_csv(registros, RUTA_SALIDA)
    print(f"Dataset generado: {RUTA_SALIDA} ({len(registros)} registros)")


if __name__ == "__main__":
    main()