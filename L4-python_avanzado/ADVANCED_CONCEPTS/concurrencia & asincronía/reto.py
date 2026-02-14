import asyncio
import random

async def descargar_archivo(nombre):
    tiempo = random.randint(1,5)
    print(f'Iniciando descarga {nombre} tardará {tiempo}s...')
    await asyncio.sleep(tiempo)
    print(f'Archivo {nombre} descargado en {tiempo}s')
    return f'{nombre} ok'

async def main():
    archivos = ['base_datos.csv', 'modelo_ia.bin', 'ventas_2025.xlsx', 'logo.png']
    tareas = [descargar_archivo(f) for f in archivos]
    print('Iniciando descagas masivas')
    resultados = await asyncio.gather(*tareas)

    print('\n---Reporte Final---')
    print(f'Descargas completadas: {resultados}')

if __name__ == '__main__':
    asyncio.run(main())