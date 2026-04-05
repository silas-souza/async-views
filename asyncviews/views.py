import asyncio
import httpx
from django.http import HttpResponse
import time


# Função assíncrona com contador
async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(f"Contador Assíncrono: {num}")

    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(f"Status da Resposta: {r.status_code}")


# View Assíncrona (Não bloqueante)
async def async_view(request):
    # Criamos a tarefa em segundo plano para não travar a resposta
    asyncio.create_task(http_call_async())
    return HttpResponse("Requisição HTTP Não-Bloqueante iniciada! Verifique o console.")


# View Síncrona (Para comparação - Bloqueante)
def sync_view(request):
    for num in range(1, 6):
        time.sleep(1)
        print(f"Contador Síncrono: {num}")

    r = httpx.get("https://httpbin.org/")
    return HttpResponse(f"Requisição Bloqueante finalizada! Status: {r.status_code}")